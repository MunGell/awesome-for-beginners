from jinja2 import Environment, FileSystemLoader
import json
import os
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"

def new_technology_dict(repo_technology):
    return {"link_id": repo_technology.lower(), "entries": []}

# Function to log warnings for missing data
def log_warning(message):
    logging.warning(message)

# Check if the data file exists
if not os.path.exists(DATAFILE):
    log_warning(f"Data file {DATAFILE} does not exist.")
    exit(1)

# Load data from the JSON file
try:
    with open(DATAFILE, "r") as datafile:
        data = json.loads(datafile.read())
except json.JSONDecodeError:
    log_warning("Error: Failed to parse JSON data in the file.")
    exit(1)

# Initialize technologies dictionary
technologies = {}

# Processing technologies
for technology in data.get("technologies", {}):
    technologies[technology] = {
        "link_id": data["technologies"].get(technology),
        "entries": [],
    }

# Processing repositories
for repository in data.get("repositories", []):
    repo_technologies = repository.get("technologies", [])
    if not repo_technologies:
        log_warning(f"Repository {repository['name']} has no technologies listed.")
    for repo_technology in repo_technologies:
        if repo_technology not in technologies:
            technologies[repo_technology] = new_technology_dict(repo_technology)
            log_warning(f"Technology {repo_technology} is newly added.")
        technologies[repo_technology]["entries"].append(repository)

# Create Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader(TEMPLATEPATH))
if not os.path.exists(os.path.join(TEMPLATEPATH, TEMPLATEFILE)):
    log_warning(f"Template file {TEMPLATEFILE} does not exist in the provided path.")
    exit(1)
template = env.get_template(TEMPLATEFILE)

# Create categories from the technologies
categories = []
for key, value in technologies.items():
    categories.append(
        {"title": key, "link_id": value["link_id"], "entries": value["entries"]}
    )

# Sorting categories and entries
categories = sorted(categories, key=lambda x: x["title"].upper())

category_groups = {"Misc": []}
for category in categories:
    category["entries"] = sorted(category["entries"], key=lambda x: x["name"].upper())
    first_char = category["title"][0].upper()
    if first_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if first_char not in category_groups:
            category_groups[first_char] = []
        category_groups[first_char].append(category)
    else:
        category_groups["Misc"].append(category)

# Process sponsors
sponsors = data.get("sponsors", [])

# Generate Table of Contents (TOC)
toc = []
for category in categories:
    toc.append(f"- [{category['title']}]({category['link_id']})")

# Prepare context for rendering the template
context = {
    "category_groups": category_groups,
    "categories": categories,
    "sponsors": sponsors,
    "toc": toc  # Adding TOC to context
}

# Rendering the README file
try:
    output = template.render(context)
    with open(TARGETFILE, "w") as targetfile:
        targetfile.write(output)
    logging.info("README file generated successfully.")
except Exception as e:
    log_warning(f"Error while rendering template: {e}")
    exit(1)

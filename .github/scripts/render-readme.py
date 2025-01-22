import json
import logging
from jinja2 import Environment, FileSystemLoader # type: ignore

# Setting up logging for better debugging and traceability
logging.basicConfig(level=logging.INFO)

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"

def new_technology_dict(repo_technology):
    """Creates a dictionary for new technology with an empty entries list."""
    return {"link_id": repo_technology.lower(), "entries": []}

def load_data(datafile):
    """Loads data from the JSON file and handles errors in case of missing file or invalid JSON."""
    try:
        with open(datafile, "r") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        logging.error(f"Data file {datafile} not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {datafile}. Please check the file format.")
        raise

def process_technologies(data):
    """Process technology data into a structured format."""
    technologies = {}
    for technology in data["technologies"]:
        technologies[technology] = {
            "link_id": data["technologies"][technology],
            "entries": [],
        }
    return technologies

def process_repositories(data, technologies):
    """Process repository data and associate technologies."""
    for repository in data["repositories"]:
        repo_technologies = repository["technologies"]
        for repo_technology in repo_technologies:
            if repo_technology not in technologies:
                technologies[repo_technology] = new_technology_dict(repo_technology)
            technologies[repo_technology]["entries"].append(repository)
    return technologies

def organize_categories(technologies):
    """Organize categories and entries for templating."""
    categories = []
    for key, value in zip(technologies.keys(), technologies.values()):
        categories.append(
            {"title": key, "link_id": value["link_id"], "entries": value["entries"]}
        )

    categories = sorted(categories, key=lambda x: x["title"].upper())
    category_groups = {"Misc": []}
    
    # Group categories by first character (A-Z), and handle miscellaneous ones separately
    for category in categories:
        category["entries"] = sorted(category["entries"], key=lambda x: x["name"].upper())
        first_char = category["title"][0].upper()
        if first_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if first_char not in category_groups:
                category_groups[first_char] = []
            category_groups[first_char].append(category)
        else:
            category_groups["Misc"].append(category)
    
    return categories, category_groups

def generate_readme(template, categories, category_groups, sponsors):
    """Render the README file using the Jinja2 template."""
    output = template.render(category_groups=category_groups, categories=categories, sponsors=sponsors)
    with open(TARGETFILE, "w") as targetfile:
        targetfile.write(output)
    logging.info(f"README generated at {TARGETFILE}")

def main():
    """Main function to load data, process repositories and generate the README."""
    try:
        # Load the data from the JSON file
        data = load_data(DATAFILE)

        # Process the technology data
        technologies = process_technologies(data)

        # Process repositories and associate them with technologies
        technologies = process_repositories(data, technologies)

        # Set up the Jinja2 environment and load the template
        env = Environment(loader=FileSystemLoader(TEMPLATEPATH))
        template = env.get_template(TEMPLATEFILE)

        # Organize categories based on technologies
        categories, category_groups = organize_categories(technologies)

        # Extract sponsors data
        sponsors = data["sponsors"]

        # Generate the README file using the template
        generate_readme(template, categories, category_groups, sponsors)
    
    except Exception as e:
        logging.error("An error occurred while generating the README.")
        logging.exception(e)

if __name__ == "__main__":
    main()

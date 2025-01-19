import json
from jinja2 import Environment, FileSystemLoader

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"

def new_technology_dict(repo_technology):
    return {"link_id": repo_technology.lower(), "entries": []}

technologies = {}

with open(DATAFILE, "r") as datafile:
    data = json.loads(datafile.read())

for technology in data["technologies"]:
    technologies[technology] = {
        "link_id": data["technologies"][technology],
        "entries": [],
    }

for repository in data["repositories"]:
    repo_technologies = repository["technologies"]
    for repo_technology in repo_technologies:
        if not technologies.get(repo_technology, False):
            technologies[repo_technology] = new_technology_dict(repo_technology)
        technologies[repo_technology]["entries"].append(repository)

env = Environment(loader=FileSystemLoader(TEMPLATEPATH))
template = env.get_template(TEMPLATEFILE)

categories = []
for key, value in zip(technologies.keys(), technologies.values()):
    categories.append(
        {"title": key, "link_id": value["link_id"], "entries": value["entries"]}
    )

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

sponsors = data["sponsors"]

output = template.render(category_groups=category_groups, categories=categories, sponsors=sponsors)

open(TARGETFILE, "w").write(output)
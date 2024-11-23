from jinja2 import Environment, FileSystemLoader
import json

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"

def new_technology_dict(repo_technology):
    return {"link_id": repo_technology.lower(), "entries": []}

technologies = {}

with open(DATAFILE, 'r') as datafile:
    data = json.loads(datafile.read())

for technology in data["technologies"]:
    technologies[technology] = {"link_id": data["technologies"][technology], "entries": []}

for repository in data["repositories"]:
    repo_technologies = repository["technologies"]
    for repo_technology in repo_technologies:
        if not technologies.get(repo_technology, False):
            technologies[repo_technology] = new_technology_dict(repo_technology)
        technologies[repo_technology]["entries"].append(repository)

env = Environment(loader = FileSystemLoader(TEMPLATEPATH))
template = env.get_template(TEMPLATEFILE)

categories = []
for key, value in zip(technologies.keys(), technologies.values()):
    categories.append({"title": key, "link_id": value["link_id"], "entries": value["entries"]})

categories = sorted(categories, key=lambda x: x["title"].upper())
for category in categories:
    category["entries"] = sorted(category["entries"], key=lambda x: x["name"].upper())

sponsors = data["sponsors"]

output = template.render(categories=categories, sponsors=sponsors)

open(TARGETFILE, "w").write(output)

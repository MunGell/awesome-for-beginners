from jinja2 import Environment, FileSystemLoader
import json

technologies = {}

with open("../../data.json", 'r') as datafile:
    data = json.loads(datafile.read())

for technology in data["technologies"]:
    technologies[technology] = {"link_id": data["technologies"][technology], "entries": []}

for repository in data["repositories"]:
    repo_technologies = repository["technologies"]
    for repo_technology in repo_technologies:
        if not technologies.get(repo_technology, False):
            technologies[repo_technology] = {"link_id": repo_technology.lower(), "entries": []}
        technologies[repo_technology]["entries"].append(repository)

env = Environment(loader = FileSystemLoader(".."))

template = env.get_template("README.j2")

categories = []
for key, value in zip(technologies.keys(), technologies.values()):
    categories.append({"title": key, "link_id": value["link_id"], "entries": value["entries"]})

categories = sorted(categories, key=lambda x: x["title"].upper())
for category in categories:
    category["entries"] = sorted(category["entries"], key=lambda x: x["name"].upper())

sponsors = data["sponsors"]

output = template.render(categories=categories, sponsors=sponsors)

open("README.md", "w").write(output)

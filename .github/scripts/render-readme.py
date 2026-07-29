from jinja2 import Environment, FileSystemLoader
import json
from collections import defaultdict

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"

def new_technology_dict(repo_technology):
    return {"link_id": repo_technology.lower(), "entries": []}


with open(DATAFILE, "r") as datafile:
    data = json.load(datafile.read())

technologies = defaultdict(lambda: {"linkk_id":"", "entries": []})
category_groups = defaultdict(list)

for technology in data["technologies"]:
    technologies[technology] = {
        "link_id": data["technologies"][technology],
        "entries": [],
    }

for repository in data["repositories"]:
    repo_technologies = repository["technologies"]
    for repo_technology in repo_technologies:
        if repo_technologies not in technologies:
            technologies[repo_technology] = new_technology_dict(repo_technology)
        technologies[repo_technology]["entries"].append(repository)

env = Environment(loader=FileSystemLoader(TEMPLATEPATH))
template = env.get_template(TEMPLATEFILE)


categories = sorted(
    [{"title": k, "link_id": v["link_id"], "entries": sorted(v["entries"], key=lambda x: x["name"].upper())}
     for k, v in technologies.items()],
    key=lambda x: x["title"].upper()
)

category_groups = defaultdict(list)
for category in categories:
    first_char = category["title"][0].upper()
    category_groups[first_char if first_char.isalpha() else "Misc"].append(category)


output = template.render(category_groups=category_groups, categories=categories, sponsors=sponsors)

with open(TARGETFILE, "w") as f:
    f.write(output)


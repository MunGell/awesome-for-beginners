from jinja2 import Environment, FileSystemLoader
import json
import re
import tempfile
import os
from urllib.parse import urlparse

DATAFILE = "./data.json"
TEMPLATEPATH = "./.github/"
TEMPLATEFILE = "README-template.j2"
TARGETFILE = "./README.md"


def escape_markdown(value: str) -> str:
    if value is None:
        return ""
    s = str(value)
    s = s.replace("\\", "\\\\")
    return re.sub(r'([`*_{}\[\]()#+\-.!|>])', r"\\\1", s)


def _atomic_write(path: str, content: str) -> None:
    dirpath = os.path.dirname(path) or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dirpath, encoding="utf-8") as tmp:
        tmp.write(content)
    os.replace(tmp.name, path)


def validate_url(url: str) -> bool:
    if not url:
        return False
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"}


class SafeRenderer:
    """Simple centralized renderer that sanitizes inputs before rendering."""

    def __init__(self, template_path: str = TEMPLATEPATH, template_file: str = TEMPLATEFILE):
        self.env = Environment(loader=FileSystemLoader(template_path))
        self.template = None
        self.template_file = template_file

    def load(self):
        self.template = self.env.get_template(self.template_file)

    def sanitize_repo(self, repo: dict) -> dict:
        link = repo.get("link", "")
        if not validate_url(link):
            raise ValueError("invalid url")
        return {
            "name": escape_markdown(repo.get("name", "")),
            "link": link,
            "label": escape_markdown(repo.get("label", "")),
            "description": escape_markdown(repo.get("description", "")),
        }

    def render_from_data(self, data: dict) -> str:
        if self.template is None:
            self.load()
        technologies = {}
        for tech, lid in data.get("technologies", {}).items():
            technologies[tech] = {"link_id": lid, "entries": []}
        for repo in data.get("repositories", []):
            try:
                r = self.sanitize_repo(repo)
            except ValueError:
                continue
            for t in repo.get("technologies", []):
                technologies.setdefault(t, {"link_id": t.lower(), "entries": []})["entries"].append(r)
        categories = [{"title": k, "link_id": v["link_id"], "entries": v["entries"]} for k, v in technologies.items()]
        categories = sorted(categories, key=lambda x: x["title"].upper())
        sponsors = [{"name": escape_markdown(s.get("name", "")), "image": s.get("image", ""), "link": s.get("link", "")} for s in data.get("sponsors", [])]
        return self.template.render(category_groups={}, categories=categories, sponsors=sponsors)


def main(datafile: str = DATAFILE, targetfile: str = TARGETFILE):
    with open(datafile, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    r = SafeRenderer()
    r.load()
    output = r.render_from_data(data)
    _atomic_write(targetfile, output)


if __name__ == "__main__":
    main()

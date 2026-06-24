import json
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from unittest import TestCase


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / ".github" / "scripts" / "render-readme.py"
TEMPLATE_PATH = REPO_ROOT / ".github" / "README-template.j2"


class RenderReadmeTests(TestCase):
    def test_generated_readme_escapes_html_but_keeps_br(self):
        with TemporaryDirectory() as tempdir:
            temp_path = Path(tempdir)
            github_dir = temp_path / ".github"
            github_dir.mkdir()
            (github_dir / "README-template.j2").write_text(TEMPLATE_PATH.read_text(), encoding="utf-8")

            data = {
                "sponsors": [{"name": "Sponsor <b>", "image": "https://example.com/s.png", "link": "https://example.com"}],
                "technologies": {"Test": "test"},
                "repositories": [{"name": "Repo <b>", "link": "https://example.com/repo", "label": "good <issue>", "technologies": ["Test"], "description": "Plain text & more<br><script>alert(1)</script>"}],
            }
            (temp_path / "data.json").write_text(json.dumps(data), encoding="utf-8")

            result = run(["python", str(SCRIPT_PATH)], cwd=temp_path, check=True, capture_output=True, text=True)

            self.assertEqual(result.returncode, 0)
            generated = (temp_path / "README.md").read_text(encoding="utf-8")
            self.assertIn("Repo &lt;b&gt;", generated)
            self.assertIn("good &lt;issue&gt;", generated)
            self.assertIn("Plain text & more<br>&lt;script&gt;alert(1)&lt;/script&gt;", generated)
            self.assertIn("Sponsor &lt;b&gt;", generated)
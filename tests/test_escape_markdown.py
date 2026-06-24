import importlib.util
from pathlib import Path


def _load_render_module():
    repo_root = Path(__file__).resolve().parent.parent
    module_path = repo_root / '.github' / 'scripts' / 'render-readme.py'
    spec = importlib.util.spec_from_file_location('render_readme', str(module_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_escape_basic():
    mod = _load_render_module()
    s = 'Hello *world* (test) [link] `code` > block'
    out = mod.escape_markdown(s)
    assert '\\*' in out
    assert '\\(' in out
    assert '\\[' in out
    assert '\\`' in out
    assert '\\>' in out


def test_escape_none():
    mod = _load_render_module()
    assert mod.escape_markdown(None) == ''

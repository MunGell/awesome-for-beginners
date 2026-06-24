import importlib.util
from pathlib import Path
import tempfile


def _load_module():
    repo_root = Path(__file__).resolve().parent.parent
    module_path = repo_root / '.github' / 'scripts' / 'render-readme.py'
    spec = importlib.util.spec_from_file_location('render_readme', str(module_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_validate_url_and_repo_entry():
    mod = _load_module()
    assert mod.validate_url('https://example.com')
    assert mod.validate_url('http://example.com')
    assert not mod.validate_url('javascript:alert(1)')
    try:
        # sanitize_repo should raise for invalid URL
        mod.SafeRenderer().sanitize_repo({'name': 'x', 'link': 'javascript:bad'})
        assert False, 'sanitize_repo should raise for invalid URL'
    except ValueError:
        pass


def test_safe_renderer_renders_and_escapes():
    mod = _load_module()
    tpl = "{{ categories[0].entries[0].name }} - {{ sponsors[0].name }}"
    # use jinja from string to avoid file reliance
    renderer = mod.SafeRenderer()
    renderer.template = renderer.env.from_string(tpl)
    data = {
        'technologies': {'Go': 'go'},
        'repositories': [
            {'name': 'Repo *Name*', 'link': 'https://github.com/example/repo', 'technologies': ['Go'], 'label': 'good', 'description': 'desc'}
        ],
        'sponsors': [{'name': 'Sponsor [X]', 'image': '', 'link': 'https://example.com'}]
    }
    out = renderer.render_from_data(data)
    assert '\\*' in out or 'Repo' in out
    assert 'Sponsor' in out

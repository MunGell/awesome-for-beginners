import importlib.util
import pathlib
import types

import pytest


def load_cghi_module() -> types.ModuleType:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    module_path = repo_root / ".github" / "scripts" / "cghi.py"
    spec = importlib.util.spec_from_file_location("cghi_module", str(module_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_get_open_issues_success(monkeypatch):
    module = load_cghi_module()

    class DummyResp:
        status_code = 200

        def json(self):
            return {"total_count": 5}

    def fake_get(url, params=None, timeout=None):
        assert "q" in params
        return DummyResp()

    monkeypatch.setattr(module, "requests", types.SimpleNamespace(get=fake_get))

    count = module.get_open_issues("owner", "repo", ())
    assert count == 5


def test_get_open_issues_invalid_owner():
    module = load_cghi_module()
    with pytest.raises(ValueError):
        module.get_open_issues("in valid", "repo", ())


def test_get_open_issues_non_200(monkeypatch):
    module = load_cghi_module()

    class DummyResp:
        status_code = 500

        def json(self):
            return {}

    def fake_get(url, params=None, timeout=None):
        return DummyResp()

    monkeypatch.setattr(module, "requests", types.SimpleNamespace(get=fake_get))

    with pytest.raises(SystemExit):
        module.get_open_issues("owner", "repo", ())


def test_get_open_issues_bad_json(monkeypatch):
    module = load_cghi_module()

    class DummyResp:
        status_code = 200

        def json(self):
            raise ValueError("bad json")

    def fake_get(url, params=None, timeout=None):
        return DummyResp()

    monkeypatch.setattr(module, "requests", types.SimpleNamespace(get=fake_get))

    with pytest.raises(SystemExit):
        module.get_open_issues("owner", "repo", ())

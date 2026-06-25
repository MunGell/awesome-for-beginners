import importlib.util
import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch


SCRIPT_PATH = Path(__file__).resolve().parents[1] / ".github" / "scripts" / "cghi.py"
SPEC = importlib.util.spec_from_file_location("cghi", SCRIPT_PATH)
cghi = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cghi
SPEC.loader.exec_module(cghi)


class IssueCounterTests(TestCase):
    def test_get_open_issues_uses_default_timeout_and_reports_count(self):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"total_count": 7}

        with patch.object(cghi.requests, "get", return_value=response) as mocked_get:
            with patch.object(cghi.click, "echo") as mocked_echo:
                cghi.get_open_issues("owner", "repo", [("label", "good first issue")])

        mocked_get.assert_called_once_with(
            "https://api.github.com/search/issues",
            params={"q": 'is:issue state:open repo:owner/repo label:"good first issue"'},
            timeout=cghi.DEFAULT_TIMEOUT_SECONDS,
        )
        mocked_echo.assert_called_once_with(7)

    def test_get_open_issues_wraps_request_errors(self):
        error = cghi.requests.RequestException("boom")

        with patch.object(cghi.requests, "get", side_effect=error):
            with self.assertRaises(cghi.click.ClickException):
                cghi.get_open_issues("owner", "repo", [])

    def test_cli_accepts_custom_timeout(self):
        with patch.object(cghi, "get_open_issues") as mocked_get_open_issues:
            cghi.cghi.main(
                ["owner", "repo", "--timeout", "3"],
                standalone_mode=False,
            )

        mocked_get_open_issues.assert_called_once_with(
            "owner",
            "repo",
            (),
            timeout_seconds=3,
        )

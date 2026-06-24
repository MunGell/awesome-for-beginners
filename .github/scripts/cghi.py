import click
import logging
from typing import Iterable, Tuple

import requests

LOG = logging.getLogger(__name__)


def _validate_repo_component(component: str) -> bool:
    """Validate GitHub owner/name components to a safe subset.

    Allow only alphanumerics, hyphen, underscore and dot. This prevents
    accidental or malicious characters from being inserted into API paths.
    """
    if not component:
        return False
    # Allow only alphanumerics, dot, underscore and hyphen
    return all(c.isalnum() or c in "._-" for c in component)


def get_open_issues(repo_owner: str, repo_name: str, search_params: Iterable[Tuple[str, str]]) -> int:
    """Return the number of open issues matching the provided filters.

    Design note: this function is a library-style call and *raises* on
    invalid input or unexpected API responses. The CLI wrapper (`cghi`)
    decides how to handle failures (exit code / logging). This keeps a
    clear separation between library logic and CLI behavior.
    """
    if not _validate_repo_component(repo_owner) or not _validate_repo_component(repo_name):
        raise ValueError("Invalid repo owner or name")

    # Base query: issues, open state, and repo scoping
    query_parts = [f"is:issue", "state:open", f"repo:{repo_owner}/{repo_name}"]

    # append additional search qualifiers, validating both parts
    for search_param, param in search_params:
        if not search_param or not isinstance(search_param, str):
            LOG.debug("Skipping invalid search_param: %r", search_param)
            continue
        if not isinstance(param, str):
            LOG.debug("Skipping non-string param: %r", param)
            continue
        # Add as a single piece; requests will take care of encoding
        # Surround param with quotes if it contains spaces
        if " " in param:
            param_value = f'"{param}"'
        else:
            param_value = param
        query_parts.append(f"{search_param}:{param_value}")

    full_query = " ".join(query_parts)
    api_endpoint = "https://api.github.com/search/issues"

    # Use safe parameter encoding and a timeout to avoid hanging requests
    try:
        resp = requests.get(api_endpoint, params={"q": full_query}, timeout=10)
    except requests.RequestException as exc:
        print(f"HTTP Error: {exc}")
        exit(1)

    if resp.status_code != 200:
        print(f"HTTP Error: {resp.status_code}")
        exit(1)

    try:
        data = resp.json()
    except ValueError:
        print("Failed to decode JSON response")
        exit(1)

    if "total_count" not in data:
        print("Unexpected response from GitHub API")
        exit(1)

    return int(data["total_count"])


@click.command()
@click.argument("repo_owner")
@click.argument("repo_name")
@click.option(
    "-p",
    "--search-param",
    "search_params",
    type=(str, str),
    multiple=True,
    help='''\b
    GitHub search filter parameters
    e.g. `-p label "good first issue"`
    '''
)
def cghi(repo_owner, repo_name, search_params):
    """Counts the number of GitHub issues for the given repository."""
    try:
        count = get_open_issues(repo_owner, repo_name, search_params)
    except Exception as exc:
        # Surface a concise error message and exit with non-zero code so
        # automation and CI can detect failures.
        LOG.error("Failed to get issues: %s", exc)
        raise SystemExit(1)

    # Preserve the original CLI behavior: print the raw count only.
    print(count)


if __name__ == "__main__":
    cghi()

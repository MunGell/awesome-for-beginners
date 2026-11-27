import os
import sys
import click
import requests

BASE_URL = "https://api.github.com/search/issues"


def build_query(repo_owner, repo_name, search_params):
    """Constructs the GitHub search query string."""
    query = f"is:issue state:open repo:{repo_owner}/{repo_name}"
    for key, value in search_params:
        query += f' {key}:"{value}"'
    return query


def get_open_issues(repo_owner, repo_name, search_params, timeout=10):
    """Fetches the number of open issues matching the search parameters."""
    query = build_query(repo_owner, repo_name, search_params)
    params = {"q": query}
    headers = {"Accept": "application/vnd.github.v3+json"}

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data.get("total_count", 0)
    except requests.exceptions.RequestException as e:
        click.echo(f"Request Error: {e}", err=True)
        raise SystemExit(1)


@click.command()
@click.argument("repo_owner")
@click.argument("repo_name")
@click.option(
    "-p",
    "--search-param",
    "search_params",
    type=(str, str),
    multiple=True,
    help="""\b
    GitHub search filter parameters
    e.g. -p label "good first issue"
    """,
)
def cghi(repo_owner, repo_name, search_params):
    """Counts the number of open GitHub issues matching specified criteria."""
    issue_count = get_open_issues(repo_owner, repo_name, search_params)
    click.echo(f"Open issues found: {issue_count}")


if __name__ == "__main__":
    cghi()


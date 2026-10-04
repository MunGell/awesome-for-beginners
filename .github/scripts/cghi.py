import click
import requests

BASE_URL = "https://api.github.com/search/issues"


def build_query(repo_owner, repo_name, search_params):
    query = f"is:issue state:open repo:{repo_owner}/{repo_name}"

    for key, value in search_params:
        query += f' {key}:"{value}"'

    return query


def get_open_issues(repo_owner, repo_name, search_params):
    query = build_query(repo_owner, repo_name, search_params)

    params = {"q": query}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return data["total_count"]

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
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
    help="""
GitHub search filter parameters

Example:
-p label "good first issue"
-p author "octocat"
""",
)
def cghi(repo_owner, repo_name, search_params):
    """Counts open GitHub issues."""

    issue_count = get_open_issues(
        repo_owner,
        repo_name,
        search_params
    )

    print(f"Open issues found: {issue_count}")


if __name__ == "__main__":
    cghi()
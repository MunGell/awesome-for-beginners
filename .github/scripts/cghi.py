import click
import requests

DEFAULT_TIMEOUT_SECONDS = 10


def get_open_issues(repo_owner, repo_name, search_params, timeout_seconds=DEFAULT_TIMEOUT_SECONDS):
    query_parts = ["is:issue", "state:open", f"repo:{repo_owner}/{repo_name}"]
    for search_param, param in search_params:
        query_parts.append(f'{search_param}:"{param}"')

    try:
        response = requests.get(
            "https://api.github.com/search/issues",
            params={"q": " ".join(query_parts)},
            timeout=timeout_seconds,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise click.ClickException(f"GitHub API request failed: {exc}") from exc

    click.echo(response.json()["total_count"])

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
@click.option(
    "--timeout",
    "timeout_seconds",
    default=DEFAULT_TIMEOUT_SECONDS,
    show_default=True,
    type=click.IntRange(min=1),
    help="Seconds to wait for GitHub before failing fast.",
)
def cghi(repo_owner, repo_name, search_params, timeout_seconds):
    """Count open GitHub issues without waiting indefinitely for the API."""
    get_open_issues(repo_owner, repo_name, search_params, timeout_seconds=timeout_seconds)

if __name__ == "__main__":
    cghi()

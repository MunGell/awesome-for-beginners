import click, requests, re, sys

ALLOWED_SEARCH_KEYS = {"label", "author", "assignee", "mentions", "milestone", "commenter", "in"}


def _validate_repo_component(component: str) -> None:
    if not re.match(r"^[A-Za-z0-9_.-]+$", component):
        raise ValueError("Invalid repository owner or name")


def get_open_issues(repo_owner, repo_name, search_params):
    _validate_repo_component(repo_owner)
    _validate_repo_component(repo_name)
    q_parts = ["is:issue", "state:open", f"repo:{repo_owner}/{repo_name}"]
    for key, val in search_params:
        safe_key = key if key in ALLOWED_SEARCH_KEYS else re.sub(r"[^A-Za-z0-9_-]", "", key)
        safe_val = str(val).replace('"', '\\"')
        q_parts.append(f'{safe_key}:"{safe_val}"')
    try:
        resp = requests.get("https://api.github.com/search/issues", params={"q": " ".join(q_parts)}, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)
    print(resp.json().get("total_count", 0))


@click.command()
@click.argument("repo_owner")
@click.argument("repo_name")
@click.option("-p", "--search-param", "search_params", type=(str, str), multiple=True,
              help=("GitHub search filter parameters. Example: -p label \"good first issue\""))
def cghi(repo_owner, repo_name, search_params):
    """Counts the number of GitHub issues"""
    get_open_issues(repo_owner, repo_name, search_params)


if __name__ == "__main__":
    cghi()

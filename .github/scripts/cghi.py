import click
import requests

def get_open_issues(repo_owner, repo_name, search_params):
    api_url = f"https://api.github.com/search/issues?q=is:issue%20state:open%20repo:{repo_owner}/{repo_name}"
    for search_param, param in search_params:
        api_url += f'%20{search_param}:"{param}"'
    print(api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        print(data["total_count"])
    else:
        printer(f"HTTP Error: {response.status_code}")
        exit(1)

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
    """Counts the number of GitHub issues"""
    print(search_params)
    get_open_issues(repo_owner, repo_name, search_params)

if __name__ == "__main__":
    cghi()

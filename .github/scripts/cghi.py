import click
import requests

def get_open_issues(repo_owner, repo_name, search_params):
    # Base search query
    query = f"is:issue state:open repo:{repo_owner}/{repo_name}"
    
    # Append additional search parameters cleanly
    for key, val in search_params:
        query += f' {key}:"{val}"'
    
    # GitHub Search API endpoint
    api_url = "https://api.github.com/search/issues"
    
    # Required headers by GitHub
    headers = {
        "User-Agent": "GitHub-Issue-Counter-App",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Pass the query via the 'params' argument so 'requests' handles URL encoding safely
    try:
        response = requests.get(api_url, params={"q": query}, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            click.echo(f"Total open issues matching criteria: {data['total_count']}")
        else:
            click.echo(f"HTTP Error {response.status_code}: {response.text}", err=True)
            raise click.Abort()
            
    except requests.exceptions.RequestException as e:
        click.echo(f"Network error occurred: {e}", err=True)
        raise click.Abort()

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
    get_open_issues(repo_owner, repo_name, search_params)

if __name__ == "__main__":
    cghi()
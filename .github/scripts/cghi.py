import os
import sys
import click
import requests
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def get_open_issues(repo_owner, repo_name, search_params, show_issues=False):
    """Obtiene y cuenta issues abiertos en un repositorio de GitHub."""
    # Construcción de la query base
    query = f"is:issue state:open repo:{repo_owner}/{repo_name}"
    for search_param, param in search_params:
        query += f' {search_param}:"{param}"'

    api_url = f"https://api.github.com/search/issues?q={query}"

    headers = {"User-Agent": "GitHub-Issues-Counter"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error en la petición HTTP: {e}")
        sys.exit(1)

    data = response.json()
    total = data.get("total_count", 0)
    logger.info(f"Issues abiertos encontrados: {total}")

    if show_issues and "items" in data:
        for issue in data["items"]:
            logger.info(f"- #{issue['number']} {issue['title']}")

@click.command()
@click.argument("repo_owner")
@click.argument("repo_name")
@click.option(
    "-p",
    "--search-param",
    "search_params",
    type=(str, str),
    multiple=True,
    help="Filtro de búsqueda en GitHub (ej: -p label 'good first issue')"
)
@click.option(
    "--show-issues",
    is_flag=True,
    default=False,
    help="Muestra los títulos de los issues encontrados"
)
def cghi(repo_owner, repo_name, search_params, show_issues):
    """Cuenta los issues abiertos en un repositorio de GitHub."""
    get_open_issues(repo_owner, repo_name, search_params, show_issues)

if __name__ == "__main__":
    cghi()

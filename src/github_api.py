import requests
from datetime import datetime

GITHUB_API_URL = "https://api.github.com"


def fetch_all_pull_requests(repo_owner, repo_name, since):
    """
    Fetches all pull requests from the specified GitHub repository and handles pagination.

    Args:
        repo_owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        since (datetime): The date from which to fetch pull requests.

    Returns:
        list: A list of all pull requests.
    """
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/pulls"
    params = {
        "state": "all",
        "per_page": 100
    }
    all_prs = []
    while url:
        response = requests.get(url, params=params)
        response.raise_for_status()
        prs = response.json()

        # Stop if pull requests are older than the since date
        if prs and datetime.strptime(prs[-1]['created_at'], '%Y-%m-%dT%H:%M:%SZ') < since:
            prs = [pr for pr in prs if datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ') >= since]
            all_prs.extend(prs)
            break

        all_prs.extend(prs)
        url = response.links.get('next', {}).get('url')
        params = {}  # Clear params after the first request
    return all_prs


def categorize_pull_requests(pull_requests):
    """
    Categorizes pull requests into opened, closed, and merged.

    Args:
        pull_requests (list): A list of pull requests.

    Returns:
        tuple: Three lists containing opened, closed, and merged pull requests.
    """
    opened = []
    closed = []
    merged = []

    for pr in pull_requests:
        if pr['state'] == 'open':
            opened.append(pr)
        elif pr['state'] == 'closed':
            if pr['merged_at']:
                merged.append(pr)
            else:
                closed.append(pr)

    return opened, closed, merged

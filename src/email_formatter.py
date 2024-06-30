def format_email_body(repo_owner, repo_name, opened, closed, merged, one_week_ago, today):
    """
    Formats the email body with the pull request summary.

    Args:
        repo_owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        opened (list): List of opened pull requests.
        closed (list): List of closed pull requests.
        merged (list): List of merged pull requests.
        one_week_ago (datetime): Date one week ago from today.
        today (datetime): Today's date.

    Returns:
        str: The formatted email body.
    """
    body = f"Pull Request Summary for the past week ({one_week_ago.date()} to {today.date()}):\n"
    body += f"Repository: {repo_owner}/{repo_name}\n\n"
    body += f"Opened: {len(opened)}\n"
    for pr in opened:
        body += f"  - {pr['title']} (#{pr['number']}) - {pr['html_url']}\n"

    body += f"\nClosed: {len(closed)}\n"
    for pr in closed:
        body += f"  - {pr['title']} (#{pr['number']}) - {pr['html_url']}\n"

    body += f"\nMerged: {len(merged)}\n"
    for pr in merged:
        body += f"  - {pr['title']} (#{pr['number']}) - {pr['html_url']}\n"

    return body

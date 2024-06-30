from github_api import fetch_all_pull_requests, categorize_pull_requests
from email_formatter import format_email_body
from email.mime.text import MIMEText
import datetime
import os

# Constants
EMAIL_FROM = "reporter@example.com"
EMAIL_TO = "manager@example.com"
REPO_OWNER = os.getenv("REPO_OWNER", "kubernetes")
REPO_NAME = os.getenv("REPO_NAME", "kubernetes")

# Get the current date and date from one week ago
today = datetime.datetime.now()
one_week_ago = today - datetime.timedelta(days=7)


def main():
    """
    Main function to fetch pull requests, categorize them, and print the email summary.
    """
    email_subject = f"Weekly GitHub Pull Request Summary for {REPO_OWNER}/{REPO_NAME}"

    # Fetch pull requests
    all_prs = fetch_all_pull_requests(REPO_OWNER, REPO_NAME, one_week_ago)

    # Categorize pull requests
    opened, closed, merged = categorize_pull_requests(all_prs)

    # Format email body
    email_body = format_email_body(REPO_OWNER, REPO_NAME, opened, closed, merged, one_week_ago, today)

    # Create email message
    email_message = MIMEText(email_body)
    email_message['From'] = EMAIL_FROM
    email_message['To'] = EMAIL_TO
    email_message['Subject'] = email_subject

    # TODO actually send email

    # Print email details
    print("From:", EMAIL_FROM)
    print("To:", EMAIL_TO)
    print("Subject:", email_subject)
    print("Body:\n", email_body)


if __name__ == "__main__":
    main()

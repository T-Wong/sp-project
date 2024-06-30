# SP Project

## Description
This project fetches pull request data from a specified GitHub repository and generates a summary report of opened, closed, and merged pull requests over the past week. The summary is formatted as an email and printed to the console.

## Setup

### Prerequisites
- Python 3.12+
- Docker (optional, for containerized execution)

### Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:T-Wong/sp-project.git
   cd sp-project
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   
   # If you are developing code
   pip install -r dev_requirements.txt
   ```

### Usage
To run the applicaiton locally:
```sh
python src/main.py
```

To run the application in Docker container:
```sh
docker build -t sp-project .

# Fetches PRs from kubernetes/kubernetes
docker run sp-project

# Fetchers PRs from a custom owner/repo
docker run -e REPO_OWNER=your_repo_owner -e REPO_NAME=your_repo_name sp-project
docker run -e REPO_OWNER=torvalds -e REPO_NAME=linux sp-project
```

### Scheduled Run
To produce regular reports of the project, you can use GitHub actions to run every week. An example is configured at `./.github/workflows/schedule.yml` and can be viewed [here](https://github.com/T-Wong/sp-project/actions/workflows/schedule.yml)

### Development
To lint the code:
```sh
flake8 .
```
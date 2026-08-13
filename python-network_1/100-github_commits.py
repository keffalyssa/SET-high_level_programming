#!/usr/bin/python3
"""
Module 100-github_commits
Takes 2 arguments (repository name and owner name)
and uses the GitHub API to list 10 most recent commits.
"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, params={'per_page': 10})
    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except Exception:
        pass

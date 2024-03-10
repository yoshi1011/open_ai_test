from github import Github
from dotenv import load_dotenv
import os


load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
username = os.getenv("USER_NAME")
repository_name = os.getenv("REPOSITORY_NAME")
repo_name = f"{username}/{repository_name}"


def get_all_pull_request_messages():
    g = Github(access_token)

    repo = g.get_repo(repo_name)

    pull_requests = repo.get_pulls(state="all")

    pr_messages = [pr.body for pr in pull_requests]
    return pr_messages


pr_messages = get_all_pull_request_messages()
print(pr_messages)

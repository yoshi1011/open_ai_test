from github import Github
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
username = os.getenv("USER_NAME")
repository_name = os.getenv("REPOSITORY_NAME")
repo_name = f"{username}/{repository_name}"


def get_source_code():
    g = Github(access_token)

    repo = g.get_repo(repo_name)
    tree = repo.get_git_tree("main", recursive=True)

    paths = list(map(lambda x: x.path, tree.tree))

    for path in paths:
        content = repo.get_contents(path)
        print(
            f"file_name: {content.name} \n",
            str(content.decoded_content, "utf-8"),
            end="",
        )


get_source_code()

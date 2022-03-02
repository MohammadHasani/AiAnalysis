import os
import shutil

from git import Repo

url = 'https://github.com/Kodex-AI/coding-challenges-input'


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


if __name__ == '__main__':
    directory = get_repo_name_from_url(url)

    parent_dir = "applications/repos/"

    path = os.path.join(parent_dir, directory)
    is_dir = os.path.isdir(path)
    if not is_dir:
        Repo.clone_from(url, path)
    else:
        shutil.rmtree(path)

        Repo.clone_from(url, path)

import os
import shutil

import pytest

from applications.Api.github import GithubAPI
from applications.constant import ROOT_DIR
from applications.model.crawler import Crawler


def get_test_repo():
    path = ROOT_DIR + "/repos/test/"

    return path


@pytest.fixture()
def init_api():
    path = get_test_repo()
    is_folder = os.path.isdir(path)
    if is_folder:
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)
    yield
    # teardown
    shutil.rmtree(path)


def test_download_repo(init_api):
    repo_url = 'https://github.com/Kodex-AI/coding-challenges-input'
    git_name = GithubAPI.get_repo_name_from_url(repo_url)
    repo_dir = ROOT_DIR + "/repos/test/" + git_name

    GithubAPI.download_repo(repo_url, repo_dir)

    challenge_repo_dir = ROOT_DIR + "/repos/test/" + git_name + '/python-challenge'

    python_files_in_repo = Crawler.get_all_python_files_in_folder(challenge_repo_dir)
    assert len(python_files_in_repo) > 1

import os
import shutil

import pytest

from applications.Api.github import GithubAPI
from applications.config import ROOT_DIR
from applications.model.crawler import Crawler
from applications.test.test_crawler import get_unittest_repo


@pytest.fixture()
def init_api():
    path = get_unittest_repo()
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
    crawler = Crawler()

    repo_url = 'https://github.com/Kodex-AI/coding-challenges-input'
    git_name = GithubAPI.get_repo_name_from_url(repo_url)
    repo_dir = ROOT_DIR + "/repos/test/" + git_name

    GithubAPI.download_repo(repo_url, repo_dir)

    challenge_repo_dir = ROOT_DIR + "/repos/test/" + git_name + '/python-challenge'

    python_files_in_repo = Crawler.get_all_python_files_in_folder(challenge_repo_dir)
    relu_result_list = []
    sigmoid_result_list = []
    for i in python_files_in_repo:
        relu_result = crawler.analysis_python_file(i, crawler.relu_regex)
        sigmoid_result = crawler.analysis_python_file(i, crawler.sigmoid_regex)
        relu_result_list.append(relu_result)
        sigmoid_result_list.append(sigmoid_result)

    classified_list = []
    for i in python_files_in_repo:
        classify_result = crawler.classify_file(i)
        classified_list.append(classify_result)

    assert relu_result_list == [17, 9, 8, 0]
    assert sigmoid_result_list == [4, 0, 4, 0]

    assert classified_list == ['high', 'low', 'medium', None]

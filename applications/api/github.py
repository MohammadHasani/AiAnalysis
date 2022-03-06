import shutil

from git import Repo, InvalidGitRepositoryError

from applications.constant import ROOT_DIR


class GithubAPI:
    @staticmethod
    def get_repo_dir(git_name):
        return ROOT_DIR + "/repos/" + git_name

    @staticmethod
    def download_repo(repo_url, repo_dir: str = None):
        if not repo_dir:
            git_name = GithubAPI.get_repo_name_from_url(repo_url)
            repo_dir = GithubAPI.get_repo_dir(git_name)

        Repo.clone_from(repo_url, repo_dir)

        return repo_dir

    @staticmethod
    def delete_repo(repo_dir):
        return shutil.rmtree(repo_dir)

    @staticmethod
    def get_repo_name_from_url(url: str) -> str:
        if url.endswith('/'):
            url = url[:-2]

        last_slash_index = url.rfind("/")
        last_suffix_index = url.rfind(".git")
        if last_suffix_index < 0:
            last_suffix_index = len(url)

        if last_slash_index < 0 or last_suffix_index <= last_slash_index:
            raise InvalidGitRepositoryError("Badly formatted url {}".format(url))

        return url[last_slash_index + 1:last_suffix_index]

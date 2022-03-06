import click
from git import InvalidGitRepositoryError, GitCommandError

from applications.api.github import GithubAPI
from applications.model.crawler import Crawler

fg = {'low': 'blue', 'medium': 'green', 'high': 'red', None: 'yellow'}


@click.command()
@click.option("--git_url", prompt="Enter GitHub repository url", help="The repo url you want to analysis.")
def hello(git_url):
    try:
        repo_name = GithubAPI.get_repo_name_from_url(git_url)
        repo_dir = GithubAPI.download_repo(git_url)
    except InvalidGitRepositoryError:
        print('The repo url is not valid, try again')
        hello()
    except GitCommandError as e:
        repo_dir = GithubAPI.get_repo_dir(repo_name)
        if 'already exists and is not an empty directory' in e.stderr:
            delete_repo(['--repo_dir', repo_dir, '--git_url', git_url])
        elif 'Not Found' in e.stderr:
            print('The repo url not found, try again')
            hello()
        else:
            print(str(e.stderr))
            hello()
    finally:
        crawler = Crawler()
        file_list = crawler.get_all_python_files_in_folder(repo_dir)
        final_list = {}
        for file in file_list:
            final_list[str(file)] = crawler.classify_file(file)

            file_path_in_dir = file.replace(repo_dir, '')
            click.echo(click.style(file_path_in_dir + ' : ' + str(final_list[str(file)]), fg=fg[final_list[str(file)]]))


@click.command()
@click.option("--delete", prompt="Repository exist, Do you want to delete it?(y) or analysis existing one?(n)",
              help="y or n")
@click.option("--repo_dir", prompt="Repository dir", help="Repository dir")
@click.option("--git_url", prompt="git_url", help="git_url")
def delete_repo(delete, repo_dir, git_url):
    if delete == 'y':
        GithubAPI.delete_repo(repo_dir)
        GithubAPI.download_repo(git_url)
        return
    else:
        return


if __name__ == '__main__':
    hello()

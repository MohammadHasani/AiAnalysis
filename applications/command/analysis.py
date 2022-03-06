import click

from applications.api.github import GithubAPI


@click.command()
@click.argument('name')
@click.option('--greeting', '-g')
def main(name, greeting):
    GithubAPI.download_repo()
    click.echo("{}, {}".format(greeting, name))


if __name__ == "__main__":
    main()

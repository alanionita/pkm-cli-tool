import click
from commands import build
from commands import deploy
from commands import create

@click.group(help="CLI tool to manage my notes garden")
def cli():
    pass

cli.add_command(build.build)
cli.add_command(deploy.deploy)
cli.add_command(create.cmd_create, name='create')


if __name__ == '__main__':
    cli()
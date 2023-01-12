import click
from commands import create
from commands import read

@click.group(help="CLI tool to manage my notes garden")
def cli():
    pass

cli.add_command(create.cmd_create, name='create')
cli.add_command(read.cmd_read, name='read')


if __name__ == '__main__':
    cli()
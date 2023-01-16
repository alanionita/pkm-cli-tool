import click
from pkmcli.commands import create
from pkmcli.commands import read

@click.group(help="CLI tool to manage my notes garden")
def cli():
    pass

cli.add_command(create.cmd, name='create')
cli.add_command(read.cmd, name='read')


if __name__ == '__main__':
    cli()
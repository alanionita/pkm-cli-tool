import click
from pkmcli.commands import create
from pkmcli.commands import read
from pkmcli.commands.store import status
from pkmcli.commands.store import change

@click.group(help="CLI tool to manage my notes garden")
def cli():
    pass

@cli.group()
def store():
    pass;


cli.add_command(create.cmd, name='create')
cli.add_command(read.cmd, name='read')

store.add_command(change.cmd, name='change')
store.add_command(status.cmd, name='status')

if __name__ == '__main__':
    cli()

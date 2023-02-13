import click
from paperclip.commands import create, read, init
from paperclip.commands.store import status, change

@click.group(help="CLI tool to manage my notes garden")
def cli():
    pass

@cli.group()
def store():
    pass;


cli.add_command(create.cmd, name='create')
cli.add_command(read.cmd, name='read')
cli.add_command(init.cmd, name='init')

store.add_command(change.cmd, name='change')
store.add_command(status.cmd, name='status')

if __name__ == '__main__':
    cli()

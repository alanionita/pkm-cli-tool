import click
from pkmcli.generators.store import NotesStore
from pkmcli.commands import create
from pkmcli.commands import read
from pkmcli.commands import echo_store

@click.group(help="CLI tool to manage my notes garden")


@click.option('--notes-home', envvar='PKMCLI_NOTES_HOME')
@click.pass_context
def cli(ctx, notes_home):
    ctx.obj = NotesStore(notes_home)
    pass

cli.add_command(echo_store.cmd, name='echo-store')
cli.add_command(create.cmd, name='create')
cli.add_command(read.cmd, name='read')


if __name__ == '__main__':
    cli()
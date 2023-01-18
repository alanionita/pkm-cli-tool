import click
from pkmcli.generators.store import NotesStore, pass_store

@click.command()
@pass_store

def cmd(notes_store):
    click.echo(isinstance(notes_store, NotesStore))
    click.echo(notes_store.location)
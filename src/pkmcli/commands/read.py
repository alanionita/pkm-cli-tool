import click
from pkmcli.generators import fm, path
from pkmcli.generators.store import click_get_ctx_location

def read_note(notes_store, filename):
    note_path = path.make(notes_store, filename)
    try:
        with open(note_path) as f:
            """
            Adds debugging for frontmatter metadata
            """
            fm.print_metadata(f.read())
            """
            Open in vscode
            """
            path.open_in(note_path, 'code')
            pass

    except BaseException as err:
        click.echo(f"Error [read_note] : Unexpected {err=}, {type(err)=}")

@click.command()
@click.option('--name', '-n', default="daily.2023.01.15", prompt='Enter type of note to read', help='Name of note')

def cmd(name):
    click.echo(f'[read] Reading note of type : {name}')
    notes_location = click_get_ctx_location 
    read_note(notes_location, name)
import click
from pkmcli.generators import fm, path

def read_note(filename):
    note_path = path.make(filename)
    try:
        with open(note_path) as f:
            """
            Adds debugging for frontmatter metadata
            """
            fm.print_metadata(f)
            """
            Open in vscode
            """
            path.open_in(note_path, 'code')
            pass

    except BaseException as err:
        click.echo(f"Error [read_note] : Unexpected {err=}, {type(err)=}")

@click.command()
@click.option('--name', '-n', default="daily.2023.01.09", prompt='Enter type of note to read', help='Name of note')

def cmd(name):
    click.echo(f'Reading note of type : {name}')
    read_note(name)
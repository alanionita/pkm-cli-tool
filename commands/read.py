import click
from datetime import datetime
from utils import frontmatter, make_note_path

def open_note_in_vscode(filename):
    os.system("code " + filename)

def read_note(filename):
    note_path = make_note_path(filename)
    try:
        note_frontmatter = frontmatter.make(f'{filename}')
        with open(note_path) as f:
            # Adds debugging for frontmatter metadata
            frontmatter.print_metadata(f)
            # Open in vscode
            open_note_in_vscode(note_path)
            pass

    except BaseException as err:
        print(f"Error [read_note] : Unexpected {err=}, {type(err)=}")

@click.command()
@click.option('--name', '-n', default="daily.2023.01.09", prompt='Enter type of note to read', help='Name of note')
def cmd_read(name):
    print(f'Reading note of type : {name}')
    read_note(name)
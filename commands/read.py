import click
from datetime import datetime
from utils import frontmatter
import os

import os
def open_note_in_vscode(file_name):
    os.system("code " + file_name)

def read_note(file_name):
    CURR_WORK_DIR = os.getcwd() 
    NOTES_FILE_PATH = f'{CURR_WORK_DIR}/my_notes' 
    NOTES_FILE_EXT = '.md'
    note_path = f'{NOTES_FILE_PATH}/{file_name}{NOTES_FILE_EXT}'
    try:
        note_frontmatter = frontmatter.make(f'{file_name}')
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
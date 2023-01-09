import click
from datetime import datetime
from utils import frontmatter
import os

import os
def open_note_in_vscode(file_name):
    os.system("code " + file_name)

def create_note(file_name, file_contents, title):
    CURR_WORK_DIR = os.getcwd() 
    NOTES_FILE_PATH = f'{CURR_WORK_DIR}/my_notes' 
    NOTES_FILE_EXT = '.md'
    note_path = f'{NOTES_FILE_PATH}/{file_name}{NOTES_FILE_EXT}'
    try:
        note_frontmatter = frontmatter.make(title)
        with open(note_path, 'x') as fp:
            fp.writelines(note_frontmatter)
            fp.write(file_contents)
            fp.close()
            pass

    except FileExistsError as err: 
        # if file exists I should just open the file
        print(f'Error [create_note] : Note [{title}] already exists, opening note now')
        open_note_in_vscode(note_path)

    except BaseException as err:
        print(f"Error [create_note] : Unexpected {err=}, {type(err)=}")

def make_note_daily():
    print(f'Creating daily note')
    curr_date = datetime.now()
    note_path = curr_date.strftime('daily.%Y.%m.%d')
    note_title = curr_date.strftime('%Y-%m-%d')
    note_contents = 'test'
    create_note(note_path, note_contents, note_title)
    return

def make_note_project(): 
    print(f'Creating project note')
    return

def make_note_area(): 
    print(f'Creating area note')
    return

def make_note_resource(): 
    print(f'Creating resource note')
    return

def make_note_archive(): 
    print(f'Creating archive note')
    return

note_types={
    'daily': make_note_daily,
    'project': make_note_project,
    'area': make_note_area,
    'resource': make_note_resource,
    'archive': make_note_archive
}

def make_note(type):

    # return switch.get(type,"Invalid note type")
    make_note = note_types[type]
    if callable(make_note):
        make_note()
    else:
        print(make_note)

@click.command()
@click.option('--type', '-t', default="daily", type=click.Choice(['daily', 'project', 'area', 'resource', 'archive'], case_sensitive=False), prompt='Enter type of note to create', help='Type of note')
def cmd_create(type):
    print(f'Creating note of type : {type}')
    make_note(type)
import click
from datetime import datetime
from . import path
from . import file
from . import fm


def daily(notes_store):
    click.echo('making daily note')
    curr_date = datetime.now()
    note_path = curr_date.strftime('daily.%Y.%m.%d')
    full_path = path.make(notes_store, note_path)
    title = curr_date.strftime('%Y-%m-%d')
    file_contents = fm.make(title)
    """
    Write the file
    """
    file.make(full_path, file_contents, title)
    return


def other(notes_store, type, name):
    """
    Deriving the path details
    """
    path_arr = name.split('.')
    path_last_part = path_arr[-1]

    """
    Creating note content
    """
    curr_date = datetime.now()
    note_path = curr_date.strftime(f'{type}.{name}')
    full_path = path.make(notes_store, note_path)
    title = path_last_part
    file_contents = ''
    """
    Write to file
    """
    file.make(full_path, file_contents, title)
    return


def make(notes_store, type, name):
    if (type == 'daily'):
        daily(notes_store)
    else:
        other(notes_store, type, name)

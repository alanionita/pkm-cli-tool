from datetime import datetime
from . import path
from . import fm


def daily(notes_store):
    NOTE_TYPE = 'daily'
    curr_date = datetime.now()
    note_file_name = curr_date.strftime('daily.%Y.%m.%d')
    file_path = path.make(notes_store, note_file_name)
    title = curr_date.strftime('%Y-%m-%d')
    contents = fm.make(title, NOTE_TYPE)
    return {
        'path': file_path,
        'contents': contents,
        'title': f'# Daily note'
    }


def other(notes_store, note_type, name):
    """
    Deriving the path details
    """
    path_arr = name.split('.')
    path_last_part = path_arr[-1]
    """
    Creating note content
    """
    curr_date = datetime.now()
    note_path = curr_date.strftime(f'{note_type}.{name}')
    file_path = path.make(notes_store, note_path)
    title = path_last_part.title()
    contents = fm.make(title, note_type)

    return {
        'path': file_path,
        'contents': contents,
        'title': f'# {title}'
    }


def make(notes_store, note_type, name):
    if (note_type == 'daily'):
        return daily(notes_store)
    else:
        return other(notes_store, note_type, name)
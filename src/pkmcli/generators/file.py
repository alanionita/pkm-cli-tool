import click
import os
from . import path

cwd = os.getcwd()
notes_folder_name = 'notes_store'
notes_folder_path = f'{cwd}/{notes_folder_name}'

def make(file_path, contents, title):
    try:
        with open(file_path, 'x') as file:
            file.writelines(contents)
            file.write(title)
            file.close()
            path.open_in(file_path, 'code')
            pass

    except FileExistsError as err:
        click.echo(
            f'Error [file.make] : Creation skipped, file [{title}] already exists. Opening file ...')
        path.open_in(file_path, 'code')
        raise err


def make_notes_folder():
    try:
        os.makedirs(notes_folder_path)
    except FileExistsError as err:
        click.echo(
            f'Error [file.make_notes_folder] : Creation skipped, folder [{notes_folder_path}] already exists.')
        raise err

def check_notes_folder():
    return os.path.isdir(notes_folder_path)  
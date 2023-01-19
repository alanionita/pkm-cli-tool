import os

def make(notes_store, filename):
    NOTES_FILE_EXT = '.md'
    path_base = ''
    if (notes_store):
        path_base = notes_store
    else:
        path_cwd = os.getcwd()
        path_base = f'{path_cwd}/notes_store'

    path_to_file = f'{path_base}/{filename}{NOTES_FILE_EXT}'
    return path_to_file

def open_in(filename, program):
    os.system(f'{program} {filename}')
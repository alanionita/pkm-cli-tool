import os

def make(notes_path_base, filename):
    NOTES_FILE_EXT = '.md'
    path_to_file = f'{notes_path_base}/{filename}{NOTES_FILE_EXT}'
    return path_to_file

def open_in(filename, program):
    os.system(f'{program} {filename}')

def get_project_base():
    cwd = os.getcwd()
    base_path = f'{cwd}/src/paperclip'
    return base_path
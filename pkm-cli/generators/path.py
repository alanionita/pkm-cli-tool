import os

def make(filename):
    CURR_WORK_DIR = os.getcwd() 
    NOTES_FILE_PATH = f'{CURR_WORK_DIR}/notes_store' 
    NOTES_FILE_EXT = '.md'
    path_to_file = f'{NOTES_FILE_PATH}/{filename}{NOTES_FILE_EXT}'
    return path_to_file

def open_in(filename, program):
    os.system(f'{program} {filename}')
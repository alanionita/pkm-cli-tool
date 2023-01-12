import os

def make_note_path(filename):
    CURR_WORK_DIR = os.getcwd()     
    NOTES_FILE_PATH = f'{CURR_WORK_DIR}/my_notes' 
    NOTES_FILE_EXT = '.md'
    note_path = f'{NOTES_FILE_PATH}/{filename}{NOTES_FILE_EXT}'
    return note_path

def open_note_in_vscode(filename):
    os.system("code " + filename)

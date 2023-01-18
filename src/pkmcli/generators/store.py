import click
import os

class NotesStore(object):
    def __init__(self, location=None):
        CURR_WORK_DIR = os.getcwd() 
        NOTES_STORE_DEFAULT = f'{CURR_WORK_DIR}/notes_store' 
        self.location = os.path.abspath(location or NOTES_STORE_DEFAULT)

pass_store = click.make_pass_decorator(NotesStore)
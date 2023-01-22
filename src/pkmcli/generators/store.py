import click
import os

class NotesStore(object):
    # _instance = None

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self):
        CURR_WORK_DIR = os.getcwd()
        NOTES_STORE_DEFAULT = f'{CURR_WORK_DIR}/notes_store'
        self._location = os.path.abspath(NOTES_STORE_DEFAULT)

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location


pass_store_ctx = click.make_pass_decorator(NotesStore, ensure=True)

def click_get_ctx_location():
    ctx = click.get_current_context()
    return ctx.obj.location
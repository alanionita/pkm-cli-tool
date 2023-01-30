import click
import json
import os

NOTES_LOCATION = 'notes_location'

def build_context_path(base_path = None, file_name = None):
    ctx_file_name = 'context' if file_name == None else file_name 
    if base_path == None:
        CURR_WORK_DIR = os.getcwd()
        CONTEXT_PATH = f'{CURR_WORK_DIR}/{ctx_file_name}.json'
        return os.path.abspath(CONTEXT_PATH)
    else:
        CONTEXT_PATH = f'{base_path}/{ctx_file_name}.json'
        return os.path.abspath(CONTEXT_PATH)


def get_location(ctx_path):
    # ctx_path = build_context_path() TODO: check that the implementation still works
    try:
        with open(ctx_path, "r") as f:
            context = json.load(f)
            value = context.get(NOTES_LOCATION)
            if value:
                return value
            else:
                raise KeyError('[get_location] Key value [{NOTES_LOCATION}] not found in context.json')
    except KeyError as err:
        click.echo(f"[get_location] {NOTES_LOCATION} is not set.")
        raise err


def set_location(base_path, new_location):
    ctx_path = build_context_path(base_path)
    context = {}
    try:
        with open(ctx_path, "r") as f:
            context = json.load(f)
    except:
        pass
    context[NOTES_LOCATION] = new_location
    with open(ctx_path, "w") as f:
        json.dump(context, f)

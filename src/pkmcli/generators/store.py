import click
import json
import os

NOTES_LOCATION = 'notes_location'

def build_context_path():
    CURR_WORK_DIR = os.getcwd()
    CONTEXT_PATH = f'{CURR_WORK_DIR}/context.json'
    return os.path.abspath(CONTEXT_PATH)


def get_location():
    ctx_path = build_context_path()
    try:
        with open(ctx_path, "r") as f:
            context = json.load(f)
            value = context.get(NOTES_LOCATION)
            if value:
                return value
            else:
                raise KeyError
    except KeyError:
        click.echo(f"[get_location] {NOTES_LOCATION} is not set.")


def set_location(new_location):
    ctx_path = build_context_path()
    print(f'[set-loc] ctx ::', ctx_path)
    context = {}
    try:
        with open(ctx_path, "r") as f:
            context = json.load(f)
    except:
        pass
    context[NOTES_LOCATION] = new_location
    with open(ctx_path, "w") as f:
        json.dump(context, f)

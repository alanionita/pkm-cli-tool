import click
import json
import os
from pkmcli.generators.path import get_project_base

NOTES_LOCATION = 'notes_location'

def build_context_path(base_path = None, file_name = None):
    ctx_file_name = 'context' if file_name == None else file_name 
    if base_path == None:
        cwd = get_project_base()
        ctx_path = f'{cwd}/{ctx_file_name}.json'
        return os.path.abspath(ctx_path)
    else:
        ctx_path = f'{base_path}/{ctx_file_name}.json'
        return os.path.abspath(ctx_path)


def get_location(ctx_path):
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


def set_location(ctx_path, new_location):
    context = {}
    try:
        with open(ctx_path, "r") as f:
            context = json.load(f)
    except:
        pass
    context[NOTES_LOCATION] = new_location
    with open(ctx_path, "w") as f:
        json.dump(context, f)

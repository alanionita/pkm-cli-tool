import click
import os
from pkmcli.commands.store import status
from pkmcli.generators.store import get_location, set_location, build_context_path

CURR_WORK_DIR = os.getcwd()
NOTES_STORE_DEFAULT = f'{CURR_WORK_DIR}/test_store'


@click.command()
@click.option("--location", required=True)
def cmd(location):
    cwd = os.getcwd()
    base_path = f'{cwd}/src/pkmcli'
    ctx_path = build_context_path(base_path)
    ctx_location = get_location(ctx_path)
    print('[changelocation] Notes Store / old location ::', ctx_location)
    set_location(base_path, location)
    click.get_current_context().invoke(status.cmd)

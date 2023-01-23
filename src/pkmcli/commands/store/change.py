import click
import os
from pkmcli.commands.store import status
from pkmcli.generators.store import get_location, set_location

CURR_WORK_DIR = os.getcwd()
NOTES_STORE_DEFAULT = f'{CURR_WORK_DIR}/test_store'


@click.command()
@click.option("--location", required=True)
def cmd(location):
    ctx_location = get_location()
    print('[changelocation] Notes Store / old location ::', ctx_location)
    set_location(location)
    click.get_current_context().invoke(status.cmd)

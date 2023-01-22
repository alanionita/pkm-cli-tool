import click, os
from pkmcli.commands.store import status

CURR_WORK_DIR = os.getcwd() 
NOTES_STORE_DEFAULT = f'{CURR_WORK_DIR}/test_store'    

@click.command()
@click.argument("location", required=False, default=NOTES_STORE_DEFAULT)
def cmd(location):
    ctx = click.get_current_context()
    print('[changelocation] Notes Store / location ::', ctx.obj.location)
    ctx.obj.location = location
    click.get_current_context().invoke(status.cmd)
import click
import os
from pkmcli.commands.store import status
from pkmcli.generators.store import get_location, set_location, build_context_path

@click.command()
@click.option("--location", required=True)
def cmd(location):
    ctx_path = build_context_path()
    ctx_location = get_location(ctx_path)
    print('[changelocation] Notes Store / old location ::', ctx_location)
    set_location(location)
    click.get_current_context().invoke(status.cmd)

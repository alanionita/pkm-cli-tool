import click
import os
from paperclip.commands.store import status
from paperclip.generators.store import get_location, set_location, build_context_path

@click.command()
@click.option("--location", required=True)
def cmd(location):
    ctx_path = build_context_path()
    ctx_location = get_location(ctx_path)
    click.echo(f'[store / change] Notes Store / old location ::')
    click.echo(ctx_location)
    set_location(ctx_path,location)
    click.get_current_context().invoke(status.cmd)

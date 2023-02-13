import click, os
from paperclip.generators.store import get_location, build_context_path

@click.command()
def cmd():
    ctx_path = build_context_path()
    ctx_location = get_location(ctx_path)
    click.echo('[status] Notes Store / location ::')
    click.echo(ctx_location)
    return ctx_location


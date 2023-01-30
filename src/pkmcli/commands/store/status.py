import click, os
from pkmcli.generators.store import get_location, build_context_path

@click.command()
def cmd():
    ctx_path = build_context_path()
    ctx_location = get_location(ctx_path)
    print(f'[status] Notes Store / location :: {ctx_location}')


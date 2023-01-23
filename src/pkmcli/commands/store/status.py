import click
from pkmcli.generators.store import get_location

@click.command()
def cmd():
    ctx_location = get_location()
    print(f'[status] Notes Store / location :: {ctx_location}')


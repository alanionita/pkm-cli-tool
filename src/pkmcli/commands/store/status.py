import click
from pkmcli.generators.store import click_get_ctx_location

@click.command()
def cmd():
    ctx_location = click_get_ctx_location()
    print(f'[status] Notes Store / location :: {ctx_location}')


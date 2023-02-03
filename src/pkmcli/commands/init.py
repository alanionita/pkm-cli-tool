import click
from pkmcli.generators import fm, path
from pkmcli.generators.store import get_location, make_context

@click.command()
@click.option('--store', '-s', help='Name of store', required=False)

def cmd(store):
    click.echo(f'[init] Creating store...')
    make_context(store)
 
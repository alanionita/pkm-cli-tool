import click
from paperclip.generators import file
from paperclip.generators.store import make_context

@click.command()
@click.option('--store', '-s', help='Name of store', required=False)

def cmd(store):
    click.echo(f'[init] Creating store...')
    if store: click.echo(f'[init] With store :: {store}')
    if file.check_notes_folder():
        click.echo(f'[init] Creating context...')
        make_context(store)    
    else:
        click.echo(f'[init] Creating default notes_store folder...')
        file.make_notes_folder();
        click.echo(f'[init] Creating context...')
        make_context(store)
 
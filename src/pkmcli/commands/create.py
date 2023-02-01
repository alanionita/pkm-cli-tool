import click
from pkmcli.generators import notes
from pkmcli.generators.store import get_location, build_context_path
from pkmcli.generators import file

CMD_NOTE_TYPES = ['daily', 'project', 'area',
                  'resource', 'archive']
CMD_PROMPT = 'Enter type of note to create'
CMD_HELP = 'Type of note'
CMD_TYPE = click.Choice(CMD_NOTE_TYPES, case_sensitive=False)
CMD_DEFAULT = "daily"

@click.command()
@click.option('--type', '-t', default=CMD_DEFAULT, type=CMD_TYPE, prompt=CMD_PROMPT, help=CMD_HELP)
@click.argument("name", required=False)

def cmd(type, name):
    click.echo(f'[create] Creating note of type ::: {type}')
    ctx_path = build_context_path()
    notes_location = get_location(ctx_path) 
    note = notes.make(notes_location, type, name)
    if (note):
        fpath = note.get("path")
        fcontents = note.get("contents")
        ftitle = note.get("title")
        if (fpath, fcontents, ftitle):
            """
            # Write the file
            # """
            file.make(fpath, fcontents, ftitle)
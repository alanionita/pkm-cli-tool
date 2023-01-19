import click
from pkmcli.generators import notes
from pkmcli.generators.store import pass_store
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

@pass_store
def cmd(notes_store, type, name):
    try:
        click.echo(f'CMD: Creating note of type ::: {type}')
        notes_location = notes_store.location 
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
    except BaseException as err:
        click.echo(f"Error [cmd.create] : Unexpected {err=}, {type(err)=}")
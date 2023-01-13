import click
from datetime import datetime
from utils import frontmatter, make_note_path, open_note_in_vscode


def create_note(filename, file_contents, title):
    note_path = make_note_path(filename)
    try:
        note_frontmatter = frontmatter.make(f'{title}')
        with open(note_path, 'x') as fp:
            fp.writelines(note_frontmatter)
            fp.write(file_contents)
            fp.close()
            open_note_in_vscode(note_path)
            pass

    except FileExistsError as err:
        click.echo(
            f'Error [create_note] : Note [{title}] already exists, opening note now')
        open_note_in_vscode(note_path)

    except BaseException as err:
        click.echo(f"Error [create_note] : Unexpected {err=}, {type(err)=}")


def make_note_daily():
    click.echo('making daily note')
    curr_date = datetime.now()
    note_path = curr_date.strftime('daily.%Y.%m.%d')
    note_title = curr_date.strftime('%Y-%m-%d')
    note_contents = ''
    create_note(note_path, note_contents, note_title)
    return


def make_note_other(type, name):
    """
    Deriving the path details
    """
    path_arr = name.split('.')
    path_last_part = path_arr[-1]

    """
    Creating note content
    """
    curr_date = datetime.now()
    note_path = curr_date.strftime(f'{type}.{name}')
    note_title = path_last_part
    note_contents = ''
    """
    Make the note
    """
    create_note(note_path, note_contents, note_title)
    return


def trigger_note_creation(type, name):
    if (type == 'daily'):
        make_note_daily()
    else:
        make_note_other(type, name)


cmd_note_types = ['daily', 'project', 'area',
                  'resource', 'archive']  # Excludes 'daily'


@click.command()
@click.option('--type', '-t', default="daily", type=click.Choice(cmd_note_types, case_sensitive=False), prompt='Enter type of note to create', help='Type of note')
@click.argument("name", required=False)
def cmd_create(type, name):
    click.echo(f'CMD: Creating note of type ::: {type}')
    trigger_note_creation(type, name)

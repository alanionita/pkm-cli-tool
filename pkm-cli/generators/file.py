import click
from . import path

def make(file_path, contents, title):
    try:
        with open(file_path, 'x') as file:
            file.writelines(title)
            file.write(contents)
            file.close()
            path.open_in(file_path, 'code')
            pass

    except FileExistsError as err:
        click.echo(
            f'Error [file.make] : Creation skipped, file [{title}] already exists. Opening file ...')
        path.open_in(file_path, 'code')

    except BaseException as err:
        click.echo(f"Error [file.make] : Unexpected {err=}, {type(err)=}")
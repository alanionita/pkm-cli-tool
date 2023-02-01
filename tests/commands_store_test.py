from click.testing import CliRunner
from pkmcli import main
import os

runner = CliRunner()
cwd = os.getcwd()
def test_store_status():
    store_status_res = runner.invoke(main.cli, ['store', 'status'])
    assert store_status_res.exit_code == 0
    store_path = store_status_res.output.split('\n')[0]
    return store_path

def test_store_change_fail():
    new_notes_store = f'{cwd}/notes_store'
    store_status_res = runner.invoke(main.cli, ['store', 'change', new_notes_store])
    assert store_status_res.exit_code != 0

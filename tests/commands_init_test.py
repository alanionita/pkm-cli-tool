from click.testing import CliRunner
from pkmcli import main
import unittest.mock
import datetime, os, pytest
from pkmcli.generators.store import build_context_path, get_project_base

runner = CliRunner()
mock_datetime = unittest.mock.Mock()
mock_datetime.now.return_value = datetime.datetime(2022, 10, 10)

def make_test_path():
    proj_base = os.getcwd()
    tests_path = 'tests/samples'
    return f'{proj_base}/{tests_path}'

@pytest.fixture(scope="session", autouse=True)
def before_all():
    store_status_res = runner.invoke(main.cli, ['store', 'status'])
    if (store_status_res.exit_code == 0):
        test_path = make_test_path()
        test_ctx = f'{test_path}/context.json'
        ctx_path = build_context_path(None, 'context')
        os.remove(test_ctx)
        if (os.path.exists(ctx_path)):
            os.remove(ctx_path)

def test_init():
    init_res = runner.invoke(main.cli, ['init'])
    assert init_res.exit_code == 0

def test_init_store():
    test_store_path = make_test_path()
    init_res = runner.invoke(main.cli, ['init', '--store', test_store_path])
    assert init_res.exit_code == 0

def test_init_errors():
    init_res = runner.invoke(main.cli, ['init'])
    assert init_res.exit_code == 1, 'Command should fail'
    includes_error = init_res.output.__contains__('Error');
    assert includes_error == True, 'Should include Error message'

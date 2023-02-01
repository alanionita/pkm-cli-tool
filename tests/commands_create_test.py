from click.testing import CliRunner
from pkmcli import main
from pkmcli.commands import create
import unittest.mock
import datetime
import pytest
import os

runner = CliRunner()
mock_datetime = unittest.mock.Mock()
mock_datetime.now.return_value = datetime.datetime(2022, 10, 10)
mock_project_name = 'live-test'

def get_store():
    store_status_res = runner.invoke(main.cli, ['store', 'status'])
    store_path = store_status_res.output.split('\n')[-2]
    return store_path

@pytest.fixture(scope="session", autouse=True)
def before_all():
    store_path = get_store()
    test_project_path = f'{store_path}/project.{mock_project_name}.md'
    if (os.path.exists(test_project_path)):
        os.remove(test_project_path)
    with unittest.mock.patch('datetime.datetime', mock_datetime):
        curr_date = datetime.datetime.now()
        daily_fname = curr_date.strftime('daily.%Y.%m.%d')
        test_daily_path = f'{store_path}/{daily_fname}.md'
        if (os.path.exists(test_daily_path)):
            os.remove(test_daily_path)

def test_create_daily():
    with unittest.mock.patch('datetime.datetime', mock_datetime):
        result = runner.invoke(main.cli, ['create', '--type', 'daily'])
        assert result.exit_code == 0

def test_create_project():
    result = runner.invoke(main.cli, ['create', '--type', 'project', mock_project_name])
    assert result.exit_code == 0
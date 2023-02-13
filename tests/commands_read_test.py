from click.testing import CliRunner
from paperclip import main
import unittest.mock
import datetime

runner = CliRunner()
mock_datetime = unittest.mock.Mock()
mock_datetime.now.return_value = datetime.datetime(2022, 10, 10)

def test_read_project():
    result = runner.invoke(main.cli, ['read', '--name', 'project.live-test'])
    assert result.exit_code == 0

def test_read_daily():
    with unittest.mock.patch('datetime.datetime', mock_datetime):
        curr_date = datetime.datetime.now()
        daily_path = curr_date.strftime('daily.%Y.%m.%d')
        result = runner.invoke(main.cli, ['read', '--name', daily_path])
        assert result.exit_code == 0
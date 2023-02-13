import os, pytest
import unittest.mock
from paperclip.generators.path import get_project_base, make, open_in

cwd = os.getcwd()   
def test_get_project_base():
    outcome = get_project_base()
    expected = f'{cwd}/src/paperclip'

    assert expected == outcome, 'Should return the correct project base'

    assert outcome.__contains__('paperclip') == True, 'Base project base should include the project name'

def test_make():
    test_base_path = cwd
    test_filename = 'test'
    test_filename_ext = 'md'
    expected = f'{test_base_path}/{test_filename}.{test_filename_ext}'
    outcome = make(test_base_path, test_filename)

    assert expected == outcome, 'Should make the correct path to the file.'

    assert outcome.__contains__(f'.{test_filename_ext}') == True, 'Path to file should include correct extension.'

    assert outcome.__contains__(test_filename) == True, 'Path to file should include correct filename.'

@unittest.mock.patch('os.system')
def test_open_in(mock_os_system):
    filename = f'{cwd}/tests/samples/project.test.md'
    expected_program = 'code'
    open_in(filename, expected_program);
    mock_os_system.assert_called_once_with(f'{expected_program} {filename}')

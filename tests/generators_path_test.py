import os, pytest
from pkmcli.generators.path import get_project_base, make

cwd = os.getcwd()   
def test_get_project_base():
    outcome = get_project_base()
    expected = f'{cwd}/src/pkmcli'

    assert expected == outcome, 'Should return the correct project base'

    assert outcome.__contains__('pkmcli') == True, 'Base project base should include the project name'

def test_make():
    test_base_path = cwd
    test_filename = 'test'
    test_filename_ext = 'md'
    expected = f'{test_base_path}/{test_filename}.{test_filename_ext}'
    outcome = make(test_base_path, test_filename)

    assert expected == outcome, 'Should make the correct path to the file.'

    assert outcome.__contains__(f'.{test_filename_ext}') == True, 'Path to file should include correct extension.'

    assert outcome.__contains__(test_filename) == True, 'Path to file should include correct filename.'

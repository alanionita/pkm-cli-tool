import os, pytest
from pkmcli.generators.path import get_project_base

def test_get_project_base():
    cwd = os.getcwd()
    outcome = get_project_base()
    expected = f'{cwd}/src/pkmcli'

    assert expected == outcome, 'Should return the correct project base'

    assert outcome.__contains__('pkmcli') == True, 'Base project base should include the project name'
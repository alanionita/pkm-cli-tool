import pytest, os
import unittest.mock
from pkmcli.generators import file
from pkmcli.generators import notes
from pkmcli.generators.store import get_location
from generators_store_test import make_test_store_path

@pytest.fixture(scope="session", autouse=True)
def before_all():
    cwd = os.getcwd()
    fpath = f'{cwd}/tests/samples/notes/project.test.pytest.md'
    if (os.path.exists(fpath)):
        os.remove(fpath)

def make_test_file():
    test_name = 'test.pytest'  # 30th February to make it stand out
    # ctx_filename = 'context'
    ctx_path = make_test_store_path()
    print(f'notes_location :: {ctx_path}')
    note = notes.make(ctx_path, 'project', test_name)
    fpath = note.get("path")
    fcontents = note.get("contents")
    ftitle = note.get("title")
    return {"path": fpath, "contents": fcontents, "title": ftitle}

@unittest.mock.patch('os.system')
def test_make(mock_os_system):
    note = make_test_file()
    if (note):
        fpath = str(note.get("path"))
        fcontents = str(note.get("contents"))
        ftitle = str(note.get("title"))
        file.make(fpath, fcontents, ftitle)
        expected_program = 'code'
        mock_os_system.assert_called_once_with(f'{expected_program} {fpath}')

        with open(fpath) as note:
            output = note.read()
            assert output.__contains__(ftitle) == True, 'Created file matches the passed in title.'

@unittest.mock.patch('os.system')
def test_make_errors_missing_params(mock_os_system):
    note = make_test_file()
    fpath = str(note.get("path"))
    fcontents = str(note.get("contents"))
    ftitle = str(note.get("title"))
    with pytest.raises(TypeError):
        file.make()  # type: ignore
    with pytest.raises(TypeError):
        file.make(fpath) # type: ignore
    with pytest.raises(TypeError):
        file.make(fpath, fcontents) # type: ignore
    with pytest.raises(FileExistsError):
        file.make(fpath, fcontents, ftitle) # type: ignore
    
    expected_program = 'code'
    mock_os_system.assert_called_once_with(f'{expected_program} {fpath}')
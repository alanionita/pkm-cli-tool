import os
import unittest.mock
from pkmcli.generators.file import make
from pkmcli.generators import notes
from pkmcli.generators.store import get_location
from generators_store_test import make_test_ctx_path


def make_test_file():
    test_name = 'test.pytest'  # 30th February to make it stand out
    ctx_filename = 'contextSamples'
    ctx_path = make_test_ctx_path(ctx_filename)
    notes_location = get_location(ctx_path)
    note = notes.make(notes_location, 'project', test_name)
    fpath = note.get("path")
    fcontents = note.get("contents")
    ftitle = note.get("title")
    make(fpath, fcontents, ftitle)
    return {"path": fpath, "contents": fcontents, "title": ftitle}


@unittest.mock.patch('os.system')
def test_file_make(mock_os_system):
    note = make_test_file()
    if (note):
        fpath = str(note.get("path"))
        # fcontents = str(note.get("contents"))
        ftitle = str(note.get("title"))

        expected_program = 'code'
        mock_os_system.assert_called_once_with(f'{expected_program} {fpath}')

        with open(fpath) as file:
            output = file.read()
            assert output.__contains__(ftitle) == True, 'Created file matches the passed in title.'
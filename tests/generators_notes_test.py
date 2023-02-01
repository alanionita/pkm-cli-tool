import re, datetime
import unittest.mock
from pkmcli.generators import notes
from pkmcli.generators.store import get_location
from generators_store_test import make_test_ctx_path

def test_other():
    ctx_path = make_test_ctx_path('contextSamples')
    notes_location = get_location(ctx_path)
    test_name = 'notes-test'
    test_type = 'resource'
    note = notes.make(notes_location, test_type, test_name)
    fpath = note.get("path")
    ftitle = note.get("title")
    fcontents = note.get("contents")
    expectedfpath = f'{notes_location}/{test_type}.{test_name}.md'
    expectedftitle = f'# {test_name.title()}'

    assert fpath == expectedfpath, 'Should match the given path'
    assert ftitle == expectedftitle, 'Should match the given title'

    if(fcontents):
        first_line = fcontents[0]
        second_last_line = fcontents[-2]
        last_line = fcontents[-1]
        assert first_line == second_last_line, 'First and last lines should match.'

        expected_pattern = '---\n'
        newline_pattern = '\n'
        first_line_match = re.search(expected_pattern, first_line)
        second_last_line_match = re.search(expected_pattern, second_last_line)
        last_line_match = re.search(newline_pattern, last_line)
        assert first_line_match != None, 'First line should match {expected_pattern} pattern.'
        assert second_last_line_match != None, 'Second to last line should match {expected_pattern} pattern.'
        assert last_line_match != None, 'Last line should be an empty \n.'

        for fcontentsline in fcontents:
            has_id = fcontentsline.__contains__('id:')
            has_title = fcontentsline.__contains__('title:')
            has_desc = fcontentsline.__contains__('desc:')
            has_updated = fcontentsline.__contains__('updated:')
            has_created = fcontentsline.__contains__('created:')
            has_type = fcontentsline.__contains__('type:')

            if has_id: assert has_id == True, 'Note contents should include an id value'
            if has_title: assert has_title == True, 'Note contents should include a title value'
            if has_desc: assert has_desc == True, 'Note contents should include a desc value'
            if has_updated: assert has_updated == True, 'Note contents should include an updated value'
            if has_created: assert has_created == True, 'Note contents should include a created value'
            if has_type: assert has_type == True, 'Note contents should include a type value'

def test_daily():
    ctx_path = make_test_ctx_path('contextSamples')
    notes_location = get_location(ctx_path)
    test_name = 'notes-test'
    test_type = 'daily'
    # create a mock datetime object
    mock_datetime = unittest.mock.Mock()
    mock_datetime.now.return_value = datetime.datetime(2022, 10, 10)
    fcontents = ''

    # use the mock datetime object to replace the real datetime object
    with unittest.mock.patch('datetime.datetime', mock_datetime):
        
        note = notes.make(notes_location, test_type, test_name)
        
        fpath = note.get("path")
        ftitle = note.get("title")
        fcontents = note.get("contents")
        print(f'fpath :: {fpath}')
        curr_date = datetime.datetime.now()
        daily_path = curr_date.strftime('daily.%Y.%m.%d')
        expectedfpath = f'{notes_location}/{daily_path}.md'
        assert fpath == expectedfpath, 'Should match the given path'
        
        expectedftitle = f'# {test_type.title()} note'
        assert ftitle == expectedftitle, 'Should match the Daily title'
        


    if(fcontents):
        first_line = fcontents[0]
        second_last_line = fcontents[-2]
        last_line = fcontents[-1]
        assert first_line == second_last_line, 'First and last lines should match.'

        expected_pattern = '---\n'
        newline_pattern = '\n'
        first_line_match = re.search(expected_pattern, first_line)
        second_last_line_match = re.search(expected_pattern, second_last_line)
        last_line_match = re.search(newline_pattern, last_line)
        assert first_line_match != None, 'First line should match {expected_pattern} pattern.'
        assert second_last_line_match != None, 'Second to last line should match {expected_pattern} pattern.'
        assert last_line_match != None, 'Last line should be an empty \n.'
        
        for fcontentsline in fcontents:
            has_id = fcontentsline.__contains__('id:')
            has_title = fcontentsline.__contains__('title:')
            has_desc = fcontentsline.__contains__('desc:')
            has_updated = fcontentsline.__contains__('updated:')
            has_created = fcontentsline.__contains__('created:')
            has_type = fcontentsline.__contains__('type:')

            if has_id: assert has_id == True, 'Note contents should include an id value'
            if has_title: assert has_title == True, 'Note contents should include a title value'
            if has_desc: assert has_desc == True, 'Note contents should include a desc value'
            if has_updated: assert has_updated == True, 'Note contents should include an updated value'
            if has_created: assert has_created == True, 'Note contents should include a created value'
            if (has_type): 
                print(f'fcontentsline ::', fcontentsline)
                assert has_type == True, 'Note contents should include a type value'
                assert fcontentsline.__contains__('type: daily') == True, 'Note contents should include a type value of daily'

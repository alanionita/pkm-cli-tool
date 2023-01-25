from typing import List
import re
import pytest
from pkmcli.generators import fm

fake_note_type = 'daily'
fake_daily_title = '2023-01-15'


def test_make():
    output = fm.make(fake_daily_title, fake_note_type)

    """
    Test general output shape
    """

    assert isinstance(output, List), 'Output should return a List.'

    """
    Test each line of the output
    """

    for line in output:
        assert isinstance(line, str), 'Output should return a List of Strings'

    """
    Test the beginning and ending Frontmatter patterns
    """
    first_line = output[0]
    second_last_line = output[-2]
    last_line = output[-1]
    assert first_line == second_last_line, 'First and last lines should match.'
    expected_pattern = '---\n'
    newline_pattern = '\n'
    first_line_match = re.search(expected_pattern, first_line)
    second_last_line_match = re.search(expected_pattern, second_last_line)
    last_line_match = re.search(newline_pattern, last_line)
    assert first_line_match != None, 'First line should match {expected_pattern} pattern.'
    assert second_last_line_match != None, 'Second to last line should match {expected_pattern} pattern.'
    assert last_line_match != None, 'Last line should be an empty \n.'

    """
    Test contents of the Frontmatter
    """
    combined_output = ''.join(output)
    has_id = combined_output.__contains__('id: ')
    has_title = combined_output.__contains__('title: ')
    has_desc = combined_output.__contains__('desc: ')
    has_updated = combined_output.__contains__('updated: ')
    has_created = combined_output.__contains__('created: ')
    has_type = combined_output.__contains__('type: ')
    assert has_id == True, 'Frontmatter should contain an id property'
    assert has_title == True, 'Frontmatter should contain a title property'
    assert has_desc == True, 'Frontmatter should contain a desc property'
    assert has_updated == True, 'Frontmatter should contain an updated property'
    assert has_created == True, 'Frontmatter should contain an created property'
    assert has_type == True, 'Frontmatter should contain an note type property'


def test_make_errors():
    """
    TODO: Test error states
    """
    with pytest.raises(TypeError):
        fm.make()  # type: ignore

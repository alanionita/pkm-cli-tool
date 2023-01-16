from typing import List
import re
import pytest
from pkmcli.generators import fm

def test_make():
    fake_daily_title = '2023-01-15'
    output = fm.make(fake_daily_title)
    
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
    last_line = output[-1]
    assert first_line == last_line, 'First and last lines should match.'
    expected_pattern = '---\n'
    first_line_match = re.search(expected_pattern, first_line)
    last_line_match = re.search(expected_pattern, last_line)
    assert first_line_match != None, 'First line matches Frontmatter pattern.'
    assert last_line_match != None, 'Last line matches Frontmatter pattern.'
    
    """
    Test contents of the Frontmatter
    """
    combined_output = ''.join(output);
    has_id = combined_output.__contains__('id: ');
    has_title = combined_output.__contains__('title: ');
    has_desc = combined_output.__contains__('desc: ');
    has_updated = combined_output.__contains__('updated: ');
    has_created = combined_output.__contains__('created: ');
    assert has_id == True, 'Frontmatter contains an id property'
    assert has_title == True, 'Frontmatter contains a title property'
    assert has_desc == True, 'Frontmatter contains a desc property'
    assert has_updated == True, 'Frontmatter contains an updated property'
    assert has_created == True, 'Frontmatter contains an created property'

def test_make_errors(): 
    """
    TODO: Test error states
    """
    with pytest.raises(TypeError):
        fm.make()
from collections import UserList 
from typing import List
import re
from . import fm

def test_make():
    fake_daily_title = '2023-01-15'
    output = fm.make(fake_daily_title)
    print(f'test_make / output :: {output}')
    
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
    TODO: Test contents of the Frontmatter
    """

    """
    TODO: Test error states
    """

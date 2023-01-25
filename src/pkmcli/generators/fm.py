import ulid
import yaml
import re
from pprint import pprint


"""
Makes the Frontmatter component of the note
"""


def make(title, note_type):
    id = ulid.new()
    timestamp = id.timestamp().int  # international format
    return [
        '---\n',
        f'id: {id}\n',
        f'title: {title}\n',
        'desc: ""\n',
        f'updated: {timestamp}\n',
        f'created: {timestamp}\n',
        f'type: {note_type}\n',
        '---\n', '\n']


"""
Pretty prints the Frontmatter metadata
"""


def print_metadata(file):
    fm_regex = "^---\n(.*?)\n---"
    fm_match = re.search(fm_regex, file, re.DOTALL)
    if (fm_match):
        fm_str = fm_match.group(1)  # Only take the first block
        fm_note = yaml.safe_load(fm_str)
        pprint(fm_note)

import ulid
import yaml
import re
from pprint import pprint


def make(title, note_type):
    # ---
    # id: 3reyhx4v2qz08p4bwi644c5
    # title: '2022-10-20'
    # desc: ''
    # updated: 1666288907825
    # created: 1666288907825
    # traitIds:
    # - journalNote
    # ---
    id = ulid.new()
    timestamp = id.timestamp().int  # international format
    return [
        '---\n',
        f'id: {id}\n',
        f'title: {title}\n',
        'desc: ""\n',
        f'updated: {timestamp}\n',
        f'created: {timestamp}\n',
        f'type: {note_type}\n'
        '---\n', '\n']


def print_metadata(file):
    fm_regex = "^---\n(.*?)\n---"
    fm_match = re.search(fm_regex, file, re.DOTALL)
    if (fm_match):
        fm_str = fm_match.group(1)  # Only take the first block
        fm_note = yaml.safe_load(fm_str)
        pprint(fm_note)

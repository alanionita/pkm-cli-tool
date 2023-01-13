import ulid
import frontmatter
from pprint import pprint

def make(title):
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
    id_str = str(id)
    timestamp = id.timestamp().int # international format
    return [
        '---\n', 
        f'id: {id}\n', 
        f'title: {title}\n', 
        'desc: ""\n',
        f'updated: {timestamp}\n',
        f'created: {timestamp}\n',
        '---\n']

def print_metadata(note):
    fm_note = frontmatter.load(note)
    pprint(fm_note.metadata)
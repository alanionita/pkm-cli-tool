import os, pytest
from pkmcli.generators.store import get_location, set_location, build_context_path

cwd = os.getcwd()

def make_test_ctx_path(file_name):
    base_path = f'{cwd}/tests/samples'
    ctx_path = build_context_path(base_path, file_name)
    return ctx_path

def make_test_store_path():
    base_path = f'{cwd}/tests/samples/notes'
    return base_path

def test_get_location() -> None:
    ctx_path = make_test_ctx_path('contextValid')
    ctx_result = get_location(ctx_path)
    assert ctx_result == 'test', 'Should retrieve the ctx value.'
    
def test_get_location_errors():
    """
    Should throw KeyError when called with wrong arguments
    """
    with pytest.raises(KeyError):
        ctx_path = make_test_ctx_path('contextError')
        get_location(ctx_path)

def test_set_location():
    '''
    Get location and test it
    '''
    test_get_location()

    '''
    Set location and test it (via get_location() )
    '''
    ctx_path = make_test_ctx_path('contextValid')
    store_path = make_test_store_path()
    set_location(ctx_path, store_path)
    ctx_location = get_location(ctx_path)
    assert ctx_location == store_path, 'Should correctly update the store path to tests/samples/notes'

    '''
    Reset location to default : "test"
    '''
    set_location(ctx_path, 'test')

def test_build_context_path():
    '''
    Should test context path creation
    - when build_context_path is called with a base path
    '''
    cwd = os.getcwd()
    test_path = f'{cwd}/tests/samples'
    test_filename = 'contextValid'
    ctx_path = build_context_path(test_path, test_filename)
    expected = f'{test_path}/{test_filename}.json'
    assert ctx_path == expected, 'Should create the correct context path'

    '''
    Should test default context path creation
    - when build_context_path is called without a base path
    '''

    default_filename = 'context'
    ctx_path = build_context_path(default_filename)

    assert ctx_path.__contains__(cwd) == True, 'Default path should contain the current working directory'

    assert ctx_path.__contains__(default_filename) == True, 'Default path should contain the file_name'

    assert ctx_path == f'{cwd}/context/{default_filename}.json', 'Default path should match expected format'

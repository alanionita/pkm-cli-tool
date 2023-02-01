from click.testing import CliRunner
from pkmcli import main
import os
import unittest

runner = CliRunner()
cwd = os.getcwd()

class CmdStoreTests (unittest.TestCase):
    def test_store_status(self):
        store_status_res = runner.invoke(main.cli, ['store', 'status'])
        self.assertEqual(store_status_res.exit_code, 0)
        store_path = store_status_res.output.split('\n')[0]
        return store_path

    def test_store_change_fail(self):
        new_notes_store = f'{cwd}/notes_store'
        store_status_res = runner.invoke(main.cli, ['store', 'change', new_notes_store])
        self.assertNotEqual(store_status_res.exit_code, 0)

    def test_store_change(self):
        old_notes_store = self.test_store_status()
        store_change_input = f'{cwd}/notes_store'
        store_status_res = runner.invoke(main.cli, ['store', 'change', '--location', store_change_input])
        self.assertEqual(store_status_res.exit_code, 0)
        
        new_store_path = store_status_res.output.split('\n')[-2]
        self.assertNotEqual(old_notes_store, new_store_path, 'Should have replaced the old store path') 
        self.assertEqual(store_change_input, new_store_path, 'Should match input path')
    


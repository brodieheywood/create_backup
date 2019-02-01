from unittest import TestCase
from comp_1510_a2 import q03


class TestBackup(TestCase):
    def test_backup(self):
        q03.backup('backup_test.txt')
        with open('backup_test.txt', 'r') as file:
            ob = file.read()

        with open('backup_test.bak', 'r') as file_2:
            b1 = file_2.read()

        self.assertEqual(ob, b1)

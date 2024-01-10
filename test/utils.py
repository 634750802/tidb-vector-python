import unittest
from itertools import repeat
from typing import Union

from tidb_vector.utils import assert_legal_table_name


class TestUtils(unittest.TestCase):
    def test_assert_safe_table_name(self):

        def make_case(should_raise: bool, table_name: str):
            def c():
                assert_legal_table_name(table_name)

            if should_raise:
                self.assertRaises(AssertionError, c)
            else:
                c()

        make_case(True, '1able')
        make_case(True, 'table我')
        make_case(True, 'table-')
        make_case(True, 'table;')
        make_case(True, ''.join(repeat('a', 65)))
        make_case(False, 'table_name')
        make_case(False, '_table_name')
        make_case(False, ''.join(repeat('a', 64)))

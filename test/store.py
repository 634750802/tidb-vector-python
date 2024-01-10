import unittest

from testutils import format_sql
from tidb_vector import VectorStore


class TestVectorStore(unittest.TestCase):
    def test_sql(self):
        store = VectorStore(
            port=3306,
            table_name_prefix='t_'
        )
        sql = store._VectorStore__get_show_create_table_sql('table')
        self.assertEqual(format_sql(sql), 'SHOW CREATE TABLE t_table;')

        sql = store._VectorStore__get_create_table_sql('table')
        self.assertEqual(format_sql(sql),
                         'CREATE TABLE t_table ( id VARCHAR(64) NOT NULL, vector VECTOR NOT NULL, content LONGTEXT NOT NULL, metadata JSON NOT NULL, PRIMARY KEY (id) );')

        sql = store._VectorStore__get_show_create_table_sql('table')
        self.assertEqual(format_sql(sql), 'SHOW CREATE TABLE t_table;')

        sql = store._VectorStore__get_list_table_sql()
        self.assertEqual(format_sql(sql), 'SHOW TABLES LIKE \'t_%\';')

        sql = store._VectorStore__get_drop_table_sql('table')
        self.assertEqual(format_sql(sql), 'DROP TABLE t_table;')

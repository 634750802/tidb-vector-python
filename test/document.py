import unittest

from tidb_vector import VectorDocument


class TestVectorDocument(unittest.TestCase):
    def test_init(self):
        doc = VectorDocument('abc', [1, 2, 3], 'abccccc', {})
        self.assertEqual(doc.id, 'abc')
        self.assertEqual(doc.vector, [1,2,3])
        self.assertEqual(doc.content, 'abccccc')
        self.assertEqual(doc.metadata, {})

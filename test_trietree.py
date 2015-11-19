import unittest
from datastructs.trees import *

class TestTrieTree(unittest.TestCase):

    def setUp(self):
        self.trie = AlphaTrieTree()

    def test_search(self):
        pass

    def test_node_getword(self):
        self.trie.insert('hello')
        self.assertEqual(self.trie.last_inserted_node.get_word(), 'hello')
        self.trie.insert('WoRld')
        self.assertEqual(self.trie.last_inserted_node.get_word(), 'world')

    def test_insert_and_search(self):
        self.trie.insert('hello')
        self.trie.insert('WoRld')
        self.assertTrue(self.trie.search('hello') is True)
        self.assertTrue(self.trie.search('Hello') is True)
        self.assertTrue(self.trie.search('wORLD') is True)
        self.assertTrue(self.trie.search('World') is True)
        self.assertTrue(self.trie.search('Wor  ld') is True)
        pass

if __name__ == '__main__':
    unittest.main()
import unittest
from datastructs.trees import *

class TestTrieTree(unittest.TestCase):

    def setUp(self):
        self.trie = AlphaTrieTree()

    def test_node_getword(self):
        # insert the word and assert that the node's word lookup matches
        # the added word
        searchterms = ['hello', 'MonTy', 'WORLD']
        for searchterm in searchterms:
            self.trie.insert(searchterm)
            self.assertEqual(self.trie.last_inserted_node._lookup_word(), 
                             searchterm.lower())

    def test_search(self):
        self.trie.insert('hello')
        self.trie.insert('WoRld')
        self.assertTrue(self.trie.search('hello'))
        self.assertTrue(self.trie.search('Hello'))
        self.assertTrue(self.trie.search(' wOR LD'))
        self.assertTrue(self.trie.search('World'))
        self.assertTrue(self.trie.search('Wor  ld'))

    def test_remove1(self):
        # case insensitive removal
        self.trie.insert('hello')
        self.trie.insert('baker')
        self.trie.remove('hello')
        self.assertFalse(self.trie.search('hello'))
        self.trie.remove('bAKER')
        self.assertFalse(self.trie.search('bAKER'))
        self.assertFalse(self.trie.search('baker'))

    def test_remove2(self):
        # assert that 'world' should not exist even though worldwings is still in
        self.trie.insert('worldwings')
        self.trie.insert('world')
        self.trie.remove('world')
        self.assertFalse(self.trie.search('world'))
        self.assertTrue(self.trie.search('worldwings'))

    def test_remove3(self):
        # assert that removing the larger word will still keep the smaller word
        self.trie.insert('worldwings')
        self.trie.insert('world')
        self.trie.remove('world')
        self.assertFalse(self.trie.search('world'))
        self.trie.insert('world')
        self.assertTrue(self.trie.search('world'))
        self.trie.remove('worldwings')
        self.assertFalse(self.trie.search('worldwings'))
        self.assertTrue(self.trie.search('world'))

    def test_remove_inbetween(self):
        self.trie.insert('back')
        self.trie.insert('backrub')
        self.trie.insert('backrubber')
        self.assertTrue(self.trie.search('back'))
        self.assertTrue(self.trie.search('backrub'))
        self.assertTrue(self.trie.search('backrubber'))
        self.trie.remove('backrub')
        self.assertTrue(self.trie.search('back'))
        self.assertFalse(self.trie.search('backrub'))
        self.assertTrue(self.trie.search('backrubber'))



    def test_properties(self):
        # TODO assert that all leaves should have _word ie that the words they
        # represent are "in" the tree
        pass

if __name__ == '__main__':
    unittest.main()
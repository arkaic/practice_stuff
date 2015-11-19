import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datastructs.trees import *

def findWords(board, words):
    """ https://leetcode.com/problems/word-search-ii/
    Implementing this with a trie tree wasn't really needed, as I could have 
    just compared the words found during the recursive traversal to what was 
    given in words and add that to an output list. It would have been more 
    efficient that way, but I wanted to demonstrate that my trie tree worked :)
    """

    tree = AlphaTrieTree()
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            # for each letter, depth first search and add all possibles into tree
            snake(board, tree, (i, j))

    found_words = []
    print(len(tree.root._get_children()))
    for word in words:
        if tree.search(word):
            found_words.append(word)
    return found_words


def snake(board, tree, start):
    def traverse(coord, visited, letters):
        """ Nested recursive depth first search """
        r, c = coord
        height = len(board)
        width = len(board[0])

        # Mark this cell visited and add the word we have into the trie tree
        visited[height * r + c] = 1
        letters.append(board[r][c])
        tree.insert(letters)

        # Go to each adjacent neighbor if within the board and not visited
        if r - 1 >= 0 and visited[height * (r-1) + c] == 0:
            traverse(((r - 1), c), visited, letters)
        if r + 1 < height and visited[height * (r+1) + c] == 0: 
            traverse(((r + 1), c), visited, letters)
        if c - 1 >= 0 and visited[height * r + c - 1] == 0:
            traverse((r, (c - 1)), visited, letters)
        if c + 1 < width and visited[height * r + c + 1] == 0:
            traverse((r, (c + 1)), visited, letters)

        # Clean up before recursive function ends: remove this letter and unvisit
        letters.pop()
        visited[height * r + c] = 0
    #------------------------------END FUNCTION---------------------------------

    # visited is a vector representation of the board to record visited cells
    # during traversal
    visited = [0] * len(board) * len(board[0])
    traverse(start, visited, list())

def run():
    board = [['o','a','a','n'],
             ['h','t','a','e'],
             ['i','a','k','r'],
             ['p','e','a','v']]
    words = ["oath","pea","eat","rain"]
    result = ['eat', 'pea', 'oath']

    # compute
    found_words = findWords(board, words)
    print(found_words)

    # Assertions
    if len(found_words) != len(result):
        print("Assert failed: length of found words != length of result")
        return
    for word in found_words:
        if word not in result:
            print("Assert failed, exiting")
            return
        result.remove(word)

    print('Program works')

if __name__ == '__main__':
    run()
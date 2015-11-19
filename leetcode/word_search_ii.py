import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datastructs.trees import *

def findWords(board, words):
    tree = AlphaTrieTree()

    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            # for each letter, add to the first level of trie tree and depth
            # first search and add all possibles into the tree
            snake(board, tree, (i, j))

    found_words = []
    for word in words:
        if tree.search(word):
            found_words.append(word)
    return found_words


def snake(board, tree, start):
    def recurse(coord, visited, letters):
        height = len(board)
        width = len(board[0])
        r, c = coord
        visited[height * r + c] = 1
        letters.append(board[r][c])
        tree.insert("".join(letters))

        if r - 1 >= 0 and visited[height * (r-1) + c] == 0:
            recurse(((r - 1), c), visited, letters)
        if r + 1 < height and visited[height * (r+1) + c] == 0: 
            recurse(((r + 1), c), visited, letters)
        if c - 1 >= 0 and visited[height * r + c - 1] == 0:
            recurse((r, (c - 1)), visited, letters)
        if c + 1 < width and visited[height * r + c + 1] == 0:
            recurse((r, (c + 1)), visited, letters)

        visited[height * r + c] = 0
        letters.pop()
    #------------------------------END FUNCTION---------------------------------

    visited = [0] * len(board) * len(board[0])
    recurse(start, visited, list())

def run():
    board = [['o','a','a','n'],
             ['e','t','a','e'],
             ['i','h','k','r'],
             ['i','f','l','v']]
    words = ["oath","pea","eat","rain"]
    result = ['eat', 'oath']

    found_words = findWords(board, words)
    print(found_words)
    for word in found_words:
        if word not in result:
            print("Assert failed, exiting")
            return
        result.remove(word)
    print('Program works')

if __name__ == '__main__':
    run()
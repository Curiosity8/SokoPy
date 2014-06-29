# Implements Zobrist Hashing.

import random


global hashbox
global hashman
global hashgoal


hashsize = pow(2, 28)
# Setting the hashsize

def init_hash(board):
    # Initialize the random bitstrings.
    global hashman
    global hashbox
    global hashgoal
    hashman = {}
    hashbox = {}
    hashgoal = {}
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            hashman[(i,j)] = random.randrange(1, hashsize)
            hashbox[(i,j)] = random.randrange(1, hashsize)
            hashgoal[(i,j)] = random.randrange(1, hashsize)
    


    #return hashman, hashbox



def gethash(board):
    # Get the hash for the board which will be unique.
    boardhash = 0

    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if board[i][j] == '@':
                boardhash ^= hashman[(i,j)]

            if board[i][j] == '+':
                boardhash ^= hashman[(i,j)]
                boardhash ^= hashgoal[(i,j)]

            if board[i][j] == '$':
                boardhash ^= hashbox[(i,j)]

            if board[i][j] == '*':
                boardhash ^= hashbox[(i,j)]
                boardhash ^= hashgoal[(i,j)]
                


    return boardhash




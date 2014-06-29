# Testing new idea...

from Stack import *
from SokobanDFS import *
from position import *
import sys
from deadlocks import *
#from pympler.asizeof import *
from zobrist import *
from FreezeDeadlock import *

def solveDFS(board):
    pos = position(board)

    init_hash(board)
    
    start = SokobanDFS(board, None)
    start.x = pos['S'][0]
    start.y = pos['S'][1]
    start.letter = ''
    q = Stack()
    q.push(start)

    visited = set()

    visited.add(gethash(board))
    #visited.add(tuple(board))

    visited2, boxpos = calc(board)

    #path = ''
    while len(q) != 0:
        top = q.pop()
        #path += top.letter
        
        if top.solved():
            path = []
            path += [top.letter]

            while top.soko != None:
                top = top.soko
                path += [top.letter]

            path.reverse()
            s = ''.join([i for i in path])
            print len(visited)
            print len(q)
            #print asizeof(visited)
            #print len(q)
            #print asizeof(q)
            #print '========='

            #print len(s)
            return s


        if easy(top.board) == True:
            ## Check easy deadlock
            continue

        if simpleDead(top, visited2) == True:
            continue

        top.move(visited, q)

        if freezeDead(top.board, visited2) == True:
            continue
     

    return -1



four = ['########',
        '#      #',
        '# .**$@#',
        '#      #',
        '#####  #',
        '    ####']



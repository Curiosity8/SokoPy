from Sokoban import *
from position import *
import sys
from deadlocks import *
#from tunnel import *
#from pympler.asizeof import *
import random
from zobrist import *
#from deadlockTable import *
from FreezeDeadlock import *





def solve(board):
    pos = position(board)

    init_hash(board)
    # First, we initialize the bitstring.
    
    start = Sokoban(board, 0,0, None)
    start.x = pos['S'][0]
    start.y = pos['S'][1]
    start.letter = ''
    q = []
    heapq.heappush(q, start)

    visited = set()
    visited.add(gethash(board))
    #x,y = pos['S'][0], pos['S'][1]

    visited2, boxpos = calc(board)
    # visited2 is a set that will be used for simple deadlock detection. 
    # See deadlock.py for more details.

    
    path = ''
    while len(q) != 0:
        top = heapq.heappop(q)
        
        if top.solved():
            path = []
            path += [top.letter]

            while top.soko != None:
                # Now retrace the path
                top = top.soko
                path += [top.letter]

            path.reverse()
            s = ''.join([i for i in path])
            #print asizeof(visited)
            #print asizeof(q)
            return s, len(visited)


        if easy(top.board) == True:
            continue

        if simpleDead(top, visited2) == True:
            continue

        
        top.move(visited, q)

        if freezeDead(top.board, visited2) == True:
            continue

        
    print len(visited)
    return 'IMPOSSIBLE', len(visited)



def test():
    print solve(four)

four = ['########',
        '#      #',
        '# .**$@#',
        '#      #',
        '#####  #',
        '    ####']


eight = ['  ######',
         '  # ..@#',
         '  # $$ #',
         '  ## ###',
         '   # #  ',
         '   # #  ',
         '#### #  ',
         '#    ## ',
         '# #   # ',
         '#   # # ',
         '###   # ',
         '  ##### ']



m = ['#######',
     '#.   ##',
     '#*$ $ #',
     '#+*   #',
     '#######']


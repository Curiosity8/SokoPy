from Stack import *
from Sokoban import *
from position import *
from Node import *

def easy(board):
    # This is a subclass of freeze deadlock positions..
    
    """

            j j+1

    i       #  #
    i+1     $  $

    $$
    ##

    #$
    #$

    $#
    $#

    $$
    $$

    """
               #    #     #B    B#
              #B    B#     #    #


    for i in xrange(len(board)-1):
        for j in xrange(len(board[0]) - 1):
            if board[i][j] == '#' and board[i][j+1] == '#' and board[i+1][j] == '$' and board[i+1][j+1] == '$':
                return True

            if board[i][j] == '$' and board[i][j+1] == '$' and board[i+1][j] == '#' and board[i+1][j+1] == '#':
                return True
            
            if board[i][j] == '#' and board[i][j+1] == '$' and board[i+1][j] == '#' and board[i+1][j+1] == '$':
                return True

            if board[i][j] == '$' and board[i][j+1] == '#' and board[i+1][j] == '$' and board[i+1][j+1] == '#':
                return True


            if board[i][j] == '$' and board[i][j+1] == '$' and board[i+1][j] == '$' and board[i+1][j+1] == '$':
                return True




            if board[i][j+1] == '#' and board[i+1][j] == '#' and board[i+1][j+1] == '$':
                return True

            if board[i][j] == '#' and board[i+1][j] == '$' and board[i+1][j+1] == '#':
                return True

            if board[i][j] == '#' and board[i][j+1] == '$' and board[i+1][j+1] == '#':
                return True

            if board[i][j] == '$' and board[i][j+1] == '#' and board[i+1][j] == '#':
                return True



            """
          
             j  j+1
             i   #  #     ##  *$  $*  
            i+1  *  $     $*  ##  ##

            #$  #*  $#  *#
            #*  #$  *#  $#

            """
            if board[i][j] == '#' and board[i][j+1] == '#' and board[i+1][j] == '*' and board[i+1][j+1] == '$':
                return True

            if board[i][j] == '#' and board[i][j+1] == '#' and board[i+1][j] == '$' and board[i+1][j+1] == '*':
                return True

            if board[i][j] == '*' and board[i][j+1] == '$' and board[i+1][j] == '#' and board[i+1][j+1] == '#':
                return True

            if board[i][j] == '$' and board[i][j+1] == '*' and board[i+1][j] == '#' and board[i+1][j+1] == '#':
                return True


            if board[i][j] == '#' and board[i][j+1] == '$' and board[i+1][j] == '#' and board[i+1][j+1] == '*':
                return True

            if board[i][j] == '#' and board[i][j+1] == '*' and board[i+1][j] == '#' and board[i+1][j+1] == '$':
                return True

            if board[i][j] == '$' and board[i][j+1] == '#' and board[i+1][j] == '*' and board[i+1][j+1] == '#':
                return True

            if board[i][j] == '*' and board[i][j+1] == '#' and board[i+1][j] == '$' and board[i+1][j+1] == '#':
                return True




            
def DFS(board, endpos):
    # Starting at the pos of '.' do DFS, and keep updating v2.
    v2 = set()
    x,y = endpos[0], endpos[1]
    v2.add((x,y))
    q = Stack()

    start = Node(x,y)

    q.push(start)

    while len(q) != 0:
        top = q.pop()

        for direction in vector:
            u,v = direction[0], direction[1]
            newX = top.x + u
            newY = top.y + v
            new2X = newX + u
            new2Y = newY + v

            oppositeX = top.x - u
            oppositeY = top.y - v

            if 0 <= new2X < len(board) and 0 <= new2Y < len(board[0]) and 0 <= oppositeX < len(board) and 0 <= oppositeY < len(board[0]):
                # Checking the boundary conditions....
                #if board[newX][newY] != '#':

                if board[new2X][new2Y] != '#' and board[newX][newY] != '#':
                    #if board[oppositeX][oppositeY] != '#':
                    if (newX, newY) not in v2:
                        current = Node(newX, newY)
                        q.push(current)
                        v2.add((newX, newY))
      

    return v2


def calc(board):
    # Calculate the possible positions of boxes, with reverse DFS.
    # It returns a set of possible pos, along with pos of endstates.
    # pos I mean a tuple (x,y)
    
    pos = position(board)

    boxpos = pos['T']

    visited2 = set()

    for i in xrange(len(boxpos)):
        box = boxpos[i]
        a,b = box[0], box[1]
        visited2 = visited2.union(DFS(board, (a,b)))


    return visited2, boxpos


def simpleDead(sokoban, visited2):
    #visited2, boxpos = calc(sokoban.board)

    boxpos = position(sokoban.board)['B']

    for i in boxpos:
        if i not in visited2:
            return True

    return False




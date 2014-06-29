from Node import *
from position import *
from Stack import *
from Functions import *

########### Freeze Deadlocks ##########
# Disclaimer : I'm not 100% certain that this is correct.


def onetwocheck(board, box_x, box_y, v):
    # Returns False if you can move horizontally or vertically.
    # Returns True if you can't move. i.e. freeze deadlock.

    vert = False
    horz = False

    if (board[box_x][box_y + 1] == '#' or board[box_x][box_y - 1] == '#') and (board[box_x + 1][box_y] == '#' or board[box_x - 1][box_y] == '#'):
        # Horizontal movement and vertical movement not possible

        return True

    
    # check for vertical movement or horizontal movement... are they possible?
    if (board[box_x][box_y + 1] == ' ' or board[box_x][box_y + 1] == '.') and (board[box_x][box_y - 1] == ' ' or board[box_x][box_y - 1] == '.'):
        #print 'horz is True'

        horz = True

    if (board[box_x + 1][box_y + 1] == ' ' or board[box_x + 1][box_y + 1] == '.') and (board[box_x - 1][box_y] == ' ' or board[box_x - 1][box_y] == '.'):
        #print 'Vert is True'
        vert = True


    if vert == True or horz == True:
        return -1



    if (box_x, box_y + 1) not in v and (box_x, box_y - 1) not in v and (box_x + 1, box_y) not in v and (box_x - 1, box_y) not in v:
        return True



    return False


#        ? $ ?
#        D   D


def freeze(b, x, y, v3):
    # Returns False if the current box on (x,y) is not in freeze deadlock
    # Returns True if the current box on (x,y) is a freeze deadlock

    #print vert, horz


    if onetwocheck(b, x, y, v3) == -1:
        return False
    
    if onetwocheck(b, x, y, v3) == True:
        return True



    board = b[:]
    visited = set()

    q = Stack()
    start = Node(x,y)
    q.push(start)
    
    while len(q) != 0:
        top = q.pop()
        
        for direction in vector:
            u = direction[0]
            v = direction[1]
            newX = top.x + u
            newY = top.y + v

            if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and (board[newX][newY] == '$' or board[newX][newY] == '*'):
                #print visited
                #print newX, newY

                if (newX, newY) not in visited:
                    visited.add((newX, newY))
                    #newboard = board[:]
                    
                    cur = Node(newX, newY)
                    q.push(cur)
                    board[top.x] = put(board[top.x], top.y, '#')
                    # Treat the previous box as a wall...
                    
                    if onetwocheck(board, newX, newY, v3) == True:
                        return True


    return False

                    
def freezeDead(board, v):
    pos = position(board)
    adjBoxes = []

    start = pos['S']
    x, y = start[0], start[1]

    for direction in vector:
        u1 = direction[0]
        v1 = direction[1]
        newX = x + u1
        newY = y + v1

        if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and (board[newX][newY] == '$' or board[newX][newY] == '*'):
            adjBoxes.append((newX, newY))


            
    for i in adjBoxes:
        if freeze(board, i[0], i[1], v):
            return True

    return False


from position import *
import heapq
from Stack import *
#from pympler.asizeof import asizeof
from zobrist import *
from Functions import *

vector = [[0,1,'r'],
          [0,-1,'l'],
          [-1,0,'u'],
          [1,0,'d']]



"""
This will be used for direction - the 4 directions to move.
r = right
l = left
u = up
d = down

                      Up (-1, 0)
                       |
                       |
                       |
                       |
                       |
  Left                 |(0,0)           Right
(0, -1)  --------------|--------------  (0, 1)
                       |    ------>  y direction
                       |   |
                       |   |
                       |   | x direction  
                       |   v
                       |
                      Down (1, 0)
              
"""



class Sokoban:
    def __init__(self, board, pushes, steps, prev):
        # About the parameters:
        # board  - List of strings. It represents the level/maze to solve.
        # pushes - int type that represents no. of pushes made so far.
        # steps  - int type that represents no. of steps made so far.
        # prev   - Sokoban type. It is the "previous" Sokoban state.
        # x, y   - int types. (x,y) position of man
        self.board = board
        self.pushes = pushes
        self.steps = steps 
        self.soko = prev   # Previous sokoban state
        self.letter = None # Which direction did it move?
        self.x = 0         # x coord of man
        self.y = 0         # y coord of man
        
        # Actually self.x and self.y are not needed.
        # Anyhow, we initialize the last three variables beforehand...


        
    def solved(self):
        # Is the level solved?
        # Return True if solved
        # Return False otherwise.
        
        # For that we just check if there is a '$' in the board.
        for i in xrange(len(self.board)):
            for j in xrange(len(self.board[0])):
                if self.board[i][j] == '$':
                    return False

        return True


    
    def move(self, visited, q):
        # The most boring, yet the most important function.
        # It does what we expect - move in 4 directions, update the board,
        # hash the result into visited. Make a new Sokoban instance and
        # push it onto q.
        
        # Parameters :
        # visited : set datatype. As we search - we want to know if that
        # board position was visited long back.
        #
        # q       : A heap.

        # Void return type.
        

        pos = position(self.board)
        # This is not necessary.

        for direction in vector:
            u = direction[0]
            v = direction[1]
            l = direction[2]
            newX = self.x + u
            newY = self.y + v

            if 0 <= newX < len(self.board) and 0 <= newY < len(self.board[0]) and self.board[newX][newY] != '#':
                # Checking boundary conditions and check if there is a wall or not.
                """
                There are many possibilities, while moving.
                
                Case 1: We push the box:

                ' ' means empty square.

                
                         MOVE it
                @ *  .    ---->   ' ' + *
                @ * ' '   ---->   ' ' + $
                @ $  .    ---->   ' ' @ *
                @ $ ' '   ---->   ' ' @ $

                + $ ' '   ---->    .  @ $
                + $  .     ---->    .  @ *
                + * ' '   ---->    .  + $
                + *  .     ---->    .  + *

                Case 2: Just the movement of man.

                         MOVE it
                @ ' '     ---->    ' ' @
                @  .      ---->    ' ' +
                + ' '     ---->     .  @
                +  .      ---->     .  +
                """

                if self.board[newX][newY] == '*':
                    """
                    This represents the following case:

                    ?  * ' ' OR    ?  *  .

                    Where ? is to be determined.
                    So let's determine it first!
                    """
                    newboard = self.board[:]
                    new2X = newX + u
                    new2Y = newY + v
                    if 0 <= new2X < len(self.board) and 0 <= new2Y < len(self.board[0]) and (self.board[new2X][new2Y] == ' ' or self.board[new2X][new2Y] == '.'):
                        # Now move it...

                        if self.board[self.x][self.y] == '@':
                            #     @ * ?
                            newboard[self.x] = newboard[self.x].replace('@',' ')
                            newboard[newX] = put(newboard[newX], newY, '+')
                            if self.board[new2X][new2Y] == '.':
                                #   @ * . ---> ' ' + *

                                #    @         ' '
                                #    *  ----->  +
                                #    .          *
                                newboard[new2X] = put(newboard[new2X], new2Y, '*')

                            else:
                                #     @ * ' '  --->  ' ' + $
                                newboard[new2X] = put(newboard[new2X], new2Y, '$')

                            h = gethash(newboard)



                            if h not in visited:

                                visited.add(h)
                                current = Sokoban(newboard, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                heapq.heappush(q, current)

                        if self.board[self.x][self.y] == '+':
                            #         + * ?
                            newboard[self.x] = newboard[self.x].replace('+','.')
                            newboard[newX] = put(newboard[newX], newY, '+')
                            if self.board[new2X][new2Y] == '.':
                                #      + * .  ->   . + *
                                newboard[new2X] = put(newboard[new2X], new2Y, '*')

                            else:
                                #      + * ' '   ->  . + $
                                newboard[new2X] = put(newboard[new2X], new2Y, '$')

                            h = gethash(newboard)

                            if h not in visited:
                                visited.add(h)
                                current = Sokoban(newboard, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                heapq.heappush(q, current)


                                
                                
                if self.board[newX][newY] == '$':
                    newboard = self.board[:]
                    new2X = newX + u
                    new2Y = newY + v
                    if 0 <= new2X < len(self.board) and 0 <= new2Y < len(self.board[0]) and (self.board[new2X][new2Y] == ' ' or self.board[new2X][new2Y] == '.'):
                        # Move it

                        if self.board[self.x][self.y] == '@':
                            #    @  $ ' '
                            #    @  $  .
                            newboard[self.x] = newboard[self.x].replace('@', ' ')

                            ## Now, we want to push the boxes....
                            #left, right -> x remains same so x = newX = new2X

                            newboard[newX] = put(newboard[newX], newY, '@')
                            if self.board[new2X][new2Y] == '.':
                                newboard[new2X] = put(newboard[new2X], new2Y, '*')
                            else:
                                newboard[new2X] = put(newboard[new2X], new2Y, '$')

                            h = gethash(newboard)
    
                            if h not in visited:
                                visited.add(h)
                                current = Sokoban(newboard, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                heapq.heappush(q, current)

                        if self.board[self.x][self.y] == '+':
                            # + $  .
                            # + $ ' '
                            newboard[self.x] = newboard[self.x].replace('+','.')
                            newboard[newX] = put(newboard[newX], newY, '@')
                            if self.board[new2X][new2Y] == '.':
                                newboard[new2X] = put(newboard[new2X], new2Y, '*')

                            else:
                                newboard[new2X] = put(newboard[new2X], new2Y, '$')

                            h = gethash(newboard)


                            if h not in visited:
                                visited.add(h)
                                current = Sokoban(newboard, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                heapq.heappush(q, current)

                #@  .
                #+ ' '
                #+  .

                # @ ' '

                if self.board[newX][newY] == ' ':
                    # + ' '
                    # @ ' '
                    newboard = self.board[:]
                    if self.board[self.x][self.y] == '+':
                        newboard[newX] = put(newboard[newX], newY, '@')
                        newboard[self.x] = newboard[self.x].replace('+','.')

                        h = gethash(newboard)
                        
                        if h not in visited:
                            visited.add(h)
                            current = Sokoban(newboard, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            heapq.heappush(q, current)



                    if self.board[self.x][self.y] == '@':
                        newboard[self.x] = newboard[self.x].replace('@',' ')
                        newboard[newX] = put(newboard[newX], newY, '@')

                        h = gethash(newboard)
                        
                        if h not in visited:
                            visited.add(h)
                            current = Sokoban(newboard, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            heapq.heappush(q, current)


                if self.board[newX][newY] == '.':
                #@  .
                #+  .
                    newboard = self.board[:]
                    if self.board[self.x][self.y] == '+':
                        newboard[self.x] = newboard[self.x].replace('+','.')
                        newboard[newX] = put(newboard[newX], newY, '+')

                        h = gethash(newboard)
                    
                        if h not in visited:
                            visited.add(h)
                            current = Sokoban(newboard, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            heapq.heappush(q, current)


                    if self.board[self.x][self.y] == '@':
                        newboard[self.x] = newboard[self.x].replace('@',' ')
                        newboard[newX] = put(newboard[newX], newY, '+')

                        h = gethash(newboard)
                        if h not in visited:
                            visited.add(h)
                            current = Sokoban(newboard, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            heapq.heappush(q, current)

        return

    def __cmp__(self, right):
        if right == None:
            if self.letter == '':
                return 0
            else:
                return 1
        if f(self) < f(right):
            return -1

        if f(self) > f(right):
            return 1
        return 0



def f(sokoban):
    return 0.5*sokoban.pushes + sokoban.steps

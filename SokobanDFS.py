#from pympler.asizeof import asizeof
from position import *
#import heapq
from zobrist import *
from Functions import *



vector = [[0,1,'r'],
          [0,-1,'l'],
          [-1,0,'u'],
          [1,0,'d']]

# In a DFS, we don't need self.steps and self.pushes.

class SokobanDFS:
    def __init__(self, board, prev):
        self.board = board
        self.soko = prev
        self.letter = None
        self.x = 0
        self.y = 0

    def solved(self):
        for i in xrange(len(self.board)):
            for j in xrange(len(self.board[0])):
                if self.board[i][j] == '$':
                    return False

        return True


    
    def move(self, visited, q):
        pos = position(self.board)
        #x = pos['S'][0]
        #y = pos['S'][1]

        for direction in vector:
            u = direction[0]
            v = direction[1]
            l = direction[2]
            newX = self.x + u
            newY = self.y + v

            if 0 <= newX < len(self.board) and 0 <= newY < len(self.board[0]) and self.board[newX][newY] != '#':
                #@ *  .
                #@ * ' '
                #+ $ ' '
                #+ $ .
                #+ * ' '
                #+ * .


                if self.board[newX][newY] == '*':
                    #?  * ' '
                    #?  *  .
                    newboard = self.board[:]
                    new2X = newX + u
                    new2Y = newY + v
                    if 0 <= new2X < len(self.board) and 0 <= new2Y < len(self.board[0]) and (self.board[new2X][new2Y] == ' ' or self.board[new2X][new2Y] == '.'):
                        # Move it

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
                                #current = Sokoban(newboard, self.pushes + 1, self.steps + 1, self)
                                current = SokobanDFS(newboard, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                q.push(current)




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
                                current = SokobanDFS(newboard, self)#, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                q.push(current)


                                
                                
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
                                current = SokobanDFS(newboard, self)#, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                q.push(current)




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
                                visited.add(tuple(newboard))
                                current = SokobanDFS(newboard, self)#, self.pushes + 1, self.steps + 1, self)
                                current.letter = l.capitalize()
                                current.x = newX
                                current.y = newY
                                q.push(current)

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
                            current = SokobanDFS(newboard, self)#, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            q.push(current)


                    if self.board[self.x][self.y] == '@':
                        newboard[self.x] = newboard[self.x].replace('@',' ')
                        newboard[newX] = put(newboard[newX], newY, '@')

                        h = gethash(newboard)
                        
                        if h not in visited:
                            visited.add(h)
                            current = SokobanDFS(newboard, self)#, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            q.push(current)



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
                            current = SokobanDFS(newboard, self)#, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            q.push(current)

                    if self.board[self.x][self.y] == '@':
                        newboard[self.x] = newboard[self.x].replace('@',' ')
                        newboard[newX] = put(newboard[newX], newY, '+')

                        h = gethash(newboard)
                        if h not in visited:
                            visited.add(h)
                            current = SokobanDFS(newboard, self)#, self.pushes, self.steps + 1, self)
                            current.letter = l
                            current.x = newX
                            current.y = newY
                            q.push(current)

        return







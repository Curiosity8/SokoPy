# This is not really required as such. Just keeping it for old times sake.

def position(board):
    # returns a dictionary of positions of Sokoban, Box, and Target.
    # We can ignore the walls as its stationary throughout.
    pos = {}
    pos['B'] = []
    pos['T'] = []

    """
    Previously Boxes were 'B', targets were 'T' and blanks were '.' etc.
    So I haven't changed the key.
    """
    
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if board[i][j] == '@':
                pos['S'] = (i,j)
            elif board[i][j] == '*':
                pos['T'].append((i,j))
                pos['B'].append((i,j))
            elif board[i][j] == '.':
                pos['T'].append((i,j))
            elif board[i][j] == '$':
                pos['B'].append((i,j))
            elif board[i][j] == '+':
                # Man on target
                pos['S'] = (i,j)
                pos['T'].append((i,j))

    # pos['N'] = len(pos['B'])
    # N -> Number of boxes

    return pos




vector = [[0,1,'r'],
          [0,-1,'l'],
          [-1,0,'u'],
          [1,0,'d']]


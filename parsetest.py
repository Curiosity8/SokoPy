# Level format:

# Separate everything with ;
"""
; 1
level

;2
level
...

;

Make sure you end with ';'!
"""


def parse2(filename):
    f = open(filename,'r')
    a = f.read()
    b = a.split(';')
    f.close()

    d = {}
    count = 1
    for i in xrange(len(b)):
        if b[i] != '':
            j = 0
            b[i] = b[i].split('\n')

            if len(b[i][0].split(' ')) != 1:
                levelname = b[i][0].split(' ')[1]

                level = []

                while j < len(b[i]):
                    if b[i][j] == '':
                        j += 1
                    else:
                        level.append(b[i][j])
                        j += 1

                if level[1:] != []:
                    d[count] = level
                    #print level
                    count += 1
            

    for i in xrange(1, len(d)+1):
        #print i
        maxWidth = max(map(len, d[i]))
        for j in xrange(1, len(d[i])):
            if len(d[i][j]) < maxWidth:
                # Add in walls to make the level into a rectangular grid.
                d[i][j] += '#'*(maxWidth - len(d[i][j]))

    return d

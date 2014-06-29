import sys
from parsetest import *
from time import *
from solve import *
from solveDFS import *


def solution2(filename, fileOut, option = None):

    """
    options

    If no option is put - use Version 8
    - DFS : use DFS
    -e : use Version 8, and scratch the old solution
    """
    
    d = parse2(filename)

    OutFile = open(fileOut,'a')
    OutFile.write('=====================================')
    OutFile.write('\n')
    print 'Starting....'
    start = clock()
    x = start
    #print d

    if option == 'DFS':
        for i in d:
            mode = 'By DFS :' + '\n'
            OutFile.write(mode)

            sol = 'Level %s solution is : %s' % (d[i][0], solveDFS(d[i][1:]))
            timetaken = 'Time taken = %.2f' % (clock() - start)
            print sol
            print timetaken

            OutFile.write(sol)
            OutFile.write('\n')
            OutFile.write(timetaken)

            start = clock()
            OutFile.write('\n')
            OutFile.write('----------------------------------')
            OutFile.write('\n')

        OutFile.write('\n')

        total = 'Total time taken = %.2f' % (clock() - x)
        print total
        OutFile.write(total)
        OutFile.write('\n')



    else:
        for i in d:
            ###
            ans = solve(d[i][1:])
            nodes = 'Number of visited nodes : %d' % (ans[1]) 
            sol = 'Level %s solution is : %s' % (d[i][0], ans[0])
            #sol = 'Level %s solution is : %s' % (d[i][0], solve(d[i][1:]))
            timetaken = 'Time taken = %.2f' % (clock() - start)
            print nodes
            print sol
            print timetaken
            OutFile.write(nodes)
            OutFile.write('\n')
            OutFile.write(sol)
            OutFile.write('\n')
            OutFile.write(timetaken)

            start = clock()
            OutFile.write('\n')
            OutFile.write('----------------------------------')
            OutFile.write('\n')

        OutFile.write('\n')

        total = 'Total time taken = %.2f' % (clock() - x)
        print total
        OutFile.write(total)
        OutFile.write('\n')






filename = sys.argv[1]
fileOut = sys.argv[2]

#print sys.argv
#print len(sys.argv)
if len(sys.argv) == 3:
    solution2(filename, fileOut)

else:
    option = sys.argv[3]
    solution2(filename, fileOut, option)

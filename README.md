SokoPy
======

Sokoban Solver in Python


My first repository in gittub. 
This is my second attempt at making a Sokoban Solver with Python.


Usage :

First, make a file containing the levels in a text editor, like Samplelevels.txt file. The format is like this:

; Levelname

level

; levelname

level

and so on. Make sure you end with ;.

To solve the levels, there are two options - to use A* (which have a bad heuristic function) or DFS.
To use A*, type in the terminal
pypy test.py [levelmap] [levelOutput]

For instance,
pypy test.py Samplelevels.txt SampleOut.txt

(The last level takes around 2GB memory, and takes quite some time for it to solve)

If you want to solve via DFS, type 
pypy test.py [levelmap] [levelOutput] DFS




P.S) Level format :
I urge you to look at the Sokoban wiki.
http://www.sokobano.de/wiki/index.php?title=Level_format


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

To solve the levels, type in the terminal
>> pypy test.py [levels] [levelOutput]

For instance,
>> pypy test.py Samplelevels.txt SampleOut.txt
[The last level takes around 2GB memory, and takes quite some time for it to solve]

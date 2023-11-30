"""
 ===============================================================================
 Auth: Alex Celani
 File: wc.py
 Revn: 04-13-2023  0.1
 Func: calculate word count, print story afterwards

 TODO: create
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 04-13-2023: init

 ===============================================================================
"""

import sys


if len( sys.argv ) < 2:
    print( "usage: python wc file [count] [show]" )
    quit()


f = sys.argv[1]

c = False
s = False

an = False

count = 0


if len( sys.argv ) > 2:
    c = sys.argv[2] == "count"
    s = sys.argv[2] == "show"

if len( sys.argv ) > 3:
    c = sys.argv[3] == "count"
    s = sys.argv[3] == "show"


with open( f, "r" ) as file:
    for line in file:
        if line != "\n":
            line = line + " "
            if s:
                print( line.replace( r"\t", "    " ), end="" )
            if line[0] != "#":
                for char in line:
                    if an:
                        if char == ">":
                            an = False
                            count -= 1
                        continue
                    an = char == "<"
                    if char == " ":
                        count += 1
    if c:
        print( count )
        

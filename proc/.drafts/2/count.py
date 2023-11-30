"""
 ===============================================================================
 Auth: Alex Celani
 File: count.py
 Revn: 04-18-2023  0.1
 Func: calculate word count, print story afterwards

 TODO: create
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 04-18-2023: copied from wc.py

 ===============================================================================
"""

import sys


if len( sys.argv ) < 2:
    print( "usage: python wc file [count] [show]" )
    quit()


f = sys.argv[1]

c = False
s = False

ilml = False

count = 0

rplc = "ZZZZZZZ"

if len( sys.argv ) > 2:
    c = sys.argv[2] == "count"
    s = sys.argv[2] == "show"

if len( sys.argv ) > 3:
    c = sys.argv[3] == "count"
    s = sys.argv[3] == "show"


with open( f, "r" ) as file:
    f = file.read()
    f = f.replace( "/*", rplc )
    f = f.replace( "*/", rplc )
    f = f.replace( "#", rplc )
    f = f.replace( "//", rplc )
    f = f.replace( "\n", rplc )

    f = f.split( rplc )
    
    for i in range( len( f ) ):
        print( f[i] )










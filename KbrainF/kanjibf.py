import os
import sys

cwd = os.getcwd()
path = cwd + "/out.kbf"

args = sys.argv
if len(args) == 2:
    with open(args[1],mode = "r") as f:
        text = f.read()
else:
    text = input("bf text>")

d = {">":"右","<":"左","+":"増","-":"減",".":"出",",":"入","[":"始","]":"終"}
table = str.maketrans(d)

after = text.translate(table)

with open(path,mode = "w") as f:
    f.write(after)

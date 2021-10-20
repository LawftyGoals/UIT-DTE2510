import os

dirList = os.listdir()

for i in dirList:
    if 'DTEO' in i:
        j = i.replace("DTEO","DTE2510")
        os.rename(i,j)
import os
import sys

sPath = '/Users/alfredyu/Desktop/Test_Code'
dPath = '/Users/alfredyu/Desktop/Test_Code'
files = os.listdir(sPath)

for file in files:
    if file.endswith(".txt"):
        filename, file_extension = os.path.splitext(file)
        path = os.path.join(dPath, filename)
        os.mkdir(path)

        prevName = os.path.join(sPath, file)
        newName = os.path.join(path, file)
        
        os.rename(prevName, newName)
        
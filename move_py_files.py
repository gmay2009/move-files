import os


# Change text below where it says MY_FOLDER to the specific path needed
src = '/Users/MY_FOLDER/Documents/Python Scripts/'
dest = '/Users/MY_OTHER_FOLDER/Documents/Python/'

files = os.listdir(src)

for f in files:
    if f.__contains__('.py'):
        os.rename(src + f, dest + f)

"""
The goal here is to copy a bunch of files over 
from targetOne to targetMany
"""

#	shutil.copy(src, dst, *, follow_symlinks=True)
import shutil
import os
from fnmatch import fnmatch

curr_path = os.getcwd()
from_dirr = curr_path+"/targetOne/"
to_dirr = curr_path+"/targetMany/"
pattern = "*.txt"

for path, subdirs, files in os.walk(from_dirr):
    for name in files:
        if fnmatch(name, pattern):
            shutil.copy(from_dirr+ name, to_dirr, follow_symlinks=True)
            

print('*'*10+"break"+"*"*10+"\n")
print("Completed copyCopy")
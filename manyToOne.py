import os
from fnmatch import fnmatch
"""
The goal of this would be to read many files 
Compile the data to a single file.

"""



curr_path = os.getcwd()
root = curr_path+"/targetMany/"
pattern = "*.txt"

filenames= []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            filenames.append(name)

my_str=""
for f in filenames:
    read_file = open(root+f,"r")
    my_str += read_file.read()
    read_file.close()


#Writing 
target_dirr = curr_path+"/outputForMany/"
target_file_name = "output.txt"
outputFile= open(target_dirr+target_file_name,"w")
outputFile.write(my_str)
#Cleanup
outputFile.close()

print('*'*10+"break"+"*"*10+"\n")
print("completed many to one")
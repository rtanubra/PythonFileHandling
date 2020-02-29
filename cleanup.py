"""
Run this to delete the files output from the main function.
This is just to clean everything, so you can re-run for fun!

"""

import os,shutil
from fnmatch import fnmatch

curr_path = os.getcwd()
dirr_one = curr_path+"/targetOne"
dirr_two = curr_path+"/targetMany"
dirr_three = curr_path+"/outputForMany"

dirs = ["targetOne","targetMany","outputForMany","monkey"]

#shutil.rmtree can delete non empty directory
#os.rmdir() can only delete empty directories

for aDir in dirs:
    try: 
        shutil.rmtree(curr_path+ "/"+ aDir)
    except OSError as e:
        print("Error: %s : %s" % (curr_path+ "/"+ aDir, e.strerror))
    os.mkdir(curr_path+ "/"+ aDir)

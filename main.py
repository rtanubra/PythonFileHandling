"""
This will be the main function.
Directories involved:

target-> this is your starting point put text in input.txt
targetOne -> first module grabs input.txt and splits to multiple files here.
targetMany-> Helper module copyCopy will copy many files from targetOne to targetMany
outputForMany ->Final take multiple files as input from targetMany and compile to a single file here.
"""

print(f"Running main function. ")

import oneToMany
import copyCopy
import manyToOne
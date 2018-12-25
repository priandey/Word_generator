# -*- coding: utf-8 -*-

import os
import numpy as np
import re
import codecs

def get_source_file(list_of_file):
    '''This function is used to print a list and the corresponding index. The
    user is asked to choose an item of the list by selecting a number'''
    for e in list_of_file:
        print("{}.{}".format(list_of_file.index(e),e))
    choice = int(input("Choose your source file by hitting the number : "))
    return list_of_file[choice]

def main():

    filepath = "source_file/"
    file_available = list()

    with os.scandir(filepath) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                if entry.name != "README.md": #Add here the files you don't want listed in the program
                    file_available.append(entry.name)

    filepath += get_source_file(file_available)
    name_output = "current_work" #If you want to keep a track of your stat_files for later usage, you should replace the value by input("Stat file name")

    count = np.zeros((256,256,256),dtype='int32')
    res = []
    print("Calculating...")
    with codecs.open(filepath, "r", "iso-8859-1") as lines:
        for l in  lines:
            # Split on white space or open parenthesis and keep the first string
            l2 = re.split("[ ,\(]",l)[0]
            l2 = l2+"\n"
            i=0
            j=0
            for k in [ord(c) for c in list(l2)]:
                count[i,j,k] += 1
                i = j
                j = k
    count.tofile("stat_file/count2D_{}.bin".format(name_output))
    count.tofile("stat_file/count2D_{}.bin".format(name_output))

    return filepath,name_output

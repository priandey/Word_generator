# -*- coding: utf-8 -*-

import os
import numpy as np
import re
import codecs

def main():

    filepath = "source_file/"
    filepath += input("Word Base File :")
    name_output = input("Stat file name : ")

    count = np.zeros((256,256,256),dtype='int32')
    res = []

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
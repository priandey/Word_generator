# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import choice, seed
import corpus_stat
seed(1)
import codecs
CODEC = "ISO-8859-1"

input_name = corpus_stat.main()

filepath = input_name[0]
outfile = "render_file/"
outfile += filepath.split("/")[1]
probafile = "stat_file/count2D_{}.bin".format(input_name[1])

dico = []
with codecs.open(filepath, "r", "ISO-8859-1") as lines:
    for l in  lines:
        dico.append(l[:-1])

count = np.fromfile(probafile,dtype="int32").reshape(256,256,256)

s=count.sum(axis=2)
st=np.tile(s.T,(256,1,1)).T
p=count.astype('float')/st
p[np.isnan(p)]=0

#%%


K = 100
while True:
    range_min = int(input("Minimal Length : "))
    range_max = int(input("Maximal Length : "))
    outfile += "_Range_{}_{}.txt".format(range_min,range_max)
    f = codecs.open(outfile,"w",CODEC)
    for TGT in range(range_min,range_max):

    #K = 100
    #for TGT in range(4,11):
        total = 0
        while total<100:
            i=0
            j=0
            res = u''
            while not j==10:
                k=choice(range(256),1,p=p[i,j,:])[0]
                res = res + chr(k)
                i=j
                j=k
            if len(res) == 1+TGT:
                x=res[:-1]
                if res[:-1] in dico:
                    x=res[:-1]+"\n"
                total += 1
                print(x)
                f.write(x+"\n")
    f.close()

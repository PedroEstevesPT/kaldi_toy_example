'''
Sorts all files in a directory
Given full path to a directory sorts all files in that directory.
'''
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

path = Path(os.getcwd())

data_folders = ["train","test"]
string_dir = str(path.parent) + str("/kaldi_toy_example/data")

for folder in data_folders:
    mypath = string_dir + "/" + folder 
    files = ["spk2gender","text","utt2spk","wav.scp"]
    
    for f in files:
    
        tmp = []
        filename = mypath + "/" + f
        with open(filename) as f:
            lines = f.readlines()
            for l in lines:
                tmp.append(l)

        tmp.sort()
        new_file = open(filename,"w")   #write mode 
        for l in tmp:
            new_file.writelines(l)
        new_file.close() 
        
import os
import sys
from datetime import datetime
import time
rootdir = '/home/aman/Desktop/some2/'

t = []

for root, subFolders, files in os.walk(rootdir):
    # print subFolders
    if 'stdout' in files:
        with open(os.path.join(root, 'stdout'), 'r') as fin:
            rf = root
            rf = rf.split('/')
            string = rootdir + '_output.txt'
            if (os.path.isfile(string)):
                f = open(string, 'a')
            else:
                f = open(string,'w+')
            # print string
            for lines in fin:
                f.write(lines)
import os
import sys
from datetime import datetime
import time
rootdir = '/home/aman/Desktop/Results/New2/'

t = []

for root, subFolders, files in os.walk(rootdir):
    # print subFolders
    if 'stdout' in files:
        with open(os.path.join(root, 'stdout'), 'r') as fin:
            rf = root
            rf = rf.split('/')
            string = rootdir + rf[6] + '_' + rf[7] + '_output.txt'
            if (os.path.isfile(string)):
                f = open(string, 'a')
            else:
                f = open(string,'w+')
            # print string
            for lines in fin:
                f.write(lines)

arr1 = ['Run1','Run2','Run3','Run4','Run5']
arr2 = ['try1','try2','try3','try4']
i = 0
f.close()
# print lines[3]
FMT = '%H:%M:%S'

for p in range (0,5):
    for q in range (0,4):
        string = rootdir + arr1[p] + '_' + arr2[q] + '_output.txt'
        f = open(string,'r')
        lines = f.readlines()
        if(arr2[q] == 'try1' or arr2[q] == 'try2'):
            string2 = rootdir + arr1[p] + '_PSDSF.txt'
            if (os.path.isfile(string2)):
            	f1 = open(string2, 'a')
            else:
            	f1 = open(string2, 'w+')

            if(arr2[q]=='try1'):
            	f1.write('1:\n')
            else:
            	f1.write('2:\n')

            i = 0
            count = 0
            while(i<len(lines)):
            	count += 1
                type_of_task = lines[0+i]
                temp = type_of_task
                type_of_task = type_of_task.split(" ")
                type_of_task[-1] = type_of_task[-1][:len(temp)-1]
                type_of_task = " ".join(type_of_task)

                tid = lines[1+i]
                temp = tid
                tid = tid.split(" ")
                tid[-1] = tid[-1][:len(temp)-1]
                tid = " ".join(tid)

                s_t = lines[2+i]
                temp = s_t
                s_t = s_t.split(" ")
                s_t[-1] = s_t[-1][:len(temp)-1]
                s_t = " ".join(s_t)

                e_t = lines[3+i]
                temp = e_t
                e_t = e_t.split(" ")
                e_t[-1] = e_t[-1][:len(temp)-1]
                e_t = " ".join(e_t)

                total = lines[4+i]
                temp = total
                total = total.split(" ")
                total[-1] = total[-1][:len(temp)-1]
                total = " ".join(total)
            
                # tdelta = datetime.strptime((e_t), FMT) - datetime.strptime((s_t), FMT)
                # print tdelta
                
                f1.write(str(count) + '. ' + type_of_task+'\t'+tid+'\t'+s_t+'\t'+e_t+'\t'+total+'\n')
                i+=5
            f1.write('\n')
            f1.close()

        else:
            string2 = rootdir + arr1[p] + '_DRF.txt'
            if (os.path.isfile(string2)):
            	f1 = open(string2, 'a')
            else:
            	f1 = open(string2, 'w+')

            if(arr2[q]=='try3'):
            	f1.write('1:\n')
            else:
            	f1.write('2:\n')

            i = 0
            count = 0
            while(i<len(lines)):
            	count += 1
                type_of_task = lines[0+i]
                temp = type_of_task
                type_of_task = type_of_task.split(" ")
                type_of_task[-1] = type_of_task[-1][:len(temp)-1]
                type_of_task = " ".join(type_of_task)

                tid = lines[1+i]
                temp = tid
                tid = tid.split(" ")
                tid[-1] = tid[-1][:len(temp)-1]
                tid = " ".join(tid)

                s_t = lines[2+i]
                temp = s_t
                s_t = s_t.split(" ")
                s_t[-1] = s_t[-1][:len(temp)-1]
                s_t = " ".join(s_t)

                e_t = lines[3+i]
                temp = e_t
                e_t = e_t.split(" ")
                e_t[-1] = e_t[-1][:len(temp)-1]
                e_t = " ".join(e_t)

                total = lines[4+i]
                temp = total
                total = total.split(" ")
                total[-1] = total[-1][:len(temp)-1]
                total = " ".join(total)
            
                # tdelta = datetime.strptime((e_t), FMT) - datetime.strptime((s_t), FMT)
                # print tdelta
                
                f1.write(str(count) + '. ' + type_of_task+'\t'+tid+'\t'+s_t+'\t'+e_t+'\t'+total+'\n')
                i+=5
            f1.write('\n')
            f1.close()
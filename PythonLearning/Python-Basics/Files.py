# -*- coding: utf-8 -*-
'''
outfile = open('outGrades.dat', 'w')
grad=0

while(grad!= 'q'):
    print('Enter the grades:')
    grad = input()
    outfile.write(grad+'\n')
    
outfile.close()
'''

inFile = open('outGrades.dat', 'r') #open the file
count = 0
total=0
line = int(inFile.readline()) #read first line
while (line):
    print(line)
    count = count + 1
    total = total + int(line)
    line = inFile.readline() #read until the eol
    
avg = total/count
print('Avg:%.2f' %avg)



import os


files = os.popen('dir *.py')

for file in files:
    print (file, end='')
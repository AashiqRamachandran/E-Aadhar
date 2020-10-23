import os

initial_file=open('indian-prefixes.txt','r')
output=open('final.txt','w')
for i in initial_file:
    for j in range(1920,2020):
        temp=i.strip()+str(j)
        output.write(temp)

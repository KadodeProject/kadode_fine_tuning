import os
import csv

path = os.getcwd()
date=[]
title=[]
content=[]
with open(path+'/data/usuyukiData.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        date.append(row[0]) 
        title.append(row[1]) 
        content.append(row[2]) 
    
# 先頭行は列名なので削除
del date[0]
del title[0]
del content[0]

print(date[0])
print(title[0])
print(content[0]) 

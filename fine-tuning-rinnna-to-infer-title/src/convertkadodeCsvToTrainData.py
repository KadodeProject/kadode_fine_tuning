#! /usr/bin/env python
import os
import csv


"""
CSVの読み込み
"""
path = os.getcwd()
titles=[]
contents=[]
with open(path+'/inputData/usuyukiData.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        titles.append(row[1]) 
        contents.append(row[2]) 
    
# 先頭行は列名なので削除
del titles[0]
del contents[0]

print(titles[0])
print(contents[0]) 
counter=len(titles)
print(str(counter)+"diary used")

"""
GPT用の学習データに変換して保存
"""

with open(path + '/trainData/gpt2_train_data.txt', 'w') as output_file:
    for i in range(counter-1):
        text = '<s>' + contents[i] + '[SEP]' + titles[i] + '</s>'
        output_file.write(text + '\n')

#!/usr/bin/env python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

path = os.getcwd()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-medium")
tokenizer.do_lower_case = True
model = AutoModelForCausalLM.from_pretrained(path+'/outputModel')
model.to(device)
model.eval()

def generate_diary_title_with_date(date, body, num_gen=10):
    input_text = '<s>'+date+'[SEP]'+body+'[SEP]'
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    out = model.generate(input_ids, do_sample=True, top_p=0.95, top_k=40,num_return_sequences=num_gen, max_length=256, bad_words_ids=[[1], [5]])
    print('='*5,'本文', '='*5)
    print(body)
    print('-'*5, 'タイトル', '-'*5)
    for sent in tokenizer.batch_decode(out):
        sent = sent.split('[SEP]</s>')[1]
        sent = sent.replace('</s>', '')
        print(sent)

def generate_diary_title(body, num_gen=10):
    input_text = '<s>'+body+'[SEP]'
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    out = model.generate(input_ids, do_sample=True, top_p=0.95, top_k=40, num_return_sequences=num_gen, max_length=256, bad_words_ids=[[1], [5]])
    print('='*5,'本文', '='*5)
    print(body)
    print('-'*5, 'タイトル', '-'*5)
    for sent in tokenizer.batch_decode(out):
        sent = sent.split('[SEP]</s>')[1]
        sent = sent.replace('</s>', '')
        print(sent)


date = '2022-10-24'
body = '''
日記の本文を入れる。

改行も含めて。
'''
# generate_diary_title_wit_date(date,body)
generate_diary_title(body)

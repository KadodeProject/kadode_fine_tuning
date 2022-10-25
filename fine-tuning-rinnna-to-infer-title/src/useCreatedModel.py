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

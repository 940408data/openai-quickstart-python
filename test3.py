#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test3.py
@Time    :   2023/03/23 17:19:47
@Author  :   huangxu3 
@Version :   1.0
@Contact :   huangxu3@newhope.cn
@License :   (C)Copyright 2021-2022, newhope.cn
@Desc    :   批量翻译
'''

# here put the import lib

import openai
import os
from dotenv import load_dotenv, find_dotenv
from data.input_data.english import text1


load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo" # 模型ID

system_text="""
翻译"""
text=text1.split("\n")
for aim_user_text in text[1:]:
    messages=[
        {"role": "system", "content":system_text},
        {"role": "user", "content": aim_user_text}]
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
    temperature = 0.8,messages=messages)
    print("""- [x] """+aim_user_text)
    print()
    text = response['choices'][0]['message']['content']
    print("""- [ ] """+text)
    print()


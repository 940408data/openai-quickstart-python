import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Hello, how are you?" # 您的对话开始语

prompt1 = """
Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: white horse
Names: """

prompt2 ="""
《Oxford English Dictionary》中对水的定义，展示原文及其中文翻译
"""

prompt3 ="""
"""

model = "text-davinci-002" # 模型ID
response = openai.Completion.create(engine=model, prompt=prompt1, max_tokens=2000)
text = response['choices'][0].text
print(text)
#print(response['usage'])

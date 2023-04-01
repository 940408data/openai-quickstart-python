import openai
import os
from dotenv import load_dotenv, find_dotenv
from data.input_data.english import text

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo" # 模型ID

print()
print("#############################prompt#######################################")
text=text.split("\n")
for i in text[1:]:
    prompt1=f"""
    # USER
    In this category it seems we should include bodily nature in general, and its extension;  likewise the shape of extended things and their quantity (magnitude and number);  likewise the place in which they exist, the time during which they exist, and suchlike.
    # ASSISTANT
    - [x] In this category it seems we should include bodily nature in general, and its extension;
    - [ ] 在这范畴里，我们似乎应当包括一般的肉体本性及其外延;
    - [x] likewise the shape of extended things and their quantity (magnitude and number);
    - [ ] 延伸事物的形状和它们的数量(大小和数量);
    - [x] likewise the place in which they exist, the time during which they exist, and suchlike.
    - [ ] 同样，他们存在的地方，他们存在的时间，诸如此类。
    # USER
    {i}
    # ASSISTANT
    """
    print(i)
    response = openai.Completion.create(engine=model, prompt=prompt1, max_tokens=2000)
    text = response['choices'][0].text
    print("#############################response#######################################")
    print(text)
    print(response["usage"])
    print("###############################end##########################################")



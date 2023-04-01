import openai
import os
from dotenv import load_dotenv, find_dotenv
from data.input_data.english import text

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo" # 模型ID

system_text="""
翻译，一句一句按照中英对照展现"""

# user_text = """
# In this category it seems we should include bodily nature in general, and its extension;  likewise the shape of extended things and their quantity (magnitude and number);  likewise the place in which they exist, the time during which they exist, and suchlike.
# """
# assistant_text = """
# - [x] In this category it seems we should include bodily nature in general, and its extension;
# - [ ] 在这范畴里，我们似乎应当包括一般的肉体本性及其外延;
# - [x] likewise the shape of extended things and their quantity (magnitude and number);
# - [ ] 延伸事物的形状和它们的数量(大小和数量);
# - [x] likewise the place in which they exist, the time during which they exist, and suchlike.
# - [ ] 同样，他们存在的地方，他们存在的时间，诸如此类。
# """

user_text="""
A plant is a living organism that belongs to the kingdom Plantae. Plants are multicellular eukaryotes that have cell walls made of cellulose and chloroplasts for photosynthesis. They are typically stationary, autotrophic organisms that produce their own food through the process of photosynthesis, which involves converting light energy into chemical energy stored in organic compounds.
"""
assistant_text="""
- [x] A plant is a living organism that belongs to the kingdom Plantae.
- [ ] 植物是属于植物界的一种生物体。
- [x]  Plants are multicellular eukaryotes that have cell walls made of cellulose and chloroplasts for photosynthesis. 
- [ ] 植物是多细胞真核生物，具有由纤维素构成的细胞壁和进行光合作用的叶绿体。
- [x] They are typically stationary, autotrophic organisms that produce their own food through the process of photosynthesis, which involves converting light energy into chemical energy stored in organic compounds.
- [ ] 植物是属于植物界的一种生物体。植物是多细胞真核生物，具有由纤维素构成的细胞壁和进行光合作用的叶绿体。它们通常是静止的自养生物，通过光合作用的过程制造自己的食物，将光能转化为有机化合物中储存的化学能。
"""

user_text1="""
Plants come in a wide range of sizes, shapes, and colors, and they can be found in virtually every habitat on Earth, from deserts to rainforests and from the bottom of the ocean to the tops of mountains. They play an important role in many ecosystems by providing food, shelter, and oxygen, and they are also important for human use, providing food, medicine, fuel, and many other products.
"""

assistant_text1="""
- [x] Plants come in a wide range of sizes, shapes, and colors, and they can be found in virtually every habitat on Earth, from deserts to rainforests and from the bottom of the ocean to the tops of mountains. 
- [ ] 植物的大小、形状和颜色各不相同，几乎可以在地球上的所有栖息地中找到它们，从沙漠到雨林，从海底到山顶。
- [x] They play an important role in many ecosystems by providing food, shelter, and oxygen, and they are also important for human use, providing food, medicine, fuel, and many other products.
- [ ] 它们在许多生态系统中扮演着重要角色，提供食物、庇护和氧气，并且对于人类的使用也很重要，提供食物、药品、燃料和许多其他产品。
"""
user_text2 ="""
"The Republic" is a book written by the ancient Greek philosopher Plato, and is considered one of his most important works. It is a Socratic dialogue that explores a wide range of philosophical topics, including justice, ethics, politics, education, and more.
"""

assistant_text2="""
- [x] "The Republic" is a book written by the ancient Greek philosopher Plato, and is considered one of his most important works.
- [ ] 《理想国》是一本由古希腊哲学家柏拉图写作的书，被认为是他最重要的作品之一。
- [x] It is a Socratic dialogue that explores a wide range of philosophical topics, including justice, ethics, politics, education, and more.
- [ ] 它是一部苏格拉底式的对话，探讨了广泛的哲学主题，包括正义、伦理学、政治、教育等等。
"""

user_text3 ="""
The book takes the form of a discussion between Socrates and various other characters, who offer their opinions on the nature of justice and the ideal society. Throughout the dialogue, Socrates develops a theory of justice that is based on the idea of the "good life", and argues that the best society is one in which everyone has a place that is suited to their abilities and talents.
"""

assistant_text3="""
- [ ] The book takes the form of a discussion between Socrates and various other characters, who offer their opinions on the nature of justice and the ideal society.
- [x] 这本书采用苏格拉底和其他不同角色之间的讨论形式，他们对正义和理想社会的本质提出了自己的意见。
- [ ] Throughout the dialogue, Socrates develops a theory of justice that is based on the idea of the "good life", and argues that the best society is one in which everyone has a place that is suited to their abilities and talents.
- [x] 在整个对话中，苏格拉底发展出一种基于“良好生活”的正义理论，并认为最好的社会是一个每个人都有适合他们能力和才华的位置的社会。
"""
aim_user_text="""
1.SEVERAL years have now elapsed since I first became aware that I had accepted, even from my youth, many false opinions for true, and that consequently what I afterward based on such principles was highly doubtful;  and from that time I was convinced of the necessity of undertaking once in my life to rid myself of all the opinions I had adopted, and of commencing anew the work of building from the foundation, if I desired to establish a firm and abiding superstructure in the sciences.  But as this enterprise appeared to me to be one of great magnitude, I waited until I had attained an age so mature as to leave me no hope that at any stage of life more advanced I should be better able to execute my design.  On this account, I have delayed so long that I should henceforth consider I was doing wrong were I still to consume in deliberation any of the time that now remains for action.  To-day, then, since I have opportunely freed my mind from all cares and am happily disturbed by no passions, and since I am in the secure possession of leisure in a peaceable retirement, I will at length apply myself earnestly and freely to the general overthrow of all my former opinions.
"""
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature = 0.8,
  messages=[
        {"role": "system", "content":system_text},
        # {"role": "user", "content":user_text },
        # {"role": "assistant", "content": assistant_text},
        # {"role": "user", "content":user_text1 },
        # {"role": "assistant", "content": assistant_text1},
        # {"role": "user", "content":user_text2 },
        # {"role": "assistant", "content": assistant_text2},
        # {"role": "user", "content":user_text3 },
        # {"role": "assistant", "content": assistant_text3},
        {"role": "user", "content": aim_user_text}
    ]
)

print("##############################user###########################################")
print(aim_user_text)
print("#############################assistant#######################################")
text = response['choices'][0]['message']['content']
print(text)
print(response["usage"])
print("###############################end###########################################")


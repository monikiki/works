import pandas as pd
import MeCab
from pyecharts.charts import WordCloud

# change excel file to text
with open("/Users/Caijing/Desktop/au comment.txt", "w") as f:
    df = pd.read_excel("/Users/Caijing/Desktop/au comment.xlsx", sheet_name="review", engine="openpyxl")
    df["review"].to_string(f, index=False)

f = open("/Users/Caijing/Desktop/au comment/au comment.txt")
review = f.read()
f.close()

# analyze words
m = MeCab.Tagger()

word=[]
node = m.parseToNode(review)
while node:
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞","動詞","形容詞"]:
        origin = node.feature.split(",")[6]
        if origin not in ["する","いる","ある","なる"]:
            word.append(origin)
    # if hinshi in ["形容詞"]:
    #     origin = node.feature.split(",")[6]
    #     word.append(origin)
    node = node.next

word_dict = {}
for i in word:
    if len(i) > 1:
        if i not in word_dict.keys():
            word_dict[i] = 1
        else:
            word_dict[i] += 1
# print(word_dict)

# create wordclud
wd = WordCloud()
wd.add(series_name = "", data_pair = word_dict.items(), word_size_range = [10, 80])
wd.render("/Users/Caijing/Desktop/au comment/aucomment(adj-noun-verb).html")
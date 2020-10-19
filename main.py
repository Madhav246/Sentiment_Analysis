import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

text_file = open("read.txt", "wt")
print("Enter string to write to text file.")
text_input = input().lower()
n = text_file.write(text_input)
text_file.close()

# Cleaning Texts

text = open('read.txt', encoding='utf-8', ).read()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenization using NLTK

tokenized_words = word_tokenize(cleaned_text, "english")

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Counting emotions

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Graphical Representation of data

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

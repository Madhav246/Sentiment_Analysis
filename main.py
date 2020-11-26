import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text_file = open("read.txt", "wt")
print("Enter string to write to text file.")
text_input = input().lower()
n = text_file.write(text_input)
text_file.close()

# Cleaning Texts

text = open('read.txt', encoding='utf-8').read()
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

w = Counter(emotion_list)


# Getting overall Sentiment
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral")


sentiment_analyse(cleaned_text)

import string

text_file = open("read.txt", "wt")
print("Enter string to write to text file.")
text_input = input().lower()
n = text_file.write(text_input)
text_file.close()

# Cleaning Texts

text = open('read.txt', encoding='utf-8', ).read()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)

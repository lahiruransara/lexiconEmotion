#
# Implementation of Lexicon based Emotion Analysis
# Version 1.5 (final)
#
# Pre-processing text for analysis with NRC Emotion Lexicon
# Text lowercase / Strip punctuations / Tokenize words / Remove stop words / Filtered output /
# Import lexicon / Create dictionary using lexicon / Get the intersection between dictionary and filtered output /
# Calculate overall emotion
#
# author W. Lahiru Ransara      lahiruransara123@gmail.com
#

import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nrc_address = "data/NRC-emotion-lexicon-test.txt"
emot_dic = ""

data = {}  # List for save the Lexicon

example_sent = "This is a sample sentence, showing off? the stop! words filtration and pre processing."


def strip_punctuation(s):
    return re.sub("[\.\t\,\?\!\:;\(\)\.]", "", s, 0, 0)  # Strip punctuation from a string


# Read NRC Emotions
def read_nrc_emotions(nrc_address):

    with open(nrc_address, "r", encoding="utf-8") as nrc_file:
        for line in nrc_file:
            splited = line.replace("\n", "").split("\t")
            word, emotion, value = splited[0], splited[1], splited[2]
            if word in data.keys():
                data[word].append((emotion, int(value)))
            else:
                data[word] = [(emotion, int(value))]
        return data


# value set for emot_dic
emot_dic = read_nrc_emotions(nrc_address)

# print(emot_dic)  #test purposes

stop_words = set(stopwords.words('english'))  # Set language to English

word_tokens = word_tokenize(
    strip_punctuation(example_sent.lower()))  # Tokenizing / turn into lowercase / Strip punctuations

# Removing stop words
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

# Display
print(example_sent)
print(word_tokens)
print(filtered_sentence)

#
# Implementation of Lexicon based Emotion Analysis
# Version 3.4
#
# Pre-processing text for analysis with NRC Emotion Lexicon
# Get words emotions
# Lowercase / Strip punctuations / Tokenize words / Remove stop words / word list
# Import Lexicon /Iterate through the lexicon list and access the data /
# Get the intersection between dictionary and filtered output / increase emotion variable value by 1 /
# Check maximum variable value / Calculate overall emotion
#
# author W. Lahiru Ransara      lahiruransara123@gmail.com
#

import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def strip_punctuation(s):
    return re.sub("[\.\t\,\?\!\:;\(\)\.]", "", s, 0, 0)  # Strip punctuation from a string


nrc_address = "data/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt"
emot_dic = ""

data = {}  # List for save the Lexicon

fear = anger = trust = anticipation = sadness = disgust = surprise = joy = positive = negative = 0  # Emotion variables

example_sent = "This is a sample sentence, showing off? the stop! words filtration and emotion analysis"

stop_words = set(stopwords.words('english'))  # Set language to English

word_tokens = word_tokenize(
    strip_punctuation(example_sent.lower()))  # Tokenizing / turn into lowercase / Strip punctuations

# Removing stop words
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


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


# Print Lexicon list keys (for testing purposes)
# print(data.keys())


# value set for emot_dic
emot_dic = read_nrc_emotions(nrc_address)

common_set = set(filtered_sentence).intersection(emot_dic)     # Get the intersection of word list & dictionary
print(common_set)

common_list = list(common_set)      # Converting set into list because 'set' does not support indexing

# Update Emotion variable values
for i in common_list:
    # print(i, " = ", emot_dic[i])  # test purposes
    anger += emot_dic[i][0][1]
    anticipation += emot_dic[i][1][1]
    disgust += emot_dic[i][2][1]
    fear += emot_dic[i][3][1]
    joy += emot_dic[i][4][1]
    negative += emot_dic[i][5][1]
    positive += emot_dic[i][6][1]
    sadness += emot_dic[i][7][1]
    surprise += emot_dic[i][8][1]
    trust += emot_dic[i][9][1]

# Find maximum valued emotion
if anger > max(anticipation, disgust, fear, joy, negative, positive, sadness, surprise, trust):
    print("Anger")
elif anticipation > max(anger, disgust, fear, joy, negative, positive, sadness, surprise, trust):
    print("Anticipation")
elif disgust > max(anger, anticipation, fear, joy, negative, positive, sadness, surprise, trust):
    print("Disgust")
elif fear > max(anger, anticipation, disgust, joy, negative, positive, sadness, surprise, trust):
    print("Fear")
elif joy > max(anger, anticipation, disgust, fear, negative, positive, sadness, surprise, trust):
    print("Joy")
elif negative > max(anger, anticipation, disgust, fear, joy, positive, sadness, surprise, trust):
    print("Negative")
elif positive > max(anger, anticipation, disgust, fear, joy, negative, sadness, surprise, trust):
    print("Positive")
elif sadness > max(anger, anticipation, disgust, fear, joy, negative, positive, surprise, trust):
    print("Sadness")
elif surprise > max(anger, anticipation, disgust, fear, joy, negative, positive, sadness, trust):
    print("Surprise")
elif trust > max(anger, anticipation, disgust, fear, joy, negative, positive, sadness, surprise):
    print("Trust")

# Display
print("Anger value = ", anger)
print("Anticipation value = ", anticipation)
print("Disgust value = ", disgust)
print("Fear value = ", fear)
print("Joy value = ", joy)
print("Negative value = ", negative)
print("Positive value = ", positive)
print("Sadness value = ", sadness)
print("Surprise value = ", surprise)
print("Trust value = ", trust)

# print(emot_dic)
# print(example_sent)
# print(word_tokens)
# print(filtered_sentence)
# print(filtered_sentence[0])

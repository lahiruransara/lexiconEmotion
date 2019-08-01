# Iterate through the emotion dictionary and access the emotional data using loop and get the final emotion output
# part of code_v1.py
#
# finished!

emotion1 = emotion2 = emotion3 = 0  # basic emotion variables

filtered_sentece = ['word1', 'word2', 'stop', 'word3']

dictionary = {
    'word1': [('emo1', 1), ('emo2', 0), ('emo3', 1)],
    'word2': [('emo1', 0), ('emo2', 1), ('emo3', 0)],
    'word3': [('emo1', 0), ('emo2', 0), ('emo3', 1)],
    'word4': [('emo1', 0), ('emo2', 1), ('emo3', 0)]}

# for key in dictionary:
#     print(key, "corresponds to ", dictionary[key])
#
# print(dictionary["word3"])          # gets the whole emotion list
# print(dictionary["word2"][1])       # gets the single emotion with value
# print(dictionary["word1"][0][1])    # gets the single data

common_set = set(filtered_sentece).intersection(dictionary)     # Get the intersection of word list & dictionary
print(common_set)

common_list = list(common_set)      # Converting set into list because 'set' does not support indexing

# print(common_list[0])

for i in common_list:
    # print(i, " = ", dictionary[i])  #test purposes
    emotion1 += dictionary[i][0][1]
    emotion2 += dictionary[i][1][1]
    emotion3 += dictionary[i][2][1]

# print(emotion1)       #test purposes
# print(emotion2)       #test purposes
# print(emotion3)       #test purposes

# output = max(emotion1, emotion2, emotion3)
# print(output)

if emotion1 > max(emotion2, emotion3):
    print("Emotion 01")
elif emotion2 > max(emotion3, emotion1):
    print("Emotion 02")
else:
    print("Emotion 03")

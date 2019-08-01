# Importing lexicon text file and making dictionary using data
# part of code_v1.py
#
# finished!

nrc_address = "data/NRC-emotion-lexicon-test.txt"
emot_dic = ""
data = {}  # List for save the Lexicon


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

print(emot_dic)

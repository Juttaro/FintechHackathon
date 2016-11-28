from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
import time
from random import shuffle

st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz','stanford-ner//stanford-ner-3.6.0.jar', encoding='utf-8')

def tokenizeClassify(text):
    tokenized_text = word_tokenize(text)
    return st.tag(tokenized_text)

def allFiles(flagged,n):
    start = time.time()
    files = os.listdir(os.getcwd() + "/emails" + flagged)
    shuffle(files)
    for file in files[:n]:
        with open("emails"+flagged+"/"+file, 'r') as email:
            text = email.read()
            tokenized = tokenizeClassify(text)
            names = set(map(lambda tup: tup[0],filter(lambda tup: tup[1] == 'PERSON',tokenized)))
            file = open("emailNames"+flagged+"/"+file, 'w')
            for name in names:
                file.write(name+"\n")
                file.flush()
            file.close()
    print(time.time() - start)

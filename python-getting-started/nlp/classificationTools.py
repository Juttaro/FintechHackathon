import nltk
import os
from random import shuffle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from datetime import datetime
from nltk import classify, NaiveBayesClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pickle


def listOfFiles(flagged):
    files = os.listdir(os.getcwd() + "/emailNames" + flagged)
    listToReturn = []
    for file in files:
        with open("emailNames" + flagged + "/" + file, 'r') as names:
            listToReturn.append(([word[:-1].lower for word in names], flagged))
            names.close()
    return listToReturn


documents = listOfFiles("Flagged") + listOfFiles("NotFlagged")
shuffle(documents)

all_words = []
for document in documents:
    all_words.extend(document[0])

word_features = nltk.FreqDist(all_words)


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

try:
    d = SklearnClassifier(MultinomialNB())
    d.train(featuresets[:300])
    print(classify.accuracy(d, featuresets[300:]))
except:
    print("d")

try:
    a = NaiveBayesClassifier.train(featuresets[:300])
    print(classify.accuracy(a, featuresets[300:]))
except:
    print("a")

try:
    e = SklearnClassifier(LinearSVC())
    e.train(featuresets[:300])
    print(classify.accuracy(e, featuresets[300:]))
except:
    print("e")
try:
    f = SklearnClassifier(SVC(), sparse=False)
    f.train(featuresets[:300])
    print(classify.accuracy(f, featuresets[300:]))
except:
    print("f")
try:
    g = SklearnClassifier(LinearSVC())
    g.train(featuresets[:300])
    print(classify.accuracy(g, featuresets[300:]))
except:
    print("g")
try:
    h = nltk.classify.DecisionTreeClassifier.train(featuresets[:300], entropy_cutoff=0, support_cutoff=0)
    print(classify.accuracy(h, featuresets[300:]))
except:
    print("h")


def saveClassifier(classifier):
    pickleClassifier = open(classifier.__name__ + datetime.now().strftime('%H:%M:%S') + ".pickle", "wb")
    pickle.dump(classifier, pickleClassifier)
    pickleClassifier.close()
    return classifier


def loadClassifier(name):
    pickledClassifier = open(name, "rb")
    classifier = pickle.load(pickledClassifier)
    pickledClassifier.close()
    return classifier

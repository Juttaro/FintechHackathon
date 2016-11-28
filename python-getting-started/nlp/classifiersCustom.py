

class classify:



    trainClassifier = lambda classifier, training_data: classifier.train(training_data)
    testClassifier = lambda classifier, test_data: classify.accuracy(classifier, test_data)
    topResults = lambda classifier, numberOfFeatures: classifier.show_most_informative_features(numberOfFeatures)

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
from numpy import *
from constructTrainingSet import constructTrainingSet
from predictLabels import predictLabels
from smoothing import smoothing

def classify(trainSet, trainLabels, testSet):
    features, survivors, deads = constructTrainingSet(trainSet,trainLabels)
    totalPassengers = survivors+ deads
    prSur = survivors / float(totalPassengers) #Compute P(surv)
    prDead = deads / float(totalPassengers) #Compute P(dead)
    smoothing(features, survivors, deads)
    predictedLabels = predictLabels(testSet, features, prSur, prDead)   
#    for i in range(len(testSet)):
#        if testSet[i,3] == 'female':
#            predictedLabels[i] = 1
    return predictedLabels
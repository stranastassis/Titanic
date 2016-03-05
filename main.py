from numpy import *
from sklearn import cross_validation
import csv as csv
from classify import classify
#from constructTrainingSet import constructTrainingSet
#from predictLabels import predictLabels
#from smoothing import smoothing


# Load data
csv_file_object = csv.reader(open('train.csv', 'rb')) # Load in the csv file
header = csv_file_object.next() 					  # Skip the fist line as it is a header
data=[] 											  # Create a variable to hold the data

for row in csv_file_object: # Skip through each row in the csv file,
    data.append(row[0:]) 	# adding each row to the data variable
X = array(data) 		    # Then convert from a list to an array.

y = X[:,1].astype(int) # Save labels to y 

X = delete(X,1,1) # Remove survival column from matrix X

X = delete (X,0 ,1)

        
#Get Social status
for j in range(X.shape[0]):
    temp=X[j,1].split('.')
    temp=temp[0].split(', ')
    X[j,1]=temp[1]
    if(X[j,9]==''):
        X[j,9]='U'

#Calculate the number of Cabins and transform the Cabin column
numofCabins=[]
for i in range(X.shape[0]):
    if(len(X[i,8])>0):
       col=X[i,8].split(' ') 
       numofCabins.append(len(col))
       if(col[0][1:]==''):
           num=0
       else:    
           num =int( col[0][1:] )
       num = num % 2
       X[i,8]=col[0][0] +str(num)
    else:
       numofCabins.append(1)
X = column_stack ( (X, numofCabins ) )     
for i in range(X.shape[0]):
        X[i,6]= X[i,6].split(' ')[0]
        

#Fill the missing ages with the average price of the same Social status' ages.        
for i in range(X.shape[0]):
    if(X[i,3]==''):
        suma=0
        count=0
        for j in range(X.shape[0]):
            if((X[i,1]==X[j,1]) and X[j,3]!=''):
                count=count+1
                suma=suma+float((X[j,3]))
                
        X[i,3]=str(suma/count)

# Initialize cross validation      
kf = cross_validation.KFold(X.shape[0], n_folds=10)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalCorrect = 0 # Variable that will store the correctly predicted intances  
#csv_file_object2 = csv.reader(open('test.csv', 'rb')) # Load in the csv file
#header = csv_file_object2.next() 					  # Skip the fist line as it is a header
data=[] 											  # Create a variable to hold the data
#
#for row in csv_file_object2: # Skip through each row in the csv file,
#    data.append(row[0:]) 	# adding each row to the data variable
#XX = array(data) 	    # Then convert from a list to an array.
#passId = XX[0:,0]
#XX=delete (XX,0 ,1)
##Get Social status
#for j in range(XX.shape[0]):
#    temp=XX[j,1].split('.')
#    temp=temp[0].split(', ')
#    XX[j,1]=temp[1]
#    if(XX[j,9]==''):
#        XX[j,9]='U'
#
#
#numofCabins=[]
#for i in range(XX.shape[0]):
#    if(len(XX[i,8])>0):
#       col=XX[i,8].split(' ') 
#       numofCabins.append(len(col))
#       if(col[0][1:]==''):
#           num=0
#       else:    
#           num =int( col[0][1:] )
#       num = num % 2
#     #  print numofCabins[i]
#       XX[i,8]=col[0][0] +str(num)
#    else:
#       numofCabins.append(1)
#XX = column_stack ( (XX, numofCabins ) )     
#for i in range(XX.shape[0]):
#        XX[i,6]= XX[i,6].split(' ')[0]
#        
#for i in range(XX.shape[0]):
#    if(X[i,3]==''):
#        suma=0
#        count=0
#        for j in range(XX.shape[0]):
#            if((XX[i,1]==XX[j,1]) and XX[j,3]!=''):
#                count=count+1
#                suma=suma+float((XX[j,3]))
#                
#        X[i,3]=str(suma/count)
#
#for i in range(XX.shape[0]):
#    if(XX[i,8]==''):
#        XX[i,8]='U'

for trainIndex, testIndex in kf:
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]
	
    predictedLabels = classify(trainSet, trainLabels, testSet)
    
#    features, survivors, deads = constructTrainingSet(X,y)
#    totalPassengers = survivors+ deads
#    prSur = survivors / float(totalPassengers) #Compute P(surv)
#    prDead = deads / float(totalPassengers) #Compute P(dead)
#    smoothing(features, survivors, deads)
#    
#    realLabels=predictLabels(XX,features,prSur,prDead)
#    

    correct = 0	
    for i in range(testSet.shape[0]):
        if predictedLabels[i] == testLabels[i]:
            correct += 1
        
    print 'Accuracy: ' + str(float(correct)/(testLabels.size))
    totalCorrect += correct
    totalInstances += testLabels.size
#target = open('myResult2.csv', 'w')
#target.write('PassengerId,Survived')
#target.write("\n")
#for i in range(passId.shape[0]):
#    target.write(passId[i])
#    target.write(',')
#    target.write(str(realLabels[i]))
#    target.write("\n")
#target.close()
print 'Total Accuracy: ' + str(totalCorrect/float(totalInstances))
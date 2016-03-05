def constructTrainingSet(trainset,trainlabel):
    
    dead = 0 # Number of dead ppl
    survivors = 0 # Number of survivors
    
    features = {} # Set of values of all passengers
    
    # Read  the training set
    for i in range(trainset.shape[0]):
        if trainlabel[i] == 1: # If the label is 1 it is a survivor
                
                survivors += 1
                for j in range(trainset.shape[1]):
                    if trainset[i,j] in features:
                        features[trainset[i,j]]['surv'] +=1
                    else:
                        features[trainset[i,j]] = {'surv':1, 'dead':0}
                
        # =====================================================================
                
        else: # If the label is 0 it is a dead
            
                dead += 1
                for j in range(trainset.shape[1]):
                    if trainset[i,j] in features:
                        features[trainset[i,j]]['dead'] +=1
                    else:
                        features[trainset[i,j]] = {'surv':0, 'dead':1}
                
    # =========================================================================          
    return features, survivors, dead

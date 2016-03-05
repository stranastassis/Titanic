def predictLabels(testSet, features, prSurv, prDead):
    predictions = []
   
    for i in range(testSet.shape[0]):
      pDead = prDead
      pSurv = prSurv 
      for j in range(testSet.shape[1]):
          if testSet[i,j] in features:
                    pDead *= features[testSet[i,j]]['dead']                
                
            
	    	# ==============================================================
          
          if testSet[i,j] in features:
              pSurv *= features[testSet[i,j]]['surv']   
                 
            # =============================================================
            
		
	 # Give the label with highest probability
      if pDead > pSurv:
          predictions.append(0)
      else:
          predictions.append(1)
                
    return predictions

def smoothing(features, survivors, dead):
    # Apply Laplace smoothing and compute P(x|surv) and 
    # P(x|dead) for the all the available characteristics        
    for word in features:
        features[word]['surv'] += 1
        features[word]['dead'] += 1
        features[word]['surv'] /= float(survivors+1)
        features[word]['dead'] /= float(dead+1)

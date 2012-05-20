from collections import Counter
from matplotlib import pyplot as plt
import Orange as orng
import math


def load_data():
    """Return data from train.tab."""
    
    f = open('train.tab')
    return [[float(v) for v in l.strip().split("\t")] for l in f.readlines()[3:]]

def print_domain_info(d):
    """Print info about the domain (number of attributes, attribute domain, etc."""
    
    c = Counter()
    [c.update(e[1:]) for e in d]
    
    # count the number of unique values for each attibute:
    discBin = 0
    disc5 = 0
    for i in range(len(d[0])):
        a = [e[i] for e in d[1:]]
        s = set()
        [s.add(e) for e in a]
        if len(s) == 2:
            discBin += 1
        if len(s) <= 5:
            disc5 += 1
    
    print "St. potencialno diskretnih %d (binarnih)" % discBin
    print "St. potencialno diskretnih %d (5 razlicnih vrednosti)" % disc5
    print "St. atributov: %d St. primerov: %d" % (len(d[0])-1, len(d))
    print "5 najbolj pogostih vrednosti atributov: " + str(c.most_common(5))

def scoring(d):
    """Return scoring based on relief algorithm"""
    
    r = orng.feature.scoring.Relief(check_cached_data=False)
    s = orng.feature.scoring.score_all(d, r)
    return orng.feature.selection.FilterAboveThreshold(measure=r, threshold=0.0)

def get_learners(d, filter):
    """Return learners used by crossvalidation"""
    
    learners = [
        orng.ensemble.forest.RandomForestLearner(),
        orng.classification.bayes.NaiveLearner(),
        orng.classification.knn.kNNLearner(), 
    ]
    return [orng.feature.selection.FilteredLearner(l, filter=filter) for l in learners]

def logloss(results):
    """Return the log loss score"""
    #for r in results:
    print sum([y[1]*math.log(y[1])+(1-y[0])*math.log(1-y[1]) for y in results])/len(results) * -1   

def set_probabilities(x):
    """Set the probabilities for each learner"""
    global pred
    [pred[i].append([x.actual_class, y[1]*0.998+0.00001]) for i,y in enumerate(x.probabilities)]
    
if __name__ == '__main__':
    #d = load_data()
    #print_domain_info(d)
    d = orng.data.Table('train.tab')
    score_filter = scoring(d)
    learners = get_learners(d, score_filter)
    
    r = orng.evaluation.testing.cross_validation(learners, d, folds=10)
    pred = [[] for _ in r.results[0].probabilities]
    
    # add predictions to each learner:
    map(set_probabilities, r.results)

    map(logloss, pred)
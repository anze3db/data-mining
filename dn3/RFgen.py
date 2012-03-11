from sys import stdout
import Orange
import cPickle
import copy
import jrs2
import sys
reload(jrs2)
r = jrs2.RawData()
r.remove_empty_features(6)
r.convert_to_orange()
discretize = False
NUM_TREES = 500

print "Loading the data ..."
data = jrs2.Data()

if discretize:
    data.ml_data = data.discretize(data.ml_data)
    data.test_data = data.discretize(data.test_data)

all = {'test':[], 'training':[]}
for i in xrange(2000):
    all['test'].append({})
    all['training'].append({})


for a,i in enumerate(data.classes):
    train = data.get_single_class_data(label=i)
    test = data.test_data
    test = jrs2.add_dummy_class(test, train)
    #Orange.ensemble.forest.RandomForestLearner(trees=100)
    learner = Orange.ensemble.forest.RandomForestLearner(trees=NUM_TREES)
    classifier = learner(train)
    stdout.flush()
    stdout.write("\rCurrent class: %s, %.2f %% done" % (str(i), a*100/82.0))
    
    train_results = []
    test_results = []
    for j,d in enumerate(train):
        all['training'][j][i] = {'real': str(d[-1]), 'predicted': classifier(d,2)[1][1]}
        
    for j,d in enumerate(test):
        all['test'][j][i] = {'predicted': classifier(d,2)[1][1]}
    
cPickle.dump(all, file("../randomForest-"+str(NUM_TREES)+"-results.pickle", "wb"), -1)
#learner = Orange.ensemble.forest.RandomForestLearner(trees=10, name="rf", )

#test = data.test_data
#test = jrs2.add_dummy_class(test, train)

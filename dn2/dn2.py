'''
Created on Feb 27, 2012

@author: smotko

'''
from sys import stdout
import Orange
import cPickle
import jrs
import random

NUM_PERM = 100
ALPHA = 0.0
ml_data = jrs.Data(discretized=True)
cnt = 0
all = []
for c in ml_data.classes.keys():
    cnt+=1
    data = ml_data.get_single_class_data(c) # c40 is defaut
    
    orgc = [d.get_class() for d in data]
    gain = []
    original = [Orange.feature.scoring.InfoGain(feature, data) for feature in data.domain.features]
    for perm in xrange(NUM_PERM):
        random.shuffle(orgc)
        [d.set_class(orgc[i]) for i,d in enumerate(data)]
        arr = [Orange.feature.scoring.InfoGain(feature, data) for feature in data.domain.features]
        gain.append(arr)
        stdout.flush()
        stdout.write("\rProgress: %3d%% current: %3s @ %3d%%" % (cnt*100/82, c, perm*100/NUM_PERM))

    less = []
    for oi,o in enumerate(original):
        less.append(len([x[oi] for i,x in enumerate(gain) if x[oi] > o])/float(NUM_PERM) < ALPHA)
    
    all.append({'c': c, 'i': [i for i,x in enumerate(less) if x]})
cPickle.dump(all, file("dump-"+str(NUM_PERM)+"-"+str(ALPHA)+".pickled", "w"), -1)
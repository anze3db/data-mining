from Rclassify import RClassify


def k_fold(X, K):
    #from random import shuffle; X=list(X); shuffle(X)
    for k in xrange(K):
        training = [x for i, x in enumerate(X) if i % K != k]
        validation = [x for i, x in enumerate(X) if i % K == k]
        yield training, validation
        
def f_score(tt, pt):
    inter = intersect(tt, pt)
    if(len(pt) == 0): return 0
    prec = float(inter)/len(pt)
    recall = float(inter)/len(tt)
    if prec*recall == 0:
        return 0
    return 2*(prec*recall/(prec+recall))

def intersect(tt, pt):
    intersect = 0
    for i in tt:
        if i in pt: intersect += 1
    return intersect

if not vars().has_key('lightData'):
    from lightData import *

scores = []
for t, v in k_fold(range(len(lightData)), 10):
    kD = [lightData[i] for i in t]
    kL = [lightLabels[i] for i in t]
    r = RClassify(kD, kL)
        
    for x in v:
        a = r.getClasses(lightData[x])
        print lightLabels[x], a
        scores.append(f_score(lightLabels[x], a))
    print sum(scores)/float(len(scores)),sum(scores),len(scores)
print sum(scores)/float(len(scores)),sum(scores),len(scores)
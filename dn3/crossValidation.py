from Rclassify import RClassify
import datetime


def k_fold(X, K):
    from random import shuffle; X=list(X); shuffle(X)
    for k in xrange(K):
        training = [x for i, x in enumerate(X) if i % K != k]
        validation = [x for i, x in enumerate(X) if i % K == k]
        yield training, validation
        
def f_score(tt, pt):
    inter = intersect(tt, pt)
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
r = None
scores = []
for t, v in k_fold(range(len(lightData)), 3):
    print len(t),len(v), len(lightData)
    kD = [lightData[i] for i in t]
    kL = [lightLabels[i] for i in t]
    r = RClassify(kD, kL)
    curr_score = []
    aaaa = 0
    for x in v:
        aaaa += 1
        a = r.getClasses(lightData[x])
        print lightLabels[x], a, f_score(lightLabels[x], a)
        
        curr_score.append(f_score(lightLabels[x], a))
    print aaaa
    print sum(curr_score)/float(len(curr_score)),sum(curr_score),len(curr_score)
    scores += curr_score
print sum(scores)/float(len(scores)),sum(scores),len(scores)

if True:
    c = open("../testDataT.csv")
    f = open('../result-1Rb.csv', 'w')
    for line in c:
        result = r.getClasses([int(i) for i in line.strip().split("\t")])
        #print result
        aa = ""
        for i in result:
            aa += str(i) + " "
        
        print aa[:-1]
        f.write(aa[:-1] + "\n")
    c.close()
    f.close()

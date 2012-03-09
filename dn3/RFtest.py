import cPickle
import crossValidation

NUM_TREES = 10
LIMIT = 5
FILTER = 0.15


all = cPickle.load(file("../randomForest-"+str(NUM_TREES)+"-results.pickle"))

fscore = []
results = []
for i in all['training']:
    tt = [int(a[1:]) for a in  i.keys() if i[a]['real'] == 'T']
    pt = [int(a[0][1:]) for a in sorted(i.items(), key=lambda t: t[1]['predicted'], reverse=True) if i[a[0]]['predicted'] > FILTER]
    pt = pt[:LIMIT]
    if len(pt) == 0:
        pt = [40, 44, 18, 62, 41]
    fscore.append(crossValidation.f_score(tt, pt)) 
for i in all['test']:
    pt = [int(a[0][1:]) for a in sorted(i.items(), key=lambda t: t[1]['predicted'], reverse=True) if i[a[0]]['predicted'] > FILTER]
    pt = pt[:LIMIT]
    if len(pt) == 0:
        print "aaa"
        pt = [40, 44, 18, 62, 41]
    results.append(pt)
finalScore = sum(fscore)/(float(len(fscore)))
print finalScore


if True:
    f = open('../resultRF-%.5f.csv' % finalScore , 'w')
    for r in results:
        result = r[:5]
        #print result
        aa = ""
        for i in result:
            aa += str(i) + " "
        
        f.write(aa[:-1] + "\n")
    f.close()
    #crossValidation.f_score(tt, pt)
import cPickle
import crossValidation

NUM_TREES = 250
LIMIT = 30
FILTER =  0.30

#randomForestCross1600-50-results.pickle
all = cPickle.load(file("../randomForest-"+str(NUM_TREES)+"-results.pickle"))

fscore = []
results = []
for i in all['training'][1600:]:
    tt = [int(a[1:]) for a in  i.keys() if i[a]['real'] == 'T']
    if(len(tt) == 0): continue
    s = sorted(i.items(), key=lambda t: t[1]['predicted'], reverse=True)
    
    #for i,x in enumerate(s):
    #    s[i][1]['predicted'] = s[i][1]['predicted']/s[0][1]['predicted']
    #pt = [int(x[0][1:]) for i,x in enumerate(s) if x[1]['predicted'] > 0.1+(i*LIMIT)]
    
    pt = [int(x[0][1:]) for i,x in enumerate(s) if x[1]['predicted'] > s[0][1]['predicted']*(FILTER+(i/LIMIT))]
    print tt, pt, crossValidation.f_score(tt, pt)
    fscore.append(crossValidation.f_score(tt, pt)) 
for i in all['test']:
    s = sorted(i.items(), key=lambda t: t[1]['predicted'], reverse=True)
    #for i,x in enumerate(s):
    #    s[i][1]['predicted'] = s[i][1]['predicted']/s[0][1]['predicted']
    #pt = [int(x[0][1:]) for i,x in enumerate(s) if x[1]['predicted'] > 0.1+(i*LIMIT)]
    pt = [x[0][1:] for i,x in enumerate(s) if x[1]['predicted'] > s[0][1]['predicted']*(FILTER+(i*LIMIT))]
    print pt
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
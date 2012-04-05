from collections import Counter

hairy = open("RFand1R-2-2")
majcn = open("resultRF-0.72388.csv")
smotko = open("smotkoTopScore.csv")
zidar = open("result-0.36027.csv")
aaa = open("resultRF-0.85714.csv")

a = []
a.append([[int(j) for j in i.strip().split(" ")] for i in majcn.readlines()])
a.append([[int(j) for j in i.strip().split(" ")] for i in zidar.readlines()])
a.append([[int(j) for j in i.strip().split(" ")] for i in smotko.readlines()])
a.append([[int(j) for j in i.strip().split(" ")] for i in hairy.readlines()])
a.append([[int(j) for j in i.strip().split(" ")] for i in aaa.readlines()])
b = []
for i in xrange(len(a[0])):
	c = Counter(a[0][i]+a[1][i]+a[2][i]+a[3][i]+a[4][i])
	b.append([x[0] for x in Counter.most_common(c) if x[1]>1])
	if len(x)==0 :
		x = [40, 44, 18, 62, 41]
		print "aa"
for i in b:
	if len(i) == 1:
		print "aaa"
print "bb"
f = file("RFand1R-2-2","w")
f.write("\n".join(   [" ".join([str(x) for x in i]) for i in b ]    ))
f.flush()
f.close()

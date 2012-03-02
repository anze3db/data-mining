from matplotlib import pyplot as plt
import cPickle


#FILE_NAME = "dump-10-0.01.pickled"
FILE_NAME = "dump-100-0.01.pickled"

PERM = FILE_NAME.split('-')[1]
ALPHA = FILE_NAME.split('-')[2][0:4]

data = cPickle.load(open(FILE_NAME))

hist = []
for i in xrange(len(data)):
    hist.append(len(data[i]['i']))

plt.close()
plt.hist(hist, 20)
plt.xlabel("St. atributov")
plt.ylabel("Razredi")
plt.title("St. atributov na posamezen razred (%s permutacij, %s alpha)" % (PERM, ALPHA))
plt.savefig('report/%s-%s.png' % (PERM, ALPHA))
plt.show()
plt.close()
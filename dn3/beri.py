import Orange
import collections
import itertools
import cPickle

labels_file_name = "../trainingLabels.csv"

def labels():
    """Store label profile (keys are labels, items labeled instances) in self.lprofile."""
    f = file(labels_file_name)
    lprofile = collections.defaultdict(set)
    for i, line in enumerate(f):
        labels = line.strip().split(",")
        for x in labels:
             lprofile[x].add(i)
    return lprofile.keys()

def to_orange(attr_file, labels_file=None, domain=None):
        
        #construct a domain
    class_vars = [Orange.feature.Discrete("c%s" % i, values=["F","T"]) for i in labels()]
    n_att = len(open(attr_file, "rt").read().split("\n")[0].strip().split("\t"))
    domain = Orange.data.Domain([Orange.feature.Continuous("%d" % i) for i in range(n_att)], False, 
         class_vars=class_vars)

    data = Orange.data.Table(domain)

    ff = open(attr_file)

    if labels_file:
        fl = open(labels_file)
        for fline, lline in itertools.izip(ff, fl):
            d = Orange.data.Instance(domain, [int(v) for v in fline.strip().split("\t")])
            dlabels = set(lline.strip().split(","))
            d.set_classes([["F", "T"][lab in dlabels] for lab in labels()])
            data.append(d)
    else:
        for fline in ff:
            d = Orange.data.Instance(domain, [int(v) for v in fline.strip().split("\t")])
            data.append(d)            

    return data

def load_data():
    train_data = to_orange("../trainingDataT.csv", labels_file="../trainingLabels.csv")
    test_data = to_orange("../testDataT.csv", labels_file=None, domain=train_data.domain)
    return train_data, test_data

def get_single_class_data(data, label="c40"):
    """Construct a data set with given label as a class."""
    name_at = { at.name: at for at in data.domain.class_vars }
    domain = Orange.data.Domain(data.domain.features, name_at[label])
    return Orange.data.Table(domain, data)

train_data, test_data = load_data()
cPickle.dump(train_data, file('../trainDataT.pickle', 'w'), -1)
cPickle.dump(test_data, file('../testDataT.pickle', 'w'), -1)
#selection of a single class
tsc = get_single_class_data(train_data, label="c40")

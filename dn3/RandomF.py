from time import time
import Orange
import cPickle
import orngEnsemble


def get_single_class_data(data, label="c40"):
    """Construct a data set with given label as a class."""
    name_at = { at.name: at for at in data.domain.class_vars }
    domain = Orange.data.Domain(data.domain.features, name_at[label])
    return Orange.data.Table(domain, data)

start = time()
train_data = cPickle.load(file('../trainDataO.pickled'))

test_data = cPickle.load(file('../testDataO.pickled'))

trainClasses = {v.name:v for v in train_data.domain.class_vars}
trainSingleClass = lambda x: Orange.data.Table(Orange.data.Domain(train_data.domain.features + [trainClasses[x]]), train_data)
forest = orngEnsemble.RandomForestLearner(trees=1, name="forest")
for cn in trainClasses:
    trainSingleData = trainSingleClass(cn)
    cl = forest(trainSingleData)
    cl(test_data[0])

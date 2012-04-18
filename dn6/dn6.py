if __name__ == '__main__':
    f = open('train.tab')
    for l in f.readlines()[3:]:
        print l.split("\t")

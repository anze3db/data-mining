a = open("../trainingDataT.csv")
lightData = []
for line in a:
    lightData.append([int(i) for i in line.strip().split("\t")])

r = RClassify(kD, kL)
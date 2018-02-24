# coding=utf-8

from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # print(dataSet.shape) # (4, 2)
    dataSetSize = dataSet.shape[0]

    # 计算距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print(diffMat)

    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    print(sortedDistIndicies)

    classCount = {}

    # 选择距离最小的k个点
    for i in range(k):
        voteIlable = labels[sortedDistIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 排序

    return sortedClassCount[0][0]


group, labels = createDataSet()
# print(group)
# print(labels)

print(classify0([0, 0], group, labels, 3))

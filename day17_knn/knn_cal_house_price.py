import numpy as np


def knn(feature, label, predict_feature, k):
    distance = feature - predict_feature
    distance_square = np.square(distance)
    sum = np.sum(distance_square, axis=1)
    sort_index = np.argsort(sum)
    sort_label = label[sort_index]
    price = np.sum(sort_label[0:k]) / k
    return price


if __name__ == '__main__':
    feature = np.loadtxt("cal_housing.data", delimiter=",", usecols=(0, 1, 2, 3, 4, 5, 6, 7))
    label = np.loadtxt("cal_housing.data", delimiter=",", usecols=(8))
    print("feature={}".format(feature))
    print("label={}".format(label))

    predict_feature = [-122.270000, 37.840000, 52.000000, 2436.000000, 541.000000, 1015.000000, 478.000000, 1.725000]
    # 113900.000000
    price = knn(feature, label, predict_feature, 200)
    print(price)

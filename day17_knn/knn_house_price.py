import numpy as np

feature = np.array([
    [-121, 47],
    [-121.2, 46.5],
    [-122, 46.3],
    [-120.9, 46.7],
    [-120.1, 46.2]
])

label = np.array([200, 210, 250, 215, 232])

predict_point = np.array([-121, 46])

distance = feature - predict_point
print("distance={}".format(distance))
distance_square = np.square(distance)
print("distance_square={}".format(distance_square))
sum = np.sum(distance_square, axis=1)
print("sum={}".format(sum))

sort_index = np.argsort(sum)
sort_label = label[sort_index]
print("sort_label={}".format(sort_label))

k = 3
price = np.sum(sort_label[0:k]) / k
print("price={}万".format(price))

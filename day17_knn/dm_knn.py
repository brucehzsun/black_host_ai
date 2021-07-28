import numpy as np
import collections

data = np.array([
    [154, 1],
    [126, 2],
    [70, 2],
    [196, 2],
    [161, 2],
    [371, 4]
])

# 取第一列
feature = data[:, 0]
print("feature=", feature)

# 取最后一列
label = data[:, -1]
print("label=", label)

# 获取距离200最近的feature的值
predict_position = 200
distance = list(map(lambda x: abs(predict_position - x), feature))
print("distance=", distance)

# 排序，获取index的值
sort_index = np.argsort(distance)
print("sort_index=", sort_index)

# 获取排序后的label
sort_label = label[sort_index]
print("sort_label=", sort_label)

# 获取topK的label
k = 3
top_k_label = sort_label[0:k]
print("top_k_label=", top_k_label)

# 获取topK的count
result = collections.Counter(top_k_label).most_common(1)
print("result=", result)

# 获取topK的label
result = result[0][0]
print("predict_label=", result)

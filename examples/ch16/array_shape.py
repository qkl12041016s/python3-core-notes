import numpy as np

# shape 说明两行两列，axis=0 沿行方向汇总。
values = np.array([[1, 2], [3, 4]], dtype=np.int64)
print(values.shape)
print(values.sum(axis=0).tolist())

# 基础切片共享数据，复制后再独立修改。
selected = values[:, :1].copy()
selected[0, 0] = 9
print(values[0, 0])

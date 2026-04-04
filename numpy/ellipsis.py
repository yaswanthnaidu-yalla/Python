import numpy as np
a = np.ones((2, 3, 4, 5))
print(a[0, ...].shape)
print(a[..., 0].shape)
print(a[0, ..., 0].shape)
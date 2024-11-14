import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])

print(array)
print(type(array))
print(array[1::2])
print(array.ndim)
print(array.dtype)
print(array.view())
print(array.base)
print(array.shape)
print(array.reshape(3,3))

x = array.copy()
print(x.base)

y = array.view()
print(y.base)
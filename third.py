import numpy as np 

my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_array5.ndim)
print(my_array5.shape)

print("#" * 50)

# reshaped_array5 = my_array5.reshape(-1)
# reshaped_array5 = my_array5.reshape(4, 5)
reshaped_array5 = my_array5.reshape(2, 5, 2)
print(reshaped_array5.ndim)
print(reshaped_array5.shape)
print(reshaped_array5)
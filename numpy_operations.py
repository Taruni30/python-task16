
import numpy as np
a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
a3 = np.array([[[1, 2], [3, 4]]])

print("1D Array:", a1)
print("2D Array:\n", a2)
print("3D Array:\n", a3)

print("\nAddition:", a1 + 5)
print("Multiplication:", a1 * 2)
print("Square Root:", np.sqrt(a1))

b = np.array([10, 20, 30])
print("\nBroadcasting:\n", a2 + b)

print("\nMean:", np.mean(a1))
print("Sum:", np.sum(a1))
print("Max:", np.max(a1))

lst = [1, 2, 3]
print("\nList * 2:", [x * 2 for x in lst])
print("NumPy * 2:", a1 * 2)

rand = np.random.randint(1, 10, (2, 2))
print("\nRandom Array:\n", rand)

x = np.arange(5)
print("\nVectorized:", x * 10)

print("\nShape:", a2.shape)
print("Dimensions:", a2.ndim)
print("Size:", a2.size)

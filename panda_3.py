import numpy as np  
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
arr1 =np.array([1,2,3,4])
arr2 = np.array([[2],[3],[4],[6]])
print(arr1)
print(arr2)
arr3 = arr1+arr2
print (arr3)

A = np.array([[1, 2], [3, 4]]) # Macierz 2x2
B = np.array([[5, 6], [7, 8]])
C = A @ B
print(C)

arr_gen = gen(pcg(seed=91))
arr=arr_gen.normal(size=(5,5))

print (f"matrix of randoms:\n {arr}")

arr_gen = gen(pcg(seed=91))
arr=arr_gen.integers(low=10,high=100,size=(5,5))

print (f"matrix of randoms:\n {arr}")


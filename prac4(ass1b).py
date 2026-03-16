import numpy as np

# Generate two 3x3 matrices with random numbers (1 to 9)
A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Matrix Addition
print("Addition of matrices:")
print(A + B)

# Matrix Multiplication
print("Multiplication of matrices:")
print(np.dot(A,B))
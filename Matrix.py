import numpy as np

# Matrix:  it looks same as 2 diamensional numpy array but type is different

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(type(arr))


matrix = np.matrix([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(type(matrix))


# arithmatic operation in matrix

m1 = np.matrix([[1,2,3],
                [4,5,6],
                [7,8,9]])

m2 = np.matrix([[10,20,31],
                [42,54,60],
                [74,85,93]])

# addition
add = m1 + m2
print(add)
print()

# subtraction
sub = m1 - m2
print(sub)

# multiplication in matrix : dot() function

multiply = m1.dot(m2)
print('multiplication: ',multiply)




# Matrix function : Transpose, Swapaxes, Inverse, Power, Determinate

# transpose: it change rows into column and,   column into rows

t = np.array([[3,4,5],
              [7,9,5]])

t1 = np.transpose(t)
print(t1)

y = np.array([[20,40],
              [10,40]])

y1=  np.transpose(y)
print(y1)
print()

# swapaxes: np.swapaxes(var,axis=0,axis=1) because by default axis =0 means row
t = np.array([[3,4,5],
              [7,9,5]])

print('swapaxes: ',np.swapaxes(t,0,1))


# inverse:  it divide each number with 1/-2

li =np.array([[1,2],
              [3,4]])
j= np.linalg.inv(li)
print('inverse: ',j)

# power : np.linalg.matrix_power(var, n) n means power n=0,n<0, n>0
li1 =np.array([[1,2],
              [3,4]])

v=  np.linalg.matrix_power(li1,2)
print('power : ',v)

# determinant : np.linalg.det(var)
li2 =np.array([[1,2],
              [3,4]])

print(np.linalg.det(li2))
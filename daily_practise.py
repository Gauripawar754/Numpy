
import numpy as np

# creating array
arr_1d= np.array([1,2,3,4])
arr_2d= np.array([[1,3,4,5],[3,4,4,4]])
aar_3d = np.array([[[2,3],
                    [5,6]],
                   [[3,7],
                     [1,0]]])


# initializing array
zeros_arr = np.zeros((3,4))
print(zeros_arr)

ones = np.ones((3,6))
print(ones)

em_arr = np.empty((3,3)) # uninitialized random number
print(em_arr)

full_arr = np.full((2,7),90) # 2 rows,7 column filled with 90
print(full_arr)

identity_matrix = np.eye((4)) # 4x4 identity matrix filled with 0 and 1
print(identity_matrix)



# range of numbers array
range_arr = np.arange(1,11,2) # Start at 1, stop before 11, step by 2
print(range_arr)

linspace_arr = np.linspace(1,10,4) # 4 equally spaced number from 1 to 10
print(linspace_arr)




# random array
# 1 random.random
random_arr = np.random.random((4,4)) # need to mention row column in one argument
print(random_arr)

# randint
randint_arr = np.random.randint(100,200,(3,4)) # 3 rows, 4 column filled with random number from 100 to 200
print(randint_arr)

# randn
randn_arr = np.random.randn(3,4)  # it takes directly values for rows and column
print(randn_arr)




# inspecting array
arr1 = np.array([[16,24,36,48,59,68,79,80],
                 [3,4,5,6,6,7,8,8]] , dtype=np.float16)
print(arr1.shape) #rows and column
print(arr1.size) # no. of element
print(arr1.ndim) #number of dimension
print(arr1.dtype) #returns datatype of element
print(arr1.itemsize) #returns size of one element in bytes
print(arr1.nbytes) #returns total size of array

print(np.info(np.array)) #provide detailed information about a NumPy function or array

print(np.info(np.array))
np.info(np.array)


print(arr1.itemsize)
print(arr1.nbytes)

# array indexing and slicing
hi = np.array([[10, 20, 30],
               [40, 50, 60], 
               [70, 80, 90]])

# basic indexing            
print(hi[1,2]) # row 1 ,second element
print(hi[0]) #row
print(hi[1,1]) #row 1 first element

# slicing
print(hi[0:2], 'yii') #row 0-2
print(hi[1 , : ],'ji') # first row all columns
print(hi[ :,1],'gi') # first column all rows
print(hi[0:1, 1:2]) # row 0 to 1 and column 1 to 2
print(hi[1, 1:2])  # output  50

# boolean indexing  and mask
mask = hi > 50
k = hi < 90
print (k)
print(mask)
print(hi[mask]) # it will print all >50 element
print(hi[k])

# fancy indexing pairs the row indices with the column indices one-to-one

rows = [0,2]
column =[1,2]
print(hi[rows,column]) 

c = [1,2]
b =[0,1]

print(hi[c,b])
# (0, 1) -> Element at row 0, column 1 -> 20.
# (2, 2) -> Element at row 2, column 2 -> 90.

x =[0,1]
y=[0,2]
print(hi [x,y])


r1 =[1,0]
r2 =[2,2]

print(hi[r1,r2],'hi')

# data types
t = np.array([1.2, 0 , 1.4, 1.9, 4], dtype=np.int16)
print(t.dtype)

new_t = t.astype(bool) # .astype() converts data types
print(new_t)

new = t.astype(float)
print(new)
print(t.astype(int))

g = np.array([12,1,2])
print(g.astype(float))

g = np.array([12,1,2])
print(g.astype(str))

g = np.array([12,1,2])
print(g.astype(bool))

print()



# random array
# 1 random.random
random_arr = np.random.random((4,4)) # need to mention row column in one argument  value = near zero
print(random_arr)
print()
b = np.random.random((3,5))

# randint
randint_arr = np.random.randint(100,200,(3,4)) # 3 rows, 4 column filled with random number from 100 to 200
print(randint_arr)
print()
x = np.random.randint(122,330,(3,5))

# randn
randn_arr = np.random.randn(3,4)  # it takes directly values for rows and column    value= 0 , less than 0 , greater than 0
print(randn_arr)

v = np.random.randn(4,5)
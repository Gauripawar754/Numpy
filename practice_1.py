# Array manipulation 
# 1.Reshaping
# 2.concatenation
# 3.splitting
# 4.arithmatic operation
# 5.aggregate function
# 6. linear algebra


import numpy as np

# arithmatic operation
a = np.array([1,22,45,4,5,6,7,8,9,10])
pr = 0
for i in  a:
    if i > 1:
      is_prime = True
      for x in range (2, i//2 + 1):
         if i % x == 0 :
            is_prime = False
      if is_prime:
        print(i, 'is prime number')
      else:
        print(i,'is not prime number')         



a = np.array([1,22,45,4,5,6,7,8,9,10])
b = np.array([20,30,60,11,444,66,4,6,8,9])

addd = a + b
print('addition',addd)

j = np.add(a,b)
print('addition using np.add',j)



sub = a - b 
print(f'subtraction: {sub}')

f = np.subtract(a,b)
print('using np.subtract',f)

modulus = np.mod(a,b)
print('mod',modulus)

di = np.divide(a,b)
h =  divmod(a,b)
print('division',di)
print(' quotiont  and remainder ',h)

power = np.power(a,2)
print('square: ',power)

print(np.power(b,3))

# reciprocal means  1/a
resi = np.reciprocal(a)
print('reciprocal:  ',resi)



# Arithmatic or aggregate function

di1 = np.array([10,23,30,49,48,50])
print('minimum: ', np.min(di1))

print('maximum: ',np.max(di1))

print('position of min value: ',np.argmin(di1))

print('position of max value: ',np.argmax(di1))

print('square root: ',np.sqrt(di1))

print('sin value of array: ', np.sin(di1))

print('cos value of array: ',np.cos(di1))

value = np.array([10,20,30,40,50,607,80,90,100])
sum_of_series = np.cumsum(value)
print('sum of series: ',sum_of_series)



#  for 2D Array
f1 = np.array([[2,1,5],
               [9,0,4]])

print('along column min: ', np.min(f1,axis=0))
print('along column max: ',np.max(f1,axis=0))

print('along row min: ', np.min(f1,axis=1))
print('along row max: ',np.max(f1,axis=1))

print('square root: ',np.sqrt(f1))



num = int(input('Enter number: '))
li = []
for i in range(1, num+1):
    li.append(i)

print('list: ',li)

arr1 = np.array(li)
add = np.cumsum(arr1)
print('cumulative sum are: ',add)


f=  int(input('Enter number: '))
k = []
for i in range(1,f+1):
   k.append(i)
print(k)

k1 = np.array(k)
print(np.cumsum(k1))


# reshaping of array:

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,22], ndmin=3)
reshap_arr = arr.reshape(4,3)   # reshape(rows,columns) multiplication of row and column number  should be equal to size of array
print(reshap_arr)

l = np.array([10,20,30,40,50])
print(l.reshape(5,1))


ori = reshap_arr.ravel()
print(ori)  # change  modified shape of  array  into  original shape
print()
print('shape  ',arr.shape)

print(reshap_arr.ndim)
print(arr.ndim)

v = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

v1 = v.reshape(2,6)
print(v1)

print('Transposing rows and column: ' )
trans = v1.T # T (transpose) :  it convert rows to column and column to rows
print(trans)

g = np.array([1,2])
print(g.T)

print('diamension of v1', v1.ndim) 

v2 = v1.ravel()

print(v2)

print()

# Broadcasting in Numpy Array
# broadcasting error occur when we perform addition on different dimension 
# if one of them diamension have column value 1  then addtion are performed 
# example: (2 x 3) (2 x 1)  one of them column have one value or same value
#          (2 x 3) (2 x 3)   performes operation
#          (2 x 3) (2 x 2)  will raise broadcast error

a1 = np.array([[1,3],
               [4,4]])
print(a1)
print('diamension of a1',a1.ndim)
print()

a2 = np.array([[1,3],
               [3,4]])

print(a2)
print('diamension of a2 ',a2.ndim)
print()

addition = a1 + a2
print(addition)


# Indexing
# 1D
c = np.array([3,5,7,1,8])
print(c[3])
print()

# 2D
c2 = np.array([[10,20,30],
               [20,305,60]])
print('diamension',c2.ndim)
print(c2[1,1])

# 3D

c3 = np.array([[[1,2],
                [4,6]],
               [[9,1],
                [7,4]]])

print(c3.ndim)
print(c3[1,0,1])


# Slicing [start:end:step]

# 1D
var1= np.array([100,200,300,456,600,678,345,245])

print('200 to 345: ',var1[1:-1] )
print('200 to End: ',var1[1: ])
print('start to 678: ',var1[ :-2])

print('start to end skip second number: ',var1[ : : 2])

# 2D

var3 =np.array([[10,20],
                [30,40]])
print('40', var3[1,1] )


# iteration

# 1D
ma = np.array([1,2,3,4,5,6,7,8,9,10])
for i in  ma:
   print(i)
print()

# 2D  : for 2 diamension 2 for loop will need
m3 =np.array([[10,20],
                [30,40]])

for i in  m3:
    print(i)
    for j in i:  
       print(j)

print()
# 3D
m5 = np.array([[[100,200],
                [400,500]],
                
                [[700,600],
                 [300,900]]
                            ])
for i in m5:
   print(i)
   for j in i:
      print(j)
      for k in j:
         print(k)

print()
# np.nditer ;using this we don't need to use multiple for loops in multiple diamension

multi_var = np.array([[[100,200],
                [400,500]],
                
                [[700,600],
                 [300,900]]
                            ])
for i in np.nditer(multi_var):
    print(i)

print()

# flags parameter stores values with changed specified datatype 
# buffered value in flags parameter  gives space to store data iterated with specific datatype
# op_dtypes: parameter  used to change datatype 
for i in np.nditer(multi_var,flags=['buffered'],op_dtypes=['S']): # 'S' for string
    print(i)
print()

# np.ndenumerate  : it gives index of each iterables

l = np.array([[1,2,3,4],
              [5,6,7,8]])

for i,d in np.ndenumerate(l):
     print(i,d)



# Copy and view function: both create exact same new array of original array
# copy : create new array , any changes made in copy does not reflect on original array and   vice versa
# view : any changes made into view will affect original array, and  any changes made in original array affect view.

# copy

b1 =  np.array(['gauri ','v','c'])
co = b1.copy()
b1[0]='tina'
co[0]=1
print('original :',b1)

print('copy: ',co)
print()

# view

x1 = np.array(['c','v','n'])
ve = x1.view()
x1[1]='z'
ve[2]='a'
print('original: ',x1)
print('view: ',ve)


l = np.array([10,20,30,40,50])
print(l.reshape(5,1))

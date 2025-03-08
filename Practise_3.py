import numpy as np

# Joining in Numpy

# 1. Concatenate function : it create new array with combination of values of two arrays

sd = np.array([1,2,3,4,5])
sd1 = np.array([8,9,7,0,0])

d2 = np.concatenate((sd,sd1))
print(d2)

dimn = np.array([[20,30],[40,50]])

dimn1 = np.array([[100,200],[300,400]])

f = np.concatenate((dimn,dimn1), axis=1) 
print('concatenate axis=0',f)
print()

# 2. stack : here axis = 0 columns and axis = 1 rows

a = np.array([1,2,3,4,5])
a1 = np.array([6,7,8,9,10])

a_new = np.stack((a,a1), axis=0)
a_new0 = np.stack((a,a1), axis=1)
a_new1 = np.vstack((a,a1))  # along column axis 
a_new2 = np.hstack((a,a1))  # along row axis
a_new3 = np.dstack((a,a1))  # along depth


print ('axis=0',a_new)
print()
print ('axis=1',a_new0)
print()
print('vstack:  ',a_new1)
print()
print('hstack:  ',a_new2)
print()
print('dstack:  ',a_new3)


#array_ Split : it breaks one array into multiple
arr = np.array([[10,20],[30,45],[60,70],[80,90]])

r = np.array_split(arr,2, axis=0)  
print(r)



# search array
# 1. where function : gives the all indices of specified number  np.where(var == number)
c = np.array([1,2,3,4,2,5,2,6,7])
ser = np.where(c == 2) 
even = np.where((c % 2) ==0) #will give index number of even number
print('2 is present at  ',ser) 
print(even)


gr = np.where(c >2)
print('greter than 2',gr)

# 2. search sorted array: in sorted array if we want to add new number the it give index of position where it fits in sorted array
d = np.array([1,2,3,4,5,7,8,9,11])
s = np.searchsorted(d ,[6,10,12,13])
print(s)

gau = np.array(['a','b','g','f'])
ac = np.searchsorted(gau,['c','k'])
ac1 = np.where(gau == 'f')
print(ac)
print(ac1)


num = np.array([1,2,3,4,5,7,8,9,10])
prime_num = np.where(num % 4 == 0 )
print(prime_num)


# sort array: arrange array in ascending order

k1 = np.array([[100,2],[333,45],[89,76]])
print(np.sort(k1))

k2 = np.array(['a','n','d','p','g','y'])
print(np.sort(k2))


# filter array:  seperate out selective element from original array and create new array
efg = np.array(['gauri','ria','priya','nick','rani'])
fil = [True,False,False,True,True]  #this value are like = gauri =  true, false=ria, false= priya, true=nick etc.
p = efg[fil]   #only true values are seperate out
print(p)

l = np.array([10,20,30,40,50])
h = [True,True,False,True,False]  
y = l[h] 
print(y)    

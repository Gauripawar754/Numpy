import numpy as np

# arithmatic functions

# 1. shuffle: it randomly changes position of all values

a = np.array([20,40,50,70,40,50])
np.random.shuffle(a)
print(a)

b = np.array([100,200,300,400,500])
np.random.shuffle(b)
print(b)


# 2.unique:  remove duplicate value , takes one value one time and sort it 
x = np.array([2,3,2,4,5,65,6,6,12,50]) 
y = np.unique(x, return_index=True, return_counts= True)
print(y)


# 3.Resize: it  changes its shape like reshape function

u = np.array([1,2,3,4,5,6,7,8])
resize = np.resize(u,(2,4))
print(resize)

# flatten  and ravel : it changes multidiamention array into 1 diamension
d3 = np.array( [[[1,2],
                 [4,5]],
                [[2,3],
                 
                 [5,6]]] )

print("Flatten ",d3.flatten(order="C"))
print()
sha = np.ravel(d3,order="K")
print("Ravel",sha)




# Insert function:  np.insert(var, index,value) it does not accept float value
num = np.array([10,30,40,50])

print(np.insert(num,(1,2,3),20))


num1 = np.array([[2,3],
                 [4,5]])

c = np.insert(num1,1,[20,32],axis=0)  #axis= 0 row and 1 column
print(c)

# np.append : adds at end, it adds float value also
k = np.append(num1, 7.8)
k1=np.append(num1, [[90,95]])
print(k)
print(k1)


# delete 
# 1d
d = np.array(['d','f','g','k'])
print(np.unique(d, return_index=True))

remove = np.delete(d,0)
print(remove)

# 2d
d1 = np.array([['d','f'],['g','k']])
print(np.unique(d, return_index=True))
print(d1)

remove = np.delete(d1,0,axis=1)  
print('2 diamension :',remove)


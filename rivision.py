import numpy as np

v = np.array([1,2,3,4,5])
for i in v:
    print(i)

print()
g = np.array([[1,2],
              [3,4],
              [6,7]])

# for i in g:
#   print(i)
#   for k in i:
#    print(k)
for i in np.nditer(g):
 print(i)

for j,k in np.ndenumerate(g):
 print(j,k)


t = np.array([1,2,3,4,5])
t[2] = 10
print('original: ',t)
y = t.copy()
y[0]=12
print('copy: ',y)
print(t)
# x = t.view()
# x [1]=30
# print('view: ',x)
# print(t)


h = np.array([10,20,30,40])
np.random.shuffle(h)
print(h)


h1 = np.array([10,10,20,30,30,40])
print(h1)
print(np.unique(h1))
print()
f = np.resize(h1,(3,9))
print(f)
print()

k =np.array([100,200,300,400,500])
print(np.resize(k,(4,8)))

j = np.array([[[3,4],
               [5,6],
               [7,1]],
               [[2,4],
               [4,5],
               [1,2]]])

np.random.shuffle(j)

print(j.flatten())
print(j.ravel())
print(j)

k = np.array([2,3,4,5,4,7,5,7])
np.random.shuffle(k)
print(k)
print(np.unique(k, return_index=True, return_counts=True))
print(np.resize(k,(3,6)))
print(k.flatten())
print(k.ravel())

k = np.array([2,3,4,5,4,7,5,7])

print(np.insert(k,(0,1,3),(10,20,30)))
print(np.append(k,100))

k4 = np.array([[2,3],
              [4,5],
              [4,7],
              [5,7]])
print(np.insert(k4,2,[10,20],axis=0))

print(np.append(k4,[[2.4,3.9]],axis=0))

k3 = np.array([[2,3],
              [4,5],
              [4,7],
              [5,7]])

print(np.delete(k3,1,axis=1))

l =np.array([1,2,3,4])
print(np.delete(l,1))


g1 = np.array([[100,200],
               [300,400]])
g2 = np.array([[700,800],
               [600,500]])

print(np.concatenate((g1,g2),axis=0))


print(np.vstack((g1,g2)))
print()
print(np.hstack((g1,g2)))

print()
print(np.dstack((g1,g2)))


# g3 = np.array([[100,200],
#                [300,400]])

g5 = np.array([[700,800],
               [600,500]])


print(np.array_split(g5,2,axis=0))



v = np.array([[91,200],
              [300,400],
              [500,600]])

# print(np.where (v %2 !=0))

h = np.array([20,30,40,10,88,66])
print(np.sort(h))
print(np.searchsorted(h,[20,30,40]))

h = np.array([20,30,40,10,88,66])
h3 =[True,False,True,False,True,True]
print(h[h3])

d2 =np.matrix([[1,2,3],
               [4,5,6],
               [7,8,9]])


d3 = np.matrix([[2,4,5],
                [8,6,0],
                [0,6,7]])


print(d2 + d3)

print(d2 - d3)

print(d2.dot(d3))


print(d2 / d3)
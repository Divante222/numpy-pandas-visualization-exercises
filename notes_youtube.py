import numpy as np 
import numpy.matlib
a = np.random.random((2,7))
print(type(a))
print(a)

print(a.ndim)

print(a.shape)

print(a.dtype)

print(a.itemsize) ## 4 bytes = float32

print(a.nbytes)

print(a[1,5])

print(np.zeros((2,3,3,2)))

print(np.ones((4,2,2), dtype='int32'))

print(np.full((2,2), 99, dtype='float32'))


print(np.full(a.shape, 4))

print(np.random.rand(4,2))

print(np.random.random_sample(a.shape))

print(np.random.randint(-5,10, size=(3,3)))
##identity matrix
print(np.identity(5))

arr = np.array([[1,2,3]])

r1 = np.repeat(arr, 3, axis=0)
print(r1)

arr = np.ones((5,5))

arr[1:-1, 1: -1] = 0
arr[2, 2] = 9
print(arr)

output = np.ones((5,5))

print(output)
z= np.zeros((3,3))

print(z)

z[1, 1] = 9
print(z)

output[1:-1, 1:4] = z
print(output)

a = np.array([1,2,3,])
# b = a ## does not create a copy
b= a.copy()


b[0]= 100

print(b)
print(a)

a = np.array([1,2,3,4])
print(a)
print(a + 2)

print(np.sin(a))

print(np.cos(a))

a = np.full((2,3),1)
print(a)

b = np.full((3,2), 2)

print(b)

print(np.matmul(a,b))

c = np.identity(3)
print(np.linalg.det(c)) ## linear algebra

stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats))

print(np.max(stats))

print(np.min(stats, axis=1))

print(np.sum(stats, axis=0))

before  = np.array([[1,2,3,4],[5,6,7,8]])
print(

)
after = before.reshape((2,2,2))

print(after)

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v2, v1]))

h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(h1)

print(h2)

print( np.hstack((h1,h2)))

filedata = np.genfromtxt('data.txt', delimiter=',')

print(filedata)

print(type(filedata))

filedata = filedata.astype('int32')

print(filedata)

print(filedata > 50)

print(filedata[filedata > 50])

x = np.array([1,2,3,4,5,6,7,8,9])

print(x[[1,2,8]]) ##get the specific index

print(np.any(filedata > 50, axis=0))

print(np.all(filedata > 50, axis=0))

print((filedata > 50) & (filedata < 100))

the_matrix = np.arange(1,6)


r1 = np.repeat([the_matrix], 5, axis=0)


r1[1,1] = 4
r1[2,1] = 4


x = r1[1:3, 0:2]

r1[0,2] = 8
r1[1,3] = 8
r1[2,4] = 8

y = [r1[0,2], r1[1,3],r1[2,4]]
z = r1[[0,1,2], [2,3,4]]
k = r1[[0,-1,-2], 3:]

print(r1)
print()
print(k)
print()
print(z)
print()
print(y)
print()
print(x)


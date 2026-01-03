Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List - list is python's data collection
>>> x = 12
>>> x = [1,2,3,4,5]
>>> x = []
>>> x
[]
>>> len(x)
0
>>> #inserting the value
>>> x
[]
>>> x.append(12)#append method is used to store the value at the end of the list
>>> x
[12]
>>> x.append(100)
>>> x
[12, 100]
>>> x.append(10)
>>> x
[12, 100, 10]
>>> x.insert(1,90)
>>> #90 will be stored at 1st index
>>> x
[12, 90, 100, 10]
>>> x.insert(0,-10)
x
[-10, 12, 90, 100, 10]
#update
x[0]
-10
x[0] = 0
x
[0, 12, 90, 100, 10]
x[0] = 8
x
[8, 12, 90, 100, 10]
#remove
x.pop()#it will remove the last value
10
x
[8, 12, 90, 100]
x.pop()
100
x
[8, 12, 90]
x.pop(0)#remove the value at 0 index
8
x
[12, 90]
x.remove(12)#remove by value
x
[90]
x = [1,2,2,2,2,2]
x.remove(2)
x
[1, 2, 2, 2, 2]
del x[0]
x
[2, 2, 2, 2]
x.clear()
x
[]

x = [i for i in range(1,101)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#indexing
x = [1,2,3,4,5,6]
x[-1]
6
#list is mutable and ordered
#ordered means indexing
#mutable means changeable - create,edit,delete

#deep copy and shallow copy
x = [1,2,3,4,5]
y = x
x
[1, 2, 3, 4, 5]
y
[1, 2, 3, 4, 5]
x.pop()
5
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]

x
[1, 2, 3, 4]
y = x.copy
x
[1, 2, 3, 4]
y
<built-in method copy of list object at 0x00000225EEAD8C40>

x
[1, 2, 3, 4]
y = x.copy()
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]
x.pop()
4
x
[1, 2, 3]
y
[1, 2, 3, 4]

#complex list
x = [1,2,3,[4,5,6]]
y = x.copy()
x
[1, 2, 3, [4, 5, 6]]
x.pop(0)
1
x
[2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6]]
del x[2][0]
x
[2, 3, [5, 6]]
y
[1, 2, 3, [5, 6]]
#Deep copy
x = [1, 2, 3, [4, 5, 6]]
from copy import deepcopy
y = deepcopy(x)
x
[1, 2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6]]
x[0]
1
x
[1, 2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6]]
del x[0]
x
[2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6]]
del x[2][0]
x
[2, 3, [5, 6]]
y
[1, 2, 3, [4, 5, 6]]

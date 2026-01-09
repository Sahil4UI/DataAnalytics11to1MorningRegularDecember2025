Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple and dictionary
x = [1,2,3,4,5]
x.append(90)
x
[1, 2, 3, 4, 5, 90]
x.insert(0,100)
x
[100, 1, 2, 3, 4, 5, 90]
x.pop()#it will remove last value
90
x = [1,1,2,2,3,3,4,4,5,5,5]
x.count(5)
3
x = [1,2,3,4,[5,6,7,8]]
#deepcopy
from copy import deepcopy
y = deepcopy(x)
x
[1, 2, 3, 4, [5, 6, 7, 8]]
y
[1, 2, 3, 4, [5, 6, 7, 8]]
del x[-1][0]
x
[1, 2, 3, 4, [6, 7, 8]]
y
[1, 2, 3, 4, [5, 6, 7, 8]]
#Tuple - tuple is immutable and ordered data collection
x = (1,2,3,4,5)
type(x)
<class 'tuple'>
#indexing and slicing
x[0]
1
x[-1]
5
#immutable - CRUD- you can create/read tuple  but (update,delete) operations restricted
#tuple is secure than list
x
(1, 2, 3, 4, 5)
del x[0]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
x[0]=100
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x[0]=100
TypeError: 'tuple' object does not support item assignment
x = (1,1,1,2,2,2,2,2,3,3,3,3,3,3)
len(x)
14
x.count(3)
6
x.index(1)
0
#dictionary
#key:value pair
#dictionary is unordered(no indexing or slicing)
data = {"rollNo":101,"name":"Ragu","class":10}
data.keys()
dict_keys(['rollNo', 'name', 'class'])
>>> data.values()
dict_values([101, 'Ragu', 10])
>>> data.items()
dict_items([('rollNo', 101), ('name', 'Ragu'), ('class', 10)])
>>> data
{'rollNo': 101, 'name': 'Ragu', 'class': 10}
>>> data['rollNo']
101
>>> data.get('rollNo')
101
>>> data['sdklfjfsd']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    data['sdklfjfsd']
KeyError: 'sdklfjfsd'
>>> data.get("fsdfsdf")
>>> data
{'rollNo': 101, 'name': 'Ragu', 'class': 10}
>>> data["contact"]=9987654210
>>> data
{'rollNo': 101, 'name': 'Ragu', 'class': 10, 'contact': 9987654210}
>>> data["rollNo"]=102#if the key exists ,the value gets updated
>>> data
{'rollNo': 102, 'name': 'Ragu', 'class': 10, 'contact': 9987654210}
>>> #in dictionary,we cannot store duplicate keys
>>> data
{'rollNo': 102, 'name': 'Ragu', 'class': 10, 'contact': 9987654210}
del data['contact']
data
{'rollNo': 102, 'name': 'Ragu', 'class': 10}
data.pop('class')
10
data
{'rollNo': 102, 'name': 'Ragu'}
data.popitem()#removelast key:value pair
('name', 'Ragu')
data
{'rollNo': 102}
del data['rollNo']
data
{}
#empty dictionary
x = {}
type(x)
<class 'dict'>
x = dict()
x
{}
x["id"]=101
x
{'id': 101}
x = {'rollNo': 102, 'name': 'Ragu', 'class': 10, 'contact': 9987654210}
len(x)
4
for k,v in x
SyntaxError: expected ':'

for key:value in x:
    
SyntaxError: invalid syntax
for key,value in x:
    print(key,value)

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    for key,value in x:
ValueError: too many values to unpack (expected 2)
x
{'rollNo': 102, 'name': 'Ragu', 'class': 10, 'contact': 9987654210}
for key in x:
    print(key,x.get(key))

rollNo 102
name Ragu
class 10
contact 9987654210

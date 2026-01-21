Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #SET - mutable and unordered data collection in Python
>>> #mutable - we can store and remove values from  it
>>> #unordered - no indexing
>>> x = {1,2,3,4,5}
>>> type(x)
<class 'set'>
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0]
TypeError: 'set' object is not subscriptable
>>> #add and remove
>>> x
{1, 2, 3, 4, 5}
>>> x.add(500)
>>> x
{1, 2, 3, 4, 5, 500}
>>> x.add(50)
>>> x
{1, 2, 3, 4, 5, 500, 50}
>>> #remove method
>>> x.discard(4)
>>> x
{1, 2, 3, 5, 500, 50}
>>> x.discard(500)
>>> X
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    X
NameError: name 'X' is not defined. Did you mean: 'x'?
x
{1, 2, 3, 5, 50}
#in set you cannot store duplicates
x = {1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5}
x
{1, 2, 3, 4, 5}
#UNION,INTERSECTION & DIFFERENCE
x = {1,2,3,4,5}
y = {4,5,6,7,8}
x.union(y)#all but without repetition
{1, 2, 3, 4, 5, 6, 7, 8}
x.intersection(y)#common
{4, 5}
#difference
x
{1, 2, 3, 4, 5}
y
{4, 5, 6, 7, 8}
x.difference(y)
{1, 2, 3}
y.difference(x)
{8, 6, 7}
#superset and subset
x = {1,2,3,4}
y = {1,2,3,4,5,6,7,8,9}
x.issubset(y)
True
y.issuperset(x)
True
x = {1,1,1,2,2,2}
len(x)
2

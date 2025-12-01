Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> x = 12
>>> #variable - x , constant  - 12
>>> #naming conventions - rules to form variables
>>> #variable name cannot be started with number or any special character other than
>>> #_
>>> 1x = 12
SyntaxError: invalid decimal literal
>>> $%%^&x = 12
SyntaxError: invalid syntax
>>> x = 12
>>> #variable name cannot contain any special character (except _)
>>> first name = "sahil"
SyntaxError: invalid syntax
>>> first_name = "sahil"
>>> #dont use python pre defined keywords as variable name - if,else,for
>>> x =12
>>> type(x)
<class 'int'>
>>> x = 23.234
>>> #Data Types
>>> x = 12
>>> type(x)
<class 'int'>
>>> x = 12.435
type(x)
<class 'float'>
x = True
type(x)
<class 'bool'>
x = "Komal"
type(X)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
#python is a case sensitive language
type(x)
<class 'str'>

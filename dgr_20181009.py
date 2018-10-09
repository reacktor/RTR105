Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 12.2
>>> y = 14
>>> x
12.2
>>> y
14
>>> type(x)
<type 'float'>
>>> type(y)
<type 'int'>
>>> x = 100
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hours * rate
>>> print(pay)
437.5
>>> x = 2
>>> print(x)
2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * ( 1 - x )
>>> print(x)
-46.8
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello' + 'there'
>>> print(eee)
hellothere
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> ns = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    niv = int(nsv)
NameError: name 'nsv' is not defined
>>> nam = input
>>> print('Welcome',nam)
('Welcome', <built-in function input>)
>>> inp = input
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    usf = int(inp) + 1
TypeError: int() argument must be a string or a number, not 'builtin_function_or_method'
>>> ________________________________________________________-
SyntaxError: invalid syntax
>>> Hours = 35
>>> Rate = 2.75
>>> Pay = Hours * Rate
>>> print(Pay)
96.25
>>> Hours = input('Dear user how many hours you work?')
Dear user how many hours you work?35
>>> Rate = input('Dear user,what about your rate?')
Dear user,what about your rate?2.75
>>> Pay = int(Hours) * 2.75
>>> print('My Pay?', Pay)
('My Pay?', 96.25)
>>> Pay = int(Hours) * int(Rate)
>>> print('My pay?', Pay)
('My pay?', 70)
>>> Hours
35
>>> Pay = int(Hours) * int(Rate)
>>> print('Your pay is:', Pay)
('Your pay is:', 70)
>>> Pay = float(Hours) * float(Rate)
>>> print('Your pay is:'Pay)
SyntaxError: invalid syntax
>>> print('Your pay is:' Pay)
SyntaxError: invalid syntax
>>> print('Your pay is:', Pay)
('Your pay is:', 96.25)
>>> 

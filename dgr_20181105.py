Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = '123'
>>> str3 = str3 + 1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3 = str3 + 1
TypeError: must be str, not int
>>> x = int(str3) + 1
>>> print(x)
124
>>> ______________
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ______________
NameError: name '______________' is not defined
>>> name = input("Enter:")
Enter:CJ
>>> print(name)
CJ
>>> apple = input("Enter:")
Enter:100
>>> x = apple - 10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = apple - 10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x= apple-10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x= apple-10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple)-10
>>> print(x)
90
>>> fruit = "banana"
>>> latter = fruit[1]
>>> print(latter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
>>> fruit = "banana
SyntaxError: EOL while scanning string literal
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	latter = fruit[index]
	print(index,letter)
	index = index + 1

	
Traceback (most recent call last):
  File "<pyshell#29>", line 3, in <module>
    print(index,letter)
NameError: name 'letter' is not defined
>>> fruit = "banana"
>>> for letter in fruit :
	print(letter)

	
b
a
n
a
n
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1
	\

	  
SyntaxError: invalid syntax
>>> word = "banana"
>>> count = 0
>>> for letter in word:
	if letter == "a":
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> print(count)
0
>>> for letter in word :
	if letter == "a":
		count = count + 1

		
>>> print(count)
3
>>> 

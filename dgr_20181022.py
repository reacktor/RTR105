Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> big = max("Hello world")
>>> print(big)
w
>>> def max(inp):
	blah
	blah
	for x in inp:
		blah
		blah

		
>>> print(float(99)/100)
0.99
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1 + 2 * float(3) / 4 - 5)
-2.5
>>> a = 42.5
>>> type(a)
<type 'float'>
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day.")

	
>>> print_lyrycs()

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print_lyrycs()
NameError: name 'print_lyrycs' is not defined
>>> print_lirics():
	
SyntaxError: invalid syntax
>>> print_lirics()

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print_lirics()
NameError: name 'print_lirics' is not defined
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> x = 5
>>> print("Hello")
Hello
>>> print_lyrics():
	
SyntaxError: invalid syntax
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> print("Yo")
Yo
>>> x = 2 + 2
>>> print(x)
4
>>> x = 5
>>> x = x + 2
>>> print(x)
7
>>> def greet(lang):
	if lang == "es":
		print("Hola")
		elif lang == "fr":
			
SyntaxError: invalid syntax
>>> elif lang == "fr":
	
SyntaxError: invalid syntax
>>> return "Hola"
SyntaxError: 'return' outside function
>>> def greet(lang):
	if lang == "es":
		return "Hola"
	elif lang == "fr":
		return "Bonjour"
	else:
		return "Hello"

	
>>> print(greet("en"),"Glenn")
('Hello', 'Glenn')
>>> print(greet("es"),"Rodrigo")
('Hola', 'Rodrigo')
>>> print(greet("fr"),"Michael")
('Bonjour', 'Michael')
>>> def addtwo(a, b):
	added = a + b
	return added
x = addtwo(3, 5)
SyntaxError: invalid syntax
>>> x
7
>>> x = addtwo(3, 5)

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x = addtwo(3, 5)
NameError: name 'addtwo' is not defined
>>> x = addtwo

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x = addtwo
NameError: name 'addtwo' is not defined
>>> addtwo()

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    addtwo()
NameError: name 'addtwo' is not defined
>>> def addtwo(3,5)
SyntaxError: invalid syntax
>>> def addtwo(3, 5):
	
SyntaxError: invalid syntax
>>> hours = input("enter your hours")
enter your hours40
>>> rate = input("enter your rate:")
enter your rate:10
>>> h = input("enter your h:")
enter your h:40
>>> r = input("enter your r:")
enter your r:10
>>> h
40
>>> h1 = input("enter bonus h:")
enter bonus h:5
>>> r1 = input("enter bonus r:")
enter bonus r:15
>>> Pay = (h * r + h1 *r1)
>>> Payy

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Payy
NameError: name 'Payy' is not defined
>>> Pay
475
>>> print(Pay) ("Good work")

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(Pay) ("Good work")
TypeError: 'int' object is not callable
>>> print(Pay) + ("Good work")

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(Pay) + ("Good work")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(Pay Good work)
SyntaxError: invalid syntax
>>> print(Pay) print(Good work)
SyntaxError: invalid syntax
>>> print(Pay)
475
>>> print"Your pay is:", Pay)
SyntaxError: invalid syntax
>>> print("Good work" , Pay)
('Good work', 475)
>>> def Pay
SyntaxError: invalid syntax
>>> def Pay:
	
SyntaxError: invalid syntax
>>> def Hours():
input("Enter your hours:")
  File "<pyshell#89>", line 2
    input("Enter your hours:")
        ^
IndentationError: expected an indented block
>>> 

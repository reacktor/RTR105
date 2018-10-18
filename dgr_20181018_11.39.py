Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print('Hello')
	print('Fun')

	
>>> thing()
Hello
Fun
>>> print('Zip')
Zip
>>> thing()
Hello
Fun
>>> big = max('Hello world')
>>> print(big)
w
>>> tiny = min('Hello world')
>>> print(tiny)
 
>>> rawstr = input('Enter a number:')
Enter a number:42
>>> try:
	ival = int(rawstr)
except:
	ival = -1

	
>>> if ival > 0 :
	print('Nice work')
else:
	print('Not a number')

	
Nice work
>>> Hours = input('Enter your hours:')
Enter your hours:45
>>> Rate = input('Enter your rate:')
Enter your rate:10
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> Hours = input('Enter your hours:')
Enter your hours:40
>>> Hours
40
>>> Above 40h. = input("Enter your hours:")
SyntaxError: invalid syntax
>>> Special hours = input("Enter your hours:")
SyntaxError: invalid syntax
>>> Above 40
SyntaxError: invalid syntax
>>> Above.40.h. = input("Enter your hours:")
SyntaxError: invalid syntax
>>> Worker above = input("Enter your hours:")
SyntaxError: invalid syntax
>>> Sp.Hours

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Sp.Hours
NameError: name 'Sp' is not defined
>>> Sp.Hours = input("Enter your hours:")
Enter your hours:5

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Sp.Hours = input("Enter your hours:")
NameError: name 'Sp' is not defined
>>> Sp.Hours

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Sp.Hours
NameError: name 'Sp' is not defined
>>> hours = input("Enter your hours:")
Enter your hours:5
>>> hours
5
>>> Hours
40
>>> rate = input("Enter your rate:")
Enter your rate:1.5
>>> rate
1.5
>>> Rate
10
>>> Pay = (Hours * Rate + hours * rate)
>>> Pay
407.5
>>> print(Pay)
407.5
>>> print("Your pay is:", Pay)
('Your pay is:', 407.5)
>>> Hours = input("Enter your hours:")
Enter your hours:20
>>> Rate = input("Enter rate:")
Enter rate:nine

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    Rate = input("Enter rate:")
  File "<string>", line 1, in <module>
NameError: name 'nine' is not defined
>>> c = nine

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c = nine
NameError: name 'nine' is not defined
>>> Rate = input("Enter rate:")
Enter rate:9
>>> Rate = 9
>>> Rate
9
>>> Rate = nine

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    Rate = nine
NameError: name 'nine' is not defined
>>> type(Rate)
<type 'int'>
>>> Rate = "nine"
>>> Rate
'nine'
>>> type(Rate)
<type 'str'>
>>> Hours * Rate
'ninenineninenineninenineninenineninenineninenineninenineninenineninenineninenine'
>>> try:
	Pay = str(Rate) * Hours
	except = 360
	
SyntaxError: invalid syntax
>>> str(Rate) = int(9)
SyntaxError: can't assign to function call
>>> str(Rate) = 9\
	    
SyntaxError: can't assign to function call
>>> Rate = "nine" = 9
SyntaxError: can't assign to literal
>>> Rate = input(nine)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    Rate = input(nine)
NameError: name 'nine' is not defined
>>> try:
	Rate = nine
except = 9
SyntaxError: invalid syntax
>>> try:
	Rate = nine
except:
	Rate = 9

	
>>> if Rate > 1
SyntaxError: invalid syntax
>>> if Rate > 1:
	print("Nice work")
else:
	print("Not a number")

	
Nice work
>>> pay = Hours * Rate
>>> pay
180
>>> try:
	Hours = forty
except:
	Hours = 40

	
>>> if Hours > 1
SyntaxError: invalid syntax
>>> if Hours > 1:
	print(Nice)
else:
	print("Not a number")

	

Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    print(Nice)
NameError: name 'Nice' is not defined
>>> if Hours > 1:
	print("Nice")
else:
	print("Not a number")

	
Nice
>>> Pay = Hours * Rate
>>> Pay
360
>>> 

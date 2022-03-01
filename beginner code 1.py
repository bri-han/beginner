Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> python_examples
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python_examples
NameError: name 'python_examples' is not defined
>>> print("Hello world!")
Hello world!
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> print("Hello world")
Hello world
>>> name= input('What is your name?\n`)
	    
SyntaxError: EOL while scanning string literal
>>> print ('Hello, world!')
Hello, world!
>>> name = input('What is your name?\n')
What is your name?
brianne
>>> print ('Hi, %s.' % name)
Hi, brianne.
>>> print('name')
name
>>> print('brianne')
brianne
>>> print(name)
brianne
>>> fave_language = "Python"
>>> print("I like coding in " + fave_languge + "the most")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("I like coding in " + fave_languge + "the most")
NameError: name 'fave_languge' is not defined
>>> print("I like coding in" + fave_language + "the most")
I like coding inPythonthe most
>>> print("I like coding in " + fave_language + " the most")
I like coding in Python the most
>>> first_mane = "Bri"
>>> first_name = "Bri"
>>> print("Hello", first_name)
Hello Bri
>>> print("Hello", first_name, "how are you?")
Hello Bri how are you?
>>> last_name = Han
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    last_name = Han
NameError: name 'Han' is not defined
>>> last_name = "Han"
>>> print("Hello", first_name,last_name, "good to see you")
Hello Bri Han good to see you
>>> work_place = "BiModal"
>>> print("Hello, my name is " first_name,last_name, "I work at " work_place)
SyntaxError: invalid syntax
>>> print("Hello, my name is" first_name,last_name, " I work at" work_place)
SyntaxError: invalid syntax
>>> print("Hello", first_name)
Hello Bri
>>> print("Hello, my name is ", first_name,last_name, " I work at ", work_place)
Hello, my name is  Bri Han  I work at  BiModal
>>> print("Hello, my name is", first_name,last_name, "I work at", work_place)
Hello, my name is Bri Han I work at BiModal
>>> print("Hello, my name is", first_name,last_name,"," "I work at", work_place)
Hello, my name is Bri Han ,I work at BiModal
>>> print(name)
brianne
>>> print(f"I want this text printed to the console!")
I want this text printed to the console!
>>> print("Hello {}, hope you're well!")
Hello {}, hope you're well!
>>> print("Hello {}, hope you're well!" .format(first_name))
Hello Bri, hope you're well!
>>> print("Hello {} {}, hope you're well!")
Hello {} {}, hope you're well!
>>> print("Hello {} {}, hope you're well!" .format(first_name,last_name))
Hello Bri Han, hope you're well!
>>> print(f"Hello, {first_name}!")
Hello, Bri!
>>> print(f"Hello, {first_name} {last_name}!")
Hello, Bri Han!
>>> num1 = 1.5
>>> num2 = 6.3
>>> sum = num1 + num2
>>> print('The sum of {0} and {1} is {2}' .format(num1, num2, sum))
The sum of 1.5 and 6.3 is 7.8
>>> num1 = input('10:')
10:num2 = input("20: ')
>>> sum = float(num1) + float(num2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    sum = float(num1) + float(num2)
ValueError: could not convert string to float: 'num2 = input("20: \')'
>>> import random
>>> print(random.randint(0,9))
8
>>> random.randint(a,b)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    random.randint(a,b)
NameError: name 'a' is not defined
>>> import random
>>> print(random.randint(0,9))
6
>>> 
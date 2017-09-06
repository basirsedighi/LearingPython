Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Exampel with numbers and strings
>>> #
>>> 
>>> a = 7
>>> a
7
>>> b = 36.24
>>> b
36.24
>>> print(b)
36.24
>>> del a
>>> # Also complex number
>>> #
>>> 
>>> myvariabel= 3-8j
>>> myvariabel
(3-8j)
>>> nyvariabel= 3+15j
>>> 
>>> myvariabel + nyvariabel
(6+7j)
>>> 
>>> # Extract a word from a sentence
>>> #
>>> strint='Hello World'
>>> str[0:5]

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str[0:5]
TypeError: 'type' object has no attribute '__getitem__'
>>> strint[0:5]
'Hello'
>>> strint[6:]
'World'
>>> strint + "what's up "
"Hello Worldwhat's up "
>>> 
>>> # List and tuples
>>> #
>>> 
>>> mylist=['one','two','three', 4, 5.0, 6+2j]
>>> mylist
['one', 'two', 'three', 4, 5.0, (6+2j)]
>>> 	# Extract from list
	
>>> 
>>> mylist[1:]
['two', 'three', 4, 5.0, (6+2j)]
>>> mylist[-2:0]
[]
>>> mylist[2:5]
['three', 4, 5.0]
>>> mylist*3
['one', 'two', 'three', 4, 5.0, (6+2j), 'one', 'two', 'three', 4, 5.0, (6+2j), 'one', 'two', 'three', 4, 5.0, (6+2j)]
>>> 	# Adding list
	
>>> newlist=[7, 'eight',9]
>>> mylist+newlist
['one', 'two', 'three', 4, 5.0, (6+2j), 7, 'eight', 9]
>>> 
>>> newlist[0]="seven"
>>> newlist
['seven', 'eight', 9]
>>> 	# Tuples
	
>>> mytuple= ('a word','a number',10)
>>> mytuple[1:]
('a number', 10)
>>> 

Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Dictionaries
>>> 
>>> 	# Method 1
	
>>> 	adress= {}
	
SyntaxError: unexpected indent
>>> address={}
>>> 	address={}
	
SyntaxError: unexpected indent
>>> address["John"]="john@gmail.com"
>>> address["Adam"]="Ada,@gmail.com"
>>> address["Victor"]="victor@gmail.com"
>>> 
>>> print(address)
{'John': 'john@gmail.com', 'Adam': 'Ada,@gmail.com', 'Victor': 'victor@gmail.com'}
>>> 
>>> 	#Method 2
>>> 
>>> email={'John':'john@gmail.com','adam':'adam@gmail.com','victor': 'victor@gmail.com'}
>>> 
>>> email
{'John': 'john@gmail.com', 'adam': 'adam@gmail.com', 'victor': 'victor@gmail.com'}
>>> 		# Extract only values then extract diroctor key
		
>>> 
>>> email.key()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    email.key()
AttributeError: 'dict' object has no attribute 'key'
>>> email.keys()
dict_keys(['John', 'adam', 'victor'])
>>> 
>>> email.values()
dict_values(['john@gmail.com', 'adam@gmail.com', 'victor@gmail.com'])
>>> 
>>> 
>>> # Data Type conversion
>>> 
>>> int(55.89)	# This is an integer 1, 2, 3
55
>>> 
>>> float(36.2)
36.2
>>> 
>>> my_string=str(9500)
>>> 
>>> mystring
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    mystring
NameError: name 'mystring' is not defined
>>> my_string
'9500'
>>> tuple("This is a string")
('T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g')
>>> 
>>> list("This is a list")
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'l', 'i', 's', 't']
>>> 
>>> chr(65) # henter kode fra ASCII verdi
'A'
>>> 
>>> ord('A') # motsatt fra chr
65
>>> 
>>> hex(19)
'0x13'
>>> 
>>> oct(24)
'0o30'
>>> 
>>> bin(128)
'0b10000000'
>>> 
>>> 
>>> # arithmetic & comparison Operators
>>> 
>>> 3**3
27
>>> 3**3 # same as 3^3
27
>>> 
>>> a=15
>>> b=10
>>> 
>>> a==b # skjekker om d er lik
False
>>> 
>>> a!=b # skjekker om de ikke er lik
True
>>> 
>>> a>b # skjekker om a er større enn b
True
>>> 
>>> a>=b # skjekker om det er a er større eller lik b
True
>>> 
>>> 
>>> # Membership & Identity Operators
>>> 
>>> str1="I have a lazy dog"
>>> "dog" in str1
True
>>> 
>>> mylist=[1,3,19,32]
>>> 
>>> 65 in mylist # skjekker om tallet 65 er i lista
False
>>>  a = 42
 
SyntaxError: unexpected indent
>>> a = 42
>>> b='42'
>>> a is b
False
>>> myvar= 50
>>> if myvar<100
SyntaxError: invalid syntax
>>> if myvar<100:
	 print('you are short of being 100%')
	 print ('fuck off')

	 
you are short of being 100%
fuck off
>>> 
>>> 	# PROGRAMMING STARTS#
	
>>> if myvar <100:
	print ('you suck dick')
	else:
		
SyntaxError: invalid syntax
>>> if mayvar <100
SyntaxError: invalid syntax
>>> if myvar <100:
	print('fasdfasdf')

	
fasdfasdf
>>> 
>>> 
>>> # if statement
>>> 
>>> sellingprice=1500
>>> costprice=1200
>>> 
>>> if (sp>cp)
SyntaxError: invalid syntax
>>> if(sp>cp):
	print('Congratulation!')
	print ("You've made a profit of",sp-cp "bucks")
	
SyntaxError: invalid syntax
>>> if(sellingprice>costprice):
	print('Congratulation!')
	print("You've made a profit of",sellingprice-costprice, "bucks")
elif (costprice>sellingprice):
	print("Ooops!")
	print("you have lost of", costprice-sellingprice, "buscks")

	
Congratulation!
You've made a profit of 300 bucks
>>> >>> if(sellingprice>costprice):
	print('Congratulation!')
	print("You've made a profit of",sellingprice-costprice, "bucks")
elif (costprice>sellingprice):
	print("Ooops!")
	print("you have lost of", costprice-sellingprice, "buscks")
	
SyntaxError: invalid syntax
>>> if(sellingprice>costprice):
	print('Congratulation!')
	print("You've made a profit of",sellingprice-costprice, "bucks")
elif (costprice>sellingprice):
	print("Ooops!")
	print("you have lost of", costprice-sellingprice, "buscks")
else :
	print("No change to balance")

	
Congratulation!
You've made a profit of 300 bucks
>>> 

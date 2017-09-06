print('Type any letter')

char=input()
if ord(char)>=65 and ord (char)<=90:
    print("You eneterd an upper case alphabet.")
    if char in ['A','E','I','O','U']:
        print ("You entered a vowel")
    else:
        print("You entered a consonant")
elif ord(char)>=97 and ord(char)<=122:
    print("You eneterd an lower case alphabet.")
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel")
    else:
        print("You entered a consonant")
else:
    print("You did not enter an alphabet")

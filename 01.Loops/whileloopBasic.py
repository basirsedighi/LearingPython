count=0
print("Enter your name:")
name=input()
for letter in name:
    if(letter in ['A','E','I','U','O','a','e','i','u','o']):
        count=count+1
print("you have ",count,"vowes in you name")

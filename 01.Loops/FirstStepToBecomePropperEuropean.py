print('1. from Fahrenheit to Celsius')
print('2. from inches to centimeter')
print('3. from Feet to meter')
valg=int(input())

if (valg == 1):
    while True:
        print("Enter a temperature in Fahrenheit, enter 10000 too quite : ")
        Fahrenheit = float(input())
        if(Fahrenheit == 10000):
            break
        Celsius =(Fahrenheit - 32)*(5.0/9)
        print ("Temperature:",Fahrenheit, " F=", Celsius, "Celsius ")


elif (valg ==2):
    while True:
        print("Enter a mesure inches , enter 10000 too quite : ")
        inches = float(input())
        if(inches == 10000):
            break
        centimeter = inches * 2.54
        print ("Mesure:", inches, "I =", centimeter, "cm")




elif (valg==3):
    while True:
        print("Enter a mesure Feet , enter 10000 too quite : ")
        feet = float(input())
        if(inches == 10000):
            break
            meter = feet*0.3
        print ("Mesure:", fett, "f =",meter , "m")

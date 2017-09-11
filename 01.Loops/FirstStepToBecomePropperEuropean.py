
while True:
    pass
    print('1. from Fahrenheit to Celsius')
    print('2. from Inches to Centimeter')
    print('3. from Feet to Meter')
    print('4. from Pounds to Kilogram')
    valg=int(input())

    if (valg == 1):
        while True:
            print("Enter a temperature in Fahrenheit, enter q too quite : ")
            Fahrenheit = float(input())
            if(Fahrenheit == ord('q')):
                break
            Celsius =(Fahrenheit - 32)*(5.0/9)
            print ("Temperature:",Fahrenheit, " F=", Celsius, "Celsius ")


    elif (valg ==2):
        while True:
            print("Enter a mesure inches , enter q too quite : ")
            inches = float(input())
            if(inches == ord('q')):
                break
            centimeter = inches * 2.54
            print ("Mesure:", inches, "I =", centimeter, "cm")




    elif (valg==3):
        while True:
            print("Enter a mesure Feet , enter q too quite : ")
            feet = float(input())
            if(inches == ord('q')):
                break
                meter = feet*0.3
            print ("Mesure:", feet, "f =",meter , "m")

    elif (valg==4):
        print('3. from Feet to meter')
        while True:
            print("Enter a mesure Pounds , enter q too quite : ")
            pounds = float(input())
            if(inches == ord('q')):
                break
            Kilogram = feet*0.456
            print ("Mesure:", Pounds, "Pounds =",Kilogram , "Kilogram")

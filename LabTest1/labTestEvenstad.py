import math

while True:
    temp = raw_input ("Enter a temperature: ")
    temp = temp.strip()
    if temp.isdigit() == True:
        print ("\n")
        temp = int(temp)
        if temp <= 0:
            print ("The temperature entered is: Extremely Cold")
        elif temp > 0 and temp <= 58:
            print ("The temperature entered is: Cold")
        elif temp > 58 and temp <= 84:
            print ("The temperature entered is: Warm")
        elif temp > 84:
            print ("The temperature entered is: Extremely Hot")

        degreesAway = abs(temp - 78)
        if temp > 78:
            print ("The temperature is %d degrees Fahrenheit above normal temperature" %degreesAway)
        elif temp < 78:
            print ("The temperature is %d degrees Fahrenheit below normal temperature" %degreesAway)
        elif temp == 78:
            print ("This is normal temperature in Fahrenheit")

        tempCelcius = (temp - 32)/(float(9)/5)
        
        print ("The temperature %d Fahrenheit is %.2f in Celcius" %(temp, tempCelcius))
        print ("\n")
    elif temp == "exit":
        break
    else:
        print "Enter a digit"
    

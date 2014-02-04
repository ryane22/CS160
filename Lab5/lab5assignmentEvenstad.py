userString = raw_input("Enter a string: ")

numCapital = 0
numSpaces = userString.strip().count(" ")
lastBlankAt = -1

while True:
#print the length of the text
    print "The entered text contains", len(userString), "character(s)"
    print ("\n")

#print the number of spaces in text
    print "The entered text contains", userString.count(" "), "blank space(s)"
    print ("\n")

#find number of upper case letters (I am aware this is very ugly)
    print "The entered text contains", userString.count("A") + userString.count("B") + userString.count("C") + userString.count("D") + userString.count("E") + userString.count("F") + userString.count("G") + userString.count("H") + userString.count("I") + userString.count("J") + userString.count("K") + userString.count("L") + userString.count("M") + userString.count("N") + userString.count("O") + userString.count("P") + userString.count("Q") + userString.count("R") + userString.count("S") + userString.count("T") + userString.count("U") + userString.count("V") + userString.count("W") + userString.count("X") + userString.count("Y") + userString.count("Z"), "upper case letter(s)"
    print ("\n")
    
#print first word entered
    blankSpaceAt = userString.find(" ")
    print "The first word is:", userString[0:blankSpaceAt]
    print ("\n")

#print last word entered
    for c in xrange(1, numSpaces + 1):
        lastBlankAt = userString.find(" ", lastBlankAt + 1, len(userString) + 1)
    print "The last word is:", userString[lastBlankAt + 1:]
    print ("\n")
    #blank = userString.rfind(" ")
    #print userString[blank+1:]

#display the text in all caps
    print "All capitals:", userString.upper()
    print ("\n")

#display the text all lower case
    print "All lower case:", userString.lower()
    print ("\n")

#replace all the blank space with dashes
    print "No spaces:", userString.replace(" ", "-")
    print ("\n")

#if only digits add 1 to the input and display the value
    if userString.isdigit() == True:
        print float(userString) + 1
    else:
        print ("Not a valid number")
    print ("\n")

#notify if there is blank space in the text
    if userString.count(" ") != 0:
        print ("There is space in the text")
    else:
        print ("There is no space in the text")
    print ("\n")

#notify the user if there is a number in the text
    if userString.count("1") !=0 or userString.count("2") !=0 or userString.count("3") !=0 or userString.count("4") !=0 or userString.count("5") !=0 or userString.count("6") !=0 or userString.count("7") !=0 or userString.count("8") !=0 or userString.count("9") !=0 or userString.count("0") !=0:
        print ("There is a number in the text")
    else:
        print ("There is no number in the text")
    print ("\n")

#display the text entered centered within 50 columns
    print userString.center(50)
    
    break

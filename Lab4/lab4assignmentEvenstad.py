'''
Ryan Evenstad
ryan.evenstad22@gmail.com
CS160 Lab 3 PM
Lab 4
'''

'''
part 1.1
write a program that accepts only positive values
'''
while True:
    valueA = input ("Enter a number: ")
    if valueA >= 0:
        print "Congratulations, input accepted"
        break
    else:
        print "Sorry, input rejected"

#space for readability
print "\n\n"

'''
part 1.2
accept only a number within (-100, 100) range
'''
while True:
    valueB = input ("Enter a number: ")
    if valueB >= -100 and valueB <= 100:
        print "Congratulations, the input is within the range desired"
        break
    else:
        print "Sorry, the input does not fall within the required range"

#space for readability
print "\n\n"

'''
part 1.3
accpet only 'n', 's', or 'a' irrevelant of case
'''

while True:
    valueC = raw_input ("Enter an input: ")
    if valueC == "n" or valueC == "N":
        print "New File"
        break
    elif valueC == "s" or valueC == "S":
        print "Saving the file"
        break
    elif valueC == "a" or valueC == "A":
        print "Save as..."
        break
    else:
        print "Please enter n, s, or a"

#space for readability
print "\n\n"

'''
part 1.4
'''

while True:
    print "\t\tMenu"
    print "1. Left"
    print "2. Right"
    print "3. Up"
    print "4. Down"
    print "5. Exit"
    option = input ("\tChoose an option: ")
    if option == 1:
        print "\nPlease go left"
        raw_input ("<Press enter to continue>\n")
    elif option == 2:
        print "\nPlease go Right"
        raw_input ("<Press enter to continue>\n")
    elif option == 3:
        print "\nPlease go Up"
        raw_input ("<Press enter to continue>\n")
    elif option == 4:
        print "\nPlease go Down"
        raw_input ("<Press enter to continue>\n")
    elif option == 5:
        print "\nGoodbye"
        break
    


#space for readability
print "\n\n"

'''
Part 2
'''
startBalance = input ("Enter a starting balance: ")
currentBalance = startBalance
while True:
    transaction = raw_input ("Enter type of transaction: ")
    if transaction == "quit":
        break
    if transaction == "deposit" or transaction == "withdraw":
        amount = input ("Enter the amount: ")
        if transaction == "deposit":
            currentBalance = currentBalance + amount
        elif transaction == "withdraw":
            currentBalance = currentBalance - amount
        print "Current balance: $%0.2f" %currentBalance
    else:
        print "Unknown transaction type - ignored"

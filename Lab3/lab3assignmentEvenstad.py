'''
Ryan Evenstad
ryan.evenstad22@gmail.com
CS160 Wednesday 3PM
Lab 3 Assignment
'''

'''
part A
count from 0 to 100 by 1's
'''
for cvA in xrange (100):
    print cvA + 1

# space for readability
print "\n\n"

'''
part B
count by -3's from 3010 to 2999
'''

for cvB in xrange (3010, 2999, -3):
    print cvB,

# space for readability
print "\n\n"

'''
part C
count by 5's from 0 to 50
'''
targetC = 50
for cvC in xrange (0, targetC + 1 , 5):
    print "\t%d" %cvC,

# space for readability
print "\n\n"

'''
part D
count by half from 20 to 30
'''
startD = 20 
targetD = 30
for cvD in xrange (startD, (2*targetD) + 1):
    print cvD/2.0

# space for readability
print "\n\n"

'''
part E
count from 1 to a number specified number in increments of 2
'''
targetE = input("Enter target value: ")
for cvE in xrange (1, targetE + 1, 2):
    print cvE

# space for readability
print "\n\n"

'''
part F
count from start to end by increments all entered by the user
'''
startF = input("Enter the start value: ")
targetF = input ("Enter the target value: ")
incrementF = input("Enter the increment value: ")
for cvF in xrange (startF, targetF + 1, incrementF):
    print "\t%d" %cvF,

# space for readability
print "\n\n"

'''
part G
Count from a user-entered start value by a user-entered increment, outputting a user-
entered number of values
'''
startG = input("Enter a start value: ")
incrementG = input("Enter the increment value: ")
numberofValues = input("Enter the number of values to be output: ")
targetG = incrementG * numberofValues
for cvG in xrange (startG, targetG + 1, incrementG):
    print cvG

'''
Ryan Evenstad
ryan.evenstad22@gmail.com
CS160 Wednesday 3PM
Lab 2 assignment
'''

'''
Part 1
Describing a number
'''
'''
# ask for input
number = input("Enter a number:")

# is value a whole number
if number == int(number):
    print number, "is a whole number"
else:
    print number, "is not a whole number"

# is value a multiple of 5
if number%5 == 0:
    print number, "is a multiple of 5"
else:
    print number, "is not a multiple of 5"

# is value even or odd
if number%2 == 0:
    print number, "is even"
else:
    print number, "is odd"
    
# is value positive negative or zero
if number == 0:
    print "The number is zero"
elif number > 0:
    print number, "is positive"
elif number < 0:
    print number, "is negative"

# is value within range
if number >= 2000:
    if number <= 2011:
        print number, "is within range"
else:
    print number, "is out of range"

# make room between exercises
print "\n\n"
'''
'''
part 2
calculating school year based on credits
'''

# ask for input
numCredits = input("Enter the amount of credits you have earned:")
semCredits = input("Enter the number of cretits you are taking this semester:")
graduation = 125 - (numCredits + semCredits)
semesters  = graduation/15

# display current status
if numCredits > 89:
    print "You are a senior"
elif numCredits > 59:
    print "You are a junor"
elif numCredits > 23:
    print "You are a sophomore"
else:
    print "You are a freshman"

# display anticipated status
if numCredits + semCredits > 89:
    print "You will be a senior"
elif numCredits + semCredits > 59:
    print "You will be a junior"
elif numCredits + semCredits > 23:
    print "You will be a sophomore"
else:
    print "You will be a freshman"

# find how many semesters it will take to graduate
print graduation, "more credits until you can graduate"
if semesters%15 == 0:
    print semesters, "more semesters at 15 credits until you can graduate"
else:
    print semesters + 1, "more semesters at 15 credits until you can graduate"

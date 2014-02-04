#need things in (here) 
def menuChoice():
    choice = raw_input("Enter your choice: ")
    if choice == "s" or choice == "o" or choice == "n" or choice == "a":
        return choice

def confirm():
    areYouSure = raw_input("Are you sure you want to choose", choice + "(yes or no):")
    areYouSure = areYouSure.strip()
    if areYouSure == "yes":
        return True
    elif areYouSure == "no":
        return False

def isAFactor():
    number1 = input("Enter a first number:  ")
    number2 = input("Enter a second number: ")
    if number2%number1 == 0:
        return True
    else:
        return False

#look at this more
'''
def endsWithPeriod():
    .endsWith(".")
'''

def getPercentage():
    number = input("Enter a number: ")
    if number >= 0 and number <= 100:
        return number

def getIntWithinRange():
    minNum = input("Enter the minimum: ")
    maxNum = input("Enter the maximum: ")
    number = input("Enter a number: ")
    if number >= minNum and number <= maxNum:
        return number

#need values to return
def letterGrade():
    value = input("Enter a number: ")
    value = int(value)
    if value >= 90:
        return
    elif value >= 80:
        return
    elif value >= 70:
        return
    elif value >= 60:
        return
    else:
        return

#look through this carefully
def main():
  print "the menu choice function will execute until the user selects a, \nthen the program will move on to the next function."
  while True:
      choice = menuChoice("Select an option (a, n, s, or o) ")
      if choice == 's' or choice == 'n' or choice == 'o' or choice == 'a':
          print "valid menu choice"
      else:
          print "invalid menu choice - check menuChoice function"
      if choice == "a":
          break

  print
  print
  print "checking confirm function - the function shoud only accept yes or no, otherwise it asks again for confirmation"
  choice = confirm("Continue with program (yes/no)? ")
  print "You entered ", choice
  if not (choice != "yes" or choice != "no"):
      print "Invalid option allowed"

  print
  print
  val1 = input ("enter the first value ")
  val2 = input ("enter the second value ")
  if isAFactor (val1, val2):
      print "your function indicates that", val1, "is a factor of ", val2
  else:
      print "your function indicates that", val1, "is not a factor of ", val2

     
  print
  print
  str1 = "This is a sentance without a period at the end"
  str2 = "This is a sentance witha period at the end."
  str1 = endWithPeriod (str1)
  str2 = endWithPeriod (str2)
  print "The next two lines should be identical"
  print str1
  print str2

  print
  print
  print "the getPercetage function will execute until the user enters a value between 0 and 100.\nThe program will contineu to accept integers until the user enters 0,\nthen it will move on to the next function."
  while True:
      value = getPercentage("Enter an integer between 0 and 100 ")
      if value < 0 or value > 100:
          print "getPercentage isn't working - it accepted ", value
      if value == 0:
          break
 
  print
  print
  minVal = 40
  maxVal = 119
  print "the getIntWithinRange function will execute until the user enters a value between the min and max value.\nThe program will contineu to accept integers until the user enters the min value,\nthen it will move on to the next function."
  while True:
      value = getIntWithinRange("Enter an integer between " + str(minVal) + " and " + str(maxVal), minVal, maxVal)
      if value < minVal or value > maxVal:
          print "getIntWithinRange isn't working - it accepted ", value
      if value == minVal:
          break

  print
  print
  print "checking the letter grades for percentage between 50 and 100"
  for percentage in xrange (50, 101):
      print "%3d  %s" % (percentage, letterGrade (percentage))


main()

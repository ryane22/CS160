def double(x):
    print "Exponent"
    return x**2
x=5
print double(x)

print "\n"

def dataAnalyst(entry):
    if entry.isdigit()==True:
        print "Digit entered"
        
entry = raw_input("Enter character!")
dataAnalyst(entry)

print "\n"

def main():
    myNum = input("Enter your number: ")
    answer = plusOne(myNum)
    print "Your number:", myNum, "plus 5 is", answer

def plusOne(myNum):
    increment=myNum+5
    return increment

main()

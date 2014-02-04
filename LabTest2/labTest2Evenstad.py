'''
Lab Test #2
Ryan Evenstad
Tuesday 3PM
'''
def readFile(tList):
    fileName = raw_input("Enter the file name: ")
    fileToOpen = open(fileName,"r")
    
    for line in fileToOpen:
        line = line.strip().split(":")
        if line[0] == "BW":
            tList[3] = float(line[1])
        elif line[0] == "D":
            tList[2] = float(line[1])
        elif line[0] == "OB":
            tList[0] = line[1]
            tList[1] = float(line[2])
            tList[4] = tList[1]
        else:
            print "File not formatted correctly"

def accountSum(tList):
    print
    print
    print "%s account summary:" % tList[0]
    print "----------------------------------"
    print "Opening Balance $%10.2f" % tList[1]
    print "Total Deposit   $%10.2f" % tList[2]
    print "Total Withdraw  $%10.2f" % tList[3]
    print "Balance         $%10.2f" % tList[4]
    print
    print

def withdraw(tList):
    print
    amount = input("Enter amount to withdraw: ")
    tList[3] = tList[3]+amount
    tList[4] = tList[4]-amount
    print
    
def deposit(tList):
    print
    amount = input("Enter amount to deposit: ")
    tList[2] = tList[2]+amount
    tList[4] = tList[4]+amount
    print

def main():
    totalsList = [None]*5

    readFile(totalsList)#first thing to do
    while True:
        print "0-Exit"
        print "1-Account Summary"
        print "2-Withdraw"
        print "3-Deposit"
        choice = input("Enter your choice: ")
        if choice == 0:
            print "Goodbye, Have a nice day!"
            break
        elif choice == 1:
            accountSum(totalsList)
        elif choice == 2:
            withdraw(totalsList)
        elif choice == 3:
            deposit(totalsList)

main()

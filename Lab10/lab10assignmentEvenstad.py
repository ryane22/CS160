def getData():
    partDictionary = {}
    while True:
        partName = raw_input("Enter the part name: ")
        if partName == "":
            break
        partPrice = raw_input("Enter the price: ")
        partDictionary[partName] = partPrice
    saveDictionary(partDictionary)
    return partDictionary

def saveDictionary(dictionary):
    fileNameToSave = raw_input("Enter the name of the file to save: ")
    fileName = open(fileNameToSave, "w")
    for key in dictionary:
        fileName.write(key + ":" + dictionary[key] + "\n")

def getDictionary():
    partDictionary = {}
    fileNameToOpen = raw_input("Enter the name of the file to open: ")
    fileName = open(fileNameToOpen, "r")
    for line in fileName:
        line = line.strip().split(":")
        partDictionary[line[0]] = line[1]
    return partDictionary

def menuItems(dictionary):
    while True:
        print "1: The Total Number of unique parts"
        print "2: All parts with a price greater then or equal to $10"
        print "3: The smallest price"
        print "4: The largest price"
        print "5: The average of all prices"
        print "6: Quit"
        print
        choice = input("Enter your choice (1-6): ")
        if choice == 1:
            uniqueParts(dictionary)
        elif choice == 2:
            priceInRange(dictionary)
        elif choice == 3:
            smallestPrice(dictionary)
        elif choice == 4:
            largestPrice(dictionary)
        elif choice == 5:
            averagePrice(dictionary)
        elif choice == 6:
            break

def uniqueParts(dictionary):
    x = 0
    for key in dictionary:
        x = x+1
    print "The total number of unique parts is", x
    print

#values in dictionary have . which doesnt float should fix this     
def priceInRange(dictionary):
    print "Parts that cost $10 or more:"
    for key in dictionary:
        partPrice = dictionary[key]
        if float(partPrice) >= 10:
            print key
    print

#values in dictionary have . which doesnt float should fix this 
def smallestPrice(dictionary):
    lowPrice = 9999999999999
    for key in dictionary:
        partPrice = dictionary[key]
        if float(partPrice) < lowPrice:
            lowPrice = partPrice
    print "The lowest price is $", lowPrice
    print

#values in dictionary have . which doesnt float should fix this 
def largestPrice(dictionary):
    highPrice = 0
    for key in dictionary:
        partPrice = dictionary[key]
        if float(partPrice) > highPrice:
            highPrice = partPrice
    print "The highest price is $", highPrice
    print
    
def averagePrice(dictionary):
    print 'averagePrice'
    print    
          

def printDict(dictionary):
    for key in dictionary:
        print key, dictionary[key]


def main():
    
    getData()
    print
    #getData()
    print
    dict1 = getDictionary()
    print
    menuItems(dict1)
    


main()

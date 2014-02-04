def addProduct(productDict):
    while True:
        productID = input("Enter the product ID: ")
        productName = raw_input("Enter the name of the product: ")
        productLocation = raw_input("Enter where the product is sold: ")
        productPrice = input("Enter the price: ")
        productDict[productID] = (productName,productLocation,productPrice)
        again = raw_input("Add another (y/n)? ")
        if again == 'n' or again == "N":
            break
    print

def fileSave(productDict):
    fileName = raw_input("Enter the name of the file to save: ")
    fileToSave = open(fileName, "w")
    for product in productDict:
        fileToSave.write(str(product)+"-"+productDict[product][0]+":"+productDict[product][1]+":"+str(productDict[product][2])+"\n")
    fileToSave.close()
    print

def search(productDict):
    query = raw_input("Enter your search: ")
    highPrice = 0
    productID = None
    for product in productDict:
        if productDict[product][0].find(query) != -1:
            if highPrice < productDict[product][2]:
                highPrice = productDict[product][2]
                productID = product
    if productID == None:
        print "No results found"
        print
    else:
        print "Product ID     Product Name        Product Location    Product Price"
        print "%-15d%-20s%-20s%10.2f" %(productID,productDict[productID][0],productDict[productID][1],productDict[productID][2])
        print

def display(productDict):
    print "Product ID     Product Name        Product Location    Product Price"
    for product in productDict:
        print "%-15d%-20s%-20s%10.2f" %(product,productDict[product][0],productDict[product][1],productDict[product][2])
    print


def main():
    productDict = {}
    
    while True:
        print "1 - Create Product Catalog"
        print "2 - Save Current Dictionary"
        print "3 - Print Data in Dictionary"
        print "4 - Search for Product at the most expensive location"
        print "5 - Exit"
        print
        
        choice = input("Enter your choice: ")
        
        if choice == 1:
            addProduct(productDict)
        elif choice == 2:
            fileSave(productDict)
        elif choice == 3:
            display(productDict)
        elif choice == 4:
            search(productDict)
        elif choice == 5:
            break

main()

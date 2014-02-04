def menu(contactDict):
    while True:
        print '1: Display all contacts'
        print '2: Add a contact'
        print '3: Load contacts from file'
        print '4: Save contacts to file'
        print '5: Search for a contact'
        print '6: Exit program'
        print
        choice = input('Enter your choice: ')

        if choice == 1:
            displayContacts(contactDict)
        elif choice == 2:
            addContact(contactDict)
        elif choice == 3:
            loadContacts(contactDict)
        elif choice == 4:
            True
        elif choice == 5:
            True
        elif choice == 6:
            break
        else:
            print 'Not a valid choice'
            print
            
def displayContacts(contactDict):
    contactList = []
    for contact in contactDict:
        contactList.append(contact)
    contactList.sort()
    print "Name                Cell Number    Work Number    E-mail"
    for item in contactList:
        print "%-20s%-15s%-15s%-20s" %(item,contactDict[item][0],contactDict[item][1],contactDict[item][2])
    print

def addContact(contactDict):
    contactName = raw_input("Enter contact name: ")
    if contactName == "":
        print
    else:
        cellNum = raw_input("Enter cell number: ")
        workNum = raw_input("Enter work number: ")
        email = raw_input("Enter e-mail: ")
        contactDict[contactName] = (cellNum, workNum, email)
        print

#note that my files don't say cell, work, or email in the information
def loadContacts(contactDict):
    
    

def main ():
    contacts = {"a":("4","5","6"),"c":("1","2","3"),"A":("7",None,None)}
    menu(contacts)

main()

fileToRead = raw_input("Enter the file name: ")
readPlaylist = open(fileToRead, "r")
listPlaylist = []

for line in readPlaylist:
    listPlaylist.append(line.strip("\n"))
readPlaylist.close()

#should probably split and get list into a decent format before this point

print "1: Sort by Artist"
print "2: Sort by Title"
print "3: Sort by Time"
print "4: Search by Artist"
choice = input("Enter your choice: ")
if choice == 1:
    for indexToSort in xrange(0, len(listPlaylist)-1):
        for index in xrange(indexToSort, len(listPlaylist)):
            if listPlaylist[index] < listPlaylist[indexToSort]:
                temp = listPlaylist[indexToSort]
                listPlaylist[indexToSort] = listPlaylist[index]
                listPlaylist[index] = temp
    print listPlaylist

#for index in listPlaylist:
#    index = index.split("-")
#    print index

#print listPlaylist

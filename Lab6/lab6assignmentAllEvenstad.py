#part 1
inputFileName = raw_input("Enter a CD filename: ")

if inputFileName.strip() == "":
    print ("invalid file name")
else:
    inputFile = open(inputFileName, "w")
    while True:
        artistName = raw_input("Enter an artist: ")
        if artistName == "QUIT":
            break
        cdTitle = raw_input("Enter CD title: ")
        inputFile.write(artistName + ":" + cdTitle +"\n")
    inputFile.close()
print ("\n")

#part 2
searchFile = raw_input("Enter a CD filename: ")
searchInfo = raw_input("Enter search information: ")
numMatches = 0
openFile = open(searchFile, "r")
print ("Artist              Title\n")
for line in openFile:
    line = line.strip("\n")
    if line.find(searchInfo)>=0:
        separate = line.find(":")
        print ("%-20s%-20s" %(line[0:separate],line[separate+1:]))
        numMatches = numMatches +1
print numMatches, "match(es) found"

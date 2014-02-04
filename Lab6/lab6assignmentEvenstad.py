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

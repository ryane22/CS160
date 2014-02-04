fileToWrite = raw_input("Enter the name of the file: ")
playlistFile = open(fileToWrite, "w")

while True:
    print "Enter the artist, enter "" to quit:"
    artistName = raw_input("Artist: ")
    if artistName == "":
        break
    songTitle = raw_input("Title: ")
    songTime = raw_input("Time: ")
    playlistFile.write(artistName + "-" + songTitle + "-" + songTime + "\n")

playlistFile.close()

'''
part 1
'''
enterFileName = raw_input("Enter data file name: ")
testScoreFile = open(enterFileName, "w")

while True:
    testScore = input("Enter the scores, enter -1 to quit: ")
    if testScore == -1:
        break
    elif testScore >= 0 and testScore <= 100:
        testScoreFile.write(str(testScore)+"\n")

testScoreFile.close()


'''
part 2
'''
openFileName = raw_input("Enter data file name: ")
readFile = open(openFileName, "r")
testScoresList = []
highTest = 0
lowTest = 100
totalTestScores = 0

for line in readFile:
    testScoresList.append(int(line.strip()))

for index in testScoresList:
    if index > highTest:
        highTest = index
    if index < lowTest:
        lowTest = index
    totalTestScores = totalTestScores + index

print "Largest score: %6d"  %highTest
print "Smallest score:%6d"  %lowTest
average = float(totalTestScores) / len(testScoresList)
print "Average Score: %6.2f" %average

Word = '**program**'
print Word.rstrip("*")
print "\n\n"

car = "Honda Civic"
brand = car.split()
print 'The brand of car i like is', brand[0]
print "\n\n"

words = raw_input("Enter a sentence")
size = words.split()
print len(size)
print size[2]
if (len(size)%2==0):
    print 'the number of words entered is even with', len(size), 'numbers of words'
    print words.lower()
else:
    print 'the number of words entered is odd with', len(size), 'numbers of words'
    mid = len(size)/2
    print mid
    print "mid word is", size[mid+1]

for number in xrange(1,5):
    print number

print "\n"

r = 5
for x in xrange (2,6):
    r += 1
print 'the sum of r is', +r

print "\n"

value = input('enter a number')
while value <= 5:
    answer = value * 2
    print value, "product is", answer
    value = value + 1

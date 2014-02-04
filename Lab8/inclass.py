#1
listOne=range(1,6)
print listOne
listTwo=[1,2,3,4,5]
print listTwo
if listOne == listTwo:
    print"equal"

#2
numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
    if x%2==0:
        odd = numbers.remove(x)
print numbers

#3
Laps = [9,4,6]
for index in xrange(1,4):
    number = input('enter a lap number')
    Laps.append(number)
print Laps

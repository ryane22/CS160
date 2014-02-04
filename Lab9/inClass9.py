Book=['python','software_engineering']
print Book[len(Book)-1]

sample = [3,5,6,5,3]
look = 5
for index in xrange(sample):
    if look == sample[index]:
        sample.pop(look)
        sample.insert(index,"A")
print sample

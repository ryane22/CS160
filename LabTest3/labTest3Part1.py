Grade = {}

def average(num):
    sum = 0
    for key in Grade:
        sum = sum + (Grade[key])
        print sum
    return sum/num

def count():
    print len(Grade)
    return len(Grade)

def main():
    while True:
        subject = raw_input('enter the name of subject')
        grade = input('enter a number')
        Grade[subject]=grade
        another = raw_input('y/n')
        if another == 'n':
            break
    Num = count()
    number = average(Num)
    print number
main()

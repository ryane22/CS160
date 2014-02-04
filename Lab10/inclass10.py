'''
info = {}
for key in xrange(1,3):
    number = raw_input("enter a phone number")
    info["number"+str(key)]= number
print info
'''
'''
account = {'name':'John','bal':55, 'd':20, 'c':13}
b=account['bal']
d=account['d']
c=account['c']
print account['name'], 'account summary', b+d-c
'''
'''
menu={1:'add a user',2:'delete a user', 3:'sort users', 4:'exit'}
while True:
    print menu
    answer = input('blah')
    if menu.has_key(answer):
        print menu[answer]
    if answer == 4:
        break
'''

                   

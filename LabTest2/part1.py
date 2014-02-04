menu = ['1-play','2-stop','3-pause']
while True:
    action = input('enter a command: ')
    if action not in  [1,2,3]:
        print 'command', action,'not in menu'
        break
    else:
        for line in menu:
            line = line.split("-")
            if action == int(line[0]):
                print 'command', line[0], 'action is', line[1]

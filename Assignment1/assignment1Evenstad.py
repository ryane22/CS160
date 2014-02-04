carCount = 0
fastestCar = -1
fastestSpeed = -1
longestDistanceCar = -1
longestDistance = -1
shortestDistanceCar = -1
shortestDistance = 10000000000000000

while True:
    print "0: Exit"
    print "1: Display Information"
    print "2: Reset All Data"
    print "3: Enter Data"

    choice = input("Enter a choice: ")
    if choice == 0:
        break
    
    elif choice == 1:
        break

    elif choice == 2:
        break

    elif choice == 3:
        while True:
            carCount = carCount + 1
            speed = input ("What is the speed of car%d: " %carCount,)
            time = input ("What is the time travelled for car%d: " %carCount,)
            distance = speed * time

            if speed > fastestSpeed:
                fastestSpeed = speed
                fastestCar = carCount
            if distance > longestDistance:
                longestDistance = distance
                longestDistanceCar = carCount
            elif distance < shortestDistance:
                shortestDistance = distance
                shortestDistanceCar = carCount
            break

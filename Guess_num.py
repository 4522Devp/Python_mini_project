import random 

target =random.randint(1,100)

while True :
    userChoice = int(input("Gauss the value: "))
    if (userChoice == target):
        print("Success : Correct Gauss")
        break
    elif (userChoice < target):
        print("too small , chose bigger")
    else:
        ("yourr number is bigger , choose smaller")    


print("__ Game Over___")
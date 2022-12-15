print("Welcome to my computer game!")

playing = input("Do you want to play? ")
Score = 0
 
if playing.lower() != "yes":
    quit()

print("Okay! Let`s Play :) ")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    Score += 1
else:
    print("Incorrect")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect")

print("You got " + str(Score) + " question correct!")
print("You got " + str((Score / 4) * 100) + "%.")
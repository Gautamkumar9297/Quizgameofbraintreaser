print("welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("okay! Let's play:) ")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is GPU stand for ?")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input(" what does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + "question correct !")
print("you got " + str((score / 4) * 100) + "%.")

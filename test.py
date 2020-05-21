import random
import time

start = input("Want to play rock,paper,scissors?")

decider = random.randint(1,3)


if start in [" yes"," Yes"," Y"," y"]:
    first = input("Rock,Paper, or Scissor?")
    yesNo = True
else:
    print("Ok i guess we wont play")
    yesNo = False

if first in [" Rock"," rock"]:
    first = 1

if first in [" Paper", " paper"]:
    first = 2

if first in [" Scissor", " scissor"]:
    first = 3

print("Thinking...")
time.sleep(3)

if decider == 1:
    print("Computer picked Rock!")

if decider == 2:
    print("Computer picked Paper!")

if decider == 3:
    print("Computer picked Scissors!")

if first == 1 and decider == 1:
    print("Ah a tie!")
    exit()

if first == 2 and decider == 2:
    print("Ah a tie!")
    exit()

if first == 3 and decider == 3:
    print("Ah a tie!")
    exit()

if first == 3 and decider == 1:
    print("Oh no you lost!")
    exit()

if first == 1 and decider == 2:
    print("Oh no you lost!")
    exit()

if first == 2 and decider == 3:
    print("Oh no you lost!")
    exit()

if first == 2 and decider == 1:
    print("You won!")
    exit()

if first == 3 and decider == 2:
    print("You won!")
    exit()

if first == 1 and decider == 3:
    print("You won!")
    exit();

    
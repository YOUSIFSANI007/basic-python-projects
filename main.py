import random

# Choices: -1 for "Water", 1 for "Snake", and 0 for "Gun"
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (Snake/Water/Gun): ").lower()
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr in youDict:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    else:
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == -1:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You win!")
        elif computer == 0 and you == -1:
            print("You win!")
        elif computer == 0 and you == 1:
            print("You lose!")
else:
    print("Invalid choice. Please enter Snake, Water, or Gun.")

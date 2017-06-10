import random
def rolldie():
    print("Rolling the Dice")
    x = random.randrange(1,6)
    print(x)



def main():
    roll_again = "yes"
    while roll_again == "yes" or roll_again== "y":
        rolldie()
        roll_again = input("Do you wanna roll the dice again and again")


if __name__ == "__name__":main()

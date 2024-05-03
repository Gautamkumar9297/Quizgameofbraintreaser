name = input("Type you name:-")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road ,it has come to an end and you can go left or right .which way would you like to go ?").lower()


if answer == "left":
    answer = input(
        "you come to a river ,you can walk around it or swim across?type walk to walk around and swim to swim accross:-")
    if answer == "swim":
        print("you swam across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles ,ran out of water and you lost your game ")
    else:
        print("Not a valid option .You lose")

elif answer == "right":
    answer = input(
        "you come to a bridge it looks wobbly ,do you want to cross it ?")
    if answer == "back":
        print("you go back and lose")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger .do you talk(yes/no)?")

        if answer == "yes":
            print("You talk with stranger and they give you gold.You WIN!")
        elif answer == "no":
            print("you ignore the stranger and they offended and you lose ")

    else:
        print("Not a valid option .You lose")

else:
    print("Not a valid option.you lose")
print("Thank for try", name)

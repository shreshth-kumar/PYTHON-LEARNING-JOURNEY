name = input ("Type your name : ")
print("Welcome", name, "to this adventure!")

answer = input("ypu are on a dirt road, it has come to an end and you can go left or right. which way would you like to go ?").lower()

if answer == "left":
    answer = input('You come to a river, you can walk around it or swin accross. Type walk to walk or swin to swim accross: ')
    if answer == "swim":
        print("You swim acrross and were eaten by an alligator." )
    elif answer == "walk":
        print("You walked for many miles, ran out of ewater and you lost the game.")
elif answer == "right":
    answer = input ("you come to a bridge , it looks wobbly, do you want ot cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose." )
    elif answer == "cross":
        answer == input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)? ")
        if answer == "yes":
                print("You talk to the stranger and they give you gold. You win!")
        elif answer =="no":
            print("You ignore the stranger and the are offended and you lose.")
        else:
            print("not a valid option . You lose!")

else:
    print("not a valid option . You lose!")
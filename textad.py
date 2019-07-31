
start = '''You are trying to figure where to go to lunch.
You mad rich, so you fuel up the private jet and you need to decide
what continent you want to go to for lunch.
'''

print(start)

print("Type 'Asia'to go to Asia or'North America' to go to North America or 'East Africa' to go to East Africa. ")
user_input = input()
    if user_input == "Asia":
        print("You decided to go to Asia.")
        print("Do you want to go to China or India")
        user_input = input("Type 'China' to go to China or 'India' to go to India\n")
        if user_input == "China":
            print("Lets go get some Chow Mein")
            user_input = input("Choose restaurant'red' or 'blue' or 'purple' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")
        if user_input == "India":
            print("Lets go get some Butter Chicken")
            user_input = input("Choose restaurant'red' or 'blue' or 'white' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")

    elif user_input == "North America":
        print("You decided to go to North America.")
        print("Do you want to go to Mexico or the USA")
        user_input = input("Type 'Mexico'to go to Mexico or 'USA' to go to the USA\n")
        if user_input == "Mexico":
            print("Lets go get some Enchiladas")
            user_input = input("Choose restaurant'red' or 'blue' or 'purple' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")
        if user_input == "USA":
            print("Lets go get some Burgers and Fries")
            user_input = input("Choose restaurant'red' or 'blue' or 'purple' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")

    elif user_input == "East Africa":
        print("You decided to go to East  Africa.")
        print("Do you want to go to Ethiopia or Somalia")
        user_input = input("Type 'Ethiopia'to go to Ethiopia or 'Somalia' to go to the Somalia\n")
        if user_input == "Ethiopia":
            print("Lets go get some Injera")
            user_input = input("Choose restaurant'red' or 'blue' or 'purple' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")
        if user_input == "Somalia":
            print("Lets go get some Bariis(rice)")
            user_input = input("Choose restaurant'red' or 'blue' or 'purple' ")
            if user_input == "red":
                print("The love of your life is here!!!")
            if user_input == "blue":
                print("You found your lover cheating in kitchen")
            if user_input == "purple":
                print("You found a health code violation and now is in management")

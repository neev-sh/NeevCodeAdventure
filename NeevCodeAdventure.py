def start_game():
    print("Welcome to Neev’s Coding adventure!”)
    print("You are a coder who falls into a dark cave...")
    print("You must find your way out!\n")
    input("Press Enter to begin...")

    scene_one()


def scene_one():
    print("\nYou see two paths in the cave.")
    print("1. A bright tunnel with green lights.")
    print("2. A dark tunnel with scary sounds.")
    choice = input("Which path do you take? (1 or 2): ")

    if choice == "1":
        green_tunnel()
    elif choice == "2":
        dark_tunnel()
    else:
        print("You wait too long and fall asleep.")
        scene_one()


def green_tunnel():
    print("\nYou follow the green lights.")
    print("You find a computer on a rock.")
    print("The screen says: 'What has keys but cannot open a door?'")
    answer = input("Your answer: ").lower()

    if "keyboard" in answer:
        print("Correct! A door opens.")
        bridge_scene()
    else:
        print("Wrong answer. Try again.")
        green_tunnel()


def dark_tunnel():
    print("\nThe tunnel is cold and dark.")
    print("A person in a black robe stops you.")
    print("They say: 'Answer my question or go back!'")
    print("What is 2 + 2?")
    answer = input("Your answer: ")

    if answer == "4":
        print("Good job! You may continue.")
        loop_room()
    else:
        print("Wrong! Go back!")
        scene_one()


def bridge_scene():
    print("\nYou come to a thin bridge over hot lava!")
    print("A robot says: 'Choose your type!'")
    print("1. int")
    print("2. str")
    print("3. bool")
    choice = input("Your choice: ")

    if choice == "2":
        print("Robot says: 'String is strong!' and lets you pass.")
        final_scene()
    else:
        print("The bridge breaks. You fall!")
        scene_one()


def loop_room():
    print("\nYou are in a room that repeats!")
    print("Voices say: 'Break the loop!'")
    print("You see a red button that says 'BREAK'.")
    choice = input("Do you press the button? (yes or no): ").lower()

    if choice == "yes":
        print("The loop ends. You are free!")
        final_scene()
    else:
        print("You stay in the loop forever...")
        scene_one()


def final_scene():
    print("\nYou see a dragon made of code!")
    print("It asks: 'Is True == 1 in Python?'")
    print("1. Yes")
    print("2. No")
    choice = input("Your answer: ")

    if choice == "1":
        print("The dragon smiles. You understand Python!")
        ending()
    else:
        print("The dragon roars. Try again!")
        scene_one()


def ending():
    print("\nYou find the Code Crystal!")
    print("You are now the Code Master.")
    print("You escape the cave.")
    print("🎉 THE END 🎉")
    exit()


# Start the game
start_game()

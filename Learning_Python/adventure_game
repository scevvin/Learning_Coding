# things to do:
# character array to store all character options.
# character name array.
# character inventory array.
# prologue
# field - when character goes to and from cabin/cave etc.
# cabin options array.
# cave options array.
# ancient book item

import random
import time


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def play_game():
    name = []
    inventory = []
    inventory_choices = random.choice(["rusty knife", "cracked bow", "empty canteen", "dwindling torch"])
    cabin_figure = random.choice(["black hooded figure", "pale, scrawny figure with red eyes", "a transparent, black cloud with purple eyes"])
    cave_figure = random.choice(["angelic figure with white robes", "three young children dressed in white and gold silk", "an old man"])
    inventory.append(inventory_choices)
    start(name, inventory, cabin_figure, cave_figure)


def start(name, inventory, cabin_figure, cave_figure):
    name_ask = input("Hello, Adventurer! What is your name?\n")
    print_pause(f"You typed {name_ask}. Is that ok?")
    time.sleep(1)
    name_check = input("Please type yes to continue or no to change\n")
    if name_check.lower() == "yes":
        name.append(name_ask)
        field_prologue(name, inventory, cabin_figure, cave_figure)
    if name_check.lower() == "no":
        name_change(name, inventory, cabin_figure, cave_figure)
    else:
        print("Sorry, I didn't understand that.")
        return start(name, inventory, cabin_figure, cave_figure)


def name_change(name, inventory, cabin_figure, cave_figure):
    change = input("Please type in what you'd like your name to be\n")
    print_pause(f"You typed {change}. Is that ok?")
    name_check = input("Please type yes to continue or no to change\n")
    if name_check.lower() == "yes":
        name.clear()
        name.append(change)
        field_prologue(name, inventory, cabin_figure, cave_figure)
    if name_check.lower() == "no":
        return name_change(name, inventory, cabin_figure, cave_figure)


# The first field option only!
def field_prologue(name, inventory, cabin_figure, cave_figure):
    print_pause("You come across a wide field, the swaying grass illuminated by the bright, full moon above.")
    print_pause(f"You look at your {inventory[0]} and wonder what else you can find here.")
    print_pause("As you scan the field, you notice a cabin to the left and a cave to the right.")
    print_pause("The cabin is lit up with smoke coming out of the chimney.")
    print_pause("Scanning right, the field turns into rolling hills.")
    print_pause("At the base of these hills, you see what looks like the top of a cave entrance.")
    print_pause("The breeze you watched sweep across the field passes you.")
    print_pause("Piercing inside, down to your bones.")
    print_pause(f"With a shiver, you look at your {inventory[0]}.")
    print_pause("'I'd better make a decision, quickly,' you think to your self.")
    print_pause("What do you choose to investigate first?")
    field_choice(name, inventory, cabin_figure, cave_figure)


# The choice of cabin or cave is stored here.
def field_choice(name, inventory, cabin_figure, cave_figure):
    direction = input("Please type cabin or cave\n")
    if direction.lower() == "cave":
        print_pause("Though it doesn't seem logical, something draws you to the cave.")
        cave(name, inventory, cabin_figure, cave_figure)
    if direction.lower() == "cabin":
        print_pause("The warm and inviting nature of the cabin is hard to pass up.")
        cabin(name, inventory, cabin_figure, cave_figure)


# Only after the user has gone through cabin or cave choices
def field_again(name, inventory, cabin_figure, cave_figure):
    print_pause("Coming back to the field, the cold overwhelms you.")
    print_pause("Which reminds you, you better choose fast.")
    print_pause("What do you choose to do?")
    field_choice(name, inventory, cabin_figure, cave_figure)


# -----------------------------------------------CABIN SEQUENCE-----------------------------------------------
def cabin(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause("As you get closer to the cabin,")
        print_pause("The smell of a home-cooked meal fills your nostrils.")
        print_pause("The heat from the fire insidefills your soul. ")
        print_pause("'Finally, I'm home. After all these years of wondering,' you think to yourself")
        cabin_choice(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause("Getting closer to the cabin, you can't help but feel uneasy.")
        print_pause(f"You look at your {inventory[0]} with unsurity.")
        print_pause("Though the warmth from the cabin pulls you in,")
        print_pause("You can't help but wonder if this is the right choice?")
        cabin_choice(name, inventory, cabin_figure, cave_figure)


# choice to knock or leave to field_choice
def cabin_choice(name, inventory, cabin_figure, cave_figure):
    print_pause("Walking up the steps to the cabin, you have one more choice left.")
    print_pause("Do you knock on the door? Or leave to see if there's more to explore?")
    cabin_choice = input("Please type knock to enter the cabin or leave to explore more\n")
    if cabin_choice.lower() == "knock":
        cabin_knock(name, inventory, cabin_figure, cave_figure)
    if cabin_choice.lower() == "leave":
        field_again(name, inventory, cabin_figure, cave_figure)


# both outcomes of knocking on cabin
def cabin_knock(name, inventory, cabin_figure, cave_figure):
    print_pause("You decide to knock on the cabin door,")
    print_pause("the warmth of the fire infront of you")
    print_pause("and the cold night air chilling your back.")
    print_pause("As soon as your knuckle makes the first sound")
    print_pause("the door flies open,")
    print_pause("the lights in the house extinguish,")
    print_pause("the smell of food disappears,")
    print_pause(f"and a{cabin_figure} appears in front of you. ")
    if "Ancient Book" in inventory:
        print_pause("Normally you would be scared stiff,")
        print_pause("but the calming experience in the cave prepared you for this.")
        print_pause("With the Ancient Book in hand,")
        print_pause("You open to the same page you saw in the cave.")
        print_pause(f"The {cabin_figure} instantly retreats into the darkness it emerged from.")
        print_pause("And as soon as the figure is gone,")
        print_pause("the lights come on, the warmth returns.")
        print_pause("You made it; you're home.")
        print_pause("Congratulations! You've won!")
        play_again()
    if "Ancient Book" not in inventory:
        print_pause("Standing in complete fear of this....thing")
        print_pause("You can not move or speak.")
        print_pause(f"You see a swirling void opening behind the {cabin_figure}.")
        print_pause("With a wave of  what seems to be its hand,")
        print_pause("you are lift off the ground and slowly float towards it.")
        print_pause("The black void begins to open, lighting surrdounding it.")
        print_pause("The figure turns as you get closer and heads into the void.")
        print_pause("Unable to control your motions, you follow the figure.")
        print_pause("The lightning flashes gets more intense,")
        print_pause("You feel an immense pressure all around you,")
        print_pause("Then weightlessness instatly.")
        print_pause("And with a thud, you hit the ground.")
        print_pause("You are back at the beginning of the forest,")
        print_pause("though, cabin and cave are gone.")
        print_pause("'Where am I,' you wonder, trying to survey where you are.")
        print_pause("You have been lost to time.")
        play_again()


# -----------------------------------------------CAVE SEQUENCE-----------------------------------------------
# cave choice to enter or leave
# cave entrace
def cave(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause("Walking closer to the cave you entered in before,")
        print_pause("You see the same glimmering lights coming from within.")
        print_pause("'Is there more for me to find,' you wonder as you approach the entrance.")
        cave_choice(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause(f"Shivering, holding your {inventory[0]} tightly,")
        print_pause("You come up to the entrance of a cave you saw earlier.")
        print_pause("As you study the entrance, you notice flickering lights coming from deep inside.")
        print_pause("A breeze of warm air suddenly hits you")
        print_pause("And a soft, deep voice fills your mind.")
        print_pause("'Come in,' it says.")
        cave_choice(name, inventory, cabin_figure, cave_figure)


# enter the cave or leave
def cave_choice(name, inventory, cabin_figure, cave_figure):
    print_pause("Do you enter the cave?")
    cabin_choice = input("Please type 'enter' to enter the cave or 'leave' to explore more\n")
    if cabin_choice.lower() == "enter":
        cave_enter(name, inventory, cabin_figure, cave_figure)
    if cabin_choice.lower() == "leave":
        field_again(name, inventory, cabin_figure, cave_figure)


# enter the cave - with or without book options
def cave_enter(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause("The memories of what you experienced here flood your mind.")
        print_pause("However, you feel as though there is nothing left for you here.")
        print_pause("You walk out of the cave and back to the field.")
        field_again(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause("The cold and dark of the cave fills you with worry.")
        print_pause("'Why did I come here first,' you wonder.")
        print_pause("As you continue walking deeper into the darkness,")
        print_pause("Another burst of warm air comes from somewhere unknown.")
        print_pause("You pause in your tracks, trying to find a source for this sensation.")
        print_pause("Looking around for an answer, the cave suddenly fills with a blinding light.")
        print_pause("You close your eyes to block out the overwhelming illumination.")
        print_pause("When you sense it has faded, the cave has transformed into an ethereal shrine.")
        print_pause("'Is this heaven,' you wonder while you study the room.")
        print_pause(f"You notice a {cave_figure} opposite an altar that you are standing infront of.")
        print_pause("A smile is on their face and you hear in your mind, 'No, this isn't heaven.'")
        print_pause("You look down at the altar and notice an old, worn book thick with pages.")
        print_pause("On the cover, you notice gold runes that seem to be shining from within,")
        print_pause("though, you can't read them.")
        print_pause("As you reach out to open the book, it suddenly opens itself to a page.")
        print_pause("More glowing runes cover the page in an unfamiliar format.")
        print_pause(f"You look to the {cave_figure} for some sort of answer.")
        print_pause("With the same smile, the figure raises its hands, making the book float.")
        print_pause("Some instinct tells you to open your arms in the same manner.")
        print_pause("The book floats to you, resting in your hands.")
        print_pause("Though the book looks as though it should be very heavy, it is as light as a feather.")
        print_pause("The confusion you have been experiencing through this has been replaced with calmness.")
        print_pause("Congratulations, you found the Ancient Book!")
        print_pause(f"Looking back to the {cave_figure}, they continue smiling, nod, and vanish.")
        print_pause("You close the book and hold it tightly.")
        print_pause("As soon as you close the book, the shrine, lights, and warmth all disappear.")
        print_pause("You find yourself at the entrance of the cave.")
        inventory.clear()
        inventory.append("Ancient Book")
        field_again(name, inventory, cabin_figure, cave_figure)


# ------------------- PLAY AGAIN/PLAY GAME -----------------------
def play_again():
    again = input("Would you like to play again? Please type yes or no\n")
    if again.lower() == "yes":
        print_pause("Restarting your adventure!")
        print_pause("3")
        print_pause("2")
        print_pause("1")
        play_game()
    if again.lower() == "no":
        print_pause("Thank you for playing!")
        exit()


play_game()

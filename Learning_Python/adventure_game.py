
import time
import random


def print_pause1(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def print_pause2(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def play_game():
    name = []
    inventory = []
    inventory_choices = random.choice(["""
        rusty knife
        cracked bow
        empty canteen
        dwindling torch"""])
    cabin_figure = random.choice(["""
        black hooded figure
        scrawny figure with red eyes
        a black cloud with purple eyes"""])
    cave_figure = random.choice(["""
        angelic figure with white robes
        three young children dressed in white and gold silk
        an old man"""])
    inventory.append(inventory_choices)
    print_pause1("Hello, Adventurer!")
    print_pause1("What is your name?")
    start(name, inventory, cabin_figure, cave_figure)


def start(name, inventory, cabin_figure, cave_figure):
    name_ask = input("Please type your name below\n")
    print_pause1(f"You typed {name_ask}. Is that ok?")
    name_check = input("Please type yes to continue or no to change\n")
    if name_check.lower() == "yes":
        name.append(name_ask)
        field_prologue(name, inventory, cabin_figure, cave_figure)
    if name_check.lower() == "no":
        return start(name, inventory, cabin_figure, cave_figure)
    else:
        print_pause1("Sorry, I didn't understand that.")
        return start(name, inventory, cabin_figure, cave_figure)


# The first field option only!
def field_prologue(name, inventory, cabin_figure, cave_figure):
    print_pause2("You come across a wide field,")
    print_pause2("the swaying grass illuminated by the bright moon above.")
    print_pause2(f"You look at your {inventory[0]}.")
    print_pause2("You wonder what else you can find here.")
    print_pause2("As you scan the field, you notice a cabin to the left...")
    print_pause2("...a cave to the right.")
    print_pause2("The cabin is lit up with smoke coming out of the chimney.")
    print_pause2("Scanning right, the field turns into rolling hills.")
    print_pause2("At the base of these hills,")
    print_pause2("you see what looks like the top of a cave entrance.")
    print_pause2("The breeze you watched sweep across the field passes you.")
    print_pause2("Piercing inside, down to your bones.")
    print_pause2(f"With a shiver, you look at your {inventory[0]}.")
    print_pause2("'I'd better make a decision, quickly,'")
    print_pause2("you think to your self.")
    print_pause2("What do you choose to investigate first?")
    field_choice(name, inventory, cabin_figure, cave_figure)


# The choice of cabin or cave is stored here.
def field_choice(name, inventory, cabin_figure, cave_figure):
    direction = input("Please type cabin or cave\n")
    if direction.lower() == "cave":
        print_pause2("Though it doesn't seem logical,")
        print_pause2(" something draws you to the cave.")
        cave(name, inventory, cabin_figure, cave_figure)
    if direction.lower() == "cabin":
        print_pause2("The warm nature of the cabin is hard to pass up.")
        cabin(name, inventory, cabin_figure, cave_figure)
    else:
        print_pause1("I'm sorry, I didn't understand that.")
        print_pause1("Could you please retype that?")
        return field_choice(name, cabin_figure, cabin_figure, cabin_figure)


# Only after the user has gone through cabin or cave choices
def field_again(name, inventory, cabin_figure, cave_figure):
    print_pause2("Coming back to the field, the cold overwhelms you.")
    print_pause2("Which reminds you, you better choose fast.")
    print_pause2("What do you choose to do?")
    field_choice(name, inventory, cabin_figure, cave_figure)


# ------------------CABIN SEQUENCE---------------------------
def cabin(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause2("As you get closer to the cabin,")
        print_pause2("The smell of a home-cooked meal fills your nostrils.")
        print_pause2("The heat from the fire insidefills your soul. ")
        print_pause2("'Finally, I'm home. After all these years of wandering,")
        print_pause2(" you think to yourself")
        cabin_choice(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause2("Getting closer to the cabin")
        print_pause2("you can't help but feel uneasy.")
        print_pause2(f"You look at your {inventory[0]} with unsurity.")
        print_pause2("Though the warmth from the cabin pulls you in,")
        print_pause2("You can't help but wonder if this is the right choice?")
        cabin_choice(name, inventory, cabin_figure, cave_figure)


# choice to knock or leave to field_choice
def cabin_choice(name, inventory, cabin_figure, cave_figure):
    print_pause2("Walking up the steps to the cabin,")
    print_pause2("you have one more choice left.")
    print_pause2("Do you knock on the door?")
    print_pause2("Or leave to see if there's more to explore?")
    cabin_choice = input("Please type knock or leave\n")
    if cabin_choice.lower() == "knock":
        cabin_knock(name, inventory, cabin_figure, cave_figure)
    if cabin_choice.lower() == "leave":
        field_again(name, inventory, cabin_figure, cave_figure)
    else:
        print_pause2("I'm sorry, I didn't understand that")
        print_pause1("Could you please retype that?")
        return cabin_choice(name, inventory, cabin_figure, cabin_choice)


# both outcomes of knocking on cabin
def cabin_knock(name, inventory, cabin_figure, cave_figure):
    print_pause2("You decide to knock on the cabin door,")
    print_pause2("the warmth of the fire infront of you")
    print_pause2("and the cold night air chilling your back.")
    print_pause2("As soon as your knuckle makes the first sound")
    print_pause2("the door flies open,")
    print_pause2("the lights in the house extinguish,")
    print_pause2("the smell of food disappears,")
    print_pause2(f"and a{cabin_figure} appears in front of you. ")
    if "Ancient Book" in inventory:
        print_pause2("Normally you would be scared stiff,")
        print_pause2("but the calming experience in the cave prepared you.")
        print_pause2("With the Ancient Book in hand,")
        print_pause2("You open to the same page you saw in the cave.")
        print_pause2(f"The {cabin_figure}  retreats into the darkness.")
        print_pause2("And as soon as the figure is gone,")
        print_pause2("the lights come on, the warmth returns.")
        print_pause2("You made it; you're home.")
        print_pause2("Congratulations! You've won!")
        play_again()
    if "Ancient Book" not in inventory:
        print_pause2("Standing in complete fear of this....thing")
        print_pause2("You can not move or speak.")
        print_pause2(f"You see a void opening behind the {cabin_figure}.")
        print_pause2("With a wave of  what seems to be its hand,")
        print_pause2("you are lifted off the ground")
        print_pause2("slowly floating towards it.")
        print_pause2("The black void begins to open.")
        print_pause2("The figure turns turns into the void as you approach.")
        print_pause2("Unable to control your motions, you follow the figure.")
        print_pause2("The lightning flashes gets more intense,")
        print_pause2("You feel an immense pressure all around you,")
        print_pause2("Then weightlessness instatly.")
        print_pause2("And with a thud, you hit the ground.")
        print_pause2("You are back at the beginning of the forest,")
        print_pause2("though, cabin and cave are gone.")
        print_pause2("'Where am I,' you wonder, trying to survey this place.")
        print_pause2("You have been lost to time.")
        play_again()


# ---------------------------CAVE SEQUENCE-----------------------------
# cave choice to enter or leave
# cave entrace
def cave(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause2("Walking closer to the cave you entered in before,")
        print_pause2("You see the same glimmering lights coming from within.")
        print_pause2("'Is there more for me to find,'")
        print_pause2("you wonder as you approach the entrance.")
        cave_choice(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause2(f"Shivering, holding your {inventory[0]} tightly,")
        print_pause2("You come up to the entrance of a cave you saw earlier.")
        print_pause2("As you study the entrance,")
        print_pause2("you notice flickering lights coming from deep inside.")
        print_pause2("A breeze of warm air suddenly hits you")
        print_pause2("And a soft, deep voice fills your mind.")
        print_pause2("'Come in,' it says.")
        cave_choice(name, inventory, cabin_figure, cave_figure)


# enter the cave or leave
def cave_choice(name, inventory, cabin_figure, cave_figure):
    print_pause2("Do you enter the cave?")
    cabin_choice = input("Please type 'enter' or 'leave'\n")
    if cabin_choice.lower() == "enter":
        cave_enter(name, inventory, cabin_figure, cave_figure)
    if cabin_choice.lower() == "leave":
        field_again(name, inventory, cabin_figure, cave_figure)
    else:
        print_pause2("I'm sorry, I didn't understand that.")
        print_pause2("Could you please retype that?")
        return cabin_choice(name,  inventory, cabin_figure, cave_figure)


# enter the cave - with or without book options
def cave_enter(name, inventory, cabin_figure, cave_figure):
    if "Ancient Book" in inventory:
        print_pause2("The memories of what you experienced come to mind.")
        print_pause2("You feel like there is nothing left to find.")
        print_pause2("You walk out of the cave and back to the field.")
        field_again(name, inventory, cabin_figure, cave_figure)
    if "Ancient Book" not in inventory:
        print_pause2("The cold and dark of the cave fills you with worry.")
        print_pause2("'Why did I come here first,' you wonder.")
        print_pause2("As you continue walking deeper into the darkness,")
        print_pause2("Another burst of warm air comes from somewhere unknown.")
        print_pause2("You pause in your tracks,")
        print_pause2("trying to find a source for this sensation.")
        print_pause2("Looking around for an answer,")
        print_pause2("the cave suddenly fills with a blinding light.")
        print_pause2("You close your eyes to block the flood of brightness.")
        print_pause2("When you sense it has faded,")
        print_pause2("the cave has transformed into an ethereal shrine.")
        print_pause2("'Is this heaven,' you wonder while you study the room.")
        print_pause2(f"You notice a {cave_figure} opposite an altar infront.")
        print_pause2("You hear in your mind, 'No, this isn't heaven.'")
        print_pause2("You look down at the altar and notice an old, worn book")
        print_pause2("thick with pages.")
        print_pause2("On the cover, you notice shining gold runes,")
        print_pause2("though, you can't read them.")
        print_pause2("As you open the book, it suddenly opens itself.")
        print_pause2("More glowing runes fill the page.")
        print_pause2(f"You look to the {cave_figure} for some sort of answer.")
        print_pause2("With the same smile, the figure raises its hands,")
        print_pause2("making the book float.")
        print_pause2("Instinct tells you to open your arms the same way.")
        print_pause2("The book floats to you, resting in your hands.")
        print_pause2("Although the book looks heavy, it is feather-light.")
        print_pause2("You don't feel confusion anymore.")
        print_pause2("Instead, you feel calm and peace.")
        print_pause2("Congratulations, you found the Ancient Book!")
        print_pause2(f"Looking back to the {cave_figure},")
        print_pause2("they continue smiling, nod, and vanish.")
        print_pause2("You close the book and hold it tightly.")
        print_pause2("As soon as you close the book, the shrine, lights,")
        print_pause2("and warmth all disappear.")
        print_pause2("You find yourself at the entrance of the cave.")
        inventory.clear()
        inventory.append("Ancient Book")
        field_again(name, inventory, cabin_figure, cave_figure)


# -------- RETRY-RESPONSE/PLAY AGAIN/PLAY GAME ------------
def play_again():
    again = input("Would you like to play again? Please type yes or no\n")
    if again.lower() == "yes":
        print_pause2("Restarting your adventure!")
        print_pause2("3")
        print_pause2("2")
        print_pause2("1")
        play_game()
    if again.lower() == "no":
        print_pause2("Thank you for playing!")
        exit()
    else:
        print_pause2("I'm sorry, I didn't understand that.")
        print_pause2("Could you please retype that?")
        return play_again()


if __name__ == '__main__':
    play_game()

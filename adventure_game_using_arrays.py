
import random
import time


def print_pause():
	print()
	time.sleep(2)


def play_game():
	character = []
	inventory = []
	dark_option = random.choice(["Black-robed figure", "Tuxedo-wearing thin figure with monocole and top hat", "Devilish imp with spiraling horns"])
	light_option = random.choice(["White-robed figure", "Angelic woman with gold-lined dress with the same symbols written across it."])
	inventory_options = random.choice(["dwindling torch", "rusted, dull knife", "cracked bow", "empty canteen"])
	inventory.append(inventory_options)
	character_creation(character, inventory, dark_option, light_option)
	prologue(character, inventory, dark_option, light_option)


def character_creation(character, inventory, dark_option, light_option):
	name = input("Adventurer, please tell me your name.\n")
	print_pause(f"You typed {name}. Is that ok?")
	confirm = input("Please type yes to continue or no to change.\n")
	if confirm.lower() == "yes":
		print_pause3("Welcome to your adventure, " + name + "!")
		print_pause2("Make sure to have your trusty " + inventory[0] + " ready!")
		character.append(name)
		character.append(inventory)
		print(character)
		prologue(character, inventory, dark_option, light_option)
	if confirm.lower() == "no":
		character_creation(character, inventory, dark_option, light_option)
	else:
		print_pause("Sorry, I didn't catch that.")
		character_creation(character, inventory, dark_option, light_option)


def prologue(character, inventory, dark_option, light_option):
	#choice: cabin or cave first
	print_pause2("Coming to the edge of the forest after hours of walking,")
	print_pause2("Your " + inventory[0] + " in one hand,")
	print_pause2("You pause to survey your new surroundings, resting against an oddly shaped tree.")
	print_pause2("A large field infront of you stretches as far as you can see beyond the horizon.")
	print_pause2("There are two distinct features in this field, illuminated by the moonlight:")
	print_pause2("a cabin, its lights all on and smoke pouring from the chimney,")
	print_pause2("sits a fair distance to your left, a fence surrounding the property.")
	print_pause2("To your right, even further in the distance,")
	print_pause2("rolling hills line the horizon, the tops of the rocks reflecting the moonlight.")
	print_pause2("You think you see an entrance to a cave, with very feint shimmers of light.")
	print_pause2("The cold night air hurries your decision making:")
	print_pause2("With only " + inventory[0] + " in hand, you realize you don't have much hope on your own.")
	print_pause("Do you head to the cabin? Or do you explore the cave?")
	prologue_choice = input("Please type cabin or cave for your choice:\n")
	if prologue_choice.lower() == "cabin":
		cabin(character, inventory, dark_option, light_option)
	if prologue_choice.lower() == "cave":
		cave(character, inventory, dark_option, light_option)
	else:
		print_pause("I'm sorry, I didn't understand that.\n")
		return prologue_choice

# def field(character, inventory, dark_option, light_option,):


def cabin(character, inventory, dark_option, light_option):
	print_pause("Walking to the cabin, a cold breeze pierces your body")
	print_pause("You hurry your pace.")
	# print_pause("The lights inside the cabin beam out")
	# print_pause("as a beacon to any lost, cold, and hungry adventurers.")
	# print_pause("The closer you get, the more you notice:")
	# print_pause("The smell of a homecooked meal fills your nostrils,")
	# print_pause("laughter of children surrounds your senses,")
	# print_pause("and the warmth eminating from the fire warms your soul.")
	# print_pause("You put a hand on the fence gate,")

	#HAS ANCIENT BOOK
	if "Ancient Book" in inventory:
		print_pause("you feel confident that you have found home.")
		print_pause("Do you open the gate to knock on the front door?")
		enter_cabin = input("Type 'knock' to enter or 'leave' to go back to the field.")
		if enter_cabin == "knock":
			print_pause("You open the gate and walk towards the front door, {inventory[0]} in hand.")
			print_pause("The instant you knock...")
			print_pause("the lights extinguish...")
			print_pause("")
			print_pause("")
			print_pause("")
			print_pause("")
			print_pause("")
			play_again()

	#NO ANCIENT BOOK
	else:
		print_pause("but you can't help but wonder what was in the cave you saw earlier.")
		print_pause("You look at your {inventory[0]} and become more worried.")
		enter_cabin = input("Type 'knock' to enter or 'leave' to go back to the field.")
		if enter_cabin == "knock":
			print_pause("you go to the cabin without the book!")
			play_again()


def cave(character, inventory, dark_option, light_option):
	print_pause("You drop your " + inventory[0] + " and pick up the Ancient Book")
	inventory.clear()
	inventory.append("Ancient Book")
	print_pause3(inventory)
	prologue(character, inventory, dark_option, light_option)

def play_again():
	again = input("Would you like to play again? (Y/N)")
	if again.lower() == "y":
		print_pause("Restarting your adventure")
		play_game()
	if again.lower() == "n":
		print_pause("Thank you for playing!")


play_game()

import sys
import random

import entity

def usage():
	print("Commands:\n\
	- play <entity> [<nb_ice>]\n\
	- shuffle <entity>\n\
	- reboot <entity>\n\
	- check <entity>\n\
	- kill <entity>\n\
	- cancel\n\
	- exit")

def expect_inputs(inputs, nb_inputs):
	if len(inputs) < nb_inputs+1:
		usage()
		return


# Returns None if the entity is not found
def retrieve_entity(ent_name):
	all_names = entity.all_entity_names()
	candidates = [] # Names starting with ent_name
	for name in all_names:
		if name == ent_name: # Found!
			ent = entity.Entity.from_name(ent_name)
			return ent
		elif ent_name in name:
			candidates.append(name)
	print(f"Entity {ent_name} not found. Did you mean one of the following?")
	print("  " + "  ".join(candidates))
	return None


def play(inputs):

	expect_inputs(inputs, 1)
	
	# Creating entity
	ent = retrieve_entity(inputs[1].lower())
	if ent == None: return
	
	# Dumping to cancel file
	ent.to_file("cancel.txt")
	
	# Ice
	if len(inputs) >= 3:
		try:
			ice_nb = int(inputs[2])
			print(f"{ent.name} is supposed to play {ent.nb_actions} actions, but is subject to {ice_nb} ice")
		except ValueError:
			usage()
			return
	else: ice_nb = 0
	
	# Nb actions
	if ent.nb_actions - ice_nb < 1:
		print(f"{ent.name} resisted to {1 - (ent.nb_actions - ice_nb)} ice")
		nb_played = 1
	else:
		nb_played = ent.nb_actions - ice_nb
	
	# Playing
	print(f"Playing {nb_played} actions with entity {ent.name}...", end="")
	played = ent.play(nb_played)
	print(" Done")
	print("Cards played:")
	for card in played:
		print(f"\t- {card}")
	
	# Update entity file
	ent.update_file()


def shuffle(inputs):

	expect_inputs(inputs, 1)
	
	# Creating entity
	ent = retrieve_entity(inputs[1].lower())
	if ent == None: return

	# Dumping to cancel file
	ent.to_file("cancel.txt")
	
	# Shuffling
	print(f"Shuffling {ent.name}'s deck only...", end="")
	random.shuffle(ent.deck)
	print(" Done")
	print(ent)
	
	# Update entity file
	ent.update_file()


def reboot(inputs):

	expect_inputs(inputs, 1)
	
	# Creating entity
	ent = retrieve_entity(inputs[1].lower())
	if ent == None: return

	# Dumping to cancel file
	ent.to_file("cancel.txt")
	
	# Rebooting
	print(f"Rebooting entity {ent.name}...", end="")
	ent.reboot()
	print(" Done")
	
	# Update entity file
	ent.update_file()


def kill(inputs):

	expect_inputs(inputs, 1)
	
	# Creating entity
	ent = retrieve_entity(inputs[1].lower())
	if ent == None: return

	# Dumping to cancel file
	ent.to_file("cancel.txt")
	
	print(f"After being killed, entity {ent.name} dropped {ent.drop}.")


def check(inputs):

	expect_inputs(inputs, 1)
	
	# Creating entity
	ent = retrieve_entity(inputs[1].lower())
	if ent == None: return
	
	print(f"State of entity {ent.name}:")
	print(ent)
	


def cancel():
	
	# Retrieving entity 
	try: ent = entity.Entity.from_file("cancel.txt")
	except:
		print("Error: nothing to cancel")
		return
	
	print(f"Cancelling the last move (for entity {ent.name})...", end="")
	ent.update_file()
	print(" Done")
	
	


if __name__ == "__main__":

	print("### Le JDR - play ###")
	while True:
		
		sinput = input(" > ")
		inputs = sinput.split(" ")
		
		if inputs[0] == "play":
			play(inputs)
		elif inputs[0] == "shuffle":
			shuffle(inputs)
		elif inputs[0] == "reboot":
			reboot(inputs)
		elif inputs[0] == "kill":
			kill(inputs)
		elif inputs[0] == "check":
			check(inputs)
		elif inputs[0] == "cancel":
			cancel()
		elif inputs[0] == "exit":
			print("Exiting...")
			exit(0)
		else:
			usage()
			continue
		print()
			

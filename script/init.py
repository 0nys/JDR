import random
import sys, os

import entity, util

def create_params(entities_base_name):
	with open("params.txt", "w") as fparam:
		fparam.write(entities_base_name)


def parse_cards(scards, ch1=",", ch2=":"):
	scard_types = scards.split(ch1)
	cards = []
	for scard_type in scard_types:
		if ":" in scard_type:
			card, nb = scard_type.split(ch2)
			cards += [card]*int(nb)
		else: cards.append(scard_type)
	random.shuffle(cards)
	return cards

def parse_global_entities_file(fname_global_entities, dirname_output):
	with open(fname_global_entities, "r") as fent:
		lines = util.clean_lines(fent)
		for line in lines: # for each entity
			name, nb_actions, drop, scards = line.split(";")
			cards = parse_cards(scards)
			ent = entity.Entity(name, int(nb_actions), drop, cards, [])
			ent.to_file(f"{dirname_output}{name}")


if __name__ == "__main__":

	if len(sys.argv) < 2:
		print(f"Usage: python3 {sys.argv[0]} <entities_base_name>")
		exit(1)
	
	entities_base_name = sys.argv[1]
	fname_global_entities = entities_base_name + ".txt"
	dirname_output = entities_base_name + "/"
	if not os.path.exists(dirname_output):
		os.makedirs(dirname_output)
	
	print(f"Entities from {fname_global_entities} will be initialised in {dirname_output}")
	
	print("- Create parameters...")
	create_params(entities_base_name)
	
	print("- Create/reset cancel buffer file...")
	with open("cancel.txt", "w") as fcan:
		pass
	
	print("- Initialise entities...")
	parse_global_entities_file(fname_global_entities, dirname_output)
	
	print("... Done")

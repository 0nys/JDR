import random

import util

class Entity:

	def __init__(self, name=None, nb_actions=None, drop=None, deck=None, discard=None):
		self.name = name
		self.nb_actions = nb_actions
		self.drop = drop
		self.deck = deck
		self.discard = discard
	
	@classmethod
	def from_file(cls, fname):
		ent = cls()
		with open(fname, "r") as fent:
			lines = util.clean_lines(fent)
			ent.name = lines[1]
			ent.nb_actions = int(lines[3])
			ent.drop = lines[5]
			
			# Create deck
			ent.deck = []
			i = 7
			while not lines[i][0].startswith("#"):
				ent.deck.append(lines[i])
				i += 1
				
			# Create discard
			ent.discard = lines[i+1:]
			
		return ent
	
	@classmethod
	def from_name(cls, ent_name):
		with open("params.txt", "r") as fparams:
			entities_base_name = fparams.read()
		ent_fname = f"{entities_base_name}/{ent_name}"
		ent = cls.from_file(ent_fname)
		return ent
	
	def to_file(self, fname):
		with open(fname, "w") as fent:
			fent.write(f"# Name\n{self.name}\n")
			fent.write(f"# Nb actions\n{self.nb_actions}\n")
			fent.write(f"# Drop\n{self.drop}\n")
			fent.write("# Deck\n")
			if self.deck != []: fent.write('\n'.join(self.deck) + "\n")
			fent.write("# Discard\n")
			if self.discard != []: fent.write('\n'.join(self.discard) + "\n")
	
	def play(self, nb_played):
		if nb_played <= len(self.deck):
			played = self.deck[:nb_played]
			self.deck = self.deck[nb_played:]
			self.discard = self.discard + played
			return played
		else: # Have to reshuffle at some point
			first_played = self.play(len(self.deck)) # play the last cards
			assert self.deck == []
			self.reboot()
			return first_played + self.play(nb_played - len(first_played))
	
	def update_file(self):
		with open("params.txt", "r") as fparams:
			entities_base_name = fparams.read()
		ent_fname = f"{entities_base_name}/{self.name}"
		self.to_file(ent_fname)
	
	def reboot(self):
		cards = self.deck + self.discard
		random.shuffle(cards)
		self.deck = cards
		self.discard = []
		
	
	def __str__(self):
		return f"\
Name:       {self.name}\n\
Nb_actions: {self.nb_actions}\n\
Drop:       {self.drop}\n\
Deck:       {self.deck}\n\
Discard:    {self.discard}"
		

def all_entity_names():
	with open("params.txt", "r") as fparams:
		entities_base_name = fparams.read()
	names = []
	with open(f"{entities_base_name}.txt", "r") as fglobal:
		lines = util.clean_lines(fglobal)
		for line in lines: # for each entity
			name, nb_actions, drop, scards = line.split(";")
			names.append(name)
	return names

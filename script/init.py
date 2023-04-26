import random
import sys, os

def create_params(dirname_output):
	with open("params.txt", "w") as fparam:
		fparam.write(dirname_output + "\n")

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print(f"Usage: python3 {sys.argv[0]} <entities_filepath> <output_dirpath>")
		exit(1)
	
	fname_entities = sys.argv[1]
	dirname_output = sys.argv[2]
	if dirname_output[-1] != "/": dirname_output += "/"
	if not os.path.exists(dirname_output):
		os.makedirs(dirname_output)
		
	create_params(dirname_output)
	
	with open(fname_entities, "r") as fent:
		lines = [line[:-1] for line in fent.readlines()]
		for line in lines:
			name, nb_actions, scards = line.split(";")
			cards = scards.split(",")
			with open(f"{dirname_output}{name}", "w") as fentity:
				fentity.write("test ok")

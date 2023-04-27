def clean_lines(f):
	lines = f.readlines()
	for i in range(len(lines)):
		if lines[i].endswith("\n"): lines[i] = lines[i][:-1]
	return lines

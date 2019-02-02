def read_files(path):
	words = []
	with open(path) as wordFile:
		for line in wordFile:
			line = line.strip()
			words.append(line)
	return words



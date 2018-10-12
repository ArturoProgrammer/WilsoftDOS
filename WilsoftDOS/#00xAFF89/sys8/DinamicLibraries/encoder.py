def main (flibname):
	file = open(flibname, 'r')
	print(file.read().replace(' ', '|'))
	newfile = open('new' + flibname, 'w')
	newfile.write()

	newfile.close()
	file.close()
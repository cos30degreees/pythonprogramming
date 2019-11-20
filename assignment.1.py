
# get the name of the file and open it
name = input('enter file name:')
handle = open(name, 'r')

#  cpimt word frequency
counts = dict()
for line in handle:
	words = line.split()
		for word in words:
			counts(word) = counts.get(word,0) + 1

#  find most common word

bigcount = None
bigword = None
for word,count in counts.items() 

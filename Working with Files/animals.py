with open('textfile.txt', 'r') as f:
    for line in f:
    	# end="" is to prevent python from adding a new line and just print what is being read from the file
        print(line, end='')

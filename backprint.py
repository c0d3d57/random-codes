# A simple function to print anything backwords

import sys

# Here we authomatically recall the function anytime a job is done.
def redo():
	mes()

# Main workflow
def mes():
	message = raw_input('Enter word > ')
	# Type exit to opt out of the program
	if "exit" in message:
		sys.exit()
	
	translated = ''
	trans = []

	i = len(message) - 1
	while i >= 0:
		translated = translated + message[i]
		i = i - 1
		# We store our outputs in a list in order not to get a wrong result.
		trans.append(translated)
	
	print(translated)
	redo()	

# Call the main function
mes()

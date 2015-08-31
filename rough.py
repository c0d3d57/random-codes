from time import sleep

year = 2014
myyear = raw_input("Enter your birth year: ")
total_year = int(year) % int(myyear)

if total_year < 18:
	print "You are not eligible to use this program!"

else:
	print "You will be " + str(total_year) + " in year " + str(year)
	print "\nYou are eligible to play this game, you will be redirected to the next round automatically."


def nigeria_yes():
	print "I never knew i had a brother from around here."

def africa_yes():
	print "I am more pleased to meet you."
	sleep(2)
	print "My name is Evans from Nigeria."
	country = raw_input("Where in Africa did you hail from? ")
	country = country.lower()
	if country == "nigeria":
		nigeria_yes()
	else:
		print "Yes fine!"

def asia_yes():
	print "I thought as much,\nI'm pleased to meet you, my name is Evans."

def main():
	print "You have less than four digit name,\nyou must be from asia.\n"
	asia_name = raw_input("Are you? ")
	asia_name = asia_name.lower()
	if asia_name == "yea" or asia_name == "yes" or asia_name == "ya":
		asia_yes()
	else:
		print "Oh sorry about that."
		location = raw_input("Where are you from? ")
		location = location.lower()
	if location == "africa":
		africa_yes()
	else:
		print "Okay Got it, Goodbye!"


name = raw_input("What is your name? ")

if len(name) < 4:
	main()
else:
	print "Nice Name, you are welcome."

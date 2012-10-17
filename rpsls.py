import random

#dictionary of numbers and plays
dict = {
        0:"rock",
        1:"Spock",
        2:"paper",
        3:"lizard",
        4:"scissors"
       }
#return the name for the given number
def number_to_name(number):
    return dict[number]


#for every item in the dictionary check to see if given name is equal
#if so, return number of given name
def name_to_number(name):
    for number, dictname in dict.items():
        print number, dictname
	if dictname == name:
            return number
        
# This function determines if the computer chose the same as player.
# We should not allow these plays. This function checks to see if 
# the computer chooses the same as the player and recalculates.
def computer_choice(player_number):
    comp_number = random.randrange(5)
    while comp_number == player_number:
        comp_number = random.randrange(5)
    return comp_number

def rpsls(number): 
    #convert player number to name
    player_number = number
    #send player number to computer_choice function, check for equality
    #then play if not equal
    comp_number = computer_choice(player_number)
    #convert player number to name
    player_name = number_to_name(player_number)
    #convert comp number to name
    
    comp_name = number_to_name(comp_number)
    #game equals computed difference modulo 5
    game = (player_number - comp_number) % 5
    
    print "Player chooses %s" % (player_name)
    print "Computer chooses %s" % (comp_name)
    
    if game <= 2:
        print "Player Wins!"
    elif game > 2:
        print "Computer Wins!"

def process_input(player_input):
    isValid = False
    try:
	int(player_input)
	if int(player_input) < 5:
        	isValid = True
    except ValueError:
	pass
    return isValid
    
def main():
    print "Rock, Paper, Scissors, Lizard, Spock!"
    print "------------------------------------"
    for number, name in dict.items():
	print str(number) + " for " + str(name.title())
    player_input = raw_input("Your choice>")
    while not process_input(player_input):
	print "Invalid input. Entries must be 0-4."
        player_input = raw_input("Your choice>")
    rpsls(int(player_input))


if __name__=='__main__':
    main()





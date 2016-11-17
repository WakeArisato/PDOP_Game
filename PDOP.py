def PDOP():
	'''Starts the Prisoner's Dilemma One Player game'''
	def Else():
		print ("Wait... what did you just say? ok, i'm not even going to let you choose")
		print ("You're going away for a long time buddy")
		exit()
	import random
	from sys import exit
	PartnerAnswer = random.randint(0,1)
	global FinalAnswer
	FinalAnswer = 0
	global GManAnswer
	GManAnswer = 0
	global YourAnswer
	YourAnswer = 0
	print ("You wake up in a dark room")
	print ("what do you do?")
	answer = raw_input("Do nothing or look around:")
	if answer == 'Do nothing' or answer == 'do nothing':
		print ("You continue just sitting there... how thrilling...")
		exit()
	if answer == 'look around' or answer == 'Look around':
		print ("it turns out that you actually have a bag on your head!")
		print ("You attepmt to remove the sack off but it appears your hands are restrained.")
		print ("What would you like to do?")
		answer = raw_input("Do nothing or Do nothing:")
		if answer == 'Do nothing' or answer == 'do nothing':
			print ("You just sit there doin nothing... how thrilling.")
			answer = raw_input("Do nothing or Do nothing:")
			if answer == 'Do nothing' or answer == 'do nothing':
				print ("You just sit there doin nothing... how thrilling.")
				print ("what would you like to do?")
				answer = raw_input("Do nothing or Do nothing")
				if answer == 'Do nothing' or answer == 'do nothing':
					print ("You continue to just sit there doing noth-")
					print ("Light starts to flash through the holes in the bag.")
					print ("But before you can say anything the bag is ripped from off your head")
					print ("the light is too bright for you to be able to open your eyes.")
					print ("what would you like to do?")
					answer = raw_input("Open your eyes or Do nothing?")
					if answer == 'open your eyes' or answer == 'Open your eyes':
						print ("What did i just tell you, you cant open your eyes.")
						print ("but i respect your enthusiasm.")
						print ("Eventually your eyes get used to the light of the room and you are able to see")
						print ("What would you like to do")
						answer = raw_input("Look around or Do nothing")
						def Game_Start():
							def Game_Final():
								if YourAnswer == 1 and PartnerAnswer == 1:
									print ("So you both Deny?")
									print ("Well, thats a shame.")
									print ("You're both going away for two years.")
									exit()
								if YourAnswer == 1 and PartnerAnswer == 0:
									print ("So you're throwing your parnter under the buss?")
									print ("Well, you'll atleast be able to see him in three years.")
									exit()
								if YourAnswer == 0 and PartnerAnswer == 0:
									print ("So you both confess.")
									print ("Atleast you two might get a cell together.")
									exit()
								if YourAnswer == 0 and PartnerAnswer == 1:
									print ("It appears that your partner thew you under the buss...")
									print ("Shame... a darn shame...")
									print ("Atleast you'll be able to see him in three years.")
									exit()
								GManAnswer = random.randint(0,1)
								if GManAnswer == PartnerAnswer:
									FinalAnswer = str("Denied")
								if GManAnswer != PartnerAnswer:
									FinalAnswer = str("Confessed")
							print ("Ok, buddy, you know why you're here.")
							print ("You got caught and there is no way around it.")
							print ("This conversation is currently being recorded both vith video and audio")
							print ("Anything you say here can and will be used against you.")
							print ("In these two folders are 9 by 11 inch peices of paper.")
							print ("One of them says confess.")
							print ("While the other one says deny.")
							print ("Your partner has already chosen an answer.")
							print ("If you both choose deny, then you both confess, you both will have to serve two years.")
							print ("But if you both confess to the crim, you both will only have to serve one year.")
							print ("But if one of you choose confess while the other one denies, the one who confesses will have to serve three years.")
							print ("It's a simple choice.")
							print ("Now, i will tell you that your parter"), FinalAnswer
							print ("Now it's your turn to choose.")
							print ("Do you Confess or Deny?")
							answer = raw_input("Confess or Deny")
							if answer == 'Confess' or answer == 'confess':
								YourAnswer == YourAnswer + 0
								print ("So you Confess...")
								Game_Final()
						if answer == 'Look around' or answer == 'look around':
							print ("You're sitting in a room with nothing up on the walls")
							print ("There is a metalic door on the far left side of the room with no lightswitch in sight")
							print ("You're sittin in a metalic chair with a drab metalic table infront of you.")
							print ("there are two tan folders infront of you.")
							print ("A man with a black suit, sunglasses, and a blue tie on.")
							print ("he walks over and stands on the other side of the table.")
							Game_Start()
						if answer == 'Do nothing' or answer == 'do nothing':
							print ("You just sit there with your eyes closed...")
							print ("How thrilling....")
							print ("Eventually you hear a door open and footsteps walk out infront of you.")
							print ("You hear him say: Open your eyes idiot.")
							Game_Start()
						else:
							Else()
					else:
						Else()
				else:
					Else()
			else:
				Else()
		else:
			Else()
	else:
		Else()
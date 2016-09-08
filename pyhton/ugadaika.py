from random import randint
ch = randint (1,5)
play = True;
while play:
	print "ugaday chislo"
	answer = raw_input("> ")
	if int(answer) == ch:
		print "ti ugadal"
		play = False
	else:
		print "ne ugadal poprobuy eshe"
		if int(answer) < ch:				
			print "vvedennoe chislo menshe togo chto zagadano"
		else:
			print "vvedennoe chislo bolshe togo chto zagadano"

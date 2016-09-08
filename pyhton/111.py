n = 0
summ = 0
while n <= 100:
	ost = n % 2
	if ost == 0:
		summ = summ + n
		print "======" + str(n)
		print summ

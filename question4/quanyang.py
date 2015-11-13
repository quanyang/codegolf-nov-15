def q():
	for x in range(26)+range(25)[::-1]:
		a=list(chr(97+i) for i in range(26))
		a[x]=chr(ord(a[x])-32)
		print ''.join(a)

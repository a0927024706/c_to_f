x = input('請輸入攝氏(c)華氏(f): \n' )
if x == 'c':
	c = input('請輸入攝氏: ')
	c = float(c)
	f = c * 9 / 5 + 32
	print ('華氏為:', f)
else:
	f = input('請輸入華氏: \n')
	f = float(f)
	c = (f - 32) /9 * 5
	print ('攝氏為:', c)

print "no. o' Z's"
x = raw_input('number> ')
x = int(x)
f = open('zzz.txt', 'w')
for i in range(x):
	f.write('z' + ' '*i)

dataarr=[]
with open('enjoysport.csv', "r") as f:
    for line in f:
    	dataarr.append(line.strip().split(','))
	
rows = len(dataarr)
cols = len(dataarr[0])
h = ['0','0','0','0','0','0']
for i in range(1,rows):
	t = dataarr[i]
	if t[cols - 1] == '1':
		for a in range(0, cols-1):
			if h[a] == t[a]:
				continue
			h[a] = '?' if h[a] != '0' else t[a]
		print(h)
print("Maximally specific Set")
print('<', end = " ")
for i in range(0,len(h)):
	print(h[i], end = " ")
	if i != len(h) -1:
		print(",", end = " ")
print(">")
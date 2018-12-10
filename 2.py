dataarr=[]
with open('enjoysport.csv', "r") as f:
    for line in f:
        dataarr.append(line.strip().split(','))

rows = len(dataarr)
cols = len(dataarr[0])
shypo = ['0']*(cols-1)
ghypo = [['?']*(cols-1)]
print("Initial S[0] = ",shypo)
print("Initial G[0] = ",ghypo)


for i in range(1, rows):
    print("\nFor Training example ",i)
    t = dataarr[i]
    if t[cols-1] == "1":
        for a in range(0, cols-1):
            if shypo[a] == t[a]:
                continue
            shypo[a] = '?' if shypo[a] != '0' else t[a]
            for g in ghypo:
                if g[a] != '?' and shypo[a] == '?':
                    ghypo.remove(g)

    elif t[cols-1] == "0":
        ghypo.clear()
        for a in range(0, cols-1):
            if t[a] != shypo[a] and shypo[a] != '?':
                temp_list = ['?']*a + [shypo[a]] + (['?']*(cols-2-a ))
                if temp_list not in ghypo:
                    ghypo.append(temp_list)

    print("S[{}] = {}".format(i,shypo))
    print("G[{}] = {}".format(i,ghypo))
print("\nFinal SHypothesis ", shypo)
print("Final GHypothesis ", ghypo)
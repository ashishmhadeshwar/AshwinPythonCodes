def CalcDiceRoll(nrolls,numlist):
    import random
    counter=0
    for a in range(0,nrolls):   
        r=random.randint(1,6)
        if r in numlist:
            counter=counter+1
    PctRolls = (counter/nrolls)*100
    return PctRolls
        
nrolls=100000
numlist = []
print(CalcDiceRoll(nrolls,numlist))




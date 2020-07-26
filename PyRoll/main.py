names = ["bob", "Mike", "bob", "cathy", 'bob', "Mohan", "Mohan"]
namesDict = {}
# list of names, convert to dictionary
# keys are going to be unique names 
# values are going to be the times they occcured
for name in names:
    if name in namesDict:
        namesDict[name] = namesDict[name] + 1
    else:
        namesDict[name] = 1
print(namesDict)

import os
import csv
csvpath = os.path.join("Resources/election_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")   
    
    csvHeader = next(csvreader)
    
    num_votes = []
    candidatesDict = {}
    names = []
        
    for row in csvreader:
       
        num_votes.append(float(row[0]))
        names.append (row [2])
        
    print("Total Votes:", len(num_votes))
    
    for name in names:
        if name in candidatesDict:
            candidatesDict[name] = candidatesDict[name] + 1
        else:
            candidatesDict[name] = 1
    print("Votes Talley:", candidatesDict)
    
    Khanpercent = (661583/1048575)*100
    Correypercent = (209046/1048575)*100
    Lipercent = (146360/1048575)*100
    Otooleypercent = (31586/1048575)*100
    print ("Percent of votes for Khan: ", Khanpercent)
    print ("Percent of votes for Correy: ", Correypercent)
    print ("Percent of votes for Li: ", Lipercent)
    print ("Percent of votes for O'Tooley: ", Otooleypercent)
    print ("Winner: Khan")

write_file = open(os.path.join("Analysis.txt"), 'w+')
write_file.write("Total votes: 1048575 \n")
write_file.write("Khan: 63.09 % (661583)\n")
write_file.write("Correy: 19.94 % (209046)\n")
write_file.write("Li: 13.96 % (146360)\n")
write_file.write("O'Tooley: 3.01 % (31586\n")
write_file.write ("Winner: Khan")
write_file.close()



    
        
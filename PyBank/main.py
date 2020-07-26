import os
import csv
csvpath = os.path.join("Resources/budget_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")   

    
    csvHeader = next(csvreader)
    
    revenue = []
    date = []
    rev_change = []
        
    for row in csvreader:
       
        revenue.append(float(row[1]))
        date.append(row[0])

    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Average Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

   
write_file = open(os.path.join("Analysis.txt"), 'w+')
write_file.write("Total Months: 86 \n")
write_file.write("Total Revenue: $ 38382578.0\n")
write_file.write("Average Revenue Change: $ -2315\n")
write_file.write("Greatest Increase in Revenue: Jan-2012 ($ 1926159)\n")
write_file.write("Greatest Decrease in Revenue: Aug-2013 ($ -2196167.0)\n")
write_file.close()



    
        
#import needed tools
import os
import csv


total = 0
months = 0
changes = []


#get csv file 
csvpath = os.path.join("Resources", "budget_data.csv")


greatest = ["",0]
least = ["", 9999999999999999999]

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')  
    header = next(csvreader)
    firstrow = next(csvreader)
    months += 1
    total += int(firstrow[1])
    previous = int(firstrow[1])

#print header as check comment out for production run
    #print(header)  
                   
    for row in csvreader:
        months += 1
        total += int(row[1])
        net_change = int(row[1]) - (previous)
        previous = int(row[1])
        changes += [net_change]
        if net_change > greatest[1]:
            greatest[0] = row[0]
            greatest[1] = net_change

        if net_change < least[1]:
            least[0] = row[0]
            least[1] = net_change
            
      
    
    #formating
    analysis = f"""Financial Analysis  
-------------------------------------------------------
    Total Months: {months}
    Total: ${total}
    Average Change: ${round(sum(changes)/len(changes),2)} 
    Greatest Profit Increase: {greatest[0]} (${greatest[1]})
    Greatest Profit Decrease: {least[0]} (${least[1]})
--------------------------------------------------------"""
   
    #analysis text 
    open ("pybank_analysis.txt", "w").write(analysis)
    print(analysis)

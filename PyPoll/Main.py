# PYPOLL
#import needed tools
import os
import csv

# Set Values & pull CSV
candidates = {}
csvpath = os.path.join('Resources','election_data.csv')


#another option 
#with open(csvpath, 'r') as csvfile:

#csvfile reading
with open(csvpath) as csvfile:

    # set delimiter and variable
    csvreader =csv.reader(csvfile,delimiter=',')
    #header row
    header = next(csvreader)
   
   # below is a check to make sure csv file is working in script remove for production
    #print(header)

   # take vote totals using length
    vote_totals = len(candidates)


#start loop for candiate counts 
    for row in csvreader:
        if row [2] in candidates:
            candidates[row[2]] +=1
        else: 
            candidates[row[2]] = 1    

      
        
#formatting and analysis

analysis = "Election Results\n--------------------------------\n"
analysis += f"""--------------------------------
Total Votes = {sum(candidates.values())}
---------------------------------------\n"""

for name in candidates:
    votes = candidates.get(name)
    pct = float(votes) / float(sum(candidates.values())) * 100
    candidate_results=(f"{name}: {pct:.3f}% ({votes})\n" )
    analysis += candidate_results

analysis+= f"""---------------------------------------
Winner: {max(candidates, key = candidates.get)} 
---------------------------------------"""
open("pypoll_analysis.txt", "w").write(analysis)
print(analysis)












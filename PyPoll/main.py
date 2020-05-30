file = '/Users/Maury/Documents/GitHub/Python-challenge/PyPoll/Resources/election_data.csv'

import os
import csv
import collections

with open(file, 'r', newline='') as csvtext:
    csvtext= csv.reader(csvtext, delimiter = ',')
    print(csvtext)
    election_list = csvtext.read()
    
#declare variables to store data
total_votes = 0
candidates = []
percent_won = 0
candidate_total_won = []
winner = []

#start loop
for row in election_list:
    next.reader
    total_votes = len(election_list)
    candidate_list = set(field.strip().lower() for field in row[2])
    candidate_list = item[row[0]].append(row[1]) # way 2
    for item in candidate_list:
            if item not in candidates:
                candidates.append(item)
    for k, v in candidate_list.items(): #way 2
        print(k)
    candidate_total_won = Counter(v)

print(f"Total votes: " {total_votes})
print(f"Candidates: " {candidates})
print(f"{candidates[0]})


with open(analyzed_election_list, "w") as txt_file:
    txt_file.write(Analysis/Analyzed_election_list.txt)
import os
import csv
from pathlib import Path
from statistics import mode


input_file = Path("Resources","election_data.csv")

#declare variables to store data
total_votes = []
khan = 0
correy = 0
li = 0
o_tooley = 0
percent_khan= 0 
percent_li= 0 
percent_correy= 0 
percent_otoole = 0 
candidates = []
candidate_list = []
#start loop
with open(input_file, 'r', newline='')as csvfile:
    csvreader= csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

#start loop
    for row in csvreader:
        total_votes.append(row[0])
        candidate_list.append(row[2])
               
        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            o_tooley +=1
    for item in candidates:
            if item not in candidate_list:
                candidates.append(row[2])

    percent_khan = round((khan / (len(total_votes)))* 100)
    percent_li = round((li / (len(total_votes))) * 100)
    percent_correy = round((correy / (len(total_votes))) * 100)
    percent_otoole = round((o_tooley / (len(total_votes))) * 100)

def most_common(candidate_list): 
    return(mode(candidate_list)) 

print(f"Total votes: {len(total_votes)}\n ---------------")
print(f"votes Khan:{khan} {percent_khan}% \n")
print(f"votes Correy: {correy} {percent_correy}%\n")
print(f"votes li: {li} {percent_li}%\n ")
print(f"votes O'Tooley: {o_tooley} {percent_otoole}%\n")
print(f"Winner : {mode(candidate_list)} \n")

output_file = Path("..","PyPoll", "Analysis","Analyzed_election_list.txt")

with open(output_file, "w") as txt_file:
    txt_file.write(f"Total votes {len(total_votes)}\n-----------------")
    txt_file.write(f"Votes for Khan {khan} Percent of votes: {percent_khan}% \n")
    txt_file.write(f"Votes for Correy {correy} Percent of votes: {percent_correy}%\n")
    txt_file.write(f"Votes for Li {li} Percent of votes: {percent_li}%  \n")
    txt_file.write(f"votes for O'Tooley {o_tooley} Percent of votes: {percent_otoole}%\n")
    txt_file.write(f"Winner : {mode(candidate_list)} \n")
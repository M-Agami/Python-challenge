import os
import csv
import pathlib

input_file = Path("..","Resources","election_data.csv")

#declare variables to store data
total_votes = 0
khan = 0
correy = 0
li = 0
o_tooley = 0
percent_won = 0

#start loop
with open(input_file, 'r', newline='', encoding = utf8) as csvtext:
    csvtext= csv.reader(csvtext, delimiter = ',')
    election_list = csvtext.read()
    next.election_list

#start loop
for row in election_list:
    total_votes = len(election_list)
    for item in candidate_list:
            if item not in candidates:
                candidates.append(row[2])
                
if row[2] == "Khan": 
        khan +=1
    elif row[2] == "Correy":
        correy +=1
    elif row[2] == "Li": 
        li +=1
    elif row[2] == "O'Tooley":
        o_tooley +=1

print(f"Total votes: {total_votes}\n ---------------")
print(f"votes Khan:{khan}\n Percent of votes: {khan / total_votes * 100}% \n ")
print(f"votes Correy: {correy}\n Percent of votes: {correy / total_votes * 100}% \n")
print(f"votes li: {li}\n Percent of votes: {li / total_votes * 100}% \n")
print(f"votes O'Tooley: {o_tooley}\n Percent of votes: {o_tooley / total_votes * 100}% \n)

output_file = Path("python-challenge", "PyPoll", "Analyzed_election_list.txt")
Analyzed_election_list = output_file
with open(Analyzed_election_list, "w") as txt_file:
    txt_file.write(f'Total votes {total_votes} \n')
    txt_file.write(f'Votes for Khan {khan}')
    txt_file.write(f'Votes for Correy {correy}\n')
    txt_file.write(f'Votes for Li {li} \n')
    txt_file.write(f"votes for O'Tooley {o_tooley}\n")
    txt_file.write(f'Percent of votes won 
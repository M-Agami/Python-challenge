import os
import csv
from pathlib import Path

input_file = Path("..","PyBank","Resources","budget_data.csv")

    #declare variables used to store data
total_months = 0
net_total = 0
monthly_change = 0
greatest_inc = 0
greatest_dec = 0

with open(input_file, 'r', newline= '',encoding="utf-8") as csvtext:
    csvreader = csv.reader(csvtext, delimiter = ',')
    print(csvtext)
    header = next(csvreader)       #this will skip the headers in the first row
    row = next(csvreader)       #1st row will be after header
    #declare variables used to store data
    total_months = []
    net_total = int()
    monthly_change = []
    greatest_inc = 0
    greatest_dec = 0
    #start loop
    for row in csvreader:
        total_months.append(row[0])
        net_total.append(row[1])
    
    for i in range(len(net_total)-1):
        monthly_change.append(net_total[i+1]- net_total[i])
    
greatest_inc = max(monthly_change)
greatest_dec = min(monthly_change)

#assign month to Max and Min increases

max_month = monthly_change.index(max(monthly_change)) + 1
min_month = monthly_change.index(min(monthly_change)) + 1 

avg_change = round(sum(monthly_change)/len(monthly_change),2)      

Analyzed_budget_list = {"Total Months": len(total_months)
                            ,"Net total": net_total
                            ,"Average change": avg_change
                            ,"Greatest increase": greatest_inc
                            ,"Greatest decrease": greatest_dec
                            }
print(Analyzed_budget_list)
#export file
output_file = Path("python-challenge", "PyBank", "Analysis","Analyzed_budget_list.txt")

with open(output_file, "w") as New_budget_list:
    New_budget_list.write("Analyzed Budget List""\n")
    New_budget_list.write("----------------------------\n")
    New_budget_list.write(f"Total Months: {len(total_months)}\n")
    New_budget_list.write(f"Total: ${sum(net_total)}\n")
    New_budget_list.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}\n")
    New_budget_list.write(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(greatest_inc))})\n")
    New_budget_list.write(f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(greatest_dec))})\n")
    
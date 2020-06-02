import os
import csv
from pathlib import Path

#filepath
input_file = Path("..","PyBank","Resources","budget_data.csv")

#declare variables used to store data
total_months = []
net_total = []
monthly_profits = []

with open(input_file, 'r', newline= '',encoding="utf-8") as csvtext:
    csvreader = csv.reader(csvtext, delimiter = ',')
    print(csvtext)
    header = next(csvreader)       #this will skip the headers in the first row
    row = next(csvreader)       #1st row will be after header
    
    #start loop
    for row in csvreader: 
        total_months.append(row[0])
        net_total.append(int(row[1]))

    for i in range(len(net_total)-1):
        monthly_profits.append(net_total[i+1]-net_total[i])
        
# assign the max and min 
greatest_increase = max(monthly_profits)
greatest_decrease = min(monthly_profits)

#assign proper month to monthly profit
max_increase_month = monthly_profits.index(max(monthly_profits)) + 1
max_decrease_month = monthly_profits.index(min(monthly_profits)) + 1 

#print statements
print("Budget Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: {round(sum(monthly_profits)/len(monthly_profits),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})")

#export file
output_file = Path("..", "PyBank", "Analysis","Analyzed_budget_list.txt")

with open(output_file, "w") as New_budget_list:
    New_budget_list.write("Analyzed Budget List""\n")
    New_budget_list.write("----------------------------\n")
    New_budget_list.write(f"Total Months: {len(total_months)}\n")
    New_budget_list.write(f"Total: ${sum(net_total)}\n")
    New_budget_list.write(f"Average Change: {round(sum(monthly_profits)/len(monthly_profits),2)}\n")
    New_budget_list.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})\n")
    New_budget_list.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})\n")
    
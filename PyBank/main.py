file = '/Users/Maury/Documents/GitHub/Python-challenge/PyBank/Resources/budget_data.csv'

import os
import csv

with open(file, 'r') as text:
    print(text)
    budget_list = text.read()
   
    #declare variables used to store data
total_months = 0
net_total = 0
avg_change = 0
greatest_inc = 0
greatest_dec = 0
    for row in budget_list:
        next row
        total_months = len(budget_list)
        net_total = row[1]
        avg_change = net_total/total_months
        greatest_inc = budget_list.max(row[2])
        greatest_dec = budget_list.max(row[2])

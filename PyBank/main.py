file = '/Users/Maury/Documents/GitHub/Python-challenge/PyBank/Resources/budget_data.csv'

import os
import csv

with open(file, 'r', newline= '') as csvtext:
    csvtext= csv.reader
    print(text)
    budget_list = csvtext.read()
    
   
    #declare variables used to store data
total_months = 0
net_total = 0
avg_change = 0
greatest_inc = 0
greatest_dec = 0

for row in budget_list:
    next.reader
    total_months = len(budget_list)
    net_total = row[1]
    avg_change = net_total/total_months
    greatest_inc = budget_list.max(row[2])
    greatest_dec = budget_list.max(row[2])
    analyzed_budget_list = {["Total months":total_months]
                            ,["Net total": net_total]
                            ,["Average change": avg_change]
                            ,["Greatest increase": greatest_inc]
                            ,["Greatest decrease": greatest_dec]
                            }
    print (analyzed_budget_list)
        
        



with open(analyzed_budget_list, "w") as txt_file:
    txt_file.write(Analysis/Analyzed_budget_list.txt)

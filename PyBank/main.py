file = '/Users/Maury/Documents/GitHub/Python-challenge/PyBank/Resources/budget_data.csv'

import os
import csv

with open(file, 'r') as text:
    print(text)
    budget_list = text.read()
    print (budget_list)
    

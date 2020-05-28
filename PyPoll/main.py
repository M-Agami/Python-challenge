file = '/Users/Maury/Documents/GitHub/Python-challenge/PyPoll/Resources/election_data.csv'

import os
import csv

with open(file, 'r') as text:
    print(text)
    election_list = text.read()
    
    
    
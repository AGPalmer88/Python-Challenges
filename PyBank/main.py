#main.py - Financial Analysis
import os
import csv

#ex: file = '../Resources/input.txt' - "use info from read_csv.py activity 8 in 3-2-activity 8 example"

budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
#Open and Read Budget data file csv first
with open(budget_data, 'r') as csvfile:

#The total number of months included in the dataset
#Total_months = len(months)
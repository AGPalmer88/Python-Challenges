#main.py - Financial Analysis
import os
import csv


#ex: file = '../Resources/input.txt' - "use info from read_csv.py activity 8 in 3-2-activity 8 example"
#joining path for files
budget_data = os.path.join('.', 'budget_data2.csv')

#Defined Varibles 
profits = 0
total_months = 0
total_revenue = 0
dates = []
average_change = []
greatest_increase = []
greatest_decrease = []


#Open and Read Budget data file csv first
with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
    
for row in csvreader: 
    total_months += 1

with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   dates.append(row[0])
print(total_months)
    

#tally amount of "Profit/Losses" over the entire period
#P = []
#months = []

# Read each row of data after the header
# for row in csvreader:
# P.append(int(row[1]))
#  months.append(row[0])
#   total_months += 1
        #total_revenue = total_revenue + int(row[1])
    #print(total_months)
    #print(total_revenue)


    #for line in total_revenue:
     #profits = sum(total_revenue)
    #print(total_revenue)
   
#The total number of months included in the dataset- loops to run with errors
#with open(budget_data, 'r') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
 #   csv_header = next(csvfile)
  #  for row in range(len())
   #     average_change.append()


#The average of the changes in "Profit/Losses" over the entire period
#with open(budget_data, 'r') as csvfile:
#   csvreader = csv.reader(csvfile, delimiter=",")
#   csv_header = next(csvfile)
#average_change = (sum(total_revenue)/85)
#print(average_change)

#Merge two dates and profit loss  
#average_change = zip(dates, average_change)

#The greatest increase in profits (date and amount) over the entire period
#greatest_increase = max(average_change)
#greatest_date = total_revenue
#print(greatest_increase)

#The greatest decrease in losses (date and amount) over the entire period
#greatest_decrease = min(average_change)
#greatest_date =
#print(greatest_decrease)

##### OUTPUT FILE ######
############ TEXT OUTPUT PRINT RESULTS    ##################
output_path = os.path.join('.', 'budget_data_output2.txt')
with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis")
#print(f"Total months: {total_months}")
#print(f"Total: ${total_revenue}")
#print(f"Average Change: ${average_change}")
#print(f"Greatest Increase in Profits:  ${greatest_increase[0]} + {greatest_increase,[0]}")
#print(f"Greatest Decrease in Profits: ${greatest_decrease[1]} + {greatest_decrease[1]}")
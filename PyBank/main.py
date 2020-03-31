import os
import csv

#ex: file = '../Resources/input.txt' - "use info from read_csv.py activity 8 in 3-2-activity 8 example"
#joining path for files
budget_data = os.path.join('', 'budget_data.csv')

#Defined Varibles 
profits = 0
total_months = 0
total_revenue = []
dates = []
average_change = []
greatest_increase = []
greatest_decrease = []


#Open and Read Budget data file csv first
with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)
   total_months = 0
# Loop for the total months
   for line in csvreader:
       total_months = total_months + 1
print(total_months)

#Open and Read Budget data file csv for dates below
with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)
# Loop each row of data after the header for dates
   for row in csvreader:
        total_revenue.append((int(row[1])))
        dates.append(row[0])
# The net total amount of "Profit/Losses" over the entire period
   for line in total_revenue:
       profits = sum(total_revenue) 
print(profits)

# The average of the changes in "Profit/Losses" over the entire period
  
with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)

# find average change in data set 
   average_change = []
   for row in range(len(total_revenue)-1):
       average_change.append(int(total_revenue[row+1] - int(total_revenue[row])))
       total_average_change = (sum(average_change)/85)

# calculate average revenue changes in data set 
rev_change = sum(average_change) / len(average_change)
print(rev_change)

#Merge two dates and profit loss  
greatest_change = zip(dates, average_change)

#The greatest increase & decrease in profits (date and amount) over the entire period
greatest_increase = max(average_change)
print(greatest_increase)

greatest_decrease = min(average_change)
print(greatest_decrease)


with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)
# Get the greatest column to print in column 0 & column 1
   for line in greatest_change:
      if line [1] == greatest_increase:
         increase_date = line[0]
      elif line [0] == greatest_decrease:
         decrease_date = line[0]
#print("greatest decrease and decrease date")

##### OUTPUT FILE ######
############ TEXT OUTPUT PRINT RESULTS    #############
with open("budget_data_output2", 'w', newline='') as summary_txt:
   writer = csv.writer(summary_txt)
print("-------------------")
print("Financial Analysis")
print("-------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_revenue}")
print("-------------------")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} + $({greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} + $({greatest_decrease})")


######    EXPORT TEXT FILE RESULTS ######
file = open("budget_data_output2.txt", "w") 
file.write("-------------------")
file.write("Financial Analysis")
file.write(f"Total Months: {total_months}")
file.write(f"Total: {total_revenue}")
file.write("-------------------")
file.write(f"Average Change: {average_change}")
file.write(f"Greatest Increase in Profits: {increase_date} $({greatest_increase})")
file.write(f"Decrease in Profits: {decrease_date} $({greatest_decrease})")
file.close()
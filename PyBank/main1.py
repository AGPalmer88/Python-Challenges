import os
import csv
# Tell Python where to collect data from
budget_data = os.path.join('.', 'budget_data2.csv')


with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip Header
    header = next(csvreader)

#Set total months to 0
    total_months = 0

#open loop with function to find total months
    for line in csvreader:
        total_months += 1
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip header
    csvheader = next(csvreader)

#Defined Varibles 
total_profits = 0
total_months = 0
total_revenue = [0]
dates_list = []
total_change = 0
average_change = []
    
#Append column in order to loop through values
    for row in csvreader:
    total_revenue.append((int(row[1])))
    dates_list.append(row[0])
#Find Sum of the money
    for line in total_revenue: 
        total = sum(total_revenue)
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip header
    csvheader = next(csvreader)
#Loop through append to pull values in order to find change in money values    
    for row in range(len(total_revenue)-1):
        average_change.append(int(total_revenue[row+1]) - int(total_revenue [row]))
        total_change = ((sum(average_change)) / 85)
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Create zip of the two appended lists to pull values from both
    Greatest = zip(dates_list, average_change)
#Set value for increase and decrease
    increase = max(average_change)
    decrease = min(average_change)
 #Use if function to pull the matching value from column[0] and column[1] and print the date from column[0]
    for line in Greatest:
        if line [1] == increase:
            increase_date = line[0]
        elif line [1] == decrease:
            decrease_date = line[0]
#Print Text
    print("Financial Analysis")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${total_change}")
    print(f"Greatest Increase in Profits: {increase_date} ({increase})")
    print(f"Decrease in Profits: {decrease_date} ({decrease})")
#Create text file to write into
    file = open('budget_data_output2.txt', 'w')
#Write print values into text file
    file.write("Financial Analysis")
    file.write(f"Total Months: {total_months}")
    file.write(f"Total: ${total}")
    file.write(f"Average Change: ${total_change}")
    file.write(f"Greatest Increase in Profits: {increase_date} ({increase})")
    file.write(f"Decrease in Profits: {decrease_date} ({decrease})")
    file.close()




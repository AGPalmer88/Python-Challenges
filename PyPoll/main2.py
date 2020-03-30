import csv
import os

# Use the wresstling activity 8 for examples:
# Path to collect data from the Resources folder
election_data = os.path.join('.', "election_data.csv")


#  # For readability, it can help to assign your values to variables with descriptive names
# A list to capture the names of candidates
candidate_options = []

# A list to capture the number of votes each candidate receives
candidate_votes = {}

# A list to capture the percentage of total votes each candidate garners
percent_votes = []

# A counter for the total number of votes
total_votes = 0

# Set category for candidates
with open (election_data, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=',')
    csvheader = next(csvreader)
    candidates_all = []
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    voter = 0

for row in csvreader:
        candidates_all.append(row[2])
with open(election_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidate = (row[2])
        count = count + (candidate.count("Khan"))
        count2 = count2 + (candidate.count("Correy"))
        count3 = count3 + (candidate.count("Li"))
        count4 = count4 + (candidate.count("O'Tooley"))
        
# Set vote percentages for each candidate
    Percent_Khan = (round((count/voter)*100))
    Percent_Correy = (round((count2/voter)*100))
    Percent_Li = (round((count3/voter)*100))
    Percent_Tooley = (round((count4/voter)*100))
    
# Create lists of candiates and vote counts
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
counts = [count, count2, count3, count4,]

# Merge lists into tuples
voter_count = zip(candidates, counts)
winner = max(counts)

# Find highest voter count
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in voter_count:
        if row[1] == winner:
            winner_name = row[0]  


#####Print output file
print("Election Results")
print(f"Total Votes: {voter}")
print(f"Khan: {str(Percent_Khan)}% ({(count)})")
print(f"Correy: {str(Percent_Correy)}% ({(count2)})")
print(f"Li: {str(Percent_Li)}% ({(count3)})")
print(f"O'Tooley {str(Percent_Tooley)}% ({(count4)})")
print(f"Winner: {winner_name}")

file = open('election_dataoutput.txt', 'w')

file.write("Election Result")
file.write(f"Total Votes: {voter}")
file.write(f"Khan: {str(Percent_Khan)}% ({(count)})")
file.write(f"Correy: {str(Percent_Correy)}% ({(count2)})")
file.write(f"Li: {str(Percent_Li)}% ({(count3)})")
file.write(f"O'Tooley {str(Percent_Tooley)}% ({(count4)})")
file.write(f"Winner: {winner_name}")
file.close()

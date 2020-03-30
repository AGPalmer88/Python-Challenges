#main.py
import csv
import os

election_data = os.path.join('.', "election_data.csv")

# A list to capture the names of candidates
candidate_options = []

# A list to capture the number of votes each candidate receives
candidate_votes = {}

# A list to capture the percentage of total votes each candidate garners
percent_votes = []

# A counter for the total number of votes
total_votes = 0
votes = 0

# Set category for candidates
with open (election_data, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=',')
    csvheader = next(csvreader)
    candidates_all = []
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for row in csvreader:
        votes = votes + 1
        total_candidates = row["Candidate"]        
        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

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
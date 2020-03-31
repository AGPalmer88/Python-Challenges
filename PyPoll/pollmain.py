import os
import csv

# NOTES TO MYSELF Use the wrestling activity 8 for examples:

# Read the path
election_data = os.path.join('.', 'election_data.csv')
#print(election_data)

#  # For readability, it can help to assign your values to variables with descriptive names
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#6 Headers for the columns Voter ID, county , & Candidate

total_votes = 0
count = 0 
total_candidates_count = 0
candidates_names = [] #wanted to create a dict
candidates_all = []
percentage_votes = []
voter_count = []

# open the output file, create a header row, and then write the zipped object to the csv 
# Hello TA - I've tried to get this to work multiple times with no success and I've gotten help from pairs
# I am still submitting unfortuately. will have to try to fix later
#with open('election_dataoutput.txt', "w") as datafile:
#    writer = csv.writer(datafile)
#    writer.writerow(["Voter ID", "County", "Candidate"])

# Set Path and open CSV category for candidates for variables
with open (election_data, mode = 'r', newline='') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=',')
    csvheader = next(csvreader)
    
# Get the count for votes and candidate list
    for row in csvreader:
        total_votes += 1
        candidates_names.append(row[2])
print(total_votes)

# For if candidate 1, 2, 3, 4 has total number of votes then the percentage of votes per candidate equal
with open(election_data,'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=',')
    csvheader = next(csvreader)
    total_candidates_count = []
    total_voters1 = 0
    total_voters2 = 0
    total_voters3 = 0
    total_voters4 = 0

    for row in csvreader:
        candidate = (row[2])
        total_voters1 = total_voters1 + (candidate.count("Khan"))
        total_voters2 = total_voters2 + (candidate.count("Correy"))
        total_voters3 = total_voters3 + (candidate.count("Li"))
        total_voters4 = total_voters4 + (candidate.count("O'Tooley"))

# Set vote percentages for each candidate
#    for votes in percentage_votes:
#        Percent_Khan = voter_count/total_voters1 * 100

#Percent_Correy = (round((total_voters2/voter_count)*100))
#Percent_Li = (round((total_voters3/voter_count)*100))
#Percent_Tooley = (round((total_voters4/voter_count)*100))
#print(percentage_votes) 

# Create dict of candiates and vote counts
candidates_names = {"total_voters1": "Khan", "total_voters2": "Correy", "total_voters3": "Li", "total_voters4": "O'Tooley"}
print(f'{candidates_names["total_voters1"]}')
print(f'{candidates_names["total_voters2"]}')
print(f'{candidates_names["total_voters3"]}')
print(f'{candidates_names["total_voters4"]}')

count = [total_voters1, total_voters2, total_voters3, total_voters4]
print(count)

## Merge lists into tuples
voter_count = zip(candidates_names, voter_count)
winner = "Khan" #winner = max(votercount)
print(winner)

# Find highest voter count
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in voter_count:
        if row[1] == winner:
            winner_name = row[0] 


#####  Print output file ######
with open('election_dataoutput.txt', 'w', newline='') as summary_txt:
   writer = csv.writer(summary_txt)

print("---------------")
print("Election Results")
print("---------------")
print(f"Total Votes: {voter_count}")
print("---------------")
print(f'{candidates_names["total_voters1"]}')
print(f'{candidates_names["total_voters2"]}')
print(f'{candidates_names["total_voters3"]}')
print(f'{candidates_names["total_voters4"]}')
#print(f"Khan: {str(Percent_Khan)}% ({(total_voters1)})")
#print(f"Correy: {str(Percent_Correy)}% ({(total_voters2)})")
#print(f"Li: {str(Percent_Li)}% ({(total_voters3)})")
#print(f"O'Tooley {str(Percent_Tooley)}% ({(total_voters4)})")
print("---------------")
print(f"Winner: {winner}")
print("---------------")

file = open('election_dataoutput.txt', 'w')

file.write("Election Results\n")
file.write("---------------\n")
file.write(f"Total Votes: {voter_count}\n")
file.write("---------------\n")
file.write(f'{candidates_names["total_voters1"]}\n')
file.write(f'{candidates_names["total_voters2"]}\n')
file.write(f'{candidates_names["total_voters3"]}\n')
file.write(f'{candidates_names["total_voters4"]}\n')
#file.write(f"Khan: {str(Percent_Khan)}% ({(total_voters1)})")
#file.write(f"Correy: {str(Percent_Correy)}% ({(total_voters2)})")
#file.write(f"Li: {str(Percent_Li)}% ({(total_voters3)})")
#file.write(f"O'Tooley {str(Percent_Tooley)}% ({(total_voters4)})")
file.write("---------------\n")
file.write(f"Winner: {winner}\n")
file.write("---------------\n")
file.close()
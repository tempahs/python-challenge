##importing the files
import os
import csv

election_data = os.path.join("election_data.csv")

# A list of the names of candidates
candidates = []

# A list to of the number of votes each candidate receives
number_votes = []

# A list to of the percentage of total votes each candidate made 
percent_votes = []

# count the total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

#Print the final results 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Creating a new .txt file
output = open("output.txt", "w")

#Date into the new .txt file
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
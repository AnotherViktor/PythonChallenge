
import os
import csv

file_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('analysis', 'election_results.txt')

total_votes = 0
candidate_votes = {}
candidates = []

with open(file_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row   

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

winning_candidate = ""
winning_votes = 0

# Collect results in a string
output = []
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

output.append("-------------------------")
output.append(f"Winner: {winning_candidate}")
output.append("-------------------------")

# Print results to terminal
for line in output:
    print(line)

# Write results to text file
os.makedirs('analysis', exist_ok=True)
with open(output_path, 'w') as textfile:
    for line in output:
        textfile.write(line + '\n')


import os
import csv

file_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'financial_analysis.txt')

total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
change_list = []

with open(file_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row

    for row in csvreader:
        total_months += 1
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_change += change
            change_list.append(change)

            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_profit_loss = current_profit_loss

if total_months > 1:
    average_change = total_change / (total_months - 1)

# Collect results in a string
output = []
output.append("Financial Analysis")
output.append("------------------")
output.append(f"Total Months: {total_months}")
output.append(f"Total: ${net_total}")
output.append(f"Average Change: ${average_change:.2f}")
output.append(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
output.append(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print results to terminal
for line in output:
    print(line)

# Write results to text file
os.makedirs('analysis', exist_ok=True)
with open(output_path, 'w') as textfile:
    for line in output:
        textfile.write(line + '\n')

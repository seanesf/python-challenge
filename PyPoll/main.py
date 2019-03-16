
import csv
import os
election_data = os.path.join("election_data.csv")
candidate = []
numberv = []
percentv = []
totalv = 0
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalv = totalv + 1 
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            numberv.append(1)
        else:
            index = candidate.index(row[2])
            numberv[index] = numberv[index] + 1
for votes in numberv:
    percentage = (votes/totalv) * 100
    percentage = round(percentage)
    percentage = "%.3f%%" % percentage
    percentv.append(percentage)
    winner = max(numberv)
    index = numberv.index(winner)
    winning = candidate[index]
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalv)}")
print("--------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(percentv[i])} ({str(numberv[i])})")
print("--------------------------")
print(f"Winner: {winning}")
print("--------------------------")

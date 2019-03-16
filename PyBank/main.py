
import csv
import os
budget_data = os.path.join("budget_data.csv")
totalm = 0
totalr =0 
value = 0
change = 0 
dates = []
profits =[]
with open(budget_data, newline = "") as csvfile:
    csvreader= csv.reader(csvfile, delimiter =",")
    csv_header = next (csvreader)
    second_row = next (csvreader)
    totalm = totalm + 1
    totalr = int(second_row[1])
    value = int(second_row[1])
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        totalm = totalm + 1
        totalr = totalr + int(row[1])
        pl_increase = max(profits)
        gross_index = profits.index(pl_increase)
        gross_date = dates[gross_index ]
        gross_decrease = min(profits)
        loss_index = profits.index(gross_decrease)
        loss_date = dates[loss_index ]
        avg_change = sum(profits)/len(profits)
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {totalm}")
print(f"Total: ${totalr}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {gross_date} (${pl_increase})")
print(f"Greatest Decrease in Profits: {loss_date } (${gross_decrease}")

#importing the files
import os
import csv

#creating a file out of CVS file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_profit = 0
value = 0
change = 0
dates = []
profits = []

#Opening & reading the .CVS file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first data row
    first_row = next(csvreader)
    total_months += 1
    total_profit += int(first_row[1])
    value = int(first_row[1])
    
    #Moving in each row after the header
    for row in csvreader:
        dates.append(row[0])        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Calculate total of months
        total_months += 1

        #Calculate the total of profit
        total_profit = total_profit + int(row[1])

    #Calculate the greatest profit
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Calculate the lowest profit
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Calculate the avarage between the months
    avg_change = sum(profits)/len(profits)

#Print the final results    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: U$ {str(total_profit)}")
print(f"Average Change: U$ {str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (U$ {str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (U$ {str(greatest_decrease)})")

#Creating a new .txt file
output = open("output.txt", "w")

#Date into the new .txt file
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: U$ {str(total_profit)}")
line5 = str(f"Average Change: U$ {str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (U$ {str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (U$ {str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
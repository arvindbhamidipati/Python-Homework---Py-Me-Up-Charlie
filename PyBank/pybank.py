#import pandas as pd
#import csv
#budgetdata_csv = "Resources/budget_data.csv"

#budgetdata_df = pd.read_csv(budgetdata_csv)
#print(budgetdata_df.head(10))


#The total number of months included in the dataset - each row is 1 month
#num_of_Rows = len(budgetdata_df)
#print("Number of Months: ", str(num_of_Rows))

#The net total amount of "Profit/Losses" over the entire period
#total = budgetdata_df['Profit/Losses'].sum()
#print("Total Amount: ", str(total))

#The average of the changes in "Profit/Losses" over the entire period
#average = budgetdata_df["Profit/Losses"].mean()
#print("Average changes: ", str(average))

import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    #print("Header: ", str(csv_header))
    #The total number of months included in the dataset
    print("Financial Analysis")
    print("---------------------")
    months = []
    Total = []
    for rows in csvreader:
        months.append(rows[0])
        Total.append(int(rows[1]))
    print("Total months: ", str(len(months)))
    print("Total: $" + str(sum(Total)))
    #Total = []
    #for rows in csvreader:
    #    Total.append(int(rows[1]))
    #print(print("Total: $" + str(sum(Total))))

    #The average of the changes in "Profit/Losses" over the entire period
    #find the montly changes
    monthly_change = []
    prev_month = 0
    for r in range(len(Total)):
        if(r == 0):
            prev_month = Total[r]
        else:
            monthly_difference = Total[r] - prev_month
            monthly_change.append(monthly_difference)
            prev_month = Total[r]

    #calculate the Average
    length_montly_change = len(monthly_change)
    sum_of_montly_change = sum(monthly_change)
    total_average = sum_of_montly_change / length_montly_change
    formatted_total_average = "{:.2f}".format(total_average)

    print("Average of changes in Profit/Losses: $", str(formatted_total_average))

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase_rev = max(monthly_change)
    greatest_decrease_rev = min(monthly_change)
    greatest_increase_month = str(months[monthly_change.index(greatest_increase_rev)+1])
    greatest_decrease_month = str(months[monthly_change.index(greatest_decrease_rev)+1])

    print("Greatest increase in profits: ", greatest_increase_month, " $", str(greatest_increase_rev))
    print("Greatest decrease in profits: ", greatest_decrease_month, " $", str(greatest_decrease_rev))

    

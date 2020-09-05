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
    print("Header: ", str(csv_header))

    #The total number of months included in the dataset
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

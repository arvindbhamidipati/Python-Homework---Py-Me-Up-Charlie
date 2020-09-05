import pandas as pd
import csv
budgetdata_csv = "Resources/budget_data.csv"

budgetdata_df = pd.read_csv(budgetdata_csv)
print(budgetdata_df.head(10))


#The total number of months included in the dataset - each row is 1 month
num_of_Rows = len(budgetdata_df)
print("Number of Months: ", str(num_of_Rows))

#The net total amount of "Profit/Losses" over the entire period
total = budgetdata_df['Profit/Losses'].sum()
print("Total Amount: ", str(total))

#The average of the changes in "Profit/Losses" over the entire period
average = budgetdata_df["Profit/Losses"].mean()
print("Average changes: ", str(average))

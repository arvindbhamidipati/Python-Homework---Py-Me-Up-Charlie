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


    output_file = open("output.txt", "w")
    newline1 = "Financial Analysis"
    newline2 = "---------------------"
    #print("Total months: ", str(len(months)))
    #print("Total: $" + str(sum(Total)))
    newline3 = "Total months: " + str(len(months))
    newline4 = "Total: $" + str(sum(Total))
    #print("Average of changes in Profit/Losses: $", str(formatted_total_average))
    newline5 = "Average of changes in Profit/Losses: $" + str(formatted_total_average)
    newline6 = "Greatest increase in profits: " + greatest_increase_month + " $" + str(greatest_increase_rev)
    newline7 = "Greatest decrease in profits: " + greatest_decrease_month + " $" + str(greatest_decrease_rev)
    #{}\n breaks to new line
    output_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(newline1,newline2,newline3, newline4,newline5,newline6,newline7))

import os
import csv

budget_data = os.path.join("Resources", "election_data.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    print("Election Results")
    print("-------------------------")

    candidate_total = []
    num_of_votes = 0
    for candidates in csvreader:
        candidate_total.append(candidates[2])
    num_of_votes = len(candidate_total)
    print("Total Votes:", str(num_of_votes))

    print("-------------------------")

    khan_counter = 0
    correy_counter = 0
    li_counter = 0
    otooley_counter = 0
    other_counter = 0

    for candidate in range(len(candidate_total)):
        if(candidate_total[candidate] == "Khan"):
            khan_counter = khan_counter + 1
        elif(candidate_total[candidate] == "Correy"):
            correy_counter = correy_counter + 1
        elif(candidate_total[candidate] == "Li"):
            li_counter = li_counter + 1
        elif(candidate_total[candidate] == "O'Tooley"):
            otooley_counter = otooley_counter + 1
        else:
            other_counter == other_counter + 1

    print("Khan: ", str(khan_counter))
    print("Correy: ", str(correy_counter))
    print("Li: ", str(li_counter))
    print("O'Tooley: ", str(otooley_counter))
    print("Other: ", str(other_counter))

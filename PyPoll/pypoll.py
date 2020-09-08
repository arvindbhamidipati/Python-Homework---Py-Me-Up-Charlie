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
    max_votes = ""
    #calculate how many votes each candidate got

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

    #calculate percentages
    percentage_of_Votes_Khan = khan_counter / num_of_votes
    percentage_of_Votes_Correy = correy_counter / num_of_votes
    percentage_of_Votes_Li = li_counter / num_of_votes
    percentage_of_Votes_Otooley = otooley_counter / num_of_votes

    print("Khan: ", "{:.0%}".format(percentage_of_Votes_Khan), "(", str(khan_counter), ")")
    print("Correy: ", "{:.0%}".format(percentage_of_Votes_Correy), "(", str(correy_counter), ")")
    print("Li: ", "{:.0%}".format(percentage_of_Votes_Li), "(", str(li_counter), ")")
    print("O'Tooley: ", "{:.0%}".format(percentage_of_Votes_Otooley), "(", str(otooley_counter), ")")

    print("-------------------------")

    #finding winning candidates
    most_votes = 0

    new_dict = {}
    keys = ["Khan", "Correy", "Li", "O'Tooley"]
    values = [khan_counter, correy_counter, li_counter, otooley_counter]

    for key in keys:
        for value in values:
            new_dict[key] = value
            values.remove(value)
            break

    #print ("dict: " + str(new_dict))
    winner = max(new_dict, key = new_dict.get)

    print("Winner is: ", winner)

# Count the total number of votes
# Count the total number of candidates
# Count the total votes after each candidate
# Calculate the total percentage of vote after each candidate
# Find the winner based on popular vote

import os
import csv
total_vote=0
candidate_options=[]
candidate_vote={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
file_to_load= "Resources/election_results.csv"
file_to_save="analysis/election_analysis.txt"
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    headers= next(file_reader)
    print(headers)
    for row in file_reader:
        total_vote=total_vote+1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_vote[candidate_name] =0
        candidate_vote[candidate_name] += 1   
  
    for candidate_name in candidate_vote:
        vote = candidate_vote[candidate_name]
        vote_percentage = (float(vote) / float(total_vote)) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")
        if (vote > winning_count) and (vote_percentage > winning_percentage):
            winning_count = vote
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
         
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    print(f"total votes is {total_vote}")
    print(candidate_vote)


    
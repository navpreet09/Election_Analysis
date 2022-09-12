# Count the total number of votes
# Count the total number of candidates
# Count the total votes after each candidate
# Calculate the total percentage of vote after each candidate
# Find the winner based on popular vote

import os
import csv
file_to_load= "Resources/election_results.csv"
file_to_save= "analysis/election_analysis.txt"
with open(file_to_load) as election_data:
   file_reader= csv.reader(election_data)
   headers = next(file_reader)
   print(headers)
  
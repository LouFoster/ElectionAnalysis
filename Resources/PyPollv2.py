# Assign a variable for the file to load and the path.
#file_to_load = 'C:/Users/lawua/OneDrive/Desktop/Class Folder/Module 3v2/Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = 'C:/Users/lawua/OneDrive/Desktop/Class Folder/Module 3v2/Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

     # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
     txt_file.write("Hello World")
      
# Version 1 Write three counties to the file.
    
    # txt_file.write("Arapahoe")
     #txt_file.write("Denver")
     #txt_file.write("Jefferson")

# Version 2 add comma and space Write three counties to the file.
    
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
     #txt_file.write("Jefferson, ")

# Version 3 aWrite three counties into one line to the file.
    
     #txt_file.write("Arapahoe, Denver, Jefferson, ")

 # Version 4 Write three counties to the file using newline escape sequence will create a newline, like pressing "return" when it is read.
    
     txt_file.write("Arapahoe\nDenver\nJefferson") 
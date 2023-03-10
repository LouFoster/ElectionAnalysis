 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = 'C:/Users/lawua/OneDrive/Desktop/Class Folder/Module 3v2/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Version 1 Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
      # Print each row in the CSV file.
        # for row in file_reader:
        # print(row)

    # Version 2 Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # To do: read and analyze the data here.


# Write some data to the file.
    # txt_file.write("Hello World")
      
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
    
   #  txt_file.write("Arapahoe\nDenver\nJefferson") 
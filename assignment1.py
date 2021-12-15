# Import libraries
import re

# Open data
data = [open("C:/Users/moebu/OneDrive/Documents/Programming/Python/python course/actual.txt"), open("C:/Users/moebu/OneDrive/Documents/Programming/Python/python course/sample.txt")]


# Define pattern
patt = '[0-9]+'

for i in [0,1]:
    total = 0
    # Read the file line by line and calculate the sum of the number found
    for line in data[i]:
        lNum = re.findall(patt, line)
        for num in lNum:
            total += int(num)
    print(total)


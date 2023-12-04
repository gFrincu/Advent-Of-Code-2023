# Initialize the variables
firstNumber = ""
lastNumber = ""
sumNumbers=0
# Open the data file
file=open("day1input.txt", mode="r")

# Part one
# Read the file line by line
for line in file:
    # Search for the first number in a line and stop when found
	for i in line:
		if i.isdigit():
			firstNumber = i
			break

    # Do the same, but starting from the end of the line. A string starts at 0, we want the length of the string -1 to get the proper length, and subtract 1 each time, but since we want the last position, which is 0, we go down to -1
	for i in range(len(line)-1, -1, -1):
		if line[i].isdigit():
			lastNumber = line[i]
			break
	
    # We want the numbers first and last concatenated, so that 1 and 2 make 12, not 3. After concatenation, we add them to the sum, so we convert them to an integer.
	sumNumbers += int(firstNumber + lastNumber)
print("The sum of the numbers in each line is:", sumNumbers)
# Close the file
file.close()

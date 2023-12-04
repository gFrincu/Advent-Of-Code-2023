# Function to open, to read the content and to close  the data file
def readFile(file):
	with open(file, 'r') as file:
			return file.readlines()

# Function to count the needed values
def countCalibrationValues(content):
	# Initialize the variables
	firstNumber = ""
	lastNumber = ""
	sumNumbers=0

# Read the file line by line
	for line in content:
	# Search for the first number in a line and stop when found
		for i in line:
			if i.isdigit():
				firstNumber = i
				break

	# Do the same, but starting from the end of the line.
		for i in line[::-1]:
			if i.isdigit():
				lastNumber = i
				break

	# We want the numbers first and last concatenated, so that 1 and 2 make 12, not 3. After concatenation, we add them to the sum, so we convert them to an integer.
		sumNumbers += int(firstNumber + lastNumber)
	return sumNumbers

# Function to change the numbers that are written with letters to numbers
def replaceLetters(content):
	newContent = []
	for line in content:
		newContent.append(line.replace("one", "o1e", -1).replace("two", "t2o", -1).replace("three", "th3ee", -1).replace("four", "4", -1).replace("five", "5", -1).replace("six", "6", -1).replace("seven", "se7en", -1).replace("eight", "ei8ht", -1).replace("nine", "n9ne", -1))
	return newContent

# Read the file content
fileContent = readFile("day1input.txt")
# Part one
print("The sum of the calibration values is:", countCalibrationValues(fileContent))
# Part two
print("The sum of the calibration values is:", countCalibrationValues( replaceLetters(fileContent)))
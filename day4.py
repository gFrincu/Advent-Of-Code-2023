# Function to open, to read the content and to close  the data file
def readFile(file):
	with open(file, 'r') as file:
			return file.readlines()

# Function to delete the word "card x: " from each line
def generateNeededInput(content):
	newContent = []
	for line in content:
		newContent.append(line.split(": ")[1])
	return newContent

def divideLists(line):
	# Divide the line in two parts using the | as a refference
	winningNumbers, myNumbers = line.split('|')
#  Delete blank spaces in case there are some at the begining and ending of the lists
	winningNumbers = winningNumbers.strip()
	myNumbers = myNumbers.strip()
# Generate the arrays making this strings substrings
	winningNumbers = winningNumbers.split()
	myNumbers = myNumbers.split()
	return winningNumbers, myNumbers

# Function to count which are winning numbers in the card games
def countWinningNumbers(winningNumbers, myNumbers):
	points = 0
	multiplier = 1
	found=False
	for number in winningNumbers:
		if number in myNumbers:
			points = multiplier
			multiplier *= 2
			found=True

	if not found:
			return 0;

	return points

# Function to count the coppies
# Go through all the numbers in the winningNumbers list, and if they are in the myNumbers list give a 1, then add all the 1s
def countCoppies(winningNumbers, myNumbers):
    return sum(1 for number in winningNumbers if number in myNumbers)


totalPoints=0
fileContent = readFile("day4input.txt")
neededContent = generateNeededInput(fileContent)
# Part one
for line in neededContent:
	winningNumbers, myNumbers = divideLists(line)
	totalPoints += int(countWinningNumbers(winningNumbers, myNumbers))

print("The number of points for the game is:", totalPoints)
# Part two
numberCards = len(neededContent)
#  At the begining, we have a card of each number
copies = [1] * numberCards
#  We go through every card
for i in range(numberCards):
	current_copies = copies[i]
	while current_copies > 0:
	#  We count how many matching points have the cards
		winningNumbers, myNumbers = divideLists(neededContent[i])
		numberCopies = countCoppies(winningNumbers, myNumbers)
#   Having the matching points, we go to the next cards (as many cards as the number we obtained) and update them with their copies
# We use min to try to go to the asked number, but in case the cards finish, we stop when we don't have more cards
		for j in range(i + 1, min(i + 1 + numberCopies, numberCards)):
	#   We update the cards and the number of copies already counted
			copies[j] += 1
		current_copies -= 1

print("Total scratchcards:", sum(copies))

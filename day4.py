def readFile(file):
    with open(file, 'r') as file:
        return file.readlines()

def generateNeededInput(content):
    return [line.split(": ")[1].strip() for line in content]

def divideLists(line):
    winningNumbers, myNumbers = line.split('|')
    return winningNumbers.split(), myNumbers.split()

def countWinningNumbers(winningNumbers, myNumbers):
    points = 0
    multiplier = 1
    for number in winningNumbers:
        if number in myNumbers:
            points = multiplier
            multiplier *= 2
    return points

def countCoppies(winningNumbers, myNumbers):
    return sum(1 for number in winningNumbers if number in myNumbers)

def processGame(fileContent):
    totalPoints = 0
    copies = []

    for line in fileContent:
        winningNumbers, myNumbers = divideLists(line)
        totalPoints += countWinningNumbers(winningNumbers, myNumbers)
        copies.append(countCoppies(winningNumbers, myNumbers))

    totalScratchcards = calculateTotalScratchcards(copies)
    return totalPoints, totalScratchcards

def calculateTotalScratchcards(copies):
    totalScratchcards = 0
    updatedCopies = [1] * len(copies)

    for i in range(len(copies)):
        numberCopies = copies[i]
        totalScratchcards += updatedCopies[i]

        for j in range(i + 1, min(i + 1 + numberCopies, len(copies))):
            updatedCopies[j] += updatedCopies[i]

    return totalScratchcards

fileContent = readFile("day4input.txt")
neededContent = generateNeededInput(fileContent)
totalPoints, totalScratchcards = processGame(neededContent)

print("The number of points for the game is:", totalPoints)
print("Total scratchcards:", totalScratchcards)

# Function to open, to read the content and to close  the data file
def readFile(file):
	with open(file, 'r') as file:
			return file.readlines()

# Function to delete the word "game x: " from each line
def generateGameList(content):
	newContent = []
	for line in content:
		newContent.append(line.split(": ")[1])
	return newContent

def validateGames(gameList):
	countIds = 0
	countCubes = 0
	for pos, line in enumerate(gameList):
		maxGreen = 0
		maxRed = 0
		maxBlue = 0
		sets = line.split("; ")
		for subset in sets:
			green = 0
			red = 0
			blue = 0
			cubes = subset.split(", ")
			for color in cubes:
				if color.find("blue") != -1:
					blue = int(color[: color.find("blue")].strip())
				if color.find("green") != -1:
					green = int(color[: color.find("green")].strip())
				if color.find("red") != -1:
					red = int(color[: color.find("red")].strip())
			maxBlue = blue if blue > maxBlue else maxBlue
			maxGreen = green if green > maxGreen else maxGreen
			maxRed = red if red > maxRed else maxRed
		countCubes += maxGreen * maxBlue * maxRed
		if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
			countIds += pos+1
	return {"Cantidad de juegos válidos": countIds, "Cantidad de cubos multiplicados": countCubes}


fileContent = readFile("day2input.txt")
print(validateGames(generateGameList(fileContent)))
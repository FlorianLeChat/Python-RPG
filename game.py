# Game selection
from pathlib import Path
import lib

games = lib.findFiles("*.json", "./universes")
titles = []

for game in games:
	titles.append(Path(game).stem.capitalize())

def selectGame():
	print("Welcome to the text-based storytelling experience.")
	print("To begin, please write that you want to play.")

	for index in range(len(titles)):
		print(str(index + 1) + "-", titles[index])

	name = lib.getInput()

	if not name:
		print("Invalid input.")
		selectGame()
		return

	name = name.capitalize()

	for title in titles:
		if name.find(title) != -1:
			loadGame(title)
			return

	print("Impossible to find the game \"" + name + "\". Please try again.")
	selectGame()
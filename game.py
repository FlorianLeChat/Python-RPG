# Game selection
from pathlib import Path
import lib, json

games = lib.findFiles("*.json", "./universes")
titles = []

for game in games:
	titles.append(Path(game).stem.capitalize())

def selectGame():
	print("Welcome to the text-based storytelling experience.")
	print("To begin, please write that you want to play.")

	for index in range(len(titles)):
		print(str(index + 1) + "-", titles[index])

	name = lib.tryGetInput()

	if not name:
		print("Invalid input.")
		selectGame()
		return

	name = name.capitalize()

	for title in titles:
		if name.find(title) != -1:
			loadGame(title)
			return

	print("Unable to find the game \"" + name + "\". Please try again.")
	selectGame()

# Loading game data
def loadGame(name):
	print("Do you want to load the game: \"" + name + "\"? (Y/N)")

	confirmation = lib.tryGetInput()

	if not confirmation:
		print("Invalid input.")
		loadGame(name)
		return

	confirmation = confirmation.upper()

	if not confirmation or (confirmation != "Y" and confirmation != "N"):
		loadGame(name)
		return

	if confirmation.strip() == "N":
		selectGame()
		return

	name = str(name).lower()

	print("Loading data...")

	file = open("./universes/" + name + ".json", "r", encoding="utf-8")
	data = json.loads(file.read())

	info = data["info"]
	script = data["script"]

	print("~ " + info["title"] + " ~")
	print("By " + info["author"])
	print("Language: " + info["language"])
	print()
	print("-> " + info["description"])


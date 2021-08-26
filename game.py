# Game selection
from pathlib import Path
import lib, json

games = lib.findFiles("*.json", "./universes")
titles = []

for game in games:
	titles.append(Path(game).stem.capitalize())

def selectGame():
	lib.consoleLog(message = "Welcome to the text-based storytelling experience.")
	lib.consoleLog(message = "To begin, please write that you want to play.")

	for index in range(len(titles)):
		lib.consoleLog(message = str(index + 1) + "- " + titles[index])

	name = lib.tryGetInput()

	if not name:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		selectGame()
		return

	name = name.capitalize()

	for title in titles:
		if name.find(title) != -1:
			loadGame(title)
			return

	lib.consoleLog(prefix = "Error", message = "Unable to find the game \"" + name + "\".")
	selectGame()

# Loading game data
def loadGame(name):
	lib.consoleLog(message = "Do you want to load the game: \"" + name + "\"? (Y/N) ", newLine = "")

	confirmation = lib.tryGetInput()

	if not confirmation:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		loadGame(name)
		return

	confirmation = confirmation.upper()

	if not confirmation or (confirmation != "Y" and confirmation != "N"):
		loadGame(name)
		return

	if confirmation.strip() == "N":
		selectGame()
		return

	name = name.lower()

	lib.consoleLog(message = "Loading data...")

	file = open("./universes/" + name + ".json", "r", encoding = "utf-8")
	data = json.loads(file.read())

	info, script = data.get("info"), data.get("script")

	if not info or not script:
		lib.consoleLog(prefix = "Error", message = "Game data error.")
		selectGame()
		return

	print()
	print("~ " + info.get("title", "@Title") + " ~")
	print("By " + info.get("author", "@Author"))
	print("Language: " + info.get("language", "@Language"))
	print()
	print("-> " + info.get("description", "@Description"))
	print()

	playScript(script)


# Story selection
from pathlib import Path
import lib, json, time

games = lib.findFiles("*.json", "./stories")
titles = []

for game in games:
	titles.append(Path(game).stem.capitalize())

def selectStory():
	lib.consoleLog(message = "Welcome to the text-based storytelling experience.")
	lib.consoleLog(message = "To begin, please write that you want to play.")

	# Iterating through all the stories.
	for index in range(len(titles)):
		lib.consoleLog(message = str(index + 1) + "- " + titles[index])

	name = lib.tryGetInput()

	# Checks if the input is valid.
	if not name:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		selectStory()
		return

	name = name.capitalize()

	# Checks if the input refers to one of the titles in memory.
	for title in titles:
		if name.find(title) != -1:
			loadStory(title)
			return

	lib.consoleLog(prefix = "Error", message = "Unable to find the story \"" + name + "\".")
	selectStory()

# Loading story data
def loadStory(name):
	lib.consoleLog(message = "Do you want to load the story: \"" + name + "\"? (Y/N) ", newLine = "")

	# Checks if the input is valid.
	confirmation = lib.tryGetInput()

	if not confirmation:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		loadStory(name)
		return

	confirmation = confirmation.upper()

	# Checks if the input means "yes" or "no".
	# Repeats until it has a correct value.
	if not confirmation or (confirmation != "Y" and confirmation != "N"):
		loadStory(name)
		return

	# Check if the answer is negative. The loading is cancelled.
	if confirmation.strip() == "N":
		selectStory()
		return

	name = name.lower()

	lib.consoleLog(message = "Loading data...")

	# Load the corresponding story file.
	file = open("./universes/" + name + ".json", "r", encoding = "utf-8")
	data = json.loads(file.read())

	info, script = data.get("info"), data.get("script")

	if not info or not script:
		lib.consoleLog(prefix = "Error", message = "Game data error.")
		selectStory()
		return

	# Displays some key information about the story.
	print()
	print("~ " + info.get("title", "@Title") + " ~")
	print("By " + info.get("author", "@Author"))
	print("Language: " + info.get("language", "@Language"))
	print()
	print("-> " + info.get("description", "@Description"))
	print()

	playScript(script)

	file.close()

loadGame("Cuban")
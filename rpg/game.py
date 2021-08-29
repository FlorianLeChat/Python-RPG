#
# Story selection
#
from pathlib import Path
import lib

games = lib.findFiles("*.json", "./rpg/data")
titles = []

for game in games:
	titles.append(Path(game).stem.capitalize())

def selectStory():
	lib.consoleLog(message = "Welcome to the text-based storytelling experience.")
	lib.consoleLog(message = "To begin, please write that you want to play.")

	# Iterating through all the stories.
	length = len(titles)

	if length == 0:
		lib.consoleLog(prefix = "Error", message = "No story found in the directory \"../rpg/data/\".")
		exit()
	else:
		for title in titles:
			print("- " + title)

	# Checks if the input is valid.
	name = lib.tryGetInput()

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

#
# Loading story data
#
import json

ACTUAL_STORY_NAME = ""

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

	# Checks if the answer is negative. The loading is cancelled.
	if confirmation.strip() == "N":
		selectStory()
		return

	# Saves the name of the story that is going to be read.
	name = name.lower()

	global ACTUAL_STORY_NAME
	ACTUAL_STORY_NAME = name

	# Loads the story file.
	file = Path("./rpg/data/" + name + ".json")

	if not file.exists():
		lib.consoleLog(prefix = "Error", message = "Missing story file.")
		selectStory()
		return

	file = file.open(encoding = "utf-8")
	data = json.loads(file.read())

	lib.consoleLog(message = "Loading story data...")

	# Checks if the story data is valid.
	info, script = data.get("info"), data.get("script")

	if not info or not script:
		lib.consoleLog(prefix = "Error", message = "Story data error.")
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

	# Waits for the user's confirmation to start reading.
	print("Press something to continue...")
	lib.tryGetInput("Tip: you have to press ENTER/SPACE to display/speed up the dialogues.\n")

	playScript(script)

#
# Playing game script
#
import settings

def playScript(script, start = 1):
	lib.consoleLog(message = "Start reading the script...")
	print()

	# Iterating across all lines of the story.
	# And asks for a confirmation to continue.
	for index in range(start, len(script)):
		readField(index, script[str(index)])
		lib.tryGetInput()
		time.sleep(settings.WAIT_TIME)

	lib.consoleLog(message = "End of the script reading...")

#
# Story processing
#
import time, re, keyboard, random, storage

COOLDOWN = True

def handleInput():
	# Remove the delay between each field on a keyboard input.
	global COOLDOWN
	COOLDOWN = False

keyboard.add_hotkey("space", handleInput)

def showText(prefix = "", value = "", _type = "", shouldWait = True):
	# Checks if the text is not a string.
	if type(value) is list:
		value = " ".join(value)

	if _type == "narrator":
		# Prefix are placed to indicate that it's the narrator.
		print(prefix, end = "")
	elif _type == "dialog":
		# Search for all prefixes like "<character name:>" before
		# putting a line break ("\n") between each.
		prefixes = re.findall("\w+:", value)

		for prefix in prefixes:
			position = value.find(prefix)

			if position > 0:
				value = value[:position] + "\n" + value[position:]
	else:
		# Adds a prefix for the action fields.
		value = prefix + value

	# Resets the wait time status for the other dialogs.
	global COOLDOWN
	COOLDOWN = True

	# Displays each letter progressively with a waiting time between each one.
	# And asks for a confirmation to continue (dialogs only).
	for character in value:
		if character == "\n":
			keyboard.wait("enter")
			COOLDOWN = True

		print(character, end = "")
		time.sleep(COOLDOWN and settings.FADE_TIME or 0)

	# Waits for any user input.
	if shouldWait == True:
		keyboard.wait("enter")
		print()

def doAction(index, data):
	# Displays a description of the current situation before the action.
	showText("Action -> ", data.get("description", "@Description"))

	# Checks if there is a required value (to make a roll or remember a previous action).
	requirement = data.get("requirement")

	if not requirement:
		return

	success = False

	if lib.tryGetNumber(requirement):
		# Roll over 100 as if to simulate a probability.
		roll = random.randrange(1, 100)
		success = roll >= requirement

		showText("Roll <-> ", str(roll) + "/100 (>=" + str(requirement) + " required)")

		# Saves the result of the action for the next scenes.
		storage.saveData(ACTUAL_STORY_NAME, "actions", str(index), success and "2" or "1")
	elif requirement.find("@"):
		# Retrieve the result of the previous scenes.
		requirement = requirement.split("@")

		result = storage.loadData(ACTUAL_STORY_NAME, "actions", requirement[0], "0")
		success = result == requirement[1]
	else:
		# No value is required, the result is displayed.
		success = True

	# Displays the result text for this action.
	if success:
		showText("Action <- ", data.get("results", ["", "@Success"])[1])
	else:
		showText("Action <- ", data.get("results", ["@Failed"])[0])

def readField(index, data):
	# Checks if the field has notes.
	type = data.get("type", "narrator")
	note = data.get("note", "")

	if note != "" and settings.DEBUG_MODE == True:
		print("Note: " + note)

	# Checks the field type.
	if type == "narrator" or type == "dialog":
		showText("**", data.get("data"), type)
	elif type == "action":
		doAction(index, data)

#
# End of file
#
#selectGame()
loadStory("Cuban")
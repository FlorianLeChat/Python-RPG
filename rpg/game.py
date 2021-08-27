#
# Story selection
#
from pathlib import Path
import lib

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

#
# Loading story data
#
import json

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
	file = open("./rpg/data/" + name + ".json", "r", encoding = "utf-8")
	data = json.loads(file.read())
	file.close()

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
		readField(script[str(index)])
		lib.tryGetInput()
		time.sleep(settings.WAIT_TIME)

	lib.consoleLog(message = "End of the script reading...")

#
# Story processing
#
import time, re, keyboard, random

cooldown = True

def handleInput():
	# Remove the delay between each field on a keyboard input.
	global cooldown
	cooldown = False

keyboard.add_hotkey("space", handleInput)

def showText(fieldValue = "", fieldType = "", shouldWait = True):
	# Checks if the text is not a string.
	if type(fieldValue) is list:
		fieldValue = " ".join(fieldValue)

	if fieldType == "narrator":
		# Two points are placed to indicate that it's the narrator.
		print("**", end = "")
	elif fieldType == "dialog":
		# Search for all prefixes like "<character name:>" before
		# putting a line break ("\n") between each.
		prefixes = re.findall("\w+:", fieldValue)

		for prefix in prefixes:
			position = fieldValue.find(prefix)

			if position != 0:
				fieldValue = fieldValue[:position] + "\n" + fieldValue[position:]

	# Resets the wait time status for the other dialogs.
	global cooldown
	cooldown = True

	# Displays each letter progressively with a waiting time between each one.
	# And asks for a confirmation to continue (dialogs only).
	for character in fieldValue:
		if character == "\n":
			keyboard.wait("enter")
			cooldown = True

		print(character, end = "")
		time.sleep(cooldown and settings.FADE_TIME or 0)

	# Waits for any user input.
	if shouldWait == True:
		keyboard.wait("enter")
		print()

def doAction(data):
	#
	showText("Action -> " + data.get("description", "@Description"))

	#
	requirement = data.get("requirement")

	if not requirement:
		return

	if lib.tryGetNumber(requirement):
		#
		roll = random.randrange(1, 100)

		showText("Roll <-> " + str(roll) + "/100 (>=" + str(requirement) + " required)")

		if roll >= requirement:
			showText("Action -> " + data.get("results", ["@Success"])[0])
		else:
			showText("Action <- " + data.get("results", ["@Failure"])[1])
	else:
		#
		pass

def readField(data):
	# Checks if the field has notes.
	type = data.get("type", "narrator")
	note = data.get("note", "")

	if note != "" and settings.DEBUG_MODE == True:
		print("Note: " + note)

	# Checks the field type.
	if type == "narrator" or type == "dialog":
		showText(data.get("data"), type)
	elif type == "action":
		doAction(data)

#
# End of file
#
#selectGame()
loadStory("Cuban")
#
# Password check
#
import lib

def checkPassword():
	lib.consoleLog(message = "Enter the password to continue: ", newLine = "")

	value = lib.tryGetInput()

	# Checks if the input is valid.
	if not value:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		checkPassword()
		return

	# Checks if the input is a number.
	if not lib.tryGetNumber(value):
		lib.consoleLog(prefix = "Error", message = "Password is invalid.")
		checkPassword();
		return

	# Checks if the input matches "27412".
	if int(value) != 27412:
		lib.consoleLog(prefix = "Error", message = "Password is incorrect.")
		checkPassword();
		return

	lib.consoleLog(message = "User authenticated.")

#
# Selection of the gamemode
#
import importlib

modes = ["RPG Story Reader", "RPG Story Creator [WIP]", "Debug/Test"]

def selectGamemode():
	lib.consoleLog(message = "Which gamemode do you want to use now?")

	# Iterates through all gamemodes.
	for index in range(len(modes)):
		lib.consoleLog(message = str(index + 1) + "- " + modes[index])

	selection = lib.tryGetInput()

	# Checks if the input is valid.
	if not selection:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		selectGamemode()
		return

	# Checks if the input is a number.
	if not lib.tryGetNumber(selection):
		lib.consoleLog(prefix = "Error", message = "Invalid number.")
		selectGamemode()
		return

	# Checks the gamemode selection before redirecting it to the appropriate file.
	selection = int(selection)

	if selection == 1:
		importlib.import_module("game")
	elif selection == 2:
		lib.consoleLog(message = "Not Yet Implemented.")
		pass # NYI
	elif selection == 3:
		importlib.import_module("testing")
	else:
		lib.consoleLog(prefix = "Error", message = "Unable to find the gamemode.")
		selectGamemode()

#
# Program end signal
# https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
#
import signal, sys

def exitHandler(signum, frame):
	sys.exit()

signal.signal(signal.SIGINT, exitHandler)

#
# End of file
#
import settings

print("------------------- PYTHON RPG ------------------")
print("-- https://github.com/FlorianLeChat/Python-RPG --")
print("-------------------------------------------------")

if settings.DEBUG_MODE == False:
	checkPassword()

selectGamemode()

#
# End of program
#
import keyboard

print("The story is over, thanks for using my program! :D")
keyboard.wait()
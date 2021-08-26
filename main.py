# Password check
import lib, importlib

def checkPassword():
	lib.consoleLog(message = "Enter the password to continue: ", terminator = "")

	value = lib.tryGetInput()

	if not value:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		checkPassword()
		return

	if not lib.tryGetNumber(value):
		lib.consoleLog(prefix = "Error", message = "Password is invalid.")
		checkPassword();
		return

	if int(value) != 27412:
		lib.consoleLog(prefix = "Error", message = "Password is incorrect.")
		checkPassword();
		return

	lib.consoleLog(message = "User authenticated.")

# Selection of the gamemode
modes = ["RPG [WIP]", "Auto-Development [Unavailable]", "Debug/Test [OK]"]

def selectGamemode():
	lib.consoleLog(message = "Which gamemode do you want to use now?")

	for index in range(len(modes)):
		lib.consoleLog(message = str(index + 1) + "- " + modes[index])

	selection = lib.tryGetInput()

	if not selection:
		lib.consoleLog(prefix = "Error", message = "Invalid input.")
		selectGamemode()
		return

	if not lib.tryGetNumber(selection):
		lib.consoleLog(prefix = "Error", message = "Invalid number.")
		selectGamemode()
		return

	selection = int(selection)

	if selection == 1:
		importlib.import_module("game")
	elif selection == 2:
		lib.consoleLog(message = "Not Yet Implemented.")
		pass # NYI
	elif selection == 3:
		importlib.import_module("test")
	else:
		lib.consoleLog(prefix = "Error", message = "Unable to find the gamemode.")
		selectGamemode()

# EOF
checkPassword()
selectGamemode()
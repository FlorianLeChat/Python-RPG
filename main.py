# Password check
import lib, importlib

def checkPassword():
	value = lib.getInput("Enter the password to continue: ")

	if not value:
		print("Invalid input.")
		checkPassword()
		return

	if not lib.tryNumber(value):
		print("Password is invalid.")
		checkPassword();
		return

	if int(value) != 27412:
		print("Password is incorrect.")
		checkPassword();
		return

# Selection of the gamemode
modes = ["RPG [WIP]", "Auto-Development [Unavailable]", "Debug/Test [OK]"]

def selectGamemode():
	print("Which gamemode do you want to use now?")

	for index in range(len(modes)):
		print(str(index + 1) + "-", modes[index])

	selection = lib.getInput()

	if not selection:
		print("Invalid input.")
		selectGamemode()
		return

	if not lib.tryNumber(selection):
		print("Invalid number.")
		selectGamemode()
		return

	selection = int(selection)

	if selection == 1:
		importlib.import_module("game")
	elif selection == 2:
		print("Not Yet Implemented.")
		pass # NYI
	elif selection == 3:
		importlib.import_module("test")
	else:
		print("Unable to find the gamemode.")
		selectGamemode()

# EOF
checkPassword()
selectGamemode()
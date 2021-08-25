# Password check
import lib, importlib

def checkPassword():
	value = input("Enter the password to continue: ")

	if not lib.tryNumber(value):
		print("Password is invalid.")
		checkPassword();
		return

	if int(value) != 27412:
		print("Password is incorrect.")
		checkPassword();
		return

checkPassword()

# Selection of the gamemode
modes = ["RPG [WIP]", "Auto-Development [Unavailable]", "Debug/Test [OK]"]

def selectGamemode():
	print("Which gamemode do you want to use now?")

	for index in range(len(modes)):
		print(str(index + 1) + "-", modes[index])

	selection = input()

	if not lib.tryNumber(selection):
		print("Error!")
		selectGamemode()
		return

	selection = int(selection)

	if selection == 1:
		importlib.import_module("game")
	elif selection == 2:
		print("Not Yet Implemented")
		pass # NYI
	elif selection == 3:
		importlib.import_module("test")
	else:
		print("Unable to find the gamemode.")
		selectGamemode()

selectGamemode()
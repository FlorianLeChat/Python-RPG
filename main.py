# Password check
import lib, importlib

password = input("Enter the password to continue: ")

if not lib.tryNumber(password):
	print("Password is invalid.")
	exit()

if int(password) != 27412:
	print("Password is incorrect.")
	exit()

# Selection of the gamemode
modes = ["RPG [WIP]", "Auto-Development [Unavailable]", "Debug/Test [OK]"]

print("Which mode do you want to use now?")

for index in range(len(modes)):
	print(str(index + 1) + "-", modes[index])

selection = input()

if not lib.tryNumber(selection):
	print("Error!")

selection = int(selection)

if selection == 1:
	importlib.import_module("game")
elif selection == 2:
	pass # NYI
elif selection == 3:
	importlib.import_module("test")
else:
	print("Impossible to find the gamemode.")
	exit()
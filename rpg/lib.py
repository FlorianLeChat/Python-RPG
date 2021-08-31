#
# Try to check if the input is a number.
# https://stackoverflow.com/a/1267145
#
def tryGetNumber(value = ""):
	try:
		return int(value)
	except ValueError:
		return False

#
# Try to retrieve the input from the usage by checking the termination
# controls like CTRL+C to stop the program.
#
def tryGetInput(prompt = ""):
	try:
		return input(prompt)
	except KeyboardInterrupt:
		return False

#
# Checks if the string is a loadable JSON object.
# https://stackoverflow.com/a/5508597
#
import json

def tryGetJSON(value = ""):
	try:
		return json.loads(value)
	except ValueError:
		return False

#
# Displays a message in the output terminal formatted for the RPG project.
#
def consoleLog(prefix = "Info", message = "", newLine = "\n"):
	print("[" + prefix + "] " + message, end = newLine, flush = True)

#
# Returns a list of files inside a single folder.
# https://stackoverflow.com/a/1724723
#
import os, fnmatch

def findFiles(pattern, path):
	result = []

	for root, _, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))

	return result
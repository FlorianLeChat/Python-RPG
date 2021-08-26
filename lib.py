# Try to check if the input is a number
# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def tryNumber(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

# Try to retrieve the input from the usage by checking the termination
# controls like CTRL+C to stop the program.
def getInput(prompt = ""):
	try:
		return input(prompt)
	except KeyboardInterrupt:
		return False

# Returns a list of files inside a single folder.
# https://stackoverflow.com/questions/1724693/find-a-file-in-python
import os, fnmatch

def findFiles(pattern, path):
	result = []

	for root, _, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))

	return result
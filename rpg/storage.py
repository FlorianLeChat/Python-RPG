#
# Save file handling
#
from pathlib import Path
import json, settings, lib

CACHE = {}

def saveFile():
	# Opens the file in write mode before converting the
	# JSON string into a Python object.
	file = open(settings.SAVE_FILE_NAME, mode = "w", encoding = "utf-8")

	global CACHE
	json.dump(CACHE, file, ensure_ascii = False, indent = 4)

	file.close()

def loadFile():
	file = Path(settings.SAVE_FILE_NAME)

	if file.exists():
		# Opens the file in read mode before converting the
		# cache to a JSON string for saving.
		file = file.open(mode = "r", encoding = "utf-8")
		json = lib.tryGetJSON(file.read())

		if json:
			global CACHE
			CACHE = json

		file.close()

#
# Save data handling
#
def debugLog(prefix = "Error", args = ""):
	# Only in debug mode.
	if settings.DEBUG_MODE == True and args != "":
		lib.consoleLog(prefix, args)

def saveData(name, field, key = "none", value = ""):
	# Retrieves all data related to the targeted story.
	data = CACHE.get(name)

	if not data:
		CACHE[name] = {}
		debugLog(args = "Missing story \"" + str(name) + "\" in cache, creating...")

	# Checks if the field is valid.
	data = CACHE[name].get(field)

	if not data:
		CACHE[name][field] = {}
		debugLog(args = "Missing field \"" + str(field) + "\" in cache, creating...")

	# Checks if the value requires a key to be saved
	# or directly a save in the field.
	if key != "none":
		CACHE[name][field][key] = value
		debugLog(prefix = "Info", args = "Insert the key \"" + str(key) + "\" with the value \"" + str(value) + "\".")
	else:
		CACHE[name][field] = value
		debugLog(prefix = "Info", args = "Insert the key \"" + str(field) + "\" with the value \"" + str(value) + "\".")

	# Finally saves the file after the transaction.
	saveFile()
	debugLog(prefix = "Info", args = "Cache file successfully saved.")

def loadData(name, field, key = "none", fallback = ""):
	# Loads the data and checks if they are valid.
	data = CACHE.get(name)

	if not data:
		debugLog(args = "The save data is missing or invalid.")
		return fallback

	# Checks if the data in the fields are valid before retrieving them.
	index = data.get(field)

	if not index:
		debugLog(args = "The previous scene data is incomplete or invalid.")
		return fallback

	# Returns the value in the field key or its name.
	name = name.capitalize()

	if key != "none":
		debugLog(prefix = "Info", args = "Data retrieved: \"" + str(field) + "\" -> \"" + str(key) + "\" @ " + name)
		return index.get(key, fallback)
	else:
		debugLog(prefix = "Info", args = "Data retrieved: \"" + str(field) + "\" -> \"" + str(index) + "\" @ " + name)
		return index

#
# End of file
#
loadFile()
#
# Internal storage
#
from pathlib import Path
import json, settings, lib

file = Path("./rpg/data/__internal__.json")
cache = {}

if file.exists():
	# Loads the save data if it exists.
	file = file.open(encoding = "utf-8")
	cache = json.loads(file.read())

def debugLog(prefix = "Error", args = ""):
	# Only in debug mode.
	if settings.DEBUG_MODE == True and args != "":
		lib.consoleLog(prefix, args)

def saveData(name, field, key = "none", value = ""):
	# Retrieves all data related to the targeted story.
	data = cache.get(name)

	if not data:
		cache[name] = {}

	# Checks if the field is valid.
	data = cache[name].get(field)

	if not data:
		cache[name][field] = {}

	# Checks if the value requires a key to be saved
	# or directly a save in the field.
	if key != "none":
		cache[name][field][key] = value
	else:
		cache[name][field] = value

def loadData(name, field, key = "none", fallback = ""):
	# Loads the data and checks if they are valid.
	data = cache.get(name)

	if not data:
		debugLog(args = "The save data is missing or invalid.")
		return fallback

	# Checks if the data in the fields are valid before retrieving them.
	index = data.get(field)

	if not index:
		debugLog(args = "The previous scene data is incomplete or invalid.")
		return fallback

	debugLog(prefix = "Info", args = "Data retrieved: \"" + field + "\" -> \"" + key + "\" @ " + name.capitalize())

	# Returns the value in the field key or its name.
	return key != "none" and index.get(key, fallback) or index
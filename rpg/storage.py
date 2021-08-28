#
# Internal storage
#
from pathlib import Path
import json, settings, lib

PATH_NAME = "./rpg/data/__internal__.json"

# Loads data of stories through the file system
# In case of failure, a fallback value is returned.
def loadData(name, index, fallback):
	# Checks if the file exists.
	file = Path(PATH_NAME)

	if not file.exists():
		return fallback

	# Loads the data and checks if they are valid.
	file = file.open(encoding = "utf-8")
	data = json.loads(file.read())

	data = data.get(name)

	if not data:
		return fallback

	# Checks if the data in the fields are valid
	# before retrieving them.
	actions = data.get("actions")

	if not actions:
		return fallback

	return actions.get(index, fallback)
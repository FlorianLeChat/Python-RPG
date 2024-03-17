# 📖 Python-RPG

> [!CAUTION]
> **This project is no longer maintained since March 2024. If you intend to run the whole or some part of my source code, please be aware that some dependencies will be outdated and you expose yourself to security vulnerabilities if proper safeguards are not enforced.**

Here is a small program which will allow you to build and read interactive stories in text format. For the moment, the stories are quite simplistic and have no advanced interaction except the basics: narration, action, consequence and dialogues. Later (maybe) the program will be able to handle more complex interactions.

At the moment, the program is written entirely in [Python](https://www.python.org/) and has been tested **only** on Windows, however due to the lack of compatibility with Linux/MacOS on some libraries, **I will not provide an executable for these versions to avoid complaints.** However, you have all the necessary files to compile it manually if needed (see below).

I created this program to learn this programming language and it's possible (even **probable**) that there are beginner and obvious mistakes, so I am quite open to improve this code via pull requests. Moreover, if you want to create stories, you must use the `data` folder for this purpose and then create a [JSON](https://en.wikipedia.org/wiki/JSON) file to write your story. If you don't know where to start, use the [default stories](https://github.com/FlorianLeChat/Python-RPG/tree/master/data) available. Don't be afraid to make mistakes, the program has some safeguards to prevent loading wrong stories. I will make sure in the future that you can create stories directly in the program.

![image](https://user-images.githubusercontent.com/26360935/131666926-4e3a4ab4-5513-4f7a-af97-b4fffb84dfd7.png)

## External libraries used

- [Keyboard](https://pypi.org/project/keyboard/)
- [pywin32](https://pypi.org/project/pywin32/)

## Manual compilation

> Requires (Python 3.9 or higher with [pyinstaller](https://pypi.org/project/pyinstaller/))
- Open the command prompt pointing to the scripts folder then enter this:
- `pyinstaller --onefile main.py --hidden-import game --hidden-import lib --hidden-import settings --hidden-import storage --hidden-import testing --icon=app.ico --clean`

## Story creation

First, go to the `data` folder and create a folder with a pretty explicit name so you can find it later. For example, we will create the file `sunday.json` (if you can't change the extension, copy/paste an existing file or go [here](https://helpdeskgeek.com/windows-10/how-to-change-file-type-in-windows-10/)).

Then copy/paste this before filling in your story information between "< >".
```
{
	"info":
	{
		"author": "<Your name>",
		"language": "<english>",
		"title": "<A classic Sunday.>",
		"description": "<It's Sunday and you are resting peacefully in your luxuriant garden.>"
	},

	"script":
	{
	}
}
```

Once this is done, you can choose between three types of fields: `narration`, `dialog` and `action`. Here is an example for each. **Be careful**, when adding fields, you must fill in the number (**in order, starting at 0**) in the upper left corner.

```
"0": {
	"type": "narrator",
	"data": [
		"Sunday is a wonderful day.",
		"The birds are singing, your children are running around and having fun.",
		"Your wife is reading her favorite books."
	]
},

"1": {
	"type": "dialog",
	"data": [
		"You: Easy kids, don't hurt yourself.",
		"Childrens: Don't worry daddy *Laughs*"
	]
},

"2": {
	"type": "action",
	"description": "Your fresh glass of water seems empty, you try to stand up but you almost fall to the ground.",
	"requirement": 50,
	"results": [
		"You are destabilized before falling to the ground, without severity.",
		"You catch yourself just before you fall and resume your walk to the kitchen."
	]
}
```

These fields **must** be added in the `script` part visible in the previous paragraph (if you still don't know where to put this, feel free to open the [existing stories](https://github.com/FlorianLeChat/Python-RPG/tree/master/data) to get an idea, they are simple to understand).

Notice there is a `note` field which is not visible in the examples but only works in the debug mode if you want to use this program on your side as a fork.

Last thing, the `requirement` field defines  if the action of the protagonist will succeed. If the value in this field is a **number**, then a number between **0 and 100** will be randomly chosen to determine if this number is greater than the one that is filled in. If it is a **string** in the form of `<field number>@<success state>` then the program will check the results of the previous scenes. For example `4@1` will check if in scene number **4**, the action failed (**1**) or succeeded (**2**). Depending on the result, it will return the appropriate sentence (first or second sentence you filled).

**If the field isn't filled, then the action will automatically succeed.**

## Note

- The password of the program is **27412**. Have you never seen this before? I know it's just to check if you read until the end :D
- When you are going to use the program, a file called `__internal__.json` will be created to store some things, avoid touching it unless you know how it works.

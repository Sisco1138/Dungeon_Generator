Dungeon Generator
=================

Dungeon Generator is a Python tool for dynamically creating dungeon layouts, ideal for RPG campaigns, game development, and procedural storytelling. It allows users to randomly generate rooms, hallways, traps, and treasures, as well as save and load dungeon layouts for continued editing.

Features
--------
- Randomized Dungeon Layout: Dynamically generates hallways, rooms, traps, and treasures with descriptions, making each layout unique.
- Dungeon Naming: Each dungeon can be personalized with a custom name.
- Save and Load Functionality: Save your current dungeon layout as a JSON file and load it later for continued editing.
- Layout Review: View the full dungeon layout in sequence for easy tracking and reference.

Requirements
------------
- Python 3.x: Make sure you have Python installed.
- JSON Support: The script uses Python's built-in `json` library to save and load files.

Getting Started
---------------
1. Clone or Download this repository to your local machine.
2. Run the script:

---------------
- There are two version of the script:
1. Dungeon_Generator
2. Dungeon_Generator_IOS

The IOS Version of the script can be downloaded on an ipad or iPhone and opened with the Pythonista app (the app i use) for an on the go experience, works exactly the same but was modified to be able to have the save feature work on IOS

-----------------
Usage
-----
- Start a New Dungeon: Enter a custom name for your dungeon at the beginning of the session.
- Add Elements:
  - Type `hallway`, `room`, `trap`, or `treasure` to add a randomly generated element to your dungeon.
  - Each element comes with a unique description to add variety.
- Review the Layout: Type `layout` to display the full dungeon layout so far.
- Save the Dungeon: Type `save` to save your layout to a JSON file with the dungeon’s name.
- Load an Existing Dungeon: Restart the script and enter the name of a previously saved dungeon to continue editing.

Example Output
--------------
Dungeon Layout So Far:
- Shrine/Altar Room with flickering torchlight
- Narrow Hallway with damp and musty air
- Trap: Swinging Blades/Pendulums
- Treasure: Rare Gemstone

Saving and Loading Dungeons
---------------------------
The dungeon generator saves each dungeon as a JSON file in the `~/Documents` folder (Pythonista on iOS) or the current working directory on other platforms.

License
-------
This project is licensed under the MIT License.

Contributing
------------
Contributions are welcome! If you have ideas for new features, bug fixes, or enhancements, feel free to reach out.

Feedback
--------
For any feedback, suggestions, or support requests, feel free to reach out.

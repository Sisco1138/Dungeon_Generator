Dungeon Generator
=================

Dungeon Generator is a Python tool for dynamically creating dungeon layouts, ideal for RPG campaigns, game development, and procedural storytelling. It allows users to randomly generate rooms, hallways, traps, and treasures, as well as save and load dungeon layouts for continued editing.

Features
--------
 - Randomized Dungeon Layout: Dynamically generates hallways, rooms, traps, and treasures with descriptions, making each layout unique.

 - Dungeon Naming: Each dungeon can be personalized with a custom name.

 - Save and Load Functionality: Save your current dungeon layout as a JSON file and load it later for continued editing.

 - ASCII Art for Each Component: Each room or hallway has a unique ASCII art representation, which can be displayed in the console or saved to an Excel file.

 - Export Layout to Excel: Exports the full dungeon layout to an Excel file with ASCII art preserved in individual cells for a visual overview.

 - Re-roll Feature: Allows users to re-roll rooms or hallways if they want different options for a better flow in the dungeon layout.

 - Coordinate-based Room Placement: Users can specify coordinates for each room, hallway, or trap (e.g., (0,1), (1,1)), allowing for detailed placement control.

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
1. Dungeon_Generator Ver.1.1.0
2. Dungeon_Generator_IOS Ver.1.0.0

The IOS Version of the script can be downloaded on an iPad or iPhone and opened with the Pythonista app (the app i use) for an on the go experience, works exactly the same but was modified to be able to have the save feature work on IOS

(NOTE: THE IOS VERSION DOES NOT SUPPORT THE ASCII ART YET)

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
The dungeon generator saves each dungeon as a JSON file in the ~/Documents folder (for Pythonista on iOS) or the current working directory on other platforms.

ASCII Art Export to Excel Each room or hallway's ASCII art representation is exported into a single cell in the Excel sheet. The text wrapping is enabled for each cell to preserve the multi-line ASCII art layout.

(NOTE: ASCII Art in excel sheet still very buggy, currently only works in terminal)
License
-------
This project is licensed under the MIT License.

Contributing
------------
Contributions are welcome! If you have ideas for new features, bug fixes, or enhancements, feel free to reach out.

Feedback
--------
For any feedback, suggestions, or support requests, feel free to reach out.

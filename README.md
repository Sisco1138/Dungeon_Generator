- 👋 Hi, I’m @Sisco1138
- 🌱 I’m currently learning python
- 💞️ I’m looking to collaborate on any projects to help me improve my skills

<!---
Sisco1138/Sisco1138 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
**Dungeon Generator Ver. 1.1.0**
Dungeon Generator is a Python tool for dynamically creating dungeon layouts, ideal for RPG campaigns, game development, and procedural storytelling. It allows users to randomly generate rooms, hallways, traps, and treasures, as well as save and load dungeon layouts for continued editing. ASCII art is also generated to visually represent the dungeon components.

**Features**
- Randomized Dungeon Layout: Dynamically generates hallways, rooms, traps, and treasures with descriptions, making each layout unique.
- Dungeon Naming: Each dungeon can be personalized with a custom name.
- Save and Load Functionality: Save your current dungeon layout as a JSON file and load it later for continued editing.
ASCII Art for Each Component: Each room or hallway has a unique ASCII art representation, which can be displayed in the console or saved to an Excel file.
- Export Layout to Excel: Exports the full dungeon layout to an Excel file with ASCII art preserved in individual cells for a visual overview.
- Re-roll Feature: Allows users to re-roll rooms or hallways if they want different options for a better flow in the dungeon layout.
- Coordinate-based Room Placement: Users can specify coordinates for each room, hallway, or trap (e.g., (0,1), (1,1)), allowing for detailed placement control.
  
**Requirements**
- Python 3.x: Ensure Python is installed on your machine.
- openpyxl: Used for exporting dungeon layouts to Excel files.

bash
pip install openpyxl

- JSON Support: The script uses Python's built-in json library to save and load files.
  
**Getting Started**
1. Clone or Download this repository to your local machine.
2. Install the required packages:
   
bash
pip install -r requirements.txt

3. Run the script:

**Versions**
There are two versions of the script available:

1. Dungeon_Generator.py - For general use on desktops.
2. Dungeon_Generator_IOS.py - For iOS devices using the Pythonista app, with slight modifications for saving functionality on iOS.

The iOS version of the script can be downloaded to an iPad or iPhone and opened with Pythonista for an on-the-go experience. It functions similarly but was modified to enable the save feature on iOS.

(NOTE: THE IOS VERSION DOES NOT SUPPORT THE ASCII ART YET)

**Usage**
1. Start a New Dungeon: Enter a custom name for your dungeon at the beginning of the session.
2. Add Elements:
   - Type hallway, room, trap, or treasure to add a randomly generated element to your dungeon.
   - Each element comes with a unique description to add variety.
   - Use the Re-roll Feature by typing n when prompted to re-roll a room or hallway, or y to keep it.
   - Specify the coordinates for each component by typing coordinates in x,y format (e.g., 0,1 or -1,2).
3. Review the Layout: Type layout to display the full dungeon layout so far.
4. View ASCII Map: Type map to see an ASCII art overview of the dungeon layout.
5. Export to Excel: Type excel to save the dungeon layout to an Excel file. Each room or hallway's ASCII art is consolidated into a single cell.
6. Save the Dungeon: Type save to save your layout to a JSON file with the dungeon’s name.
7. Load an Existing Dungeon: Restart the script and enter the name of a previously saved dungeon to continue editing.

**Example Output**
Dungeon Layout So Far:

- Shrine/Altar Room with flickering torchlight
- Narrow Hallway with damp and musty air
- Trap: Swinging Blades/Pendulums
- Treasure: Rare Gemstone

**Saving and Loading Dungeons**
The dungeon generator saves each dungeon as a JSON file in the ~/Documents folder (for Pythonista on iOS) or the current working directory on other platforms.

**ASCII Art Export to Excel**
Each room or hallway's ASCII art representation is exported into a single cell in the Excel sheet. The text wrapping is enabled for each cell to preserve the multi-line ASCII art layout.

(NOTE: ASCII Art in excel sheet still very buggy, currenlty only works in terminal)

**License**
This project is licensed under the MIT License.

**Contributing**
Contributions are welcome! If you have ideas for new features, bug fixes, or enhancements, feel free to reach out.

**Feedback**
For any feedback, suggestions, or support requests, feel free to reach out.

****

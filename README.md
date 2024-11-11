- 👋 Hi, I’m @Sisco1138
- 🌱 I’m currently learning python
- 💞️ I’m looking to collaborate on any projects to help me improve my skills

<!---
Sisco1138/Sisco1138 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
# Dungeon Generator

**Dungeon Generator** is a Python tool for dynamically creating dungeon layouts, ideal for RPG campaigns, game development, and procedural storytelling. It allows users to randomly generate rooms, hallways, traps, and treasures, as well as save and load dungeon layouts for continued editing.

## Features

- **Randomized Dungeon Layout**: Dynamically generates hallways, rooms, traps, and treasures with descriptions, making each layout unique.
- **Dungeon Naming**: Each dungeon can be personalized with a custom name.
- **Save and Load Functionality**: Save your current dungeon layout as a JSON file and load it later for continued editing.
- **Layout Review**: View the full dungeon layout in sequence for easy tracking and reference.

## Requirements

- **Python 3.x**: Make sure you have Python installed. This script was developed in Python 3 and may not be compatible with Python 2.
- **JSON Support**: The script uses Python's built-in `json` library to save and load files, so no additional installations are needed.

## Getting Started

### Installation

1. **Clone or Download** this repository to your local machine:
   ```bash
   git clone https://github.com/Sisco1138/dungeon-generator.git
   cd dungeon-generator
2. Run the Script
python dungeon_generator.py

**Versions**
Dungeon_Generator: Main version for use on desktops and other devices.
Dungeon_Generator_IOS: Modified version compatible with iOS (Pythonista app), allowing for mobile use and adjusted save functionality.

**Usage**
1. **Start a New Dungeon**: Enter a custom name for your dungeon at the beginning of the session.
2. **Add Elements**:
  - Type hallway, room, trap, or treasure to add a randomly generated element to your dungeon.
  - Each element comes with a unique description to add variety.
3. **Review the Layout**: Type layout to display the full dungeon layout so far.
4. **Save the Dungeon**: Type save to save your layout to a JSON file with the dungeon’s name.
5. **Load an Existing Dungeon**: Restart the script and enter the name of a previously saved dungeon to continue editing.

**EXAMPLE OUTPUT** 
Dungeon Layout So Far:
- Shrine/Altar Room with flickering torchlight
- Narrow Hallway with damp and musty air
- Trap: Swinging Blades/Pendulums
- Treasure: Rare Gemstone

**Saving and Loading Dungeons**
The dungeon generator saves each dungeon as a JSON file in the ~/Documents folder (Pythonista on iOS) or the current working directory on other platforms.

**Sample JSON Output**
Here’s an example of a saved dungeon file (MyDungeon.json):

{
    "name": "MyDungeon",
    "layout": [
        "Shrine/Altar Room with flickering torchlight",
        "Narrow Hallway with damp and musty air",
        "Trap: Swinging Blades/Pendulums",
        "Treasure: Rare Gemstone"
    ]
}

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Contributing**
Contributions are welcome! If you have ideas for new features, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

**Feedback**
For any feedback, suggestions, or support requests, feel free to reach out or open an issue on this GitHub repository.

****

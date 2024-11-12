import random
import json
import os

# Dungeon Generator
# Copyright (c) 2024 Sisco1138
# Licensed under the MIT License
# See the LICENSE file or https://opensource.org/licenses/MIT for full details.

"""
Dungeon Generator is a Python tool for creating randomized dungeon layouts,
ideal for RPG campaigns, game development, and procedural storytelling.

This program allows users to generate rooms, hallways, traps, and treasures
and save or load layouts for ongoing use.
"""

# Lists for dungeon components
hallway = [
    'Narrow Hallway', 'Straight Hallway', 'L-Shaped Hallway', "T-Junction", 
    'Crossroad', 'Curved Hallway', 'Staircase Hallway', 'Dead-End Hallway'
]
room = [
    'Shrine/Altar Room', 'Storage Room', 'Hidden Room', 'Trap Room', 
    'Puzzle Room', 'Treasure Room', 'Boss Room', 'Single-Door Room', 
    'Two-Door Room', 'Corner Room', 'Four-Door Room'
]
trap = [
    'Illusion/Disorientation Traps', 'Poisonous Gas Traps', 
    'Swinging Blades/Pendulums', 'Arrow/Dart Traps', 
    'Pitfalls', 'Spike Traps'
]
treasures = [
    'Pile of Gold Coins', 'Rare Gemstone', 'Ancient Sword', 
    'Potion of Healing', 'Enchanted Ring', 'Magic Scroll', 
    'Mysterious Artifact'
]
descriptions = [
    "flickering torchlight", "damp and musty", "echoes of distant footsteps", 
    "crumbling walls", "covered in cobwebs", "filled with a mysterious fog"
]

# Function to load a dungeon layout from JSON
def load_dungeon(name):
    filename = f"{name}.json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            dungeon_data = json.load(f)
            print(f"Dungeon '{name}' loaded successfully!")
            return dungeon_data
    else:
        print("Dungeon not found. Starting a new one.")
        return {"name": name, "layout": []}

# Function to save a dungeon layout to JSON
def save_dungeon(dungeon_data):
    # Save file to Pythonista's Documents directory
    filename = os.path.expanduser(f"~/Documents/{dungeon_data['name']}.json")
    with open(filename, 'w') as f:
        json.dump(dungeon_data, f, indent=4)
    print(f"Dungeon '{dungeon_data['name']}' saved successfully at {filename}!")

# Initialize the dungeon
dungeon_name = input("Enter a name for your dungeon: ").strip()
dungeon_data = load_dungeon(dungeon_name)

print("Welcome to the Dungeon Generator!")

while True:
    print("\nWhat would you like to add to your dungeon? (hallway, room, trap, treasure, def for definitions, layout to review, save to save, or quit to exit)")
    choice = input(": ").strip().lower()
    
    if choice == "hallway":
        hallway_choice = random.choice(hallway)
        hallway_description = random.choice(descriptions)
        final_hallway = f"{hallway_choice} with {hallway_description}"
        print("The next part of your dungeon is:", final_hallway)
        dungeon_data["layout"].append(final_hallway)
        
    elif choice == "room":
        room_choice = random.choice(room)
        room_description = random.choice(descriptions)
        final_room = f"{room_choice} with {room_description}"
        print("The next part of your dungeon is:", final_room)
        dungeon_data["layout"].append(final_room)
        
    elif choice == "trap":
        trap_choice = random.choice(trap)
        print("The next part of your dungeon is a trap:", trap_choice)
        dungeon_data["layout"].append(f"Trap: {trap_choice}")
        
    elif choice == "treasure":
        treasure_choice = random.choice(treasures)
        print("You've found a treasure:", treasure_choice)
        dungeon_data["layout"].append(f"Treasure: {treasure_choice}")
    
    elif choice == "layout":
        print("\nDungeon Layout So Far:")
        for part in dungeon_data["layout"]:
            print("-", part)
    
    elif choice == 'def':
        print("""
HALLWAYS
Straight Hallway – A simple, direct corridor.
L-Shaped Hallway – A hallway that takes a 90-degree turn.
T-Junction – Hallway splits into two branches, forming a "T" shape.
Crossroad (4-Way Junction) – Intersection with four directions.
Curved Hallway – Hallway that curves instead of a sharp angle.
Staircase Hallway – A hallway with stairs going up or down.
Dead-End Hallway – A hallway that ends abruptly, often a place for secrets.
Narrow Hallway – Tight, cramped hallway that restricts movement or visibility.

ROOMS
Single-Door Room – A simple room with one entry/exit.
Two-Door Room – Room with doors on opposite walls, often a passageway.
Corner Room (L-Room) – Room with two doors at a 90-degree angle, creating a corner.
Four-Door Room – Central room with a door on each wall, ideal for crossroads.
Boss Room – Large room designed for encounters with bosses or mini-bosses, often with unique features or obstacles.
Treasure Room – Room specifically for valuable loot or rewards, often locked or trapped.
Puzzle Room – Contains a puzzle or riddle that needs solving to proceed.
Trap Room – Room with traps, hidden or obvious, meant to challenge or harm players.
Hidden Room – Secret or concealed room accessible through special means, often contains rare items or lore.
Storage Room – Room filled with crates, barrels, or chests, potentially hiding items or enemies.
Shrine/Altar Room – Room with a magical or sacred object, sometimes used to save, heal, or trigger special events.

TRAPS
Spike Traps – Hidden spikes that activate when a pressure plate is triggered.
Pitfalls – Floor sections that give way, potentially leading to lower dungeon levels or damage.
Arrow/Dart Traps – Shoots projectiles from walls when triggered.
Swinging Blades/Pendulums – Set obstacles that players must time movements to avoid.
Poisonous Gas Traps – Fills the room with toxic gas, requiring quick escape or special items to withstand.
Illusion/Disorientation Traps – Warps perception, changes room appearance, or flips directions to confuse explorers.
        """)
    
    elif choice == "save":
        save_dungeon(dungeon_data)
    
    elif choice == "quit":
        print("Thank you for using the Dungeon Generator!")
        break
    
    else: 
        print("That is not an option. Please select one of the options: hallway, room, trap, treasure, def, layout, save, or quit.")

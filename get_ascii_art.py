# ascii_art.py

# ASCII Art representations of dungeon components

# Add more hallways, rooms, and configurations as needed

ASCII_ART = {
    "Straight_Hallway_Horizontal": """
    ------------
    ------------
    """,
    "Straight_Hallway_Vertical": """
    | |
    | |
    | |
    | |
    | |
    """,
    "L_Hallway_East_South": """
      ---------
      ------   |
           |   |
           |   |
           |   |   
    """,
    "L_Hallway_North_West": """
      ---------
      ------   |
           |   |
           |   |
           |   |   
    """,
    "L_Hallway_North_East": """
    ----------
    |   ------
    |   |
    |   |
    |   |
    """,
    "L_Hallway_West_South": """
    ----------
    |   ------
    |   |
    |   |
    |   |
    """,
    "L_Hallway_South_East": """
    
    |   |
    |   |
    |   |
    |   ------
    ----------
    """,
    "L_Hallway_West_North": """
    
    |   |
    |   |
    |   |
    |   ------
    ----------
    """,
    "L_Hallway_South_West": """
    
         |   |
         |   |
         |   |
    ------   |
    ----------
    """,
    "L_Hallway_Easr_North": """
    
         |   |
         |   |
         |   |
    ------   |
    ----------
    """,
    "T_Junction_Upward": """

         |   | 
         |   |
         |   |
         |   |
    ------   -------
    ------   -------
         |   |
    """,
    
    "T_Junction_Downward": """

         |   |
    ------   -------
    ------   -------
         |   |
         |   |
         |   |
         |   |
    """,
    "T_Junction_Left": """

         |   |
         |   |
         |   |
    ------   |
    ------   |
         |   |
         |   |
         |   |
  
    """,
    "T_Junction_Right": """

         |   |
         |   |
         |   |
         |   ------
         |   ------
         |   |
         |   |
         |   |
  
    """,
    "T_Junction_Right": """

         |   |
         |   |
         |   |
    ------   ------
    ------   ------
         |   |
         |   |
         |   |
  
    """,
    "Crossroad": """

         |   |
         |   |
         |   |
    ------   ------
    ------   ------
         |   |
         |   |
         |   |
  
    """,
        "Dead_End_Hallway_North": """

         _____  
         |   |
         |   |
         |   |
         |   |
  
    """,
        "Dead_End_Hallway_South": """
 
         |   |
         |   |
         |   |
         |   |
         _____

    """,
"Dead_End_Hallway_East": """
 
    ------------|
    ------------|

    """,
"Dead_End_Hallway_West": """
 
    |------------
    |------------

    """,
"Single_Door_Room_North": """
 
    |-------------|
    |             |
    |             |
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Single_Door_Room_South": """
 
    |----|   |----|
    |             |
    |             |
    |             |
    |             |
    |_____________|

    """,
"Single_Door_Room_East": """
 
    |-------------|
    |             |
    |             |
    |             |
-----             |
-----             |
    |             |
    |_____________|

    """,
"Single_Door_Room_West": """
 
    |-------------|
    |             |
    |             |
    |             |
    |             ------
    |             ------
    |             |
    |_____________|

    """,
"Two_Door_Room_North_and_South": """
 
    |----|   |----|
    |             |
    |             |
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Two_Door_Room_East_and_West": """
 
     |-------------|
     |             |
     |             |
------              ------
------              ------  
     |             |
     |             |
     |_____________|

    """,
"Two_Door_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |              |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Two_Door_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |              |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Two_Door_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |              |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Two_Door_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |              |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Shrine_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |    Shrine    |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Shrine_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |    Shrine    |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"shrine_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |    Shrine    |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Shrine_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |    Shrine    |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Four-Door Room_North_South_East_and_West": """
 
     |----|   |----|
     |             |
     |             |
------             ------
------             ------
     |             |
     |             |
     |____     ____|
          |   |

    """,
"Boss_Room_Single_Door_Room_North": """
 
    |-------------|
    |             |
    |  Boss Room  |
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Boss_Room_Single_Door_Room_South": """
 
    |----|   |----|
    |             |
    |  Boss Room  |
    |             |
    |             |
    |_____________|

    """,
"Boss_Room_Single_Door_Room_East": """
 
    |-------------|
    |             |
    |  Boss Room  |
    |             |
-----             |
-----             |
    |             |
    |_____________|

    """,
"Boss_Room_Single_Door_Room_West": """
 
    |-------------|
    |             |
    |  Boss Room  |
    |             |
    |             ------
    |             ------
    |             |
    |_____________|

    """,
"Boss_Room_Two_Door_Room_North_and_South": """
 
    |----|   |----|
    |             |
    |  Boss Room  |
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Boss_Room_Two_Door_Room_East_and_West": """
 
     |-------------|
     |             |
     |  Boss Room  |
------              ------
------              ------  
     |             |
     |             |
     |_____________|

    """,
"Boss_Room_Two_Door_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Two_Door_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Two_Door_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Two_Door_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |   Boss Room  |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Corner_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |   Boss Room  |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Corner_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Corner_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Corner_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |  Boss Room   |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Boss_Room_Four-Door Room_North_South_East_and_West": """
 
     |----|   |----|
     |             |
     |  Boss Room  |
------             ------
------             ------
     |             |
     |             |
     |____     ____|
          |   |

    """,
"Treasure_Room_Single_Door_Room_North": """
 
    |-------------|
    |             |
    |Treasure Room|
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Treasure_Room_Single_Door_Room_South": """
 
    |----|   |----|
    |             |
    |Treasure Room|
    |             |
    |             |
    |_____________|

    """,
"Treasure_Room_Single_Door_Room_East": """
 
    |-------------|
    |             |
    |Treasure Room|
    |             |
-----             |
-----             |
    |             |
    |_____________|

    """,
"Treasure_Room_Single_Door_Room_West": """
 
    |-------------|
    |             |
    |Treasure Room|
    |             |
    |             ------
    |             ------
    |             |
    |_____________|

    """,
"Treasure_Room_Two_Door_Room_North_and_South": """
 
    |----|   |----|
    |             |
    |Treasure Room|
    |             |
    |             |
    |____     ____|
         |   |

    """,
"Treasure_Room_Two_Door_Room_East_and_West": """
 
     |-------------|
     |             |
     |Treasure Room|
------              ------
------              ------  
     |             |
     |             |
     |_____________|

    """,
"Treasure_Room_Two_Door_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |Treasure Room |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Two_Door_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |Treasure Room |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Two_Door_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |Treasure Room |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Two_Door_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |Treasure Room |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Corner_Room_North_and_West": """
 
     |----|    |----|
     |              |
     |Treasure Room |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Corner_Room_North_and_East": """
 
     |----|    |----|
     |              |
     |Treasure Room |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Corner_Room_South_and_East": """
 
     |----|    |----|
     |              |
     |Treasure Room |
     |              ------
     |              ------  
     |              |
     |              |
     |______________|

    """,
"Treasure_Room_Corner_Room_South_and_West": """
 
     |----|    |----|
     |              |
     |Treasure Room |
------              |
------              | 
     |              |
     |              |
     |______________|

    """,
}

# Function to get ASCII art by key
def get_ascii_art(key):
    return ASCII_ART.get(key, "ASCII art not found")

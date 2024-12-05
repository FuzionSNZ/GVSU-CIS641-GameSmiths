# Overview
This document serves as a Software Requirements Specification (SRS) for the Overthrone board game. It details the key features of the game and outlines both functional and non-functional requirements to ensure the game functions as intended while meeting quality standards.

# Functional Requirements

### Player Registration  
| 1 | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| FR1 | Players shall be able to join a game lobby to chat with other players.                       |  
| FR2 | Players shall be able to select a unique player name to identify themselves in the game.     |  
| FR3 | Players shall be able to see the name of the other players that join the same lobby.         |  
| FR4 | Players shall be able to set their ready status in a public lobby.                           |  
| FR5 | Players shall be able to send messages in a public lobby.                                    |  

### Game Board Mechanics  
| 2 | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| FR6 | The game shall display the main game board.                                                  |  
| FR7 | Players shall be able to roll dice to determine movement across the game board.              |  
| FR8 | The game shall implement space-specific actions based on the type of space landed on, including points gain/loss and mini-game triggers. |  
| FR9 | The game shall handle player turns in a sequential manner, ensuring that players cannot take actions out of order. |  
| FR10 | The game shall display turn count and all player data.                                      |  

### Mini-Game Integration  
| 3 | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| FR11 | The game shall randomly select a mini-game for players to participate in at the end of each round. |  
| FR12 | Players shall be able to compete in mini-games to earn bonus points based on their performance. |  
| FR13 | The game shall track and display the player's score for mini-game results after each round. |  
| FR14 | Players shall have access to a variety of mini-games that test different skills and strategies. |  
| FR15 | The game shall ensure that the mini-games selected at the end of each round are unique and non-repetitive within a session, providing variety to the players. |  

### Cell Actions  
| 4  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| FR16 | The game shall add x points to a player's score if they land on a positive integer cell.    |  
| FR17 | The game shall subtract x points from a player's score if they land on a negative integer cell. |  
| FR18 | The game shall set all players' points to 0 if they land on an "N" cell.                    |  
| FR19 | The game shall prompt the player to choose a path if they land on a choose-path block.      |  
| FR20 | The game shall increment the turn count by 1 after the final player lands on a cell.        |  

### Snake Minigame  
| 5  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| FR21 | The game shall draw all graphics within the game, including snakes, walls, and randomly generated textures and patterns. |  
| FR22 | Each game session shall generate walls with random locations and textures.                  |  
| FR23 | Three types of fruits (orange, apple, pineapple) shall spawn at random locations with random selection in each game. |  
| FR24 | Snakes shall grow longer after eating fruits, and when a snake collides with another, the cut-off section of the shorter snake must be added to the longer one. |  
| FR25 | Snakes shall be able to move off one edge of the board and reappear on the opposite edge.   |  


# Non-Functional Requirements

### Player Registration and Lobby Creation  
| 1  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| NFR1 | The system shall ensure that all player names are stored locally and are unique to each game session. |  
| NFR2 | The lobby joining process shall be intuitive.                                               |  
| NFR3 | The system shall support a minimum of 6 concurrent users without performance degradation.    |  
| NFR4 | The player interface shall be intuitive and user-friendly to ensure ease of navigation for players of all ages. |  
| NFR5 | The server shall handle all 3 lobby clients separately, without disrupting other game logic. |  

### Game Board Mechanics  
| 2  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| NFR6 | The game board shall load within 3 seconds to minimize wait time for players.               |  
| NFR7 | The game shall maintain a consistent frame rate of at least 60 frames per second during gameplay to ensure smooth animations. |  
| NFR8 | All game mechanics shall be thoroughly tested to ensure there are no bugs or glitches that affect gameplay. |  
| NFR9 | The user interface shall be visually appealing and thematic, enhancing the overall gaming experience. |  
| NFR10 | The game shall be optimized to consume minimal system resources, ensuring smooth performance even on devices with lower hardware specifications. |  

### Mini-Game Integration  
| 3  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| NFR11 | Mini-games shall have a maximum load time of 2 seconds to keep players engaged.            |  
| NFR12 | The mini-game selection process shall be random but balanced, ensuring fairness and variety in gameplay. |  
| NFR13 | The system shall analyze player progress and accurately determine players' scores/awards.  |  
| NFR14 | Mini-games shall be designed to be accessible for players with varying skill levels to ensure inclusivity. |  
| NFR15 | The system shall support the addition of new mini-games without requiring significant modifications to the existing codebase or gameplay mechanics. |  

### Cell Actions  
| 4  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| NFR16 | The game shall handle all cell actions without affecting performance.                      |  
| NFR17 | Cell displays shall be intuitive to their action.                                           |  
| NFR18 | Cell actions must happen within 3 seconds of players landing.                              |  
| NFR19 | Cells shall render within 1 second of the board game display.                              |  
| NFR20 | Cells' paths shall append to the chosen path within 1 second of the player’s choice.       |  

### Snake Mini-Game Integration  
| 5  | Requirement                                                                                  |  
| :--:| :-------------------------------------------------------------------------------------------:|  
| NFR21 | The game shall render all graphics and handle collisions smoothly at a frame rate of at least 5 FPS. |  
| NFR22 | The game shall support at least 2 players in multiplayer mode without performance degradation. |  
| NFR23 | Controls shall be intuitive and responsive, allowing players to navigate easily.           |  
| NFR24 | Random generation algorithms shall produce fair and diverse results for wall placements and fruit spawning. |  
| NFR25 | The generated graphics (textures, patterns, and colors) shall maintain a visually appealing and consistent style. |

# Change management plan
##	How will you train people to use it?
To train users on how to use the game, we will present a video for those interested. This video will feature the startup sequence, up until the end sequence. Throughout the video, we will explain rules, setup, and navigation.
#	How will you ensure it integrates within their ecosystem / software?
To ensure that it integrates with the current ecosystem(assuming that it is a game publisher), 
#	How will you ensure that it any discovered issues are resolved?
To ensure that any discovered issues are resolved, we will have continued matintnence 
# Tracability Links
Dectiption of this section
## Use Case Diagram Traceability
| Artifact ID | Artifact Name         | Requirement ID |
| :----------: | :--------------------: | :------------: |
| UseCase1     | Roll Dice              | FR1            |
| UseCase2     | Move Player            | FR2            |
| UseCase3     | Land on "S" Space      | FR3            |
| UseCase4     | Land on "N" Space      | FR4            |
| UseCase5     | Land on "Z" Space      | FR5            |
| UseCase6     | Land on "GP" Space     | FR6            |
| UseCase7     | Land on "TP" Space     | FR7            |
| UseCase8     | Land on "+X" Space     | FR8            |
| UseCase9     | Land on "-X" Space     | FR9            |
| UseCase10    | Start Random Minigame | FR10           |
| UseCase11    | Choose Path            | FR11           |
| UseCase12    | Switch Turn            | FR12           |
| UseCase13    | CPU Player AI          | FR13           |
| UseCase14    | Add/Remove Players     | FR14           |
| UseCase15    | View Scoreboard        | FR15           |
| UseCase16    | Start New Game         | FR16           |


# Overview
This document outlines the Software Requirements Specification (SRS) for the "Overthrone" game. It serves to define the functional and non-functional requirements for the development of the game, including system behavior, performance expectations, user interactions, and technical constraints. This SRS will guide the development team in creating a robust, engaging, and scalable multiplayer board game experience.

# Software Requirements
This section provides a detailed description of the software requirements for the "Overthrone" game. It is divided into two main parts: functional requirements and non-functional requirements. Functional requirements define the expected behaviors and interactions within the game, such as player actions, game logic, and system responses. Non-functional requirements focus on performance, reliability, usability, and other system attributes that ensure the game operates efficiently and provides a high-quality user experience. Each requirement is linked to specific game features and processes to ensure traceability and clear implementation goals.

## Functional Requirements

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


## Non-Functional Requirements

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
## How will you train people to use it?
To train users on how to use the game, we will present a video for those interested. This video will feature an in-game tutorial that walks users through the basic mechanics (e.g., creating a lobby, rolling dice, choosing paths). This allows users to learn the game step-by-step without feeling overwhelmed. We will also make the training process more engaging, consider gamifying the onboarding experience, where players can complete challenges and earn rewards for learning the game's features. 
##	How will you ensure it integrates within their ecosystem / software?
To ensure that it integrates with the current ecosystem, we will ensure that the game can be played across the most common platforms used by the customer, including desktops, laptops, and mobile devices. This will ensure that employees can play regardless of the device they use. We will also integrate with the company’s authentication systems (e.g., Active Directory or SSO services) to simplify user access and avoid the need for additional login credentials, and repeated name creation ingame.
##	How will you ensure that it any discovered issues are resolved?
To ensure that any discovered issues are resolved, we will incorporate a built-in feedback tool that allows players to report bugs, suggest improvements, or submit feature requests. This will help us gather insights into user experiences and pinpoint pain points. With this we will establish a dedicated support team or helpdesk to resolve technical issues quickly. This team should be available to provide assistance via chat, email, or ticketing systems. They should be well-versed in common issues that might arise in corporate environments. Following these evenets, we will also have Regularly releases of software updates that address discovered issues and introduce new features. Provide patch notes so users can see what changes have been made, helping them stay informed.
# Tracability Links
This section outlines the traceability links between the various game artifacts (use cases, class diagrams, activity diagrams, etc.) and their corresponding functional and non-functional requirements. Traceability ensures that each requirement is properly addressed throughout the design and development process. By mapping requirements to specific game components and actions, we can ensure that the "Overthrone" game meets its intended functionality, performance, and user experience expectations. This section serves as a reference to track the implementation of requirements and verify that all aspects of the system are accounted for and properly executed.

## Use Case Diagram Traceability

| Artifact ID | Artifact Name           | Requirement ID |  
| :----------: | :----------------------: | :------------: |  
| UseCase1     | Move Player              | FR5, NFR16     |  
| UseCase2     | Join Lobby               | FR1, NFR1      |  
| UseCase3     | Roll Dice                | FR8, NFR18     |  
| UseCase4     | Select Path              | FR9, NFR20     |  
| UseCase5     | Trigger Mini-Game        | FR15, NFR15    |  
| UseCase6     | Interact with Space      | FR16, NFR16    |  
| UseCase7     | Add/Subtract Points      | FR17, FR18, NFR18 |  
| UseCase8     | Trigger Game Logic       | FR19, FR20, NFR19 |  
| UseCase9     | Add/Remove Player Profile| FR2, NFR3      |  
| UseCase10    | Load Game Board          | FR10, NFR6     |  
| UseCase11    | Handle Game Events       | FR20, NFR16    |  
| UseCase12    | Switch Between Players   | FR6, NFR7      |  
| UseCase13    | Randomize Game Board     | FR12, NFR14    |  
| UseCase14    | Handle CPU Player        | FR19, NFR22    |  
| UseCase15    | Track Player Progress    | FR15, NFR13    |  
| UseCase16    | Start Mini-Game          | FR16, NFR11    |  
| UseCase17    | Display Graphics         | FR15, NFR25    |  
| UseCase18    | Ensure Smooth Gameplay   | FR10, NFR10    |  
| UseCase19    | Maintain Fairness in Mini-Game | FR15, NFR12  |  
| UseCase20    | Track Player Scores      | FR10, NFR20    |  

## Class Diagram Traceability

| Artifact Name       | Requirement ID        |  
| :------------------: | :-------------------: |  
| classPlayer          | NFR3, FR5, FR1        |  
| classGameBoard       | FR10, NFR6, NFR16     |  
| classLobby           | FR1, NFR1, NFR7       |  
| classDice            | FR8, NFR18            |  
| classMiniGame        | FR15, NFR11, NFR12    |  
| classSpace           | FR16, NFR16, FR17     |  
| classTurnManager     | FR20, NFR16           |  
| classCPUPlayer       | FR19, NFR22           |  
| classScoreTracker    | FR17, NFR20, NFR18    |  
| classGameSession     | FR19, NFR19           |  
| classGraphics        | FR15, NFR25           |  
| classPathChoice      | FR9, NFR20            |  
| classGameEvents      | FR20, NFR16           |  
| classLobbyManager    | FR1, NFR1, NFR7       |  
| classRandomizer      | FR12, NFR14           |  
| classActionSpace     | FR16, NFR16, FR17     |  
| classPlayerProfile   | FR2, NFR3             |  
| classMatchmaking     | FR1, NFR1, NFR7       |  
| classPointModifier   | FR18, NFR18           |  
| classMiniGameManager | FR15, NFR12, NFR13    |  
| classNetworkHandler  | NFR10, NFR5           |  
| classSoundManager    | NFR25, FR10           |  
| classBoardRenderer   | FR10, NFR6            |  
| classAnimationHandler| NFR25, FR10           |  
| classRandomEvent     | FR12, NFR14           |  


## Activity Diagram Traceability

| Artifact ID        | Artifact Name              | Requirement ID        |
| :-----------------: | :-------------------------: | :-------------------: |
| activityPlayerInput | Handle Player Input         | FR1, FR5, NFR2        |
| activityLobby       | Join Game Lobby             | FR1, NFR1, NFR7       |
| activityRollDice    | Roll Dice                   | FR8, NFR18            |
| activityMovePlayer  | Move Player                 | FR5, NFR16, NFR18     |
| activitySelectPath  | Select Path                 | FR9, NFR20            |
| activityMiniGame    | Start Mini-Game             | FR15, NFR11, NFR12    |
| activitySpaceAction | Trigger Space Action        | FR16, NFR16, FR17     |
| activityTurnChange  | Change Turn Sequence        | FR6, FR7, NFR10       |
| activityUpdateScore | Update Player Score         | FR17, NFR18, NFR20    |
| activityCPUPlayer   | Handle CPU Player Actions   | FR19, NFR22           |
| activityGameStart   | Start Game Logic            | FR19, NFR19           |
| activityEndGame     | End Game Logic              | FR10, NFR25           |
| activityHandleEvent | Handle Game Events          | FR20, NFR16           |
| activityRandomizer  | Randomize Game Elements     | FR12, NFR14           |
| activityPathChoice  | Handle Path Choice          | FR9, NFR20            |
| activityTriggerMiniGame | Trigger Mini-Game Based on Round | FR15, NFR13   |
| activityHandlePlayerAction | Process Player Action | FR16, NFR18           |
| activityGameSetup   | Setup Game Environment      | FR10, NFR6            |
| activityRenderBoard | Render Game Board           | FR10, NFR6            |
| activityDisplayGraphics | Display Game Graphics   | FR15, NFR25           |
| activityNetworkSync | Sync Game State Across Clients | NFR10, NFR5       |

# Software Artifacts

<Describe the purpose of this section>

* [I am a link]([artifacts](https://github.com/FuzionSNZ/GVSU-CIS641-GameSmiths/tree/3ff4ef3ee32c53b6d14deeb694213c3aec8c36fc/artifacts))


# Overview
This document serves as a Software Requirements Specification (SRS) for the Overthrone board game. It details the key features of the game and outlines both functional and non-functional requirements to ensure the game functions as intended while meeting quality standards.

# Functional Requirements

## 1. Player Registration
FR1. |Players shall be able to join a game lobby to chat with other players.|
2. Players shall be able to select a unique player name to identify themselves in the game.
3. Players shall be able to see the name of the other player's that join the same lobby.
4. Players shall be able set their ready status in a public lobby.
5. Players shall be able to send messages in a public lobby.

## 2. Game Board Mechanics
1. The game shall display the main game board.
2. Players shall be able to roll dice to determine movement across the game board.
3. The game shall implement space-specific actions based on the type of space landed on, including points gain/loss and mini-game triggers.
4. The game shall handle player turns in a sequential manner, ensuring that players cannot take actions out of order.
5. The game shall display turn_count, and all player data.

## 3. Mini-Game Integration
1. The game shall randomly select a mini-game for players to participate in at the end of each round.
2. Players shall be able to compete in mini-games to earn bonus points based on their performance.
3. The game shall track and display the player's score for mini-game results after each round.
4. Players shall have access to a variety of mini-games that test different skills and strategies.
5. The game shallensure that the mini-games selected at the end of each round are unique and non-repetitive within a session, providing variety to the players.
   
## 4. Cell Actions
1. The game shall add x points to a player's score if they land on a positive integer cell.
2. The game shall subtract x points to a player's score if they land on a positive integer cell.
3. The game shall set all player's points to 0 if they land on a "N" cell.
4. The game shall prompt the player to choose a path if they land on a choose path block.
5. The game shall increment the turn count by 1 after the final player lands on a cell.
   
## 5. Snake Minigame 
1. The game shall draw all graphics within the game, including snakes, walls, and randomly generated textures and patterns.
2. Each game session shall generate walls with random locations and textures.
3.  Three types of fruits (orange, apple, pineapple) must shall at random locations with random selection in each game.
4. Snakes shall grow longer after eating fruits, and when a snake collides with another, the cut-off section of the shorter snake must be added to the longer one.
5. Snakes shall be able to move off one edge of the board and reappear on the opposite edge.


# Non-Functional Requirements

## 1. Player Registration and Lobby Creation
1. The system shall ensure that all player names are stored locally and are unique to each game session.
2. The lobby joining process shall be intuitive.
3. The system shall support a minimum of 6 concurrent users without performance degradation.
4. The player interface shall be intuitive and user-friendly to ensure ease of navigation for players of all ages.
5. The server shall handle all 3 lobby clients seperately, without distupting other game logic. 

## 2. Game Board Mechanics
1. The game board shall load within 3 seconds to minimize wait time for players.
2. The game shall maintain a consistent frame rate of at least 60 frames per second during gameplay to ensure smooth animations.
3. All game mechanics shall be thoroughly tested to ensure there are no bugs or glitches that affect gameplay.
4. The user interface shall be visually appealing and thematic, enhancing the overall gaming experience.
5. The game shall be optimized to consume minimal system resources, ensuring smooth performance even on devices with lower hardware specifications.

## 3. Mini-Game Integration
1. Mini-games shall have a maximum load time of 2 seconds to keep players engaged.
2. The mini-game selection process shall be random but balanced, ensuring fairness and variety in gameplay.
3. The system shall analyze player progress, and acurrately determine players' scores/ awards.
4. Mini-games shall be designed to be accessible for players with varying skill levels to ensure inclusivity.
5. The system shall support the addition of new mini-games without requiring significant modifications to the existing codebase or gameplay mechanics.
   
## 4. Cell Actions
1. The game shall handel all cell actions without effecting performance.
2. Cell display's shall be intuitive to their action.
3. Cell actions must happen within 3 seconds of players landing.
4. Cells shall render within 1 second of the board game display.
5. Cells path shall append to chosen path within 1 second of player choice.

## 5. Mini-Game Integration
1. The game shall render all graphics and handle collisions smoothly at a frame rate of at least 5 FPS.
2. The game shall support at least 2 players in multiplayer mode without performance degradation.
3. Controls shall be intuitive and responsive, allowing players to navigate easily.
4. Random generation algorithms shall produce fair and diverse results for wall placements and fruit spawning.
5. The generated graphics (textures, patterns, and colors) shall maintain a visually appealing and consistent style.

# Overview
This document serves as a Software Requirements Specification (SRS) for the Overthrone board game. It details the key features of the game and outlines both functional and non-functional requirements to ensure the game functions as intended while meeting quality standards.

# Functional Requirements

## 1. Player Registration and Lobby Creation
1. Players shall be able to create a game lobby with customizable settings such as the number of players and game duration.
2. Players shall be able to select a unique player name to identify themselves in the game.
3. Players shall be able to join a public lobby or enter a private lobby using a generated key.
4. Players shall be able to view and manage their chosen player names before starting the game.

## 2. Game Board Mechanics
1. The game shall provide a randomized board layout for each game session to enhance replayability.
2. Players shall be able to roll dice to determine movement across the game board.
3. The game shall implement space-specific actions based on the type of space landed on, including points gain/loss and mini-game triggers.
4. The game shall handle player turns in a sequential manner, ensuring that players cannot take actions out of order.

## 3. Mini-Game Integration
1. The game shall randomly select a mini-game for players to participate in at the end of each round.
2. Players shall be able to compete in mini-games to earn bonus points based on their performance.
3. The game shall track and display the leaderboard for mini-game results after each round.
4. Players shall have access to a variety of mini-games that test different skills and strategies.

# Non-Functional Requirements

## 1. Player Registration and Lobby Creation
1. The system shall ensure that all player names are stored locally and are unique to each game session.
2. The lobby creation process shall be completed within 5 seconds under normal conditions.
3. The system shall support a minimum of 8 concurrent users in the lobby creation feature without performance degradation.
4. The player interface shall be intuitive and user-friendly to ensure ease of navigation for players of all ages.

## 2. Game Board Mechanics
1. The game board shall load within 3 seconds to minimize wait time for players.
2. The game shall maintain a consistent frame rate of at least 30 frames per second during gameplay to ensure smooth animations.
3. All game mechanics shall be thoroughly tested to ensure there are no bugs or glitches that affect gameplay.
4. The user interface shall be visually appealing and thematic, enhancing the overall gaming experience.

## 3. Mini-Game Integration
1. Mini-games shall have a maximum load time of 2 seconds to keep players engaged.
2. The mini-game selection process shall be random but balanced, ensuring fairness and variety in gameplay.
3. The system shall log and analyze mini-game performance data to improve game design in future updates.
4. Mini-games shall be designed to be accessible for players with varying skill levels to ensure inclusivity.

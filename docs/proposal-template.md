Team name:

Team members:

Quinton Randall, Khoi Tran

(In 2-4 paragraphs, describe your project concept)

The game is called Overthrown. It's a boardgame for 2 players up to 4 players.

Over throne Game Rules Updated
Main Objective:
End the game with the most amount of points
Startup:
Set number of total turns.
Max players = 8
Min Players = 2 (one of these players can be CPU)
Choose map / table to play on
host lobby, create game room
public matches = join any open lobby
private matches = generate private key' need privet key to join
Choose characters

(What technologies are needed to build this project)

# Method/Approach
We are using agile process. We are having the first set of requirements, then along the way we'll add more features to
the game. We are using Python for this project.

(What is your estimated "plan of attack" for developing this project)

# Estimated Timeline
Basic game function testing (roll dice, record scores, switch musics, player interaction)

Sep 26:
Add different maps (3) (note: rando space might be added in the future)

Oct 12:
2 player profiles

Oct 19:
Start Game:
All players roll dice 1 at a time to determine the order of play.
Highest number stars first, lowest number goes last.

Oct 16:
Logic:
Player rolls dice, and moves amount that amout of spaces. They will take the action of the space they landed on.
"S" spaces = If a player lands on an S, they are safe and cannot be affected by any action
"N" spaces = If a player lands on an N, set all players's points to 0
"Z" spaces = If a player lands on an Z, All players move backwars that many spaces (only the player who landed on he Z take subsequent actions)
"Choose Path = If a player lands touches this tile on their turn they must stop, reroll, and chose a path to go down
"GP" spaces = If a player lands on an GP, player must give X points to one other player (ie. GP = Give 1 of your points to 1 other player, GP2 = Give 2 of your points to one other player of your choice)
"TP" spaces = If a player lands on an TP, player must take X points from one other play(ie. TP = Take 1 point from 1 other player, TP2 = Take 2 points from one other player of your choice)

"+X" spaces = If a player lands on an a positive number, add this number to your point total
"-X" spaces = If a player lands on a negative number, subtract this number from your point total
After last player rolls: Start a random minigame, winners of minigame get points based on placement
If a player reaches an endpoint, their spawn at a random start point


Nov 2:
CPU player (1)

Nov 16:
Mini games


(Figure out what your major milestones for this project will be, including how long you anticipate it *may* take to reach that point)

# Anticipated Problems
Multiplayer Integration: The game must be designed to work well with multiple players at 
the same time.

Modularity: The game needs to be flexible, allowing for more mini-games to be added 
depending on how much time is available during development.

Testing: Additional mini-games will need thorough testing to ensure they function correctly, 
especially as new ones are added later in development.

(Describe any problems you foresee that you will need to overcome)

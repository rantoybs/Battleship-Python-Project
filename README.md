# Battleship_Project

Proposal:
Our team members are Russell Deady, John Ronzo, Andrew Franklin, Randy Toyberman, and Tyler Flaherty. The title of our project is Dynamic Fighting Ships. We hope to program a battleship-styled game where you can move your ships in-between every turn. We plan on utilizing the pygame library to do this. We plan to  have two people focus on the GUI, two people focusing on the mechanics of the game, and one person focusing on the networking.

Project Design:
There are several Battleship games written in Python with some using the Pygame library. We will extended the current state of the art for those that use Pygame by introducing a rule change that allows players to move their ships during the game. We will also implement a multiplayer feature with socket programming that allows for a multiplayer experience. There are also many python games that incorporate a multiplayer aspect as well as an AI component that allows users to play alone. Out goal is to combine these two philosophies into a multiplayer battleship game. 

Libraries: Pygame, Socket, Random, Pygame-ai, Threading, Time, Requests, _Thread

- Multiplayer: Randy
- GUI: Russell, Tyler
- Mechanics: John, Andrew

Status Report 1: For the backend mechanics, we have finalized our descision to use Pygame for most of the functionality and well as Pygame-ai for one player games. We also progammed the initial Pygame interface which the rest of the game will be built on. We have also begun to research as much as we can about the Pygame library to get the most functionality out of it.

As for the multiplayer functionality, we have setup a basic network and server which currently functions to establish a connection between clients running on the same network. In addition to this, research has been started on sending information between clients in order to send and recieve game moves and to update game data over the network.

We have also began the initial setup of the back-end part of the game that sets up each players gameboard with some other functions such as placing a ship in a given location, checking whether a ship exists in a given position. These features will be developed further on that will allow players to choose where they want to shoot and allow players to customize where they want their ships.

Status Report 2:
The new libraries we have added are numpy, OcempGUI, pickle, and \_thread. We haven't changed any goals from the original plan.


Instructions on how to play:

In order to play the game, run the file app.py. Once the game is opened and loaded, select whether you want a single player or multiplayer game. If single player, the game will start up on the placing ships screen. If multiplayer, select whether you want to create a game or join a game. In order for two people to play, one player must create the game and the other must join the game. If you click create the game, you will be brought to the placing ships screen, with your IP address displayed on top. The player who is joining your game, must launch app.py on their own, select the multiplayer option, and type in the IP listed on the other screen, and click join game. If not type correctly, the player will be unable to join and the game must be launched again. Once the other player has joined, both players will be on the placing ships screen. 
    
In order to place ships, you must click and drag the ship icons on the right side of the game board onto the game board itself. A highlight will appear on the board to show you where you are dropping your ships and if they fit in the space you are dropping them in. Once you unclick the mouse, the ship will be dropped in place. You are allowed to pick up and move your ship after you place it, but once all ships have been placed on the board you cannot move any ship. Ships can only be placed horizontally.

In single player: Once you have placed all your ships, the game will start. The player will always have the first turn, and you must click a square on the game board to take a shot at the computer's ships. Once you click a square on the game board, the game will show you if it is a hit by marking an explosion on the spot you clicked, or a miss by marking an X on the spot you clicked. In addition to the graphical representations, there will be text that tells you whether you hit or missed a ship. After you take your shot, the screen will switch and show your own ships, and the game will show you the move the computer made and  whether it is a hit or a miss. The game will continue until someone is crowned a winner, in which text will pop up on the side that all ships have been sunk and the game will close.

In multiplayer: Once all the ships are placed by both players, the screen will change for both players. Player 1 will go first and their screen will become an empty grid where you can click on a square to take a shot. Just like single player, if your shot is a hit, an explosion will show on your screen and the other players screen, and if your shot is a miss then an X will show up on your screen and the other players screen. After player one has taken their turn, the move will show on both screens and the screens will switch. Player 1 will be shown their own game board with all hits/misses present on the board, and player 2 will be show the game board to take a shot. The two players will switch roles until one player wins, and the winning text shows up on the side of the board and the game will close. 

A few important notes:
* The ships will disappear off the game board as they are sunk
* Ships cannot be moved once all of them have been placed.
* The multiplayer will not work on FSUSecure, has not been tested on other FSU Wifi, look in the terminal for connected messages on player 1's terminal.
* In order to enter the multiplayer menu you must click the button twice.
* Unless on the menu screen, press the ESC key to close the game.
* If one player is a Apple user, it is better for them to create the game as if a Apple computer tries to join a Windows game there is often times connection issues.



Citations and Links:
    Images used:
        https://depositphotos.com/75534743/stock-illustration-militaristic-ships-icons.html
        https://www.freeiconspng.com/img/9151
        https://www.iconsdb.com/red-icons/x-mark-icon.html
        https://www.google.com/url?sa=i&url=https%3A%2F%2Ffineartamerica.com%2Ffeatured%2Fworld-war-two-battleship-cartoon-aloysius-patrimonio.html%3Fproduct%3Dgreeting-card&psig=AOvVaw31YQFuJR4EEmqYCt8NNbG2&ust=1650741385150000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIja14CxqPcCFQAAAAAdAAAAABAT

    Code snippets for menu functions:
        https://www.geeksforgeeks.org/creating-start-menu-in-pygame/



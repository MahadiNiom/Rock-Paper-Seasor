This is a simple Rock-Paper-Scissor game which runs in console.

Unlike classical Rock-Paper-Scissor game, our game supports arbitraty odd number of moves.

To play the game run main.py file giving odd number of moves as command line arguments.
Example:

	$ py main.py rock paper scissor

or

	$ py main.py rock paper scissor lizard spoke

Note: You can pass as many number of arguments you want but it must be greater then or equal three.

After running the program you will see a MAC function and available options for your moves to enter.
You can enter "0" to exit the game and "?" for help.
The MAC is provided as computers move. 
This MAC is made by concatinating computers move with a 256 cryptographically pseudo random key and then hashing it.
The key will be provided after you make your moves.
This allows users to be able to check wheather computer is cheating by changing its move after user chooses his moves.

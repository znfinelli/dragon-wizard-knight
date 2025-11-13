====================================================== Python OOP Game: Dragon, Wizard, Knight

A.B Cognitive Science - CSCI1300
Author: Zoë Finelli

PROJECT OVERVIEW

This project is an Object-Oriented Programming (OOP) implementation of a
"Rock, Paper, Scissors"-style console game called "Dragon, Wizard, Knight."

The primary goal of this project was to refactor a procedural script (which
relied heavily on global variables) into a robust, class-based application.
This demonstrates key OOP principles and creates a more stable and extensible
program.

The game includes two main phases:

Standard Game: The user plays against a single AI opponent ("Sally").

Bonus Round: If the user wins the standard game, a bonus round
is unlocked. This round introduces a second AI opponent ("Bob") and a new
playable character ("Druid") with unique win/loss rules.

HOW TO RUN

Language: Python 3.10+

Dependencies: None. This project uses only the Python Standard Library
(specifically the random module).

Installation:
No installation is required. Just clone or download the repository.

Run Main Script:
From your terminal, simply execute the Python file:

python dragon_knight_wizard_game.py


EXPECTED OUTPUT

Running dragon_knight_wizard_game.py will:

Print the welcome message and game rules.

Prompt the user for their name and the desired number of rounds.

Begin the game loop, prompting the user for their move (D, K, W)
in each round.

Print the winner of each round and the cumulative score.

Declare an "ULTIMATE winner" at the end of the standard game.

If the user is the winner, the script will then initiate the bonus
round, which has its own rules, rounds, and final winner.

PROJECT STRUCTURE

This is a single-file project, keeping the structure simple.

dragon_knight_wizard_game/
│
├── README.md                       # This file
└── dragon_knight_wizard_game.py    # The complete Python script

PROJECT DESIGN & KEY CONCEPTS

The core of this project was the transition from procedural to
Object-Oriented Programming. The design is built on three main classes:

Player (Base Class):
A parent class that defines the "interface" for all players. It
initializes common attributes (name, points) and a placeholder
choose_move() method.

HumanPlayer (Child Class):
Inherits from Player. Its choose_move() method is implemented to
prompt the user for a validated text input.

RobotPlayer (Child Class):
Also inherits from Player. Its choose_move() method is
implemented to select a move at random from the list of
available characters.

DragonWizardKnightGame (Main Class):
This class acts as the "controller" for the entire application.

State Management: All former global variables (like
userPoints, currentRound, etc.) are now instance attributes
(e.g., self.player, self.current_round). This is a much
safer and cleaner way to manage the program's state.

Encapsulation: All game logic (play_standard_round,
get_final_winner, run_bonus_game) is encapsulated as
methods within this class.

Clean Logic: The win/loss rules are stored in a dictionary
(self.normal_rules) for fast lookups, which avoids a large and
cluttered if/elif/else chain.

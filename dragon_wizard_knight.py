"""
This script implements the 'Dragon, Wizard, Knight' game using an
Object-Oriented Programming (OOP) structure. This approach organizes
the game into logical components (Classes) to manage game state,
player actions, and rules effectively.
"""

import random

# ---------------------------------------------------------------------------
# PLAYER CLASSES
# ---------------------------------------------------------------------------

class Player:
    """
    This 'Player' class serves as a base (or 'parent') for all participants.
    It defines the common properties that all players share, like 'name'
    and 'points'. Using a base class like this (a concept called 'inheritance')
    helps us avoid duplicating code.
    """
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points_to_add):
        """A simple method to update a player's score."""
        self.points += points_to_add

    def choose_move(self, allowed_moves):
        """
        This method is defined here as a 'placeholder'. It establishes a
        common interface, but each specific player type (Human, Robot) will
        provide its own concrete implementation. This is known as polymorphism.
        """
        raise NotImplementedError("This method must be implemented by a child class")

    def reset_points(self):
        """Helper method to reset a player's points to 0. This will be
        used to start the bonus round fresh.
        """
        self.points = 0


class HumanPlayer(Player):
    """
    The HumanPlayer 'inherits' from the base Player class.
    This means it automatically gets the 'name' and 'points' attributes.
    We just need to define the 'choose_move' method to handle
    validated user input.
    """
    def __init__(self, name):
        # 'super()' calls the __init__ method of the parent (Player) class
        super().__init__(name)

    def choose_move(self, allowed_moves):
        """
        This 'overrides' the parent's 'choose_move' method.
        It provides the specific logic for a human by prompting for
        input and looping until a valid move is entered.
        """
        # Create a string of valid inputs (e.g., "dkwDKW")
        valid_inputs = "".join(allowed_moves) + "".join(allowed_moves).upper()
        prompt = f"choose your character ({'/'.join(allowed_moves)}): "

        while True:
            move = input(prompt)
            if move in valid_inputs:
                return move.lower()  # Return the validated, lowercase move
            else:
                print(f"--> please enter one of {', '.join(allowed_moves).upper()}")


class RobotPlayer(Player):
    """
    The RobotPlayer also inherits from Player.
    Its version of 'choose_move' implements the AI logic,
    which is a random choice from the list of allowed moves.
    """
    def __init__(self, name):
        super().__init__(name)

    def choose_move(self, allowed_moves):
        """Overrides the parent's placeholder with a random choice."""
        move = random.choice(allowed_moves)
        return move  # Return the random move


# ---------------------------------------------------------------------------
# GAME LOGIC CLASS
# ---------------------------------------------------------------------------

class DragonWizardKnightGame:
    """
    This is the main 'controller' class for the game. It manages all the
    core components: the players, the game state (like rounds and scores),
    and the rules.

    Using a class like this encapsulates all the game logic, avoiding the
    need for global variables, which can make code hard to manage.
    """
    def __init__(self):
        # --- Game State Attributes ---
        # These attributes will hold our game's 'state'.
        self.player = None  # Will hold the HumanPlayer object
        self.sally = None   # Will hold the RobotPlayer("Sally")
        self.bob = None     # Will hold the RobotPlayer("Bob") for the bonus
        self.tie_points = 0
        self.winner_final = ""
        self.current_round = 0
        self.rounds_total = 0
        
        # --- Game Rules Definition ---
        # Storing rules in a dictionary is a clean and 'Pythonic' way
        # to handle win/loss logic. It's much cleaner than a giant
        # if/elif/else block.
        # Key = winner, Value = loser
        self.normal_rules = {
            'd': 'k',  # Dragon beats Knight
            'k': 'w',  # Knight beats Wizard
            'w': 'd'   # Wizard beats Dragon
        }
        self.normal_moves = ['d', 'k', 'w']
        self.bonus_moves = ['d', 'k', 'w', 'r'] # 'r' for Druid

    def print_rules(self):
        """A simple method to print the game's intro text."""
        print('''welcome to Dragon, Wizard, Knight! this is a game of luck, mind-reading, and superpowers.\n
    please read the rules below:\n
    during this game, the user plays against a robot named Sally. the game will keep score and declare
    a winner after a certain number of rounds determined by the user at the beginning of the game.\n
    when prompted, the user will enter their choice of character: Dragon, Wizard, or Knight.\n\n
    dragon beats Knight -- the Knight cannot withstand fire obviously\n
    knight beats Wizard -- the Wizard is slain by the Knights sword of course\n
    wizard beats Dragon -- the Dragon cannot break the spell of the Wizard on his own clearly\n\n
    if you are strong enough to withstand the forces of the great and powerful Sally, perhaps you may
    be invited to the secret world and more features will be unlocked!\n''')

    def print_bonus_rules(self):
        """Prints the special rules for the bonus round."""
        self._divider()
        print('''congrats! you defeated the almighty Sally... but can you defeat Sally AND Bob to become the ultimate winner? 
    now you must choose two characters, one to take on Sally and one to take on Bob.
    to win the round you, you now must beat both Bob AND Sally... oh and here's one more catch:\n
    there is one new character -- the Druid -- if you choose to play the Druid, you automatically win the
    round and GAIN two points... UNLESS the other player has also chosen to play the Druid this round. then, 
    everyone that has chosen to play the Druid LOSES two points, while the other player who did not 
    play the Druid receives two points. continue at your own risk... to become the MOST ULTIMATE winner.\n''')

    def _divider(self):
        """
        A "private" helper method (indicated by the '_' prefix) to print
        a formatted divider. This keeps the code DRY (Don't Repeat Yourself).
        """
        print('\n--------------------------------------------------\n')

    def get_num_rounds(self, prompt_message):
        """
        A robust method to get the total number of rounds.
        It includes input validation with a try/except block to
        ensure a positive integer is entered.
        """
        while True:
            try: 
                rounds_str = input(f'{prompt_message} {self.player.name}? enter a number: ')
                rounds_int = int(rounds_str) # Use int() for whole numbers
                if rounds_int > 0:
                    return rounds_int
                else:
                    print('--> please enter a number that is GREATER than zero\n')
            except ValueError:
                print('--> please enter a valid integer number\n')

    def print_scores(self, is_bonus_round=False):
        """
        Prints the current scores. It accepts a boolean flag
        to know whether to include Bob's score for the bonus round.
        This makes the method flexible.
        """
        print(f"\n--- scores (round {self.current_round} / {self.rounds_total}) ---")
        print(f"{self.player.name}'s points = {self.player.points}")
        print(f"sally's points = {self.sally.points}")
        if is_bonus_round:
            print(f"bob's points = {self.bob.points}")
        print(f"tied points = {self.tie_points}\n")

    def get_round_winner(self, p_move, r_move, player, robot):
        """
        This method determines the winner of a standard round.
        It takes the two moves and the player objects, then updates
        the points on the winning object directly.
        """
        winner_name = ""
        
        if p_move == r_move:
            winner_name = f"it's a tie :( no one"
            self.tie_points += 1
        # Use our rule dictionary to check for a win
        elif self.normal_rules[p_move] == r_move:
            winner_name = player.name
            player.add_points(1)
        else: # If it's not a tie and the player didn't win, the robot must have
            winner_name = robot.name
            robot.add_points(1)
            
        return winner_name

    def play_standard_round(self):
        """
        Controls the logic for a single standard round.
        It coordinates getting moves from the players,
        determining the winner, and printing the result.
        """
        self.current_round += 1
        print(f"\n--- round {self.current_round} of {self.rounds_total} ---")
        
        # 1. Get moves from both players
        p_move = self.player.choose_move(self.normal_moves)
        r_move = self.sally.choose_move(self.normal_moves)
        print(f"sally chose: {r_move.upper()}")
        
        # 2. Determine the winner and update scores
        winner = self.get_round_winner(p_move, r_move, self.player, self.sally)
        print(f'\n{winner} is the winner of this round!\n')

    def get_bonus_winner(self, p_move, r_move, player, robot):
        """
        Determines the winner for a bonus round. This logic is
        more complex as it includes the special rules for the
        'Druid' character ('r').
        """
        winner_name = ""
        
        # Case 1 & 2: One player plays Druid ('r')
        if p_move == 'r' and r_move != 'r':
            winner_name = f'someone played druid... {player.name}'
            player.add_points(2)
            robot.add_points(-2)
        elif p_move != 'r' and r_move == 'r':
            winner_name = f'someone played druid... {robot.name}'
            player.add_points(-2)
            robot.add_points(2)

        # Case 3: Both play Druid
        elif p_move == 'r' and r_move == 'r':
            winner_name = 'you both played druid! no one'
            player.add_points(-2)
            robot.add_points(-2)

        # Case 4: Standard tie (d/w/k)
        elif p_move == r_move:
            winner_name = 'tie! no one'
            self.tie_points += 1

        # Case 5 & 6: Standard win/loss (d/w/k)
        elif p_move in self.normal_rules and self.normal_rules[p_move] == r_move:
            winner_name = player.name
            player.add_points(1)
        else: # robot must win
            winner_name = robot.name
            robot.add_points(1)
            
        return winner_name

    def play_bonus_round(self):
        """
        Controls the logic for a single bonus round, which consists
        of two separate battles (Player vs. Sally and Player vs. Bob).
        """
        self.current_round += 1
        print(f"\n--- bonus round {self.current_round} of {self.rounds_total} ---")

        # --- Battle 1: Player vs. Sally ---
        print(f"\nfirst, for your battle against Sally...")
        p_move_sally = self.player.choose_move(self.bonus_moves)
        r_move_sally = self.sally.choose_move(self.bonus_moves)
        print(f"sally chose: {r_move_sally.upper()}")
        winner_sally = self.get_bonus_winner(p_move_sally, r_move_sally, self.player, self.sally)
        
        # --- Battle 2: Player vs. Bob ---
        print(f"\nnext, for your battle against Bob...")
        p_move_bob = self.player.choose_move(self.bonus_moves)
        r_move_bob = self.bob.choose_move(self.bonus_moves)
        print(f"bob chose: {r_move_bob.upper()}")
        winner_bob = self.get_bonus_winner(p_move_bob, r_move_bob, self.player, self.bob)

        # --- Round Summary ---
        print(f'\n{winner_sally} is the winner of Sally vs {self.player.name}.')
        print(f'{winner_bob} is the winner of Bob vs {self.player.name}.\n')

    def get_final_winner(self, is_bonus_round=False):
        """
        Calculates and prints the final winner of the game.
        It uses the 'is_bonus_round' flag to apply the
        correct winning logic (standard vs. bonus).
        """
        self._divider()
        winner_name = ""
        tie_msg = ""
        
        # We access the points directly from our player objects
        p_pts = self.player.points
        s_pts = self.sally.points
        
        if not is_bonus_round:
            # Standard game logic
            if s_pts > p_pts:
                winner_name = self.sally.name
            elif p_pts > s_pts:
                winner_name = self.player.name
            else:
                winner_name = 'no one'
                tie_msg = "it's a tie :( "
            
            # Store the winner, in case we need to check for the bonus round
            self.winner_final = winner_name 
            return f"{tie_msg}{winner_name} is the ULTIMATE winner!\n"
            
        else:
            # Bonus round logic
            b_pts = self.bob.points
            if s_pts > p_pts and s_pts > b_pts:
                winner_name = self.sally.name
            elif b_pts > s_pts and b_pts > p_pts:
                winner_name = self.bob.name
            elif p_pts > s_pts and p_pts > b_pts:
                winner_name = self.player.name
            elif s_pts > p_pts and b_pts > p_pts:
                winner_name = 'Bob and Sally'
                return f'{winner_name} are the MOST ULTIMATE winners!\n'
            else:
                winner_name = 'no one'
                tie_msg = "it's a tie :( "
                
            return f"{tie_msg}{winner_name} is the MOST ULTIMATE winner!\n"

    def run_bonus_game(self):
        """
        This method sets up and executes the bonus game. It's
        called only if the human player wins the standard game.
        """
        self.print_bonus_rules()
        
        # Reset game state for the new round
        self.player.reset_points()
        self.sally.reset_points()
        self.tie_points = 0
        self.bob = RobotPlayer(name="Bob") # Create the Bob player
        
        # Get new round total
        self.rounds_total = self.get_num_rounds('how many bonus rounds')
        self.current_round = 0
        
        # Bonus game loop
        for i in range(self.rounds_total):
            self.play_bonus_round()
            self.print_scores(is_bonus_round=True)
            
        print(self.get_final_winner(is_bonus_round=True))

    def run(self):
        """
        This is the main 'entry point' method for the game.
        It controls the high-level flow: setup, standard game
        loop, check for bonus round, and cleanup.
        """
        # --- Setup ---
        self.print_rules()
        # Create our player objects
        self.player = HumanPlayer(input("good luck... sorry, I didn't catch your name. what is it? "))
        self.sally = RobotPlayer(name="Sally")
        print(f"\nright, apologies {self.player.name}. good luck, but you won't need it. sally never fails...\n")
        self._divider()
        
        # --- Standard Game ---
        self.rounds_total = self.get_num_rounds('how many rounds would you like to play,')
        self.current_round = 0
        
        for i in range(self.rounds_total):
            self.play_standard_round()
            self.print_scores(is_bonus_round=False)
            
        print(self.get_final_winner(is_bonus_round=False))
        
        # --- Bonus Game Check ---
        # Check the 'winner_final' attribute to see if the player won
        if self.winner_final == self.player.name:
            self.run_bonus_game()
        
        print('bye bye. thanks for playing, come again soon!\n')


# ---------------------------------------------------------------------------
# SCRIPT EXECUTION
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    """
    This 'if __name__ == "__main__"' block is the standard
    entry point for a Python script. This code will only run
    when the file is executed directly (not imported as a module).
    
    All we do here is:
    1. 'Instantiate' (create an object from) our game class.
    2. Call the 'run' method to start the game.
    """
    game = DragonWizardKnightGame()
    game.run()
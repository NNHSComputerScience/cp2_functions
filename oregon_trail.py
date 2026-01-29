"""
Partner 1:
Partner 2:
Title: Oregon Trail
Description: Recreation of the adventure simulation game of traveling out west in 1800's.
"""
import random, os

# -----------------------------------------------------------
# Help Text -- global variables that contain helper text to display in game (don't edit)
# -----------------------------------------------------------
welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel (t) - moves you randomly between 30-60 miles and takes 3-7 days (random).
  rest   (r) - increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
  hunt   (h) - adds 100 lbs of food and takes 2-5 days (random).

You can also enter one of these commands without using up your turn:

  status (s) - lists food, health, distance traveled, and day.
  help   (?) - lists all the commands.
  quit   (q) - will end the game.
"""

good_luck_text = "\nGood luck, and see you in Oregon!"

# -----------------------------------------------------------
# FUNCTION DEFINITIONS -- beginning of function definitions; see comments explaining each function above each function header
# -----------------------------------------------------------
# first function is done for you!
def handle_invalid_input(response):
    """Display a helpful response when an invalid command is entered.

    Args:
        response (str): The invalid command entered by the player.

    Returns:
        None

    Example:
        >>> handle_invalid_input('x')  # prints a message to stdout
        "'x' is not a valid command. Try again."
    """
    print(f"'{response}' is not a valid command. Try again.")

def date_as_string(m, d):
    """Convert a numeric date to a readable string.

    Args:
        m (int): Month (1-12).
        d (int): Day (1-31).

    Returns:
        str: A string like "December 24".

    Note:
        This function does not enforce calendar rules and may return impossible dates such as "June 95" or "February 31".

    Example:
        >>> date_as_string(12, 24)
        'December 24'
    """
    date_string = NAME_OF_MONTH[m] + " " + str(d)
    return date_string

def miles_remaining():
    """Return the number of miles remaining until Oregon.
    Returns:
		int: Miles remaining to reach Oregon.
    Hint: Use the global distance constants and the current miles_traveled.
    """
    pass # Enter your code here

def handle_status():
    """Print the player's current status.

    Displays food remaining, health level, distance traveled, miles remaining, and current date to stdout.

    Returns:
        None

    Example:
        >>> handle_status()  # prints status to stdout
    """
    pass

def handle_help():
    """Show the help text describing available commands.

    Prints the global `help_text` to stdout.

    Returns:
        None

    Example:
        >>> handle_help()  # prints the help text
    """
    pass

def handle_quit():
    """Handle quitting the game mid-play.

    Performs any necessary cleanup, prints a farewell message, and stops play.

    Returns:
        bool: False to indicate the game should end; True otherwise.

    Example:
        >>> handle_quit()  # prints goodbye message and exits loop in `main`
    """
    pass

def days_in_month(m):
    """Return the number of days in a month.

    Args:
        m (int): Month number (1=January, ..., 12=December).

    Returns:
        int: Number of days in the month (28, 30, or 31). Returns 0 for invalid month values.

    Example:
        >>> days_in_month(2)
        28
    """
    pass

def maybe_rollover_month():
    """Advance the month/day if the current day exceeds days in the current month.

    Modifies the global `month` and `day` variables when rollover is needed.

    Returns:
        bool: True if month/day were adjusted, False otherwise.

    Example:
        >>> month, day = 1, 32
        >>> maybe_rollover_month()
        True
        >>> (month, day)
        (2, 1)
    """
    pass

def consume_food():
    """Consume food for a single day by reducing the global `food_remaining`.

    Side effects:
        Modifies the global `food_remaining` variable by subtracting `FOOD_EATEN_PER_DAY`.

    Returns:
        None

    Example:
        >>> food_remaining = 500
        >>> consume_food()
        >>> food_remaining
        495
    """
    pass

def handle_sickness():
    """Apply the effects of sickness to the player.

    Side effects:
        Decrements global `health_level`, may print a message, and updates `sicknesses_suffered_this_month`.

    Returns:
        None

    Example:
        >>> health_level = 5
        >>> handle_sickness()
        >>> health_level
        4
    """
    pass

def handle_hunt():
    """Handle hunting: add food and advance the game clock.

    Side effects:
        Adds `FOOD_PER_HUNT` to global `food_remaining` and advances the game clock by a random number of days within hunt bounds.

    Returns:
        None

    Example:
        >>> food_remaining = 200
        >>> handle_hunt()
        >>> food_remaining >= 300
        True
    """
    pass

def random_sickness_occurs():
    """Determine if sickness occurs today using the monthly guarantee system.

    Returns:
        bool: True if sickness occurs today, False otherwise.

    Example:
        >>> random_sickness_occurs() in (True, False)
        True
    """
    pass

def advance_game_clock():
    """Advance the game clock day-by-day and process daily events such as sickness.

    Notes:
        The intended behavior is to accept an integer `days` representing how many days to advance. Each day should:
          - consume food,
          - increment the day counter,
          - call `maybe_rollover_month()` to handle month/day rollover, and
          - check for sickness via `random_sickness_occurs()` and handle_sickness() accordingly
          
	Parameters:
		days (int): Number of days to advance the game clock.
    Returns:
        None

    Example:
        >>> advance_game_clock(3)  # advance internal game clock by 3 days and performs daily actions
    """
    pass

def handle_travel():
    """Perform a travel action: move, advance the game clock, and update state accordingly.

    Side effects:
        - Updates global `miles_traveled`, 
        - advances the game clock, and 
        - may also display messages about travel progress

    Returns:
        None

    Example:
        >>> miles_traveled = 0
        >>> handle_travel()
        >>> miles_traveled > 0
        True
    """
    pass

def handle_rest():
    """Handle resting: increase health and advance the game clock.

    Side effects:
        - Increases global `health_level`, not exceeding `MAX_HEALTH`,
        - advances game clock, and 
        - may display messages about resting

    Returns:
        None

    Example:
        >>> health_level = 3
        >>> handle_rest()
        >>> health_level
        4
    """
    pass

def player_wins():
    """Return True if the player has won the game.

    Returns:
        bool: True if the player has reached Oregon before the final date and is alive, False otherwise.

    Example:
        >>> miles_traveled = MILES_BETWEEN_MISSOURI_AND_OREGON
        >>> player_wins()
        True
    """
    pass

def game_is_over():
    """Return True if the game is over.

    The game is over if the player has died, run out of food, or reached the final date.

    Returns:
        bool: True if the game has ended, False otherwise.

    Example:
        >>> game_is_over() in (True, False)
        True
    """
    pass

# ---------------------------------------------------------
# Game Constants -- global variable constants that define the rules of the game, and which don't change.
# ---------------------------------------------------------
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_MISSOURI_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]

# -----------------------------------------------------------
# Game State -- global variables that collectively represent the state of the game
# -----------------------------------------------------------
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
player_name = None

# -----------------------------------------------------------
# MAIN GAME -- beginning of the main game code
#        You should not change any global variables in this function.
# -----------------------------------------------------------
def main():
    global player_name

    playing = True

    print(welcome_text + help_text + good_luck_text)
    player_name = input("\nWhat is your name, player? ").title()

    handle_status()
    input("\nPress enter to start your journey...")
    while playing:
        print()
        action = input(f"\nChoose an action, {player_name} --> ").lower().strip()
        if action == "travel" or action == "t":
            handle_travel()
        elif action == "rest" or action == "r":
            handle_rest()
        elif action == "hunt" or action == "h":
            handle_hunt()
        elif action == "quit" or action == "q":
            playing = handle_quit()
        elif action == "help" or action == "?":
            handle_help()
        elif action == "status" or action == "s":
            handle_status()
        else:
            handle_invalid_input(action)

        if game_is_over():
            playing = False

    if player_wins():
        print("\n\nCongratulations you made it to Oregon alive!\n")
        handle_status()
        print("""\n
            __   __              _    _  _         _
            \ \ / /             | |  | |(_)       | |
             \ V / ___   _   _  | |  | | _  _ __  | |
              \ / / _ \ | | | | | |/\| || || '_ \ | |
              | || (_) || |_| | \  /\  /| || | | ||_|
              \_/ \___/  \__,_|  \/  \/ |_||_| |_|(_)
            """)

    else:
        print("\n\nAlas, you lose...\n")
        handle_status()
        print("""\n
             _____                        _____
            |  __ \                      |  _  |
            | |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __
            | | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
            | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |
             \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
            """)
if __name__ == "__main__":
    main()
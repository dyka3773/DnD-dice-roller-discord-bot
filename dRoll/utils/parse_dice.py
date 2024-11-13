import re


def parse_roll_string(roll_string: str) -> tuple[int, int, int]:
    """Parses a string representing a dice roll into a tuple of the number of dice, the number of sides, and the bonus on the roll.

    Args:
        roll_string (str): The string representing the dice roll. eg. "1d6+2"

    Returns:
        tuple[int, int, int]: A tuple of the number of dice, the number of sides, and the bonus on the roll.
    """
    if not re.match(r"^\d+d\d+(\s*\+\s*\d+)?$", roll_string):
        raise ValueError(
            "Invalid input. Please provide a valid dice roll string. eg. 1d6+2 or 2d8")
    if "+" in roll_string:
        number_of_dice, number_of_sides = map(str, roll_string.split("d"))
        number_of_dice = int(number_of_dice)
        number_of_sides, bonus_on_roll = map(int, number_of_sides.split("+"))
    else:
        number_of_dice, number_of_sides = map(int, roll_string.split("d"))
        bonus_on_roll = 0

    return number_of_dice, number_of_sides, bonus_on_roll

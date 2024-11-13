import random


class Dice:
    number_of_dice: int
    number_of_sides: int
    bonus_on_roll: int

    warn_str: str = ""
    error_str: str = ""

    def roll_dice(self) -> list[int]:
        """Rolls the dice and returns the results as a list.

        Returns:
            list[int]: A list of the results of the dice rolls.
        """
        return [
            random.randint(1, self.number_of_sides)
            for _ in range(self.number_of_dice)
        ]

    def __str__(self) -> str:
        """Returns a string representation of the dice roll.

        Returns:
            str: A string representation of the dice roll.
        """
        rolls = self.roll_dice()
        total = sum(rolls) + self.bonus_on_roll

        rolls_str = "Rolls: " + ", ".join(map(str, rolls))
        bonus_str = f"Bonus: {self.bonus_on_roll}" if self.bonus_on_roll else ""
        total_str = f"Total: {total}"

        return "\n".join(filter(None, [self.error_str, self.warn_str, rolls_str, bonus_str, total_str]))

import crescent
import hikari
import random

plugin = crescent.Plugin[hikari.GatewayBot, None]()

@plugin.include
@crescent.command(name="roll_handwritten", description="Rolls a dice using a string to represent the dice.")
class Dice:
    roll_string = crescent.option(
        str,
        description="The dice to roll.",
        default="1d6",
    )
    
    @staticmethod
    def parse_roll_string(roll_string: str) -> tuple[int, int, int]:
        """Parses a string representing a dice roll into a tuple of the number of dice, the number of sides, and the bonus on the roll.

        Args:
            roll_string (str): The string representing the dice roll. eg. "1d6+2"

        Returns:
            tuple[int, int, int]: A tuple of the number of dice, the number of sides, and the bonus on the roll.
        """
        # TODO: Move this to a utility directory
        
        number_of_dice, number_of_sides = map(int, roll_string.split("d")) #TODO: Implement error handling for invalid input
        bonus_on_roll = 0
        
        if "+" in str(number_of_sides):
            number_of_sides, bonus_on_roll = map(int, number_of_sides.split("+")) #TODO: Implement error handling for invalid input
        
        return number_of_dice, number_of_sides, bonus_on_roll
    
    async def callback(self, ctx: crescent.Context) -> None:
        # TODO: Sanitize input
        self.number_of_dice, self.number_of_sides, self.bonus_on_roll = self.parse_roll_string(self.roll_string)
        
        rolls = [
            random.randint(1, self.number_of_sides)
            for _ in range(self.number_of_dice)
        ]
        total = sum(rolls) + self.bonus_on_roll
        
        rolls_str = "Rolls: " + ", ".join(map(str, rolls))
        bonus_str = f"Bonus: {self.bonus_on_roll}" if self.bonus_on_roll else ""
        total_str = f"Total: {total}"
        
        await ctx.respond(
            "\n".join(filter(None, [rolls_str, bonus_str, total_str]))
        )

import crescent
import hikari
import random

plugin = crescent.Plugin[hikari.GatewayBot, None]()

@plugin.include
@crescent.command(name="roll", description="Rolls a dice.")
class Dice:
    number_of_dice = crescent.option(
        int,
        description="The number of dice to roll.",
        default=1,
        min_value=1,
    )
    
    number_of_sides = crescent.option(
        int,
        description="The number of sides on each die.",
        default=6,
        min_value=1,
    )
    
    bonus_on_roll = crescent.option(
        int,
        description="A bonus to add to the roll.",
        default=0,
    )
    
    async def callback(self, ctx: crescent.Context) -> None:
        rolls = [
            random.randint(1, self.number_of_sides)
            for _ in range(self.number_of_dice)
        ]
        total = sum(rolls) + self.bonus_on_roll
        
        error_str = "" # TODO: Implement error handling
        warn_str = ""
        
        if ctx.options.get("number_of_dice") == None:
            warn_str += "Number of dice not specified. Defaulting to 1. \n"
        if ctx.options.get("number_of_sides") == None:
            warn_str += "Number of sides not specified. Defaulting to 6. \n"
        if ctx.options.get("bonus_on_roll") == None:
            warn_str += "Bonus on roll not specified. Defaulting to 0. \n"
        
        rolls_str = "Roll(s): " + ", ".join(map(str, rolls))
        bonus_str = f"Bonus: {self.bonus_on_roll}" if self.bonus_on_roll else ""
        total_str = f"Total: {total}"
        
        await ctx.respond(
            "\n".join(filter(None, [error_str, warn_str, rolls_str, bonus_str, total_str]))
        )

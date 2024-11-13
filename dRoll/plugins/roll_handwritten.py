import crescent
import hikari

from dRoll.models.dice import Dice
from dRoll.utils.parse_dice import parse_roll_string

plugin = crescent.Plugin[hikari.GatewayBot, None]()


@plugin.include
@crescent.command(name="roll_handwritten", description="Rolls a dice using a string to represent the dice.")
class DiceHandwritten(Dice):
    roll_string = crescent.option(
        str,
        description="The dice to roll.",
        default="1d6",
    )

    async def callback(self, ctx: crescent.Context) -> None:
        self.number_of_dice, self.number_of_sides, self.bonus_on_roll = parse_roll_string(
            self.roll_string)

        if ctx.options.get("roll_string") == None:
            self.warn_str += "> Roll string not specified. Defaulting to 1d6. \n"

        await ctx.respond(str(self))

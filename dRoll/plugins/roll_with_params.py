import crescent
import hikari

from dRoll.models.dice import Dice

plugin = crescent.Plugin[hikari.GatewayBot, None]()


@plugin.include
@crescent.command(name="roll", description="Rolls a dice.")
class DiceWithParams(Dice):
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
        # TODO: Implement error handling

        if ctx.options.get("number_of_dice") == None:
            self.warn_str += "> Number of dice not specified. Defaulting to 1. \n"
        if ctx.options.get("number_of_sides") == None:
            self.warn_str += "> Number of sides not specified. Defaulting to 6. \n"
        if ctx.options.get("bonus_on_roll") == None:
            self.warn_str += "> Bonus on roll not specified. Defaulting to 0. \n"

        await ctx.respond(str(self))

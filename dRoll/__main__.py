import os

import hikari
import crescent

bot = hikari.GatewayBot(
    token=os.getenv("DISCORD_TOKEN"),
    intents=hikari.Intents.ALL
)
client = crescent.Client(bot)
client.plugins.load_folder("dRoll.plugins")

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        import asyncio

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    bot.run(
        asyncio_debug=True,
        activity=hikari.Activity(
            name="τάβλι",
            type=hikari.ActivityType.COMPETING
        ),
        check_for_updates=True,
    )

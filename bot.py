#!/usr/bin/env python3
import io
import os
from contextlib import redirect_stdout
from discord.ext.commands import Bot
from dotenv import load_dotenv
istanbul_setup = __import__('istanbul-setup')

def main(args):
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    bot = Bot(command_prefix='!')

    @bot.command()
    async def layout(ctx, *args):
        """Layout the board
        """
        with io.StringIO() as f:
            with redirect_stdout(f):
                istanbul_setup.main(args)
            f.seek(0)
            await ctx.send(f'```\n{f.read()}```')

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    bot.run(token)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
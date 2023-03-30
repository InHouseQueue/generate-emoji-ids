import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user.name}")


@bot.slash_command(name="ping", description="Check if the bot is online")
async def ping(ctx):
    await ctx.send("Pong!")


@bot.slash_command(name="listemojis", description="List all custom emojis with their IDs")
async def listemojis(ctx):
    emojis = [f"`<:{emoji.name}:{emoji.id}>`" for emoji in ctx.guild.emojis if not emoji.managed]
    emoji_list = "\n".join(emojis)
    if emoji_list:
        await ctx.send(f"Server Emojis:\n{emoji_list}")
    else:
        await ctx.send("No custom emojis found in this server.")


# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot.run("")

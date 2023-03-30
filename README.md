# Custom Emoji List Bot
This script creates a Discord bot using the disnake library, which is a fork of discord.py with native support for slash commands. The bot has two slash commands: `/ping` and `/listemojis`. The `/ping` command checks if the bot is online, and the `/listemojis` command sends a list of custom emojis with their IDs from the server where the command is executed.

## How it works
The bot connects to the Discord API using the disnake library and listens for incoming events, such as slash commands. When a user issues a slash command, the corresponding command function is executed, and the bot responds with the appropriate message.

The /listemojis command iterates through the custom emojis of the server and formats them in the form <:emoji:ID>. The bot then sends this list of custom emojis wrapped in code blocks, which prevents Discord from converting the emoji format into the actual emoji image, allowing users to see the raw text.

## How to run the script
Make sure you have Python 3.6 or higher installed on your system.

Install the disnake library using pip:


`pip install disnake`

Replace the `YOUR_BOT_TOKEN` placeholder in the bot.py script with your bot's actual token.

## Run the script using Python:

`python bot.py`

The bot should now be online and ready to receive commands in the servers it has been invited to. Make sure to invite your bot to the server with the "applications.commands" OAuth scope for the slash commands to work.

## Usage
`/ping`: Checks if the bot is online. The bot will respond with "Pong!" if it is online.
`/listemojis`: Lists all custom emojis with their IDs in the server where the command is executed. The bot will send the list in the format `<:emoji:ID>` wrapped in code blocks.


## Results 
![image](https://user-images.githubusercontent.com/31442053/228791111-517c4f64-d04e-4b25-9de1-e0e79896f494.png)

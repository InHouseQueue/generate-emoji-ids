# Custom Emoji List Bot
This script creates a Discord bot using the disnake library, which is a fork of discord.py with native support for slash commands. 

## Features:
- /ping: A simple command to check if the bot is online and responsive.
- /listemojis: Lists all custom emojis within the server and their respective IDs.
- /toggledquotes: Toggles the inclusion of double quotes around the custom emoji IDs in the list.

## How it works
The bot connects to the Discord API using the disnake library and listens for incoming events, such as slash commands. When a user issues a slash command, the corresponding command function is executed, and the bot responds with the appropriate message.

The `/listemojis` command iterates through the custom emojis of the server and formats them in the form <:emoji:ID>. The bot then sends this list of custom emojis wrapped in code blocks, which prevents Discord from converting the emoji format into the actual emoji image, allowing users to see the raw text.

`/toggledquotes`: Toggles the use of double quotes around the custom emoji IDs in the /listemojis output. When enabled, the list will include double quotes around each custom emoji ID; when disabled, the list will exclude double quotes.

## How to run the script
Make sure you have Python 3.6 or higher installed on your system.

Install the disnake library using pip:


`pip install disnake`

Replace the `YOUR_BOT_TOKEN` placeholder in the bot.py script with your bot's actual token.

## Run the script using Python:

`python bot.py`

The bot should now be online and ready to receive commands in the servers it has been invited to. Make sure to invite your bot to the server with the "applications.commands" OAuth scope for the slash commands to work.


## Results 
With quotes

```
"<:Udyr:1072140234474651688>"
"<:Urgot:1072140235745546300>"
"<:Varus:1072140238144671794>"
"<:Vayne:1072140240157945948>"
"<:Veigar:1072140243286888559>"
"<:Velkoz:1072140245497303060>"
```
Without 

```
<:Udyr:1072140234474651688>
<:Urgot:1072140235745546300>
<:Varus:1072140238144671794>
<:Vayne:1072140240157945948>
<:Veigar:1072140243286888559>
<:Velkoz:1072140245497303060>
```

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

# Load command files
command_files = [file for file in os.listdir('./commands') if file.endswith('.py')]
commands = {}

for file in command_files:
    command_name = os.path.splitext(file)[0]
    command = getattr(__import__('commands.' + command_name), command_name)
    commands[command_name] = command

@bot.event
async def on_message(message):
    # Ignore messages from bots
    if message.author.bot:
        return

    # Check for command
    if message.content.startswith('?'):
        args = message.content[1:].strip().split(' ')
        command_name = args.pop(0).lower()

        # Check if the command exists
        if command_name not in commands:
            await message.channel.send(f"{message.author.mention}, Tuntematon komento '{command_name}'. tee komento ?help nähdäksesi käytössä olevat komennot.")
            return

        # Execute the command
        command = commands[command_name]
        await command.execute(message, args, bot, commands)

        # Delete the user's command message only for configured commands
        if command_name in ['clear','wiki','ping','troll','ehdotus']:  # Add other configured commands as needed
            await message.delete()

# Load events from the "events" folder
for filename in os.listdir('./events'):
    if filename.endswith('.py') and not filename.startswith('__'):
        event_module = __import__(f'events.{filename[:-3]}', fromlist=[''])
        if hasattr(event_module, 'setup'):
            event_module.setup(bot)

bot_token = os.getenv('BOT_TOKEN')
if not bot_token:
    print("Bot token not found. Set the 'BOT_TOKEN' environment variable.")
    exit()

bot.run(bot_token)
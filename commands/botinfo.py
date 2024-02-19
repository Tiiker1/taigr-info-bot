# commands/botinfo.py
import discord

# Replace 'YOUR_USER_ID' with your actual Discord user ID
ALLOWED_USER_ID = 267240625596792833  # Example user ID

async def execute(message, args, client, commands):
    # Check if the command is being executed by the allowed user
    if message.author.id != ALLOWED_USER_ID:
        await message.channel.send("Sinulla ei ole oikeuksia tämän komennon suorittamiseen.")
        return

    bot_user = client.user
    bot_info = (
        f"Botin nimi: {bot_user.name}\n"
        f"Botin ID: {bot_user.id}\n"
        f"Luotu: {bot_user.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Botin prefix: {client.command_prefix}\n"
        f"Palvelimet: {len(client.guilds)}\n"
        f"Käyttäjät: {len(client.users)}"
    )

    await message.channel.send(bot_info)

# Assign the execute function to a 'name' attribute
execute.__command_name__ = 'botinfo'
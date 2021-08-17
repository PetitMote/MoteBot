import discord

from settings import settings

client = discord.Client()


@client.event
async def on_ready():
    print("Connecté en tant que {0.user}".format(client))


@client.event
async def on_message(message):
    if client.user in message.mentions:
        print(f"Message de {message.author} reçu : {message.content}")
        await message.channel.send(settings.get("insult", "Je n'aime pas les gens. Veuillez me laisser tranquille. Je suis un bot."))


client.run(settings["token_id"])

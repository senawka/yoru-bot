import discord

client = discord.Client()
key = ""

block_words = ["dylan", "catz", "minor"]


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


@client.event
async def on_message(msg):
    if msg.author != client.user:

        for text in block_words:
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return
    if msg.author != client.user:
        if msg.content.lower().startswith("?hi"):
            await msg.delete()
            await msg.channel.send(f"Yoru Bot is fully operational.")
    if msg.author != client.user:
        if msg.content.lower().startswith("?dword"):
            await msg.delete()
            await msg.channel.send(f"https://cdn.discordapp.com/attachments/1040931449517391872/1042285890006945842/image.png")
    if msg.author != client.user:
        if msg.content.lower().startswith("?sus"):
            await msg.delete()
            await msg.channel.send(f"https://cdn.discordapp.com/attachments/1040931449517391872/1042340515808563251/image.png")


client.run(key)

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
            await msg.channel.send(f"Yoru Bot is fully operational.")



client.run(key)

import discord as disc

intents = disc.Intents.default()
intents.message_content = True

client = disc.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send("yes")
        #displayHelp()
        pass

    elif message.content.startswith("$Xur"):
        #getXurItems()
        pass
    
    elif message.content.startswith("$Banshee"):
        #getBansheeItems()
        pass

client.run('your token here')
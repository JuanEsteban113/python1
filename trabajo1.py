import discord
from bot_loging import gen_pass 

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):  
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("MTI3NTk3ODk5MTY4NTIwNjAxNw.Gk9IPL.tQkp3W56XNI7OgXyva8Dz0xnkOxwGzo_stA_e8")

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Configurar permisos del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

# Comando para repetir un mensaje
@bot.command()
async def repetir(ctx, *, message: str):
    await ctx.send(message)

# Comando de saludo
@bot.command()
async def saludo(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()  # Convertir a minúsculas y eliminar espacios extra
    respuestas = {
        "hola": "¡Hola! ¿Cómo estás? 😊",
        "adiós": "¡Hasta luego! 👋",
        "gracias": "¡De nada! 😃"
    }
    
    # Verificar si alguna palabra clave está en el mensaje
    for clave, respuesta in respuestas.items():
        if clave in mensaje:
            await ctx.send(respuesta)
            return

    await ctx.send("No entendí tu saludo. 😕")  # Respuesta por defecto

# Iniciar el bot con el token seguro
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: No se encontró el token del bot en las variables de entorno.")

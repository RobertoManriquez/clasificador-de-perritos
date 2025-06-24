import discord
from discord.ext import commands
from modelo import get_class
#permisos
intencions = discord.Intents.default()
intencions.message_content = True
#Objeto bot
bot = commands.Bot(command_prefix='!', intents=intencions)
#Prender bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord')
    
#Primer comando
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for img in ctx.message.attachments:
            nombre_img = img.filename

            import os
            os.makedirs("imagenes", exist_ok=True)

            await img.save(f'imagenes/{nombre_img}')
            await ctx.send("Imagen guardada ✅")

            try:
                resultado = get_class(
                    model_path="./keras_model.h5",
                    labels_path="labels.txt",
                    image_path=f'imagenes/{nombre_img}'
                )
                await ctx.send(f"🔎 RESULTADO: {resultado}")
            except Exception as e:
                await ctx.send(f"❌ Error al procesar la imagen: {e}")
    else:
        await ctx.send("❌ No hay archivo adjunto.")

#Correr    
token = 'MTMyNjMzMjgyNjk5NTY1ODc3Mg.GttFla.vl-tPRw-YL8TS-beb-E_3ZZw_L2B7olO0k3AAE'
bot.run(token)
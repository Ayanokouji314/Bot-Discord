import discord
from discord.ext import commands
import os
import websever

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# 📩 Evento para enviar mensaje de bienvenida cuando alguien se une al servidor
@bot.event
async def on_member_join(member):
    canal_bienvenida = discord.utils.get(member.guild.channels, name="𓂀-𝕎𝕖𝕝𝕔𝕠𝕞𝕖-𓂀")  # Nombre del canal
    if canal_bienvenida:
        embed = discord.Embed(
             title=f"𖧁᭕᭢ 𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {member.mention} ꨄ︎",
             description=f"""
𝐸𝑠𝑡𝑎𝑚𝑜𝑠 𝑐𝑎𝑢𝑡𝑖𝑣𝑎𝑑𝑜𝑠 𝑝𝑜𝑟 𝑞𝑢𝑒 𝑓𝑜𝑟𝑚𝑒𝑠 𝑝𝑎𝑟𝑡𝑒 𝑑𝑒 𝑛𝑢𝑒𝑠𝑡𝑟𝑜 𝑐𝑎𝑓𝑒𝑡𝜄́𝑛. . .ᐟ

𝑉𝑒𝑛﹐ 𝑡𝑒 𝑖𝑛𝑣𝑖𝑡𝑜 𝑎 𝑣𝑖𝑠𝑖𝑡𝑎𝑟 𝑛𝑢𝑒𝑠𝑡𝑟𝑜𝑠 𝑐𝑎𝑛𝑎𝑙𝑒𝑠 ﹔

- * 𝜗𝜚 ℛℰ𝒢ℒ𝒜𝒮: 𝑒𝑛𝑐𝑜𝑛𝑡𝑟𝑎𝑟𝑎́𝑠 𝑙𝑎𝑠 𝑐𝑜𝑛𝑑𝑖𝑐𝑖𝑜𝑛𝑒𝑠 𝑞𝑢𝑒 𝑛𝑜𝑠 𝑎𝑦𝑢𝑑𝑎𝑟𝑎́𝑛 𝑎 𝑚𝑎𝑛𝑡𝑒𝑛𝑒𝑟 𝑢𝑛 𝑎𝑚𝑏𝑖𝑒𝑛𝑡𝑒 𝑝𝑙𝑒𝑛𝑜 𝑒 𝜄́𝑛𝑡𝑒𝑔𝑟𝑜.
- * 𝜗𝜚 ℛ𝒪ℒℰ𝒮: 𝑒𝑙𝑖𝑔𝑒 𝑙𝑜𝑠 𝑟𝑜𝑙𝑒𝑠 𝑞𝑢𝑒 𝑡𝑒 𝑔𝑢𝑠𝑡𝑒𝑛 𝑦 𝑞𝑢𝑒 𝑚𝑒𝑗𝑜𝑟 𝑡𝑒 𝑖𝑑𝑒𝑛𝑡𝑖𝑓𝑖𝑞𝑢𝑒𝑛.

🌸 ¡Disfruta tu estancia en **𝓜𝓸𝓴𝓪’𝓼 🧋 𝓚𝓮𝓲**! 🌸
            """,
            color=discord.Color.purple()  # Cambia el color si deseas
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/1285762781420720311/1371648224430915654/IMG_20250512_183945_044.jpg?ex=6823e674&is=682294f4&hm=b33c83d470a300732937d26508544785c8ac5255a1eca822b6071e6b7ca9ddb1&")  # Reemplaza con la URL de la imagen

        await canal_bienvenida.send(embed=embed)
# 🏆 Evento para asignar el rol cuando envían mensaje en #intro
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.name == "𓂀-𝕀𝕟𝕥𝕣𝕠-𓂀":
        role_name = "𝖒𝖎𝖊𝖒𝖇𝖗𝖔"
        role = discord.utils.get(message.guild.roles, name=role_name)

        if role:
            await message.author.add_roles(role)
            await message.channel.set_permissions(message.author, send_messages=False)
            await message.channel.send(f"{message.author.mention} ha recibido el rol **{role.name}**. 🎉", delete_after=10)

    await bot.process_commands(message)  # Permitir otros comandos

# Comando de prueba
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Soy tu bot de Discord. 🚀")

websever.keep_alive()
# Token del bot
bot.run("MTM3MTYyMzkyMDY1ODE1MzUzMw.G8sAaP.TfdWh5YPR67Yh60btebv4WrAl6nowY9kzzwu94")  # Reemplázalo con el token de tu bot

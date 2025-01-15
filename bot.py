

import discord
from discord.ext import commands

# Создаем экземпляр клиента с намерениями для работы с личными сообщениями
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')

@bot.event
async def on_message(message):
    # Проверяем, является ли сообщение личным и не от самого бота
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        await message.channel.send("Я робот, у меня памяти пять мегабайт.")

# Запуск бота. Замените 'YOUR_BOT_TOKEN' на токен вашего бота.
bot.run('MTMyOTEyOTMwNjk5NTI5ODM1NA.GJMaJ5.Aty5VKJ31QYMrDBbp934zhCuOTbZiFZy80MDpU')


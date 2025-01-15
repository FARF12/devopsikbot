import os
import discord
from discord.ext import commands

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения.")


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
        await message.channel.send("Я робот, у меня памяти 16 мегабайт.")

# Запуск бота с использованием токена из переменной окружения
bot.run(BOT_TOKEN)

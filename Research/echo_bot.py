import logging  # Importing logging module for logging purposes
from aiogram import Bot, Dispatcher, executor, types  # Importing necessary modules from aiogram library
from dotenv import load_dotenv  # Importing load_dotenv function from dotenv module
import os  # Importing os module for interacting with the operating system
load_dotenv()  # Loading environment variables from .env file
API_TOKEN = os.getenv('TOKEN')  # Getting the API token from environment variables
#print(API_TOKEN)

logging.basicConfig(level=logging.INFO)  # Configuring logging to display INFO level messages

bot = Bot(token=API_TOKEN)  # Creating a Bot instance with the provided API token
dp = Dispatcher(bot)  # Creating a Dispatcher instance associated with the Bot instance
# Dispatcher helps you to connect this token to your Telegram account

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")  # Sending a welcome message to the user

@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler will be called for any message other than `/start` or `/help` commands
    """
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)  # Echoing back the received message

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # Starting the event loop to process incoming updates

import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Get Telegram bot token from environment variable
TOKEN = os.getenv('TOKEN')

# Set the model name for OpenAI's GPT-3.5 model
MODEL_NAME = "gpt-3.5-turbo-0125"

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Create a bot instance
bot = Bot(token=TOKEN)

# Create a Dispatcher instance
dispatcher = Dispatcher(bot)

# Class to store reference to the previous response
class Reference:
    def __init__(self) -> None:
        self.response = ""

# Instance of Reference class
reference = Reference()

# Function to clear the previous conversation and context
def clear_past():
    reference.response = ""

# Handler for '/start' command
@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hi!\nI am a ChatBot!\nCreated by Abrar. How may I help you?")

# Handler for '/clear' command
@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    await message.reply("I have cleared the past conversation!")
    clear_past()

# Handler for '/help' command
@dispatcher.message_handler(commands=['help'])
async def help(message: types.Message):
    help_command = """
    Hi there, I am a Chatbot created by Abrar! Please follow the instructions -
    /start - to start a new conversation
    /clear - to clear the past conversation.
    /help - to get help.
    """
    await message.reply(help_command)

# Handler for chat interaction
@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    print(f">>> USER: \n\t{message.text}")  # Print user message to console
    # Generate response using OpenAI's GPT-3.5 model
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response['choices'][0]['message']['content']  # Store the response for reference
    print(f">>> ChatGPT: \n\t{reference.response}")  # Print ChatGPT response to console
    await bot.send_message(chat_id=message.chat.id, text=reference.response)  # Send ChatGPT response to user

# Start the event loop to process incoming updates
if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)

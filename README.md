# ChatBot using OpenAI LLM and Telegram

## Description

Welcome to our ChatBot project! This project aims to provide an interactive chatbot experience using OpenAI's GPT-3.5 model and the Telegram messaging platform. With this ChatBot, you can engage in natural language conversations on a wide range of topics.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Integration with Telegram for real-time chat interaction.
- Utilizes OpenAI's GPT-3.5 model for generating natural language responses.
- Command-based functionality for starting conversations, clearing context, and accessing help.

## Getting Started

To get started with the chatbot, follow the instructions below.

### Prerequisites

Make sure you have the following installed:

- Python 3.8
- Required Python packages listed in `requirements.txt`
- Telegram account

### Installation

1. Clone this repository:

git clone https://github.com/Abrar-Hussain0/ChatBot-using-OpenAI-LLM.git


2. Navigate to the project directory:

cd your-repository


3. Install dependencies using pip:

pip install -r requirements.txt

4. Set up Environment Variables:

TOKEN = your_telegram_bot_token_here
OPENAI_API_KEY = your_openai_api_key_here


### Usage

1. Set up your environment variables by creating a `.env` file and adding your Telegram bot token and OpenAI API key:

TOKEN=your-telegram-bot-token
OPENAI_API_KEY=your-openai-api-key


2. Run the main script `my_bot.py`:

python my_bot.py


3. Interact with the chatbot using your Telegram account.

## Contributing

Contributions are welcome! Please follow the standard GitHub flow: fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to OpenAI for providing access to the GPT-3.5 model.
- Special thanks to the aiogram community for their Telegram bot framework.

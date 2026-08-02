# 🔐 Telegram Encrypt/Decrypt Bot

A simple Telegram bot built with Python that encrypts and decrypts text using the Devglan Online Encryption API.

## Features

- 🔒 Encrypt any text
- 🔓 Decrypt encrypted text
- 🤖 Telegram inline buttons
- ⚡ Instant responses
- 📨 Simple and lightweight

## Tech Stack

- Python 3
- pyTelegramBotAPI
- Requests
- Devglan Encryption API

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/cryptographyBot.git
cd cryptographyBot
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install pyTelegramBotAPI requests
```

or

```bash
pip install -r requirements.txt
```

## Configuration

Open the source file and replace:

```python
bot = TeleBot("BOT_TOKEN", parse_mode="HTML")
```

with your BotFather token.

You can also update the Telegram links:

```python
Group 
Channel
```

to your own community links.

## Usage

Start the bot.

```bash
python main.py
```

Open your bot on Telegram.

Send any message.

Example:

```
Hello World
```

The bot will reply with two buttons:

- Encrypt
- Decrypt

Press **Encrypt** to get the encrypted version.

Press **Decrypt** to convert it back.

## Project Structure

```
.
├── main.py
├── requirements.txt
└── README.md
```

## Dependencies

```
pyTelegramBotAPI
requests
```

Generate a requirements file:

```bash
pip freeze > requirements.txt
```

## Notes

- This project relies on the Devglan online encryption service.
- An active internet connection is required.
- If the external API changes or becomes unavailable, encryption/decryption may stop working.
- Avoid committing your Telegram Bot Token to GitHub.

## Disclaimer

This project is intended for educational purposes only.

Do not use it to store or transmit sensitive information. Since encryption is performed through a third-party service, you should not rely on it for production-grade security.

## License

MIT License

---

Made with ❤️ using Python and the Telegram Bot API.

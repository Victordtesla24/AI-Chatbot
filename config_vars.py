import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

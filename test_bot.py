```python
import os
import unittest
import discord
import openai
from dotenv import load_dotenv
import agency_swarm
import main

class TestRosaAIChatbot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.discord_token = os.getenv('DISCORD_TOKEN')
        cls.openai_api_key = os.getenv('OPENAI_API_KEY')

    def test_env_variables(self):
        self.assertIsNotNone(self.discord_token, "DISCORD_TOKEN is not set")
        self.assertIsNotNone(self.openai_api_key, "OPENAI_API_KEY is not set")

    def test_discord_client(self):
        client = discord.Client(intents=discord.Intents.default())
        self.assertIsInstance(client, discord.Client)

    def test_openai_api(self):
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, AI!"}]
        )
        self.assertIsNotNone(response.choices[0].message.content)

    def test_agency_swarm(self):
        result = agency_swarm.get_financial_prediction("Test data")
        self.assertIsNotNone(result)

    def test_main_bot_commands(self):
        self.assertIn('forecast', main.bot.all_commands)
        self.assertIn('inventory', main.bot.all_commands)
        self.assertIn('campaign', main.bot.all_commands)
        self.assertIn('report', main.bot.all_commands)

if __name__ == '__main__':
    unittest.main()

```

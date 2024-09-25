import os
import unittest
import discord
import openai
import requests
from dotenv import load_dotenv
import agency_swarm
import main

class TestRosaAIChatbot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.discord_token = os.getenv('DISCORD_TOKEN')
        cls.openai_api_key = os.getenv('OPENAI_API_KEY')
        cls.heroku_api_key = os.getenv('HEROKU_API_KEY')
        cls.heroku_app_name = os.getenv('HEROKU_APP_NAME')

    def test_env_variables(self):
        self.assertIsNotNone(self.discord_token, "DISCORD_TOKEN is not set")
        self.assertIsNotNone(self.openai_api_key, "OPENAI_API_KEY is not set")
        self.assertIsNotNone(self.heroku_api_key, "HEROKU_API_KEY is not set")
        self.assertIsNotNone(self.heroku_app_name, "HEROKU_APP_NAME is not set")

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

    def test_heroku_api_connection(self):
        headers = {
            'Accept': 'application/vnd.heroku+json; version=3',
            'Authorization': f'Bearer {self.heroku_api_key}'
        }
        response = requests.get(f'https://api.heroku.com/apps/{self.heroku_app_name}', headers=headers)
        self.assertEqual(response.status_code, 200, "Failed to connect to Heroku API")

    def test_dyno_scaling(self):
        headers = {
            'Accept': 'application/vnd.heroku+json; version=3',
            'Authorization': f'Bearer {self.heroku_api_key}'
        }
        response = requests.get(f'https://api.heroku.com/apps/{self.heroku_app_name}/formation', headers=headers)
        self.assertEqual(response.status_code, 200, "Failed to get dyno formation")
        formation = response.json()
        web_dyno = next((dyno for dyno in formation if dyno['type'] == 'web'), None)
        worker_dyno = next((dyno for dyno in formation if dyno['type'] == 'worker'), None)
        self.assertIsNotNone(web_dyno, "Web dyno not found")
        self.assertIsNotNone(worker_dyno, "Worker dyno not found")
        self.assertEqual(web_dyno['quantity'], 0, "Web dyno should be scaled to 0")
        self.assertEqual(worker_dyno['quantity'], 1, "Worker dyno should be scaled to 1")

if __name__ == '__main__':
    unittest.main()


import discord
from discord.ext import commands
import openai
from config_vars import DISCORD_TOKEN, OPENAI_API_KEY
import agency_swarm


# Set up OpenAI
openai.api_key = OPENAI_API_KEY

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='forecast')
async def forecast(ctx):
    result = agency_swarm.get_financial_prediction("Sample historical data")
    await ctx.send(f"Profit and Loss Forecast:\n{result}")

@bot.command(name='inventory')
async def inventory(ctx):
    result = agency_swarm.manage_inventory("Sample current inventory")
    await ctx.send(f"Current Inventory Status:\n{result}")

@bot.command(name='campaign')
async def campaign(ctx):
    result = agency_swarm.create_marketing_campaign("young adults", "$5000")
    await ctx.send(f"New Marketing Campaign:\n{result}")

@bot.command(name='report')
async def report(ctx):
    result = agency_swarm.generate_financial_report("Sample financial data")
    await ctx.send(f"Financial Report:\n{result}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Use OpenAI for general responses
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for a Mexican restaurant called Rosa."},
            {"role": "user", "content": message.content}
        ]
    )
    
    await message.channel.send(response.choices[0].message.content)
    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)

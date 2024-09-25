# agency_swarm.py
from openai import OpenAI
import config_vars

client = OpenAI(api_key=config_vars.OPENAI_API_KEY)

def get_financial_prediction(historical_data):
    prompt = f"Based on this historical data: {historical_data}, predict future profit and loss for Rosa Mexicano restaurant."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial expert for Rosa Mexicano restaurant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def manage_inventory(current_inventory):
    prompt = f"Given this current inventory: {current_inventory}, provide recommendations for inventory management for Rosa Mexicano restaurant."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an inventory management expert for Rosa Mexicano restaurant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def create_marketing_campaign(target_audience, budget):
    prompt = f"Create a marketing campaign for Rosa Mexicano restaurant targeting {target_audience} with a budget of {budget}."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a marketing expert for Rosa Mexicano restaurant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_financial_report(financial_data):
    prompt = f"Generate a professional financial report based on this data: {financial_data} for Rosa Mexicano restaurant."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial analyst for Rosa Mexicano restaurant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

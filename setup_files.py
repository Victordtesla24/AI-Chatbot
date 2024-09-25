import os
import requests

def create_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"{filename} created successfully.")

def create_procfile():
    content = "worker: python main.py"
    create_file("Procfile", content)

def create_runtime():
    content = "python-3.9.16"
    create_file("runtime.txt", content)

def create_requirements():
    content = """
discord.py==2.3.2
openai==1.3.5
python-dotenv==1.0.0
requests==2.26.0
"""
    create_file("requirements.txt", content)

def create_gitignore():
    content = """
__pycache__/
*.py[cod]
*$py.class
.env
"""
    create_file(".gitignore", content)

def create_env_file():
    discord_token = input("Enter your Discord token: ")
    openai_api_key = input("Enter your OpenAI API key: ")
    
    content = f"""DISCORD_TOKEN={discord_token}
OPENAI_API_KEY={openai_api_key}
"""
    create_file(".env", content)
    print(".env file created with your API keys. Keep this file secure and do not share it.")

def set_heroku_config(app_name, api_key, config_vars):
    url = f"https://api.heroku.com/apps/{app_name}/config-vars"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.patch(url, json=config_vars, headers=headers)
    if response.status_code == 200:
        print("Heroku config vars set successfully.")
    else:
        print(f"Failed to set Heroku config vars. Status code: {response.status_code}")

def prepare_for_deployment():
    create_procfile()
    create_runtime()
    create_requirements()
    create_gitignore()
    create_env_file()
    
    print("\nAll necessary files have been created.")
    print("\nNext steps:")
    print("1. Run the test script: python test_app.py")
    print("2. If tests pass, commit these files to your GitHub repository (except .env)")
    print("3. Set up Heroku:")
    print("   a. Create a new Heroku app via web UI or Heroku CLI")
    print("   b. Connect your GitHub repository to the Heroku app")
    print("   c. Set config vars in Heroku (manually or using the function below)")
    print("4. Deploy your app on Heroku using the GitHub integration")

    use_heroku_api = input("Do you want to set Heroku config vars using the API? (y/n): ")
    if use_heroku_api.lower() == 'y':
        app_name = input("Enter your Heroku app name: ")
        api_key = input("Enter your Heroku API key: ")
        config_vars = {
            "DISCORD_TOKEN": os.getenv('DISCORD_TOKEN'),
            "OPENAI_API_KEY": os.getenv('OPENAI_API_KEY')
        }
        set_heroku_config(app_name, api_key, config_vars)

if __name__ == "__main__":
    prepare_for_deployment()

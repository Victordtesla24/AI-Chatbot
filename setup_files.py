import os
import requests

def create_file(filename, content):
    documents_dir = os.path.expanduser('~/Documents')
    file_path = os.path.join(documents_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"{filename} created successfully at {file_path}")

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
    heroku_api_key = input("Enter your Heroku API key: ")
    heroku_app_name = input("Enter your Heroku app name: ")
    
    content = f"""DISCORD_TOKEN={discord_token}
OPENAI_API_KEY={openai_api_key}
HEROKU_API_KEY={heroku_api_key}
HEROKU_APP_NAME={heroku_app_name}
"""
    create_file(".env", content)
    print(".env file created with your API keys. Keep this file secure and do not share it.")

def scale_dynos(api_key, app_name):
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': f'Bearer {api_key}'
    }

    # Scale web to 0
    requests.patch(
        f'https://api.heroku.com/apps/{app_name}/formation/web',
        json={'quantity': 0},
        headers=headers
    )

    # Scale worker to 1
    requests.patch(
        f'https://api.heroku.com/apps/{app_name}/formation/worker',
        json={'quantity': 1},
        headers=headers
    )

    print("Heroku dynos scaled: web=0, worker=1")

def prepare_for_deployment():
    create_procfile()
    create_runtime()
    create_requirements()
    create_gitignore()
    create_env_file()
    
    print("\nAll necessary files have been created in your Documents folder.")
    print("\nNext steps:")
    print("1. Move these files to your project directory on a computer with Git access")
    print("2. Initialize a git repository if you haven't already:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Initial commit'")
    print("3. Create a GitHub repository and push your code:")
    print("   git remote add origin <your-github-repo-url>")
    print("   git push -u origin main")
    print("4. On Heroku, connect your app to the GitHub repository")
    print("5. Set environment variables on Heroku:")
    print("   - Go to Settings > Config Vars")
    print("   - Add DISCORD_TOKEN, OPENAI_API_KEY, and HEROKU_API_KEY with their respective values")
    print("6. Deploy your app on Heroku using the GitHub integration")
    
    # Scale dynos
    heroku_api_key = os.getenv('HEROKU_API_KEY')
    heroku_app_name = os.getenv('HEROKU_APP_NAME')
    if heroku_api_key and heroku_app_name:
        scale_dynos(heroku_api_key, heroku_app_name)
    else:
        print("Heroku API key or app name not found in .env file. Skipping dyno scaling.")

if __name__ == "__main__":
    prepare_for_deployment()

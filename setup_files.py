import os

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
    print("   - Add DISCORD_TOKEN and OPENAI_API_KEY with their respective values")
    print("6. Deploy your app on Heroku using the GitHub integration")

if __name__ == "__main__":
    prepare_for_deployment()


import os
import sys

def install_package(package):
    os.system(f"{sys.executable} -m pip install {package}")

packages = ['discord.py', 'openai', 'python-dotenv']

for package in packages:
    install_package(package)

print("All required packages have been installed.")

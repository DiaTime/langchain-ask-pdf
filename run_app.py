import os
import subprocess
import sys

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_app():
    os.system("streamlit run app.py")

if __name__ == "__main__":
    install_requirements()
    run_app()

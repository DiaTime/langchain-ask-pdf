import os
import subprocess
import sys
import venv

def create_and_activate_venv():
    if not os.path.exists('env'):
        venv.create('env', with_pip=True)
    if sys.platform == 'win32':
        activate_script = 'env\\Scripts\\activate.bat'
    else:
        activate_script = 'source env/bin/activate'
    os.system(activate_script)

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_app():
    os.system("streamlit run app.py")

if __name__ == "__main__":
    create_and_activate_venv()
    install_requirements()
    run_app()

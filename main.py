import multiprocessing
import subprocess
import os
import webbrowser
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")
FRONTEND_DIR = os.path.join(BASE_DIR, "SeaPortOptimizerFrontend")

def start_backend():
    subprocess.run([PYTHON_DIR, "-m", "flask", "run"])

def run_frontend():
    subprocess.run(["ng", "serve", "--open"], cwd=FRONTEND_DIR)

if __name__ == '__main__':
    #start backend
    multiprocessing.Process(target=start_backend).start()
    #start frontend
    multiprocessing.Process(target=run_frontend).start()
    time.sleep(5)
    #webbrowser.open("http://localhost:4200")

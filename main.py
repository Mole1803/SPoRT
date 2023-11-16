import multiprocessing
import subprocess
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_DIR = os.path.join(BASE_DIR, "venv", "bin", "python")
FRONTEND_DIR = os.path.join(BASE_DIR, "SeaPortOptimizerFrontend")

def start_backend():
    subprocess.run([PYTHON_DIR, "-m", "flask", "run"])

def run_frontend():
    # run angular
    subprocess.run(["ng", "serve", "--open"], cwd=FRONTEND_DIR)

if __name__ == '__main__':
    print(BASE_DIR)
    #os.system( f"{BASE_DIR} -m flask run")
    multiprocessing.Process(target=start_backend).start()
    multiprocessing.Process(target=run_frontend).start()



    print("Running frontend")
    #subprocess.run("")
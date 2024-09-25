import subprocess
from os.path import dirname

def wait(title, message):
    subprocess.call(["python3", dirname(__file__) + '/wait-script.py', title, message])
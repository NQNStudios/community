from talon import Module, app, actions
import subprocess
from os import environ
from os.path import exists, dirname
from time import sleep, strftime
from . wait import wait
import pyperclip

mod = Module()

HOME = environ["HOME"]
ffmpeg_path = "/opt/homebrew/bin/ffmpeg"
environ['PATH'] += f':{dirname(ffmpeg_path)}'

def wait_for_file(file):
    while not exists(file):
        sleep(0.1)
    return file

@mod.action_class
class Actions:
    def view_log():
        """view talon log"""
        actions.mimic("focus talon")
    def view_config():
        """view talon config"""
        subprocess.call(["open", f'{HOME}/.talon/user/community'])

    def type():
        """launch audacity, record audio, then transcribe it with Whisper"""
        # Start recording
        subprocess.call(["open", "-a", "Audacity"])
        actions.speech.disable()
        actions.key("r")

        # Wait for user to close a window
        wait("Recording", "Close this window to transcribe")

        # Export
        actions.key("super-shift-e")
        sleep(0.1)
        timestamp = strftime("%Y-%m-%d-%h-%m-%s")
        filename = timestamp + ".wav"
        actions.insert(filename)
        actions.key("enter")
        sleep(0.1)

        # Transcribe
        output = subprocess.check_output([f'{HOME}/Library/Python/3.9/bin/whisper', f'{HOME}/Documents/{filename}', '--model', 'tiny', '--language', 'English'], text=True).splitlines()
        output = list(filter(lambda line: line.startswith('['), output))
        just_text = ' '.join([line[line.find(']') + 2:] for line in output])
        print(just_text)
        pyperclip.copy(just_text)

        actions.speech.enable()
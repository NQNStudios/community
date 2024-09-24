from talon import Module, app, actions
import subprocess
from os import environ
from . pipeclient import PipeClient

mod = Module()

@mod.action_class
class Actions:
    def view_log():
        """view talon log"""
        actions.mimic("focus talon")
    def view_config():
        """view talon config"""
        home = environ["HOME"]
        subprocess.call(["open", f'{home}/.talon/user/community'])

    def type():
        """launch audacity"""
        subprocess.call(["open", "-a", "Audacity"])
        client = PipeClient()
        client.write("GetInfo")
        print(client.wait_read())


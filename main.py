import os
import subprocess
import json
import push

class Git():
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.json_path = os.path.join(self.script_dir, "set", "userdata.json")
        self.git_path = os.path.join(self.script_dir, "lib", "Git.exe")
        self.result = subprocess.run(self.git_path, shell=True, capture_output=True, text=True)
        with open(self.json_path, 'r') as json_file:
            data = json.load(json_file)
        self.name = str(data.get('name', ''))
        self.email = str(data.get('email', ''))

    def install(self):
        if self.result.returncode == 0:
            print("Installer:[installed]")
            self.set_git()
        else:
            print("ERROR:[File not found]")
            self.set_git()
        

    def set_git(self):
        subprocess.run(["git", "config", "--global", "user.name", self.name])
        subprocess.run(["git", "config", "--global", "user.email", self.email])
        result = subprocess.run(["git", "config", "--global", "user.name"], capture_output=True, text=True)
        print(f"Git user.name set to: {result.stdout.strip()}")
        result = subprocess.run(["git", "config", "--global", "user.email"], capture_output=True, text=True)
        print(f"Git user.email set to: {result.stdout.strip()}")
        run = push.Git_init()
        run.init()

if __name__ == "__main__":
    git_installer = Git()
    git_installer.install()

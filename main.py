import os
import subprocess
import json
import time

class Git_installer():
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.json_path = os.path.join(self.script_dir, "set", "userdata.json")
        self.git_path = os.path.join(self.script_dir, "lib", "Git.exe")
        self.install_state = os.path.isfile(
            os.path.join("C:\\Program Files\\Git", "git-bash.exe")
            ) or os.path.isfile(
            os.path.join("C:\\Program Files\\Git", "git-cmd.exe")
            )
        with open(self.json_path, 'r') as json_file:
            data = json.load(json_file)
        self.name = str(data.get('name', ''))
        self.email = str(data.get('email', ''))

    def install(self):
        if self.install_state == True:
            print("Installer:[installed]")
            self.set_git()
        else:
            print("ERROR:[File not found]")
            subprocess.run(self.git_path, shell=True, capture_output=True, text=True)

    def set_git(self):
        os.system(f"git config --global user.name {self.name}")
        os.system(f"git config --global user.email {self.email}")
        os.system(f"git config --global user.name")
        os.system(f"git config --global user.email")

class Git_clone():
    def init(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(script_dir, "set", "userdata.json")
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        self.project = str(data.get('project', ''))
        self.path = self.find()
        subprocess.run(f"git init", shell=True, cwd=self.path)
        self.clone()
        self.drive_removal()

    def drive_removal(self):
        drives = []
        for drive_letter in range(ord('A'), ord('Z') + 1):
            drive = f"{chr(drive_letter)}:\\"
            if os.path.exists(drive):
                drives.append(drive)

        while True:
            time.sleep(1)

            current_drives = [drive for drive in drives if os.path.exists(drive)]

            if len(current_drives) < len(drives):
                removed_drive = set(drives) - set(current_drives)
                print(f"Drive {removed_drive} has been removed.")
                self.push()
                break
            drives = current_drives

    def clone(self):
        subprocess.run(f"git clone {self.project}", cwd=self.path)
        return
    
    def push(self):
        print("push")
        pass

    def find(self):
        onedrive_path = os.path.join(os.path.expanduser("~"), "OneDrive")
        onedrive_path = os.path.join(onedrive_path, "桌面")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        try:
            test = os.system(f"cd {onedrive_path}")
            if test == 0:
                path = onedrive_path
            return path
        except:
            path = desktop_path
            return path

if __name__ == "__main__":
    git_installer = Git_installer()
    git_installer.install()

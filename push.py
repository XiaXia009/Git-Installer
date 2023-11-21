import os
import time
import subprocess
import desktop_finder
import json

class Git_init():
    def init(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(script_dir, "set", "userdata.json")
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        self.project = str(data.get('project', ''))
        self.path = desktop_finder.find()
        subprocess.run(f"git init", shell=True, cwd=self.path)
        Git_init.clone()
        Git_init.drive_removal()

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
                Git_init.push()
                break
            drives = current_drives

    def clone(self):
        subprocess.run(f"git clone {self.project}", cwd=self.path)
        return
    
    def push(self):
        pass
import os
import time
import subprocess
import desktop_finder
import json

def init():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(script_dir, "lib", "userdata.json")
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    path = desktop_finder.find()
    subprocess.run(f"git init", shell=True, cwd=path)
    drive_removal()

def drive_removal():
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
            main()
            break

        drives = current_drives

def main():
    subprocess.run(f"git clone ")

init()
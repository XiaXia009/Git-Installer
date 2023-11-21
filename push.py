import os
import time
import subprocess
import desktop_finder

def init():
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
    path = desktop_finder.find()
    subprocess.run(f"git init", shell=True, cwd=path)
    pass


init()
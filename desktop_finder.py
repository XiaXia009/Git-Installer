import os

def find():
    onedrive_path = os.path.join(os.path.expanduser("~"), "OneDrive")
    onedrive_path = os.path.join(onedrive_path, "桌面")

    print(f"OneDrive 中的桌面路徑：{onedrive_path}")

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    print(f"桌面路徑：{desktop_path}")

    try:
        test = os.system(f"cd {onedrive_path}")
        if test == 0:
            path = onedrive_path
        return path
    except:
        path = desktop_path
        return path

print(find())
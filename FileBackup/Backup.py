import os
import shutil
import datetime
import time

sourceDirectory = "D:/Flutter"
backupDirectory = "D:/Backups/FlutterBackup"

def copyToDirectory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied successfully to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists at {dest_dir}")


copyToDirectory(sourceDirectory, backupDirectory)
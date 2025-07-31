# Automatic Folder Backup Script

This Python script creates a backup of a specified source directory by copying it into a destination directory. The backup folder is named with the current date (`YYYY-MM-DD` format) to avoid overwriting previous backups.

---

## 📌 Features

- On-demand, one-time execution
- Automatically creates a dated backup folder
- Prevents overwriting if a backup for the day already exists
- Works cross-platform with valid path formatting

---

## 📂 Folder Structure

- **Source Directory**: `C:/Projects/MyApp`
- **Backup Directory**: `C:/Backups/MyAppBackup`
  - Backups will be saved here in folders like:
    - `C:/Backups/MyAppBackup/2025-07-31`
    - `C:/Backups/MyAppBackup/2025-08-01`

---

## 🚀 How to Use

1. Make sure Python is installed on your system.
2. Install any dependencies (none needed beyond the Python standard library).
3. Run the script:

   ```bash
   python Backup.py
   ```

4. The script will:

- Create a new backup folder with today’s date.
- Copy the contents of the source folder into it.

---

## 🛡️ Safety Notes

- Make sure the backup directory is **not inside** the source directory.

- Example of **invalid setup** (causes infinite nesting):
  - `source = C:/Projects/MyApp`
  - `backup = C:/Projects/MyApp/Backup` ❌

---

## 🧩 Dependencies

- `os` – for path and directory handling
- `shutil` – to perform directory copy
- `datetime` – to generate dated folder names

These are all part of Python's standard library.

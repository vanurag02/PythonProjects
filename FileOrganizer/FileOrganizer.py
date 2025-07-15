import os
import shutil

# Define categories and their corresponding file extensions
FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    "Music": ['.mp3', '.wav', '.aac', '.ogg'],
    "Archives": ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "Code": ['.py', '.java', '.cpp', '.html', '.js', '.css'],
    "Others": []  # For unknown or uncategorized extensions
}

def get_category(extension):
    """Return the folder category based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("The folder path does not exist.")
        return

    files_moved = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        category = get_category(ext)

        # Create target folder if it doesn't exist
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

        # Move file to the categorized folder
        try:
            shutil.move(file_path, os.path.join(category_path, filename))
            files_moved += 1
        except Exception as e:
            print(f"Could not move file '{filename}': {e}")

    print(f"\n✅ Organization complete. Files moved: {files_moved}")

def main():
    print("File Organizer")
    folder_path = input("Enter the full path of the folder to organize: ").strip()
    organize_folder(folder_path)

if __name__ == "__main__":
    main()

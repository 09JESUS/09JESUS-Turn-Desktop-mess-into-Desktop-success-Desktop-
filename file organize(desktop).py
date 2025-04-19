import os
import shutil

# Define your Desktop path
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Define categories and their corresponding file extensions
categories = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.html', '.css', '.js', '.cpp', '.java'],
    'Others': [],
    'Folders': []  # To handle random folders
}

# Create folders if they don't exist
for folder in categories.keys():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize the Desktop
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)

    # Skip the folders we created for organizing
    if item in categories.keys():
        continue

    if os.path.isdir(item_path):
        # It's a folder, move it to "Folders"
        shutil.move(item_path, os.path.join(desktop_path, 'Folders', item))
    else:
        # It's a file, move based on extension
        _, ext = os.path.splitext(item)
        moved = False
        for folder, extensions in categories.items():
            if ext.lower() in extensions:
                shutil.move(item_path, os.path.join(desktop_path, folder, item))
                moved = True
                break
        if not moved:
            shutil.move(item_path, os.path.join(desktop_path, 'Others', item))

print("Desktop fully organized (files + folders)!")

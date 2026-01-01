import os
import shutil  # <--- New library for moving files

# Get the path to your User profile (e.g., C:\Users\Name or /Users/Name)
user_path = os.path.expanduser("~")
TARGET_FOLDER = os.path.join(user_path, "Downloads")

EXTENSIONS = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".md"], # Added .md here!
    "setup_files": [".exe", ".dmg", ".pkg", ".zip", ".msi"],
    "music": [".mp3", ".wav"]
}

def clean_folder():
    print(f"--- Cleaning {TARGET_FOLDER} ---")
    
    if not os.path.exists(TARGET_FOLDER):
        print("Folder not found!")
        return

    files = os.listdir(TARGET_FOLDER)
    
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        
        if file == "cleaner.py":
            continue
            
        found = False
        for folder_name, ext_list in EXTENSIONS.items():
            if extension in ext_list:
                # 1. Create the new folder path string
                target_folder_path = os.path.join(TARGET_FOLDER, folder_name)
                
                # 2. Check if folder exists, if not, create it
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                    print(f"Created new folder: {folder_name}")
                
                # 3. Construct the old and new file paths
                old_file_path = os.path.join(TARGET_FOLDER, file)
                new_file_path = os.path.join(target_folder_path, file)
                
                # 4. Move the file
                shutil.move(old_file_path, new_file_path)
                print(f"Moved: {file} -> /{folder_name}/{file}")
                found = True
                break
        
        if not found and extension:
            print(f"Skipped: {file}")

if __name__ == "__main__":
    clean_folder()
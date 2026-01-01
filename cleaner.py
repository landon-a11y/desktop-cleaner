import os

# 1. Define the directory we want to clean
# For now, let's just use the current directory where this script is running
# 'Win' users might need raw strings like r"C:\Users\Name\Downloads" later
TARGET_FOLDER = "." 

def scan_folder():
    """Scans the target folder and prints files found."""
    print(f"Scanning folder: {os.path.abspath(TARGET_FOLDER)}")
    
    # List all files in the directory
    if os.path.exists(TARGET_FOLDER):
        files = os.listdir(TARGET_FOLDER)
        for file in files:
            print(f"Found file: {file}")
    else:
        print("Folder not found!")

if __name__ == "__main__":
    scan_folder()
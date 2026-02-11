import os
import shutil

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return f"[OK] Folder created: {path}"
    else:
        return f"[SKIP] Folder already exists: {path}"

def move_file(src, dest):
    # Check source file
    if not os.path.exists(src):
        return f"[ERROR] Source file not found: {src}"

    # Ensure destination folder exists
    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.move(src, dest)
    return f"[OK] Moved {src} → {dest}"

def delete_file(path):
    if not os.path.exists(path):
        return f"[ERROR] File not found: {path}"

    os.remove(path)
    return f"[OK] Deleted file: {path}"


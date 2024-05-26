import os
import shutil

def delete_downloads():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # List all files and directories in the Downloads folder
    files_and_dirs = os.listdir(downloads_path)

    for item in files_and_dirs:
        item_path = os.path.join(downloads_path, item)
        try:
            confirm = input(f"Do you want to delete {item_path}? (yes/no): ").strip().lower()
            if confirm == 'yes':
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                print(f"Deleted: {item_path}")
            else:
                print(f"Skipped: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")

if __name__ == "__main__":
    delete_downloads()

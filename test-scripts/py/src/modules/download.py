import requests
from tqdm import tqdm
from src.modules.utils import print_ascii_line, clear_console, CONFIG

SRC_DIR = CONFIG.src_dir
API = CONFIG.api

def download_file(download_url, file_path):
    response = requests.get(download_url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)

        with open(file_path, "wb") as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()
        return True

    return False


def download_files():
    import os
    existing_folders = [folder for folder in os.listdir(SRC_DIR) if os.path.isdir(os.path.join(SRC_DIR, folder))]
    while True:
        clear_console("Download JSON")
        if not existing_folders:
            print("No existing databases found in the Root directory.")
            return
        print("Existing databases in the Root directory:")
        print_ascii_line('-')
        for index, folder in enumerate(existing_folders):
            print(f"[{index+1}] {folder}")
        print_ascii_line('-')
        selected_index = input("Select Database: ")
        if selected_index == "":
            return
        if not selected_index.isdigit() or int(selected_index) - 1 >= len(existing_folders):
            print(f"ERROR: Invalid folder index.")
        else:
            clear_console("Download JSON")
            folder_name = existing_folders[int(selected_index) - 1]
            print(f"Selected main folder: {folder_name}")
            break

    success = False

    while not success:
        response = requests.get(API)
        data = response.json()

        if response.status_code == 200:
            success = True
        else:
            print("Failed to fetch data.")
            retry = input("Do you want to retry? (y/n): ")
            if retry.lower() != "y":
                return

    options = data["data"]
    num_options = len(options)

    print_ascii_line('-')
    print("Available database files:")
    for index, option in enumerate(options):
        name = option["name"]
        print(f"[{index + 1}] {name}")
    print_ascii_line('-')
    user_input = input("Select files (separated by spaces): ")
    indices = user_input.split()

    for index in indices:
        if index.isdigit() and int(index) - 1 < num_options:
            selected_option = options[int(index) - 1]
            download_url = selected_option["download_uri"]
            filename = f"{selected_option['type']}.json"
            file_path = os.path.join(SRC_DIR, folder_name, "db", filename)

            if os.path.exists(file_path):
                overwrite = input(f"The file '{filename}' already exists. Do you want to overwrite it? (y/n): ")

                if overwrite.lower() != "y":
                    print_ascii_line()
                    print(f"Skipping the download of '{filename}'...")
                    continue

            print_ascii_line()
            print(f"Downloading file: {filename}")

            if download_file(download_url, file_path):
                print_ascii_line()
                print(f"File '{filename}' downloaded successfully.")
            else:
                print_ascii_line()
                print("Failed to download the file.")
        else:
            print_ascii_line()
            print(f"Invalid index: {index}")

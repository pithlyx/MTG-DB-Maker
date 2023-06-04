import os
import yaml
import shutil as sh

class Config:
    def __init__(self, data):
        self.src_dir = data['SRC_DIR']
        self.chunk_size = data['CHUNK_SIZE']
        self.api= data['API']
        self.clear = data['CLEAR']
        self.safe = data['SAFE']

with open('config.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        CONFIG = Config(data)
        print(CONFIG)

SRC_DIR = CONFIG.src_dir
CLEAR = CONFIG.clear
SAFE = CONFIG.safe
def clear_console(menu):
    if CLEAR:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_ascii_line()
        print(f"Json Parser - {menu}")
        print_ascii_line()
    else:
        print_ascii_line()



def print_ascii_line(char = '='):
    print(char * 80)


def folder(path, delete = False):
    if SAFE and delete:
        print_ascii_line('*')
        if input("Are you sure you would like to PERMANENTLY DELETE this Database? (y/n): ") is not "y":
            return
    if delete:
        if os.path.exists(path):
            sh.rmtree(path)
        else:
            print("File Not Found!")
    elif not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        print(f"File already exists: {path}")
        overwrite = input("Wound you like to overwrite this file? (y/n): ")
        if overwrite.lower() == 'y':
            sh.rmtree(path)
            folder(path)
    
    return False


def validate_structure(main_folder=None):
    if not os.path.exists(SRC_DIR):
        os.makedirs(SRC_DIR)
        print(f"Created DATABASE root folder: {SRC_DIR}")
        return False

    if main_folder:
        main_folder_path = os.path.join(SRC_DIR, main_folder)
        all_parts_folder_path = os.path.join(main_folder_path, "all-parts")
        db_folder_path = os.path.join(main_folder_path, "db")

        if folder(main_folder_path):
            folder(all_parts_folder_path)
            folder(db_folder_path)

        return main_folder_path

    return True

def display_structure(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return []
    items = []
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            items.append(item)
        elif os.path.isdir(item_path):
            items.append("/" + item + "/")
    
    # Display the folders and files
    for index, item in enumerate(items, start=1):
        print(f"|- [{index}] {item}")
    
    return items



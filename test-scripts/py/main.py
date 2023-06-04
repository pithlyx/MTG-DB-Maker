from src.modules.utils import folder, validate_structure, display_structure, CONFIG
from src.modules.download import download_files
from src.modules.split import split_files

SRC_DIR = CONFIG.src_dir
CHUNK_SIZE = CONFIG.chunk_size

def main():
    main_folder_path = None
    
    if not validate_structure():
        pass

    while True:
        print("1. Database Manager")
        print("2. Download Files")
        print("3. Split JSON File")
        
        choice = input("Select menu: ")
        val = val_input('main', choice)
        while True:
            if val in ['r','q']:
                option = input("Would you like to exit? (y/n): ")
                if option == 'y':
                    break
            elif val == 'f':
                choice = input("Select menu: ")
                val = val_input('main', choice)
                print('\r', end='')
                # Clear the entire line
                print('\033[K', end='')    
        if choice == "1":
            while True:
                print("Available Databases")
                
                db = display_structure(SRC_DIR)
                
                if db:
                    print("1. Create New Database")
                    print("2. Delete Database")
                    choice = input("Enter your choice: ")
                else:
                    choice = "1"
                    
                if choice == "":
                    break
                elif choice == "1":
                    print("Current Databases")
                    db = display_structure(SRC_DIR)
                    if not db:
                        print("No databases available")
                    main_folder_path = input("Enter a name for your new database: ")
                    if main_folder_path != "":
                        validate_structure(main_folder_path)
                    
                elif choice == "2" and db:
                    while True:
                        print("Available Databases")
                        db = display_structure(SRC_DIR)
                        if not db:
                            print("No databases available")
                        selection = input("Select a db to delete: ")
                        if selection == "":
                            break
                        elif len(db) > int(selection)-1:
                            target = SRC_DIR+db[int(selection)-1]
                            folder(target, delete=True)
                            print(f"DELETING '{target}'")
                            if not display_structure(SRC_DIR):
                                break
                        else:
                            print("Invalid Selection")
        elif choice == "2":
            download_files()
        elif choice == "3":
            split_files(main_folder_path)


def val_input(menu, input):
    if menu == 'main':
        return \
            'r' if input == "" else \
            'q' if input == "q" else \
            't' if input in [1, 2, 3] else \
            'f'
        
if __name__ == "__main__":
    main()

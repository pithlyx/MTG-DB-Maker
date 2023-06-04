# MTG-DB Maker

MTG-DB Maker is a script that allows you to download and process Magic: The Gathering (MTG) card data from the Scryfall API. The script provides functionalities to fetch the data, split it into smaller files, and parse the data based on specific attributes.

## Prerequisites

- Python 3.x
- Required Python libraries: aiohttp, tqdm, colorama

## Installation

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Navigate to the project directory: `cd MTG-DB-Maker`
3. Install the required libraries: `pip install -r requirements.txt`

## Usage

1. Navigate to the `scripts` directory: `cd scripts`
2. Run the `main.py` script: `python main.py`
3. Follow the menu prompts to select the desired options.

### Fetching MTG card data

The `fetch_cards.py` script is responsible for fetching MTG card data from the Scryfall API. It uses asynchronous HTTP requests to efficiently download the data.

To fetch the card data, the script performs the following steps:

1. Sends a request to the Scryfall API to retrieve the available bulk data.
2. Displays the available data types and prompts the user to select the desired files to download.
3. Downloads the selected files from the provided download URIs.
4. Saves the downloaded files to the `../db` folder.

### Splitting JSON files

The `splitter.py` script allows you to split large JSON files into smaller parts. This can be useful for handling large datasets more efficiently or when working with limited system resources.

To split the JSON files, the script performs the following steps:

1. Specifies the input folder path where the JSON files are located.
2. Specifies the output directory path where the split files will be saved.
3. Specifies the desired chunk size, which determines the number of items per chunk.
4. Processes each JSON file in the input folder.
5. Splits the file into smaller parts, saving each part in separate JSONL files (newline-delimited JSON).

### Parsing card data based on attributes

The `parse.py` script allows you to parse the card data based on specific attributes. It generates a folder attribute library, which contains information about the attributes present in each folder.

To parse the card data, the script performs the following steps:

1. Generates a folder attribute library by scanning the parent folder (`../all-parts` by default).
2. Displays all the unique attributes found in the card data.
3. Prompts the user to enter an attribute key to search for in the data.
4. Searches for the attribute in the available folders and displays the folders containing the attribute.
5. Prompts the user to select a folder for parsing.
6. Parses the card data in the selected folder based on the chosen attribute, creating separate JSONL files for each attribute value.

## Examples

### Example 1: Fetching and splitting card data

Suppose you want to download and split the MTG card data into smaller parts. Follow these steps:

1. Run the `main.py` script: `python main.py`
2. Select option 2 to download the card data.
3. Once the download is complete, select option 3 to split the JSON files.
4. The script will split the files into smaller parts and save them in the `../all-parts` directory.

### Example 2: Parsing card data based on attributes

Suppose you want to parse the card data based on specific attributes. Follow these steps:

1. Run the `main.py` script: `python main.py`
2. Select option 4 to parse the card data.
3. Enter the attribute key you want to search for.
4. The script will search for the attribute in the available folders and display the folders containing the attribute.
5. Select a folder number to parse.
6. The script will create separate JSONL files for each attribute value in the selected folder.

## Credits

This script was developed by Cody and is available at [GitHub](https://github.com/codybarr/MTG-DB-Maker).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/codybarr/MTG-DB-Maker/blob/main/LICENSE) file for more information.

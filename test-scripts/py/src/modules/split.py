import os
import ijson
import json
from src.modules.utils import CONFIG

CHUNK_SIZE = CONFIG.chunk_size

def split_files(main_folder_path):
    json_file_path=input('Enter JSON file path: ')

    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        # Create an iterator using ijson to read the JSON file incrementally
        json_data = ijson.items(json_file, 'item')

        # Initialize variables
        file_counter = 1
        item_counter = 0
        current_chunk = []

        # Iterate through the JSON data
        for item in json_data:
            # Append the current item to the current chunk
            current_chunk.append(item)
            item_counter += 1

            # If the chunk size is reached, write the chunk to a new file
            if item_counter == CHUNK_SIZE:
                output_file_path = os.path.join(
                    main_folder_path, f'part-{file_counter}.jsonl')
                with open(output_file_path, 'w') as output_file:
                    # Write each item as a separate line in JSON Lines format
                    for chunk_item in current_chunk:
                        output_file.write(json.dumps(chunk_item))
                        output_file.write('\n')

                # Reset counters and current chunk
                item_counter = 0
                current_chunk = []
                file_counter += 1

        # Write the remaining items to a new file
        if item_counter > 0:
            output_file_path = os.path.join(
                main_folder_path, f'part-{file_counter}.jsonl')
            with open(output_file_path, 'w') as output_file:
                for chunk_item in current_chunk:
                    output_file.write(json.dumps(chunk_item))
                    output_file.write('\n')

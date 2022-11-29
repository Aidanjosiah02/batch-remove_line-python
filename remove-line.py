import os

SELECTED_LINE = 8
DIRECTORY = "."
FILE_TYPES = [".txt", ".csv"]

file_list = []
objects = os.scandir(DIRECTORY)
for entry in objects:
    if entry.is_file():
        file_list.append(entry.name)

text_files = []
for file_name in file_list:
    for file_types in FILE_TYPES:
        if file_types in file_name:
            text_files.append(file_name)
print(text_files)
for file in text_files:
    try:
        with open(file, 'r') as file_read:
            lines = file_read.readlines()
            pointer = 1 # pointer for position
            with open(file, 'w') as file_write:
                for line in lines:
                    if pointer != SELECTED_LINE:
                        file_write.write(line)
                    pointer += 1
        print("Deleted line " + str(SELECTED_LINE) + " in: " + str(file))
    except:
        print("Error when opening " + str(file))
import os
import shutil

path = "./Resources"

files = os.listdir(path)

for file in files:
    # skip if it's a directory
    if os.path.isdir(os.path.join(path, file)):
        continue

    
    prefixes = ('8')
    
    for prefix in prefixes:
        if file.startswith(prefix):
            category = file[len(prefix)]
            new_filename = f'{file[len(prefix):].rsplit(".", 1)[0]}_{prefix}.{file.rsplit(".", 1)[1]}'
            break
    else:
        category = file[0]
        new_filename = file

    # create a new directory for each category if it doesn't exist already
    new_directory_path = os.path.join(path, category)
    
    if not os.path.exists(new_directory_path):
        os.makedirs(new_directory_path)

     # move files using shutil.move()
    shutil.move(os.path.join(path, file), os.path.join(new_directory_path, new_filename))

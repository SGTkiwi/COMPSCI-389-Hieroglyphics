import os


root_dir = './Resources'

data_size = {}
for subdir, dirs, files in os.walk(root_dir):
    
    img_count = 0

    
    for file in files:
        
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img_count += 1

    # print the count for this category
    if os.path.basename(subdir) == 'Resources':
        continue
    data_size[os.path.basename(subdir)] = img_count

# Sort the dictionary by key
data_size = dict(sorted(data_size.items())) 

for key, value in data_size.items():
    print(f'{key}: {value}')

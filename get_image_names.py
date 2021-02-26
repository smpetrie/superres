import os

image_dir = 'images/'
images = sorted(os.listdir(image_dir))

with open('image_names.txt', 'w') as out:
    for i in images:
        out.write('![](' + image_dir + i + ')\n\n')

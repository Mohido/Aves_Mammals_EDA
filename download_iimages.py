import os
import urllib.request
from tqdm.notebook import tqdm
import json
import sys


# getting the file list passed
file_list = []
for dirname, _, filenames in os.walk('./urls/'):
    for filename in filenames:
        file_list.append(os.path.join(dirname, filename))

print(file_list)



for json_file in file_list:
    # Loading the image links
    with open(json_file, 'r') as f:
        image_urls = json.load(f)
        
    # Getting the file name
    file_name_base = os.path.splitext(os.path.basename(json_file))[0]

    # Checking if we have a folder with the name of the file
    if not os.path.exists(f'images/{file_name_base}'):
        os.makedirs(f'images/{file_name_base}')

    # Downloading images from the list
    for i in tqdm(range(len(image_urls)), desc=file_name_base):
        try:
            urllib.request.urlretrieve(image_urls[i], f'images/{file_name_base}/{i}.jpg')
        except ConnectionResetError:
            print(f'*** ConnectionResetError: {image_urls[i]}')
            pass
        except:
            print(f'Unexpected error: {sys.exc_info()[0]}')
            print(f'Error happended in url: {image_urls[i]}')
            pass
#### In here I have made a function to make the directory and then
####           saving images into that directory.

import shutil
import os
import pandas as pd
import csv
import requests

def make_directory(dirname):
    current_path=os.getcwd()
    path=os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

# Making different functions to save images with different name
def save_images_shirt(data, dirname, page):
    for index,link in enumerate(data['image_urls']):
        print("Downloading {0} of {1} images ".format(index+1,len(data["image_urls"])))
        response=requests.get(link)
        with open("{0}/Shirt_img_{1}{2}.jpeg".format(dirname,page,index),"wb") as file:
            file.write(response.content)
            
def save_images_saree(data, dirname, page):
    for index,link in enumerate(data['image_urls']):
        print("Downloading {0} of {1} images ".format(index+1,len(data["image_urls"])))
        response=requests.get(link)
        with open("{0}/Saree_img_{1}{2}.jpeg".format(dirname,page,index),"wb") as file:
            file.write(response.content)
            
def save_images_tshirt(data, dirname, page):
    for index,link in enumerate(data['image_urls']):
        print("Downloading {0} of {1} images ".format(index+1,len(data["image_urls"])))
        response=requests.get(link)
        with open("{0}/Tshirt_img_{1}{2}.jpeg".format(dirname,page,index),"wb") as file:
            file.write(response.content)





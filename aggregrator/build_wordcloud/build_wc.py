import numpy as np
import pandas as pd
from os import path, remove, getenv
from pathlib import Path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import cloudinary
import cloudinary.uploader
from datetime import datetime


# import matplotlib.pyplot as plt

class Build_WC: 
    @staticmethod
    def build_wc(news_array, cloudinary_params):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent   
        
        cloudinary.config(
            cloud_name = cloudinary_params["CLOUDINARY_NAME"],
            api_key = cloudinary_params["CLOUDINARY_API_KEY"],
            api_secret = cloudinary_params["CLOUDINARY_API_SECRET"]
        )
        
        # Create stopword list:
        module_dir = path.dirname(__file__)  # get current directory
        file_path = path.join(module_dir, 'stopwords_indo.txt')
        file1 = open(file_path, 'r')           
        stopword_list = []
        while True:            
            line = file1.readline()            
            stopword_list.append(line.strip())
            # if line is empty
            # end of file is reached
            if not line:
                break
        file1.close()                
        stopwords = set(STOPWORDS)
        stopwords.update(stopword_list)
        text = " ".join(news_array)
        wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
        # Save the image in the img folder:
        filePath = path.join(BASE_DIR, "static/wc_img")
        date_time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = filePath + "/" + date_time_now + "_wordcloud.png"
        wordcloud.to_file(file_name)
        result = cloudinary.uploader.upload(file_name)
        if path.exists(file_name):
            remove(file_name)
        else:
            print("The file does not exist")
        url = result.get("url")
        return url
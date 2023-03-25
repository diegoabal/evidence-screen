#pip install pillow
#pip install selenium webdriver-manager

import sys
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

now = datetime.now()
title_font = ImageFont.truetype('roboto/roboto-regular.ttf', 20)
#title_font = ImageFont.load_default()


filename = now.strftime("%Y%m%d_%H%M")
filename+=".jpg"

title_text = sys.argv[1] + "\nScreenshot Taken: " + now.strftime("%Y-%m-%d %H:%M")


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)



driver.get(sys.argv[1]) 
driver.maximize_window()
driver.save_screenshot("temp.png")

driver.quit()

img = Image.open("temp.png")
rgb_im = img.convert('RGB')

d1 = ImageDraw.Draw(rgb_im)
#d1.text((cords),text,color_text,font)
d1.text((15,15), title_text, (25, 176, 2), font=title_font)

rgb_im.save(filename, "JPEG", 
                 optimize = True, 
                 quality = 85)
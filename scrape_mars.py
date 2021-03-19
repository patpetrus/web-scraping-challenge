#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


filepath = os.path.join("nasa_latest_news.html")
with open(filepath, encoding='utf-8') as file:
    html = file.read()


# In[3]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


soup


# In[5]:


# Examine the results and look for a div for the article title
#find_all returns all articles, while .find returns the first one (the one closest to the top of the site)
title_results = soup.find('div', class_='content_title').find('a').text
article_results = soup.find('div', class_='article_teaser_body').find('#text').text
#WHY IS THIS RETURNING NO TEXT???


# In[6]:


# Access the thread's text content
print(title_results)

#not printing because there is no data in article_results. See above scrape cell
print(article_results)


# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[9]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

path = soup.find('img', class_='headerimage fade-in')['src']

featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{path}'

print(featured_image_url)


# In[10]:


browser.quit()


# In[ ]:





# In[ ]:





# In[12]:


url = 'https://space-facts.com/mars/'


# In[13]:


tables = pd.read_html(url)
tables


# In[17]:


mars_df = tables[0]
mars_df


# In[22]:


mars_df = mars_df.rename(columns={"0": "Interrogative", "1": "Answer"})
mars_df
#rename not working :(


# In[23]:


mars_html = mars_df.to_html()
mars_html


# In[24]:


mars_html.replace('\n', '')


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]


# In[ ]:





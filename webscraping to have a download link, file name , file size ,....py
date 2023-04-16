#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of websites to scrape
websites = [
    "https://dl.rozmusic.com/",
    "https://www.ganja2music.com/",
    "https://rozmusic.com/"
]

# List to store the data
data = []

# Loop through the websites and scrape the required information
for website in websites:
    # Make a GET request to the website
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the download links on the page
    download_links = soup.select('a[href$=".mp3"]')

    # Loop through the download links and extract the required information
    for link in download_links:
        # Extract the download link
        download_link = link['href']

        # Extract the file name
        file_name = link.text.strip()

        # Extract the file size (if available)
        file_size = ""
        file_size_elem = link.find_next_sibling('span')
        if file_size_elem:
            file_size = file_size_elem.text

        # Extract the bit rate (if available)
        bit_rate = ""
        bit_rate_elem = link.find_previous('span', class_='media__detail media__detail--single')
        if bit_rate_elem:
            bit_rate = bit_rate_elem.text.split()[0]

        # Extract the file upload date (if available)
        file_upload_date = ""
        file_upload_elem = link.find_previous('time', class_='metadata__date')
        if file_upload_elem:
            file_upload_date = file_upload_elem.text

        # Append the data to the list
        data.append([download_link, file_name, file_size, bit_rate, file_upload_date])

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=['Download Link', 'File Name', 'File Size', 'Bit Rate', 'File Upload Date'])

# Save the DataFrame to an Excel file
df.to_excel('music_data.xlsx', index=False)


# In[6]:


df


# In[3]:


import requests

url = 'https://dl.rozmusic.com/Music/1401/'

# set headers for API request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.mybia2music.com/',
    'X-Requested-With': 'XMLHttpRequest'
}

# set payload for API request
payload = {
    'artist': '',
    'name': '',
    'id': '',
    'page': '1',
    'type': 'song'
}

# send POST request to API and retrieve response
response = requests.post(url, headers=headers, data=payload)
songs = response.json()['result']['songs']

# extract MP3 download links from response
mp3_links = [song['url'] for song in songs if song['type'] == 'song']

# print list of MP3 download links
print(mp3_links)


# In[17]:


df


# In[ ]:





'''
Name: Gloria Pappalardo
Date: 9/17/20
Version of Python: 3.6
Description: This script scrapes information from the National Weather Service 
website about weather in Montauk, New York. Inputs are longitude and latitude and 
outputs are weather conditions (wind speed, humidity, barometer, dewpoint,
visibility, and date and time of last update).
'''

# Import required libraries
import requests
from bs4 import BeautifulSoup

# Provide the latitude and longitude for the location you would like to check the weather for
# Lat/lon in decimal degrees provided for Montauk, New York
lat = '41.031319'
lon = '-71.950981'

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate element on page to be scraped
# This element is located within an id tag called current_conditions_detail
# find() locates the element in the BeautifulSoup object
cur_conditions_detail = soup.find(id="current_conditions_detail") # edited from here forward to scrape weather details

# Extract text from the selected BeautifulSoup object using .text
cur_conditions_detail = cur_conditions_detail.text

# Final Output
# Return scraped information
print('The Current Weather Conditions at '+ lat +  ", " + lon + " are:" + cur_conditions_detail) 

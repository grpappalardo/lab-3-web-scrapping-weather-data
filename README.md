

You should edit your README file to provide the following information:
- Summarize what your script does or the problem you were trying to solve.
- Summarize any major errors you encountered and what sources they used to resolve the errors
- How you fixed the errors, or where the error is if you couldn't figure something out.


This script scrapes the National Weather Service's website to print weather data on a U.S. location given its latitude and longitude. It does this with BeautifulSoup, by concatenating the URL for the latitude/longitude, checking and printing this URL, using get() to find and hold the URL, then creating an object with BeautifulSoup and accessing the information on the webpage with .content and the html_parser. From there, the specific element on the page (found via Inspect in the browser) is found and .text is used to extract. This text is printed.
I did not have any major issues workng on this script. The use of latitude/longitude means there can be a variation of weather outputs from adjacent locales, as long as there is another weather information station collecting data that is even closer to the chosen latitude/longitude.

# web-scraping
## About
The purpose of this repository is to scrape various websites for data relating to mars and to load that information into a Mongo Database and to display the information on an html page using a Flask server.

---

## mission_to_mars.ipynb
This notebook uses pandas, requests, splinter and BeautifulSoup to scrape various websites to retrieve data on mars. This data is then put into a final dictionary which is used in app.py, scrape_mars.py, and index.html.

---

## scrape_mars.py
A python script containing the code from mission_to_mars.ipynb to be used in app.py and index.html.

---

## app.py
Flask template python script used to interact between the Mongo Database and index.html.

---

## index.html
 HTML page to display the information gathered.

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Create a BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, "html.parser")

    # Find the latest news title and it's teaser paragraph
    results = soup.find('div', {"class": "list_text"})

    latest_news_title = results.find("div", {"class": "content_title"}).text

    latest_news_paragraph = results.find("div", {"class": "article_teaser_body"}).text

    # Select relavent page for broswer
    jpl_url = "https://spaceimages-mars.com/"

    browser.visit(jpl_url)

    # Navigate page to find full image of the featured picture
    browser.links.find_by_partial_text("FULL IMAGE").click()

    # Retrieve html
    jpl_soup = bs(browser.html, "html.parser")

    # Find full image
    jpl_results = jpl_soup.find("img", {"class" : "fancybox-image"})

    # Save full image url
    featured_image_url = jpl_url + jpl_results["src"]

    # URL containing relavent tables
    mars_facts_url = "https://galaxyfacts-mars.com/"

    tables = pd.read_html(mars_facts_url)

    # Save table as a dataframe
    mars_facts_df = tables[1]

    # Create html table string from the dataframe
    mars_facts_html_table = mars_facts_df.to_html()

    # Initialize base mars hemispheres' url and list to hold hemiphere's names
    # and images
    mars_hemispheres_url = "https://marshemispheres.com/"

    browser.visit(mars_hemispheres_url)

    hemisphere_image_urls = []

    # Navigate to target page
    browser.links.find_by_partial_text("Cerberus Hemisphere Enhanced").click()

    # Create soup object
    cerb_soup = bs(browser.html, "html.parser")

    # Scrape for the hemisphere title and image url
    cerb_title = cerb_soup.find("h2", {"class" : "title"}).text

    cerb_image = cerb_soup.find("ul")

    cerb_image_url = mars_hemispheres_url + cerb_image.li.a["href"]

    # Append dictionary to hemispheres list
    hemisphere_image_urls.append({"title": cerb_title, "img_url": cerb_image_url})

    # Navigate to target page
    browser.visit(mars_hemispheres_url)

    browser.links.find_by_partial_text("Schiaparelli Hemisphere Enhanced").click()

    # Create soup object
    schi_soup = bs(browser.html, "html.parser")

    # Scrape for the hemisphere title and image url
    schi_title = schi_soup.find("h2", {"class" : "title"}).text

    schi_image = schi_soup.find("ul")

    schi_image_url = mars_hemispheres_url + schi_image.li.a["href"]

    # Append dictionary to hemispheres list
    hemisphere_image_urls.append({"title": schi_title, "img_url": schi_image_url})

    # Navigate to target page
    browser.visit(mars_hemispheres_url)

    browser.links.find_by_partial_text("Syrtis Major Hemisphere Enhanced").click()

    # Create soup object
    syrt_soup = bs(browser.html, "html.parser")

    # Scrape for the hemisphere title and image url
    syrt_title = syrt_soup.find("h2", {"class" : "title"}).text


    syrt_image = syrt_soup.find("ul")


    syrt_image_url = mars_hemispheres_url + syrt_image.li.a["href"]

    # Append dictionary to hemispheres list
    hemisphere_image_urls.append({"title": syrt_title, "img_url": syrt_image_url})

    # Navigate to target page
    browser.visit(mars_hemispheres_url)

    browser.links.find_by_partial_text("Valles Marineris Hemisphere Enhanced").click()

    # Create soup object
    vall_soup = bs(browser.html, "html.parser")

    # Scrape for the hemisphere title and image url
    vall_title = vall_soup.find("h2", {"class" : "title"}).text

    vall_image = vall_soup.find("ul")

    vall_image_url = mars_hemispheres_url + vall_image.li.a["href"]

    # Append dictionary to hemispheres list
    hemisphere_image_urls.append({"title": vall_title, "img_url": vall_image_url})

    # Close browser
    browser.quit()

    # Final dictionary containing all scraped data
    final_dict = {
        "latest_news_title": latest_news_title,
        "latest_news_paragraph": latest_news_paragraph,
        "featured_image_url": featured_image_url,
        "mars_facts_html_table": mars_facts_html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    return final_dict
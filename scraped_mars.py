
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def init_browser():
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', *executable_path, headless=False)

def scrape_info():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', *executable_path, headless=False)
    

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)
    response = requests.get(url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find ('div',class_='content_title')
    news_title = results.a.text
    results_p = soup.find('div',class_='article_teaser_body')
    news_p = results_p.text

    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    time.sleep(1)
    response2 = requests.get(img_url)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    results2 = soup.find('li',class_='slide')
    link = results2.find('a',class_='fancybox').get('data-fancybox-href')
    featured_img_url = 'https://www.jpl.nasa.gov' + link

    w_url = 'https://twitter.com/MarsWxReport'
    browser.visit(w_url)
    time.sleep(1)
    
    response3 = requests.get(w_url)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    results = soup.find('div', class_='tweet')
    mars_weather = results.find('p',class_= 'TweetTextSize').text

    mars_url ='https://space-facts.com/mars/'
    table = pd.read_html(mars_url)[1]
    html_table = table.to_html()
    html_table.replace('\n', '')
    html_file = table.to_html()

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    response3 = requests.get(url)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    results = soup.find_all('div',class_='item')
    hemisphere_img_url = []
    titles_list = []
    for result in range(len(results)):
    	browser.visit(url)
    	browser.find_by_css("a.product-item h3")[result].click()
    	html = browser.html
    	soup = BeautifulSoup(html,'html.parser')
    	title = soup.find('h2', class_='title').text
    	titles_list.append(title)
    	browser.click_link_by_partial_text('Sample')
    	html = browser.html
    	soup = BeautifulSoup(html,'html.parser')
    	link = soup.find('img')
    	img_url = link['src']
    	hemisphere_img = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'+img_url
    	hemisphere_img_url.append(hemisphere_img)
    	hemis = {
    	"title":titles_list,
    	"img":hemisphere_img_url
    	}

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "mars_weather": mars_weather,
        "featured_img_url": featured_img_url,
        "html_file":html_file,
        "titles_list":titles_list,
        "hemisphere_img_url":hemisphere_img_url
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

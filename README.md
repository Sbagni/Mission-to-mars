### Mission to Mars



In this assignment, we build a web application that scrapes various websites for data related to Mission to Mars and displays the information in a single HTML page. The following outlines what we did.

![mission_to_mars](https://github.com/Sbagni/Mission-to-mars/blob/master/mission_mars.png)

**Web Scraping**

We used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter for initial scraping.Created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all of scraping and analysis tasks. 

**1. NASA Mars News**

We scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that one can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

**2. JPL Mars Space Images - Featured Image**

We visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). Here we
used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.


```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

**3. Mars Weather**

Another important part of this assignment was to visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. We saved the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

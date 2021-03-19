from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # try: 
    step1 = soup.select_one('ul', class_ = 'item_list')
    news_title = soup.find_all('div', class_='content_title')[1].text
    print(step1)

    news_p = soup.find('div', class_ = 'article_teaser_body').text

    mars_dict["news_title"] = news_title
    mars_dict["paragraph"] = news_p
    # except:
        # print("No dice! Try again.")



    print(mars_dict)
    return mars_dict
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(7)

def scrape():
    headers = ["name", "light_yearsPfromPearth", "planet_mass", "stella_magnitude", "discovery_date"]
    planet_list = []
    for i in range(439):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            empt = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    empt.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        empt.append(li_tag.contents[0])
                    except: 
                        empt.append("")
        planet_list.append(empt)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('data.csv', "w") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(planet_list)
scrape()
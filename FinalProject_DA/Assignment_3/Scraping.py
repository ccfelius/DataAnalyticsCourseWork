### you can use multiprocessing in python. You made a function to scrape parts of the dataset and run that in parallel.

### Imports

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Define driver and base url

driver = webdriver.Chrome("/Users/Lotte Felius/Drivers/chromedriver.exe")
base_url = "https://news.tabularazor.org"

# Loop trough every year and month
# Also possible to use multiprocessing with 4 processes
# WITHOUT multiprocessing it takes approx 5 hours to complete
# just change range (begin, end) e.g. (2012, 2014) to obtain 2012 and 2013

def scrape(begin, end):
    for year in range(begin, end):
        for month in range(1,13):

            # Get url, driver, parse content
            url = "https://news.tabularazor.org/" + str(year) + "-" + str(month) + ".html"
            driver.get(url)
            content = driver.page_source
            soup = BeautifulSoup(content, 'html.parser')

            # Store all links on webpage of a particular month in list 'links'
            links=[]
            for a in soup.find_all('div', class_ = 'articlelink'):
                link = a.find('a', href=True)
                links.append(link.text)

            url_list = []
            for i in links:
                url_list.append(base_url + i)

            authors=[]
            dates=[]
            times=[]

            # Loop trough all articles written in a particular month
            for url_ in url_list:
                # print("Processing {}...".format(url_))
                driver.get(url_)
                content2 = driver.page_source
                soup2 = BeautifulSoup(content2, 'html.parser')

                data = soup2.find_all('div')
                authors.append(data[0].text)
                dates.append(data[1].text)
                times.append(data[2].text)

            # Save to pandas DataFrame
            df = pd.DataFrame({'Author name':authors, 'Date':dates, 'Time':times})

            # Write to .txt file to save intermediate results per month
            df.to_csv('output/' + str(year) + '/' + str(year) + '-' + str(month) + '.txt', mode='a', header=False,
                    index=False, encoding='utf-8')

    return "FINISHED"

scrape(2012,2020)

###### IN BASH ######

# cat * > complete.txt


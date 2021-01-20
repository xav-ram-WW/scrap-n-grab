from bs4 import BeautifulSoup
import requests

# creating empty list
urls = []

# function created
def scrape(site):
    # getting the request from url
    r = requests.get(site)
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)
                # calling the scrape function itself
                # generally called recursion
                scrape(site)

# main function
if __name__ == "__main__":
    # website to be scrape 
    site = "http://example.webscraping.com//"
    # calling function 
     scrape(site)
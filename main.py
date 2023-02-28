import requests
from bs4 import BeautifulSoup


def scrape(url):
  response = requests.get(
		url=url,)
	
  soup = BeautifulSoup(response.content, 'html.parser')

  title = soup.find(id="firstHeading")
  print("Title : " + title.text)

  allLinks = soup.find(id="bodyContent").find_all("a")
  print("This file contains "+ str(len(allLinks)) +" links")

  allSubHeadings = soup.find(id="bodyContent").find_all("h2")
  print("\nThis topic has "+ str(len(allSubHeadings)) +" Subtopics")
  i = 0
  for SubHeadings in allSubHeadings:
    i += 1
    text = SubHeadings.text
    if "[edit]" in text:
      SubHeading = text[0:-6]
    else:
      SubHeading = text
    print(str(i) + ") " + SubHeading)

scrape("https://en.wikipedia.org/wiki/C._V._Raman")

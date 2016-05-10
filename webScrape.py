from BeautifulSoup import BeautifulSoup
import requests

def getLinks(text):
    soup = BeautifulSoup(text)
    return [a['href'] for a in soup.findAll('a')]


def getPage(url):
    r = requests.get(url)
    return r.content


def main():
    url = "http://seanplusplus.com"
    page = getPage(url)
    links = getLinks(page)
    print links


if __name__ == '__main__':
    main()

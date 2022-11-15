from unittest import result
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        return 0

def scrape_google(query):
    """Return the non google related urls from a google search. 

    Args: 
        search query (string): Google search key words.

    Returns:
        urls (list): Urls scraped from google page. 
    """
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
                links.remove(url)
        
    return links

def get_beatport_url(query, track_name):
    """Return the first url in a list which contains the track name.

    Args: 
        search query (string): Google search key words.

    Returns:
        url (string): Beatport url of track. 
    """
    links = scrape_google(query)

    for link in links[:]:
        if 'www.beatport.com/track/' in link and '/charted-on' not in link and track_name.split(' ')[0].lower().replace("!", "").replace("'", "") in link:
            return link
    return 'No links found.'

def scrape_beatport(url):
    """Returns the genre of a beatport track.

    Args: 
        url (string): Beatport url. 

    Returns:
        genre (string): The genre of the track. 
    """
    response = get_source(url)
    html_doc = response.html.html
    soup = BeautifulSoup(html_doc, 'html.parser')
    for li in soup.findAll('li', attrs={'class':'interior-track-genre'}):
        # return li
        for a in li.findAll('a'):
            if a.text:
                return a.text
            else:
                return "No genre."

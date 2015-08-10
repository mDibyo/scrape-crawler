#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from urlopeners import URL_OPENER


__author__ = "Dibyo Majumdar"
__email__ = "dibyo.majumdar@gmail.com"



class ElementScraper(metaclass=ABCMeta):
    @abstractmethod
    def scrape(self, html_soup):
        pass


class AttributeBasedElementScraper(ElementScraper):
    def __init__(self, key, tag, attrs):
        self.key = key
        self.tag = tag
        self.attrs = attrs

    def scrape(self, html_soup):
        ele = html_soup.find(self.tag, **self.attrs)
        return {self.key: ele.text}


class CustomElementScraper(ElementScraper):
    def __init__(self, scrape_func):
        self.scrape_func = scrape_func

    def scrape(self, html_soup):
        return self.scrape_func(html_soup)


class PageScraper(object):
    def __init__(self, subscrapers):
        self.subscrapers = subscrapers

    @abstractmethod
    def scrape(self, url):
        html_soup = None
        page = URL_OPENER.open(url)
        html_soup = BeautifulSoup(page.read())
        page.close()

        data = {}
        for scraper in self.subscrapers:
            if isinstance(scraper, ElementScraper):
                new_data = scraper.scrape(html_soup)
            elif isinstance(scraper, PageScraper):
                new_data = scraper.scrape(url)




class IMDBMoviePageScraper(Scraper):
    def __init__(self, url):
        self.url = url

        self.scrapers = [
            AttributeBasedElementScraper('rating', 'span',
                                         {'itemprop': 'ratingValue'})
        ]


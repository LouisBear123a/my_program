import requests
from bs4 import BeautifulSoup


class WebCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url, max_depth=1):
        """
        Crawls the given URL and returns all internal links found within the given depth.
        """
        self.visited_urls.clear()  # Reset visited URLs on each crawl
        return self._crawl(url, max_depth, 0)

    def _crawl(self, url, max_depth, current_depth):
        """
        Recursively crawls the given URL and all internal links within the given depth.
        """
        # Check if max depth has been reached
        if current_depth >= max_depth:
            return set()

        # Check if URL has already been visited
        if url in self.visited_urls:
            return set()

        # Add URL to visited URLs
        self.visited_urls.add(url)

        # Get page content
        try:
            response = requests.get(url)
            response.raise_for_status()
        except (requests.RequestException, ValueError):
            return set()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links on page
        internal_links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/') or href.startswith(url):
                internal_links.add(href)
            elif not href.startswith('http'):
                internal_links.add(url + href)

        # Recursively crawl internal links
        for internal_link in internal_links.copy():
            internal_links |= self._crawl(internal_link, max_depth, current_depth + 1)

        return internal_links

class UrlManager:
    def __new__(cls, *args, **kwargs):
        return super(UrlManager, cls).__new__(cls)

    def __init__(self):
        # the url being scraped right now
        self.new_urls = set()
        # the url that has been scraped
        self.old_urls = set()

    def add_new_url(self, url):
        # return if url is None or empty
        if not url or len(url) == 0:
            return 
        # return if url already exists
        if url in self.new_urls or url in self.old_urls:
            return 
        # push url to self.new_urls
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if not urls or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0
    
if __name__ == "__main__":
    url_manager = UrlManager()






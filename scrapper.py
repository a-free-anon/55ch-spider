import cfscrape
from parser import FiveFiveParser

class FiveFiveScrapper():
  def __init__(self):
    self.scraper = cfscrape.create_scraper()
    self.parser = FiveFiveParser()

  def _get(self, url):
    request = self.scraper.get("http://55chan.org/b/{}".format(url))
    return request

  def _get_thread_list(self):
    request = self._get("threads.json")

    if request.status_code == 200:
      return self.parser.parse_thread_list(request.content)
    else:
      raise Exception

  def _get_thread(self):
    request = self.scraper.get("http://55chan.org/b/threads.json")
    return request.content

  def _scrape_loop(self):
    while True:
      threads = self._get_thread_list()
      print(threads)
      exit()

  def start(self):
    self._scrape_loop()

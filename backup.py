from scrapper import FiveFiveScrapper
from db import BackupBotDb
from tinydb import Query
import json


import time

class BackupBot():
  def __init__(self):
    self.scrapper = FiveFiveScrapper()
    self.db = BackupBotDb()

  def start(self):
    print(":: Starting cloudflare client")
    self.scrapper._get_threads() # First run takes up to five seconds

    print(":: Starting post loop")
    while True:
      try:
        self._tick()
      except json.decoder.JSONDecodeError:
        pass

  def _tick(self):
    print(":::: Scrapping threads")
    threads = self.scrapper._get_threads()

    for no, last_modified in threads.items():
      self._update_thread(no, last_modified)

    time.sleep(5)

  def _update_thread(self, no, last_modified):
    Thread = Query()

    try:
      thread = self.db.threads.search(Thread.no == no)[0]
      print(":::: Thread {} already registered.".format(no))
    except IndexError:
      print(":::: Thread {} not registered. Saving.".format(no))
      thread = {"no": no, "last_modified": last_modified}
      self.db.threads.insert(thread)

    if thread["last_modified"] == last_modified:
      print(":::: Thread not modified.")
      pass
    else:
      print(":::: Thread modified, updating.")

      try:
        thread = self.scrapper._get_thread(no)
        self.db.update_thread(no, thread)
      except:
        pass

    print(":::: Updating last seen.".format(no))
    self.db.update_thread(no, {"last_seen": time.time()})



if __name__ == "__main__":
  d = BackupBot()
  d.start()

from scrapper import FiveFiveScrapper

class DoubleBot():
  def __init__(self):
    self.scrapper = FiveFiveScrapper()

  def start(self):
    print(":: Starting cloudflare client")
    self.scrapper._get_threads() # First run takes up to five seconds

    print(":: Starting post loop")
    self.double_posting_loop()

  def double_posting_loop(self):
    while True:
      try:
        last_post = self._get_last_post_id()
      except KeyboardInterrupt:
        raise
      except:
        print(":: Fetching error")
        next

      print(last_post)
      if (self._is_next_doubles(last_post)):
        print("Next is doubles!")

  def _is_next_doubles(self, last_post):
    next_id = last_post+1
    last_digits = str(next_id)[-2:]
    if len(set(last_digits)) == 1:
      return True
    return False

  def _get_lastest_modified_thread_id(self):
    threads = self.scrapper._get_threads()
    return sorted(threads, key=threads.get, reverse=True)[0]

  def _get_last_post_id(self):
    last_modified_thread = self._get_lastest_modified_thread_id()
    thread = self.scrapper._get_thread(last_modified_thread)

    if len(thread["posts"]):
      return thread["posts"][-1]["no"]
    else:
      return last_modified_thread

if __name__ == "__main__":
  d = DoubleBot()
  d.start()

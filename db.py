from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from tinydb import TinyDB, Query
import time


class BackupBotDb():
  def __init__(self):
    self.db = TinyDB("db.json", storage=CachingMiddleware(JSONStorage))
    self.threads = self.db.table("threads")

  def update_thread(self, no, value):
    Thread = Query()
    self.threads.update(value, Thread.no == no)

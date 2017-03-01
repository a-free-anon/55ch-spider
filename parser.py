import json
import codecs

class FiveFiveParser():
  def parse_thread_list(self, content):
    threads = json.loads(content.decode('utf-8'))
    output_dict = {}
    for page in threads:
      for thread in page["threads"]:
        output_dict[thread["no"]] = thread["last_modified"]
    return output_dict

  def parse_thread(self):
    pass

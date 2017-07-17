import time
import threading

import pyperclip

from iteminfo_parser import ItemInfoParser


class ClipboardWatcher(threading.Thread):
    def __init__(self, predicate=None, callback=None, pause=0.5):
        super(ClipboardWatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = pause

    def run(self):
        recent_str = ""
        while True:
            paste_str = pyperclip.paste()
            if paste_str != recent_str:
                recent_str = paste_str
                ItemInfoParser(recent_str).parse()
                # if self._predicate(recent_value):
                #     self._callback(recent_value)
            time.sleep(self._pause)


def main():
    ClipboardWatcher().start()


if __name__ == "__main__":
    main()

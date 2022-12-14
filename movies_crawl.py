import logging
import time

from settings import CONFIG
from base import Crawler_Site

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

crawler = Crawler_Site()

if __name__ == "__main__":
    i = 2
    while True:
        try:
            crawled_page = crawler.crawl_page(
                f"{CONFIG.SERIES9_MOVIES_LATEST_PAGE}?page={i}",
                post_type="post",
            )
            if not crawled_page and i >= CONFIG.SERIES9_MOVIES_LATEST_PAGE:
                i = 2
            else:
                i += 1
        except Exception as e:
            pass
        time.sleep(CONFIG.WAIT_BETWEEN_ALL)

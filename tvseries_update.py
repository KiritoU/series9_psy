import logging
import time

from settings import CONFIG
from base import Crawler_Site

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


crawler = Crawler_Site()

if __name__ == "__main__":
    while True:
        try:
            crawler.crawl_page(CONFIG.SERIES9_TVSERIES_LATEST_PAGE)
        except Exception as e:
            pass
        time.sleep(CONFIG.WAIT_BETWEEN_LATEST)

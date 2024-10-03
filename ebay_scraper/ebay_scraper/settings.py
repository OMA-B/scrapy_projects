import os, json, datetime
# Scrapy settings for ebay_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "ebay_scraper"

SPIDER_MODULES = ["ebay_scraper.spiders"]
NEWSPIDER_MODULE = "ebay_scraper.spiders"


def get_config_value(value: str):
    with open(file=os.path.join(os.path.dirname(__file__), 'config.json'), mode='r') as file:
        config_data = json.load(fp=file)
    return config_data[value]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ebay_scraper (+http://www.yourdomain.com)"

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'ebay_scraper.middlewares.LogOperationMiddleware': 200,
    'ebay_scraper.middlewares.ProxyMiddleware': 350,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'ebay_scraper.middlewares.CustomRetryMiddleware': 320,
}

# Retry many times since proxies often fail
# RETRY_TIMES = 3
RETRY_TIMES = get_config_value(value='RETRY_TIMES')
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [403, 407, 502, 500, 503, 504, 400, 429, 408]

# Proxy list containing entries like
PROXY_LIST = os.path.join(os.path.dirname(__file__), 'proxies.txt')

# Proxy mode
# PROXY_MODE = 0

RANDOM_UA_PER_PROXY = True

FAKEUSERAGENT_FALLBACK = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# LOG_ENABLED = False

OUTPUT_FORMAT = get_config_value(value='OUTPUT_FILE_TYPE')  # options: 'json', 'jsonlines', 'parquet'
BATCH_SIZE = get_config_value(value='CHUNK_SIZE')
EACH_SPIDER_URLS_PORTION = get_config_value(value='EACH_SPIDER_URLS_PORTION')

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = get_config_value(value='CHUNK_SIZE')

CONCURRENT_ITEMS = get_config_value(value='CHUNK_SIZE')
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = get_config_value(value='CHUNK_SLEEP_TIME')

RANDOMIZE_DOWNLOAD_DELAY = False

LOG_LEVEL = 'INFO'
LOG_FILE = f"scrapy_logs_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.txt"
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "ebay_scraper.middlewares.EbayScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "ebay_scraper.middlewares.EbayScraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "ebay_scraper.pipelines.EbayScraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 0.1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = get_config_value(value='RETRY_SLEEP_TIME')
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = get_config_value(value='CHUNK_SIZE')
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

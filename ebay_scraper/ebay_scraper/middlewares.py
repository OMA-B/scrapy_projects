# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import logging, random, datetime
from collections import defaultdict
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from scrapy.exceptions import NotConfigured


class ProxyMiddleware:
    def __init__(self, settings):
        self.logger = logging.getLogger(__name__)
        self.proxy_list = self.load_proxy_list(settings.get('PROXY_LIST'))
        self.failed_proxies = defaultdict(int)
        self.max_failed_requests = settings.get('RETRY_TIMES', 3)
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.excluded_proxies = []

    def log_excluded_proxy(self, proxy, reason):
        self.excluded_proxies.append((proxy, reason))
        with open(file='excluded_proxies.txt', mode='a') as file:
            file.write(f'Proxy {proxy} excluded due to {self.failed_proxies[proxy]} failures: {reason}\n')

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('PROXY_LIST'):
            raise NotConfigured
        return cls(crawler.settings)

    def load_proxy_list(self, path):
        with open(file=path, mode='r') as file:
            proxies = [line.strip() for line in file if line.strip()]
            self.logger.info(f'Loaded proxies: {proxies}')
            return proxies

    def process_request(self, request, spider):
        proxy = self.get_random_proxy()
        if proxy:
            request.meta['proxy'] = proxy
            self.logger.info(f'Using proxy: {proxy} for URL: {request.url}')
            spider.logger.info(f'Using proxy: {proxy} for URL: {request.url}')

    def process_response(self, request, response, spider):
        proxy = request.meta.get('proxy')
        if proxy and (response.status in self.retry_http_codes or "blocked" in response.text.lower()):
            self.failed_proxies[proxy] += 1
            spider.logger.warning(f'Proxy {proxy} failed with status {response.status} for URL: {request.url}')
            self.logger.warning(f'Proxy {proxy} failed with status {response.status} for URL: {request.url}')
            if self.failed_proxies[proxy] >= self.max_failed_requests:
                self.proxy_list.remove(proxy)
                self.log_excluded_proxy(proxy, f'Status {response.status}')
                spider.logger.error(f'Proxy {proxy} excluded after {self.failed_proxies[proxy]} failures')
                self.logger.error(f'Proxy {proxy} excluded after {self.failed_proxies[proxy]} failures')
            new_request = request.copy()
            new_request.dont_filter = True
            return new_request
        return response

    def process_exception(self, request, exception, spider):
        proxy = request.meta.get('proxy')
        if proxy:
            try:
                self.failed_proxies[proxy] += 1
                spider.logger.error(f'Proxy {proxy} failed with exception {exception} for URL: {request.url}')
                self.logger.error(f'Proxy {proxy} failed with exception {exception} for URL: {request.url}')
                if self.failed_proxies[proxy] >= self.max_failed_requests:
                    self.proxy_list.remove(proxy)
                    self.log_excluded_proxy(proxy, f'Exception {exception}')
                    spider.logger.error(f'Proxy {proxy} excluded due to {self.failed_proxies[proxy]} failures')
                    self.logger.error(f'Proxy {proxy} excluded due to {self.failed_proxies[proxy]} failures')
                    spider.logger.info(f'Removed failed proxy: {proxy}')
            except ValueError:
                spider.logger.warning(f'Attempted to remove non-existent proxy: {proxy}')
        
        # Retry the request with a different proxy if available
        if self.proxy_list:
            new_proxy = self.get_random_proxy()
            spider.logger.info(f'Retrying with new proxy: {new_proxy}')
            request.meta['proxy'] = new_proxy
            return request
        else:
            spider.logger.error('No proxies left to retry with')
            return None
        
    def get_random_proxy(self):
        if self.proxy_list:
            proxy = random.choice(self.proxy_list)
            self.logger.info(f'Chosen proxy: {proxy}')
            return proxy
        return None


class CustomRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super().__init__(settings)
        self.logger = logging.getLogger(__name__)
        self.proxy_list = self.load_proxy_list(settings.get('PROXY_LIST'))
        self.failed_proxies = defaultdict(int)
        self.max_failed_requests = settings.get('RETRY_TIMES', 3)
        self.excluded_proxies = []

    def log_excluded_proxy(self, proxy, reason):
        self.excluded_proxies.append((proxy, reason))
        with open(file='excluded_proxies.log', mode='a') as file:
            file.write(f'Proxy {proxy} excluded due to {self.failed_proxies[proxy]} failures: {reason}\n')

    def load_proxy_list(self, path):
        with open(file=path, mode='r') as file:
            proxies = [line.strip() for line in file if line.strip()]
            self.logger.info(f'Loaded proxies: {proxies}')
            return proxies

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes or "blocked" in response.text.lower():
            reason = response_status_message(response.status)
            proxy = request.meta.get('proxy')
            if proxy:
                self.failed_proxies[proxy] += 1
                spider.logger.warning(f'Proxy {proxy} failed with status {response.status} for URL: {request.url}')
                if self.failed_proxies[proxy] >= self.max_failed_requests:
                    self.proxy_list.remove(proxy)
                    self.log_excluded_proxy(proxy, f'Status {response.status}')
                    spider.logger.error(f'Proxy {proxy} excluded after {self.failed_proxies[proxy]} failures')
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        if request.meta.get('dont_retry', False):
            return None
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
            proxy = request.meta.get('proxy')
            if proxy:
                self.failed_proxies[proxy] += 1
                spider.logger.error(f'Proxy {proxy} failed with exception {exception} for URL: {request.url}')
                if self.failed_proxies[proxy] >= self.max_failed_requests:
                    self.proxy_list.remove(proxy)
                    self.log_excluded_proxy(proxy, f'Exception {exception}')
                    spider.logger.error(f'Proxy {proxy} excluded due to {self.failed_proxies[proxy]} failures')
            return self._retry(request, exception, spider)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1

        if retries <= self.max_retry_times:
            new_request = request.copy()
            new_request.meta['retry_times'] = retries
            new_request.dont_filter = True
            new_proxy = self.get_random_proxy()
            if new_proxy:
                new_request.meta['proxy'] = new_proxy
            spider.logger.info(f"Retrying {new_request.url} (failed {retries} times): {reason}")
            return new_request
        else:
            spider.logger.error(f"Giving up {request.url} (failed {retries} times): {reason}")

    def get_random_proxy(self):
        if self.proxy_list:
            return random.choice(self.proxy_list)
        return None

class LogOperationMiddleware:
    def process_response(self, request, response, spider):
        proxy = request.meta.get('proxy')
        url = request.url
        status = response.status
        comment = 'Success' if 200 <= status < 400 else 'Failed'
        if proxy:
            log_entry = f"[Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}, Input URL: {url}, Proxy Used: {proxy}, Status Code: {status}, Comment: {comment}]"
            spider.logger.info(log_entry)
            with open('Operations_log.txt', 'a+') as file:
                file.write(f"\n{log_entry}")
        return response


class EbayScraperSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class EbayScraperDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

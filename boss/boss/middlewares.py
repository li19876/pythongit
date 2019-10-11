# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64

from scrapy import signals
import random
import requests
import json
from boss.modules import ProxyModules
from twisted.internet.defer import DeferredLock
from base64 import b64decode

class BossSpiderMiddleware(object):
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

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BossDownloaderMiddleware(object):
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

        proxy="123.56.162.200:16817"
        username="2270657376"
        password="bxzh9pu4"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': proxy},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': proxy}
        }
        request.headers['Accept-Encoding']="Gzip"
        request.meta['proxies'] = proxies
        # request.headers['proxy-Authorization'] = 'Basic '+ b64.decode('utf-8')
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
        spider.logger.info('Spider opened: %s' % spider.name)

class UserAgentDownloadMiddleware(object):
    UG = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.360',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:10.0) Gecko/20100101 Firefox/62.0'
    ]
    def process_request(self,request,spider):
        user = random.choice(self.UG)
        request.headers['User-Agent'] = user
        request.headers['Accept-Language'] = 'en'
        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

class IPProxyDownloadMiddleware(object):
    proxy_url = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    def __init__(self):
        super(IPProxyDownloadMiddleware,self).__init__()
        self.current_proxy = None
        self.lock = DeferredLock()

    def process_request(self,request,spider):
        print(request.url,"当前请求的链接")

        if 'proxy' not in request.meta or self.current_proxy.is_expring:
            print("重新获取了一个代理")
            self.update_proxy()
        request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self, request, response, spider):
        print("%s当前网页状态"%response.status)
        if "zpAntispam" in response.url:
            print("%s当前网页链接,这个链接包含zpAntispam"%response.url)
        if response.status != 200 or "zpAntispam" in response.url:
            print("%s这个代理被加入黑名单了"%self.current_proxy.ip)
            if not self.current_proxy.blacked:
                self.current_proxy.blacked=True
            self.update_proxy()
            return request
        return response

    def update_proxy(self):
        self.lock.acquire()
        if not self.current_proxy or self.current_proxy.is_expring or self.current_proxy.blacked:
            resp = requests.get(url=self.proxy_url)
            text = resp.text
            jsonHTML=json.loads(text)
            if len(jsonHTML['data'])>0:
                respJ = jsonHTML['data'][0]
                proxy_model = ProxyModules(data=respJ)
                self.current_proxy = proxy_model
                return proxy_model
        self.lock.release()




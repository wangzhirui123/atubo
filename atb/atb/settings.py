# -*- coding: utf-8 -*-

import requests
# Scrapy settings for atb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'atb'

SPIDER_MODULES = ['atb.spiders']
NEWSPIDER_MODULE = 'atb.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'atb (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'atb.middlewares.AtbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'atb.middlewares.MyCustomDownloaderMiddleware': 543,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#     'atb.middlewares.MyProxyMiddleware':125
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'atb.pipelines.AtbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []

#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IPPOOL = str(requests.get('http://webapi.http.zhimacangku.com/getip?num=30&type=3&pro=&city=0&yys=0&port=1&time=3&ts=0&ys=0&cs=0&lb=6&sb=\n&pb=4&mr=2&regions=').content).split('\n')


DNSCACHE_ENABLED =False


# IPPOOL = ['175.153.73.205:7684',
# '175.154.202.87:4226',
# '117.57.38.5:4273',
# '111.76.65.104:1863',
# '122.192.24.218:13406',
# '117.67.143.79:2644',
# '115.85.206.235:3012',
# '110.18.136.19:6410',
# '222.188.14.155:3456',
# '117.69.231.221:3852',
# '58.218.201.143:3075',
# '59.62.6.114:4261',
# '115.225.65.109:5946',
# '58.218.201.143:6534',
# '59.62.7.19:4261',
# '140.255.7.243:7889',
# '42.226.94.81:1246',
# '117.65.47.193:4251',
# '113.121.23.156:9077',
# '116.7.173.81:4223',
# '60.183.104.11:2314',
# '122.192.24.218:12077',
# '122.192.24.218:13449',
# '220.179.219.144:4276',
# '115.199.218.156:1246',
# '58.218.201.143:3601',
# '124.94.203.157:1767',
# '58.218.201.143:9325',
# '58.218.201.143:7124',
# '58.218.201.143:2970',
# '115.85.206.164:3012',
# '118.79.54.24:6996',
# '124.152.85.125:3012',
# '119.5.216.92:4246',
# '58.218.201.143:7405',
# '111.201.96.9:4282',
# '113.27.102.32:4236',
# '117.57.32.186:4226',
# '122.192.24.218:12831',
# '140.224.153.214:4275']













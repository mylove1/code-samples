# -*- coding: utf-8 -*-

# Scrapy settings for estate project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'estate'

SPIDER_MODULES = ['estate.spiders']
NEWSPIDER_MODULE = 'estate.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'estate (+http://www.yourdomain.com)'

DB = {
    'host': 'localhost',
    'port': 33060,
    'user': 'homestead',
    'passwd': 'secret',
    'db': 'estate'
}

DOWNLOADER_MIDDLEWARES = {
    #'misc.middleware.CustomHttpProxyMiddleware': 400,
    'estate.middlewares.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    'estate.pipelines.EstatePipeline': 300,
    #'template.pipelines.RedisPipeline': 301,
}

#DOWNLOAD_DELAY = 1

#LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'INFO'

COOKIES_ENABLED = False

# Close spider extension
CLOSESPIDER_ITEMCOUNT = 3000

# @todo: 需要配置抓取数目
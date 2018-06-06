# -*- coding: utf-8 -*-
BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"

ITEM_PIPELINES = {
   'douban.pipelines.DoubanPipeline': 300,
}

# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "Douban"
# 存放数据的表名称
MONGODB_SHEETNAME = "doubanmovies"


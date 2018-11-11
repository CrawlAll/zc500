# -*- coding: utf-8 -*-

BOT_NAME = 'zc500'

SPIDER_MODULES = ['zc500.spiders']
NEWSPIDER_MODULE = 'zc500.spiders'

LOG_FILE = "sfr9.log"
# LOG_FILE = "zcExponential.log"
LOG_LEVEL = "INFO"

USER_AGENT = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2.5
COOKIES_ENABLED = False  # (enabled by default)

DOWNLOADER_MIDDLEWARES = {
	'zc500.middlewares.RandomUserAgentMiddleware': 100,
}

ITEM_PIPELINES = {
	# 'zc500.pipelines.Zc500MongodbPipeline': 300,
	'zc500.pipelines.sfr9MysqlPipeline': 301,
	# 'zc500.pipelines.zcExponentialMysqlPipeline': 302,
}

# MongoDB数据库的配置信息
MONGODB_HOST = "localhost"  # MONGODB 主机名
MONGODB_PORT = 27017  # MONGODB 端口号
MONGODB_DBNAME = "SpotteryRollList"  # 数据库名称
MONGODB_SHEETNAME = "fb_list.py"  # 存放数据的表名称

# Mysql数据库的配置信息
MYSQL_HOST = '192.168.1.5'
MYSQL_DBNAME = 'crawler'  # 数据库名字，请修改
MYSQL_USER = 'xx'  # 数据库账号，请修改
MYSQL_PASSWD = 'xx'  # 数据库密码，请修改
MYSQL_PORT = 3306  # 数据库端口

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

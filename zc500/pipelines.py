# -*- coding: utf-8 -*-
import pymysql
import pymongo


class Zc500MongodbPipeline(object):
	def __init__(self, host, dbname, port, sheetname):
		self.host = host
		self.dbname = dbname
		self.port = port
		self.sheetname = sheetname

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host=crawler.settings.get('MONGODB_HOST'),
			port=crawler.settings.get('MONGODB_PORT'),
			dbname=crawler.settings.get('MONGODB_DBNAME'),
			sheetname=crawler.settings.get('MONGODB_SHEETNAME')
		)

	def open_spider(self, spider):
		# 连接MONGODB
		self.client = pymongo.MongoClient(host=self.host, port=self.port)
		# 指定数据库
		self.mydb = self.client[self.dbname]
		# 存放数据的数据库表名
		self.sheet = self.mydb[self.sheetname]

	def process_item(self, item, spider):
		data = dict(item)
		self.sheet.insert(data)
		return item


class sfr9MysqlPipeline(object):
	def __init__(self, host, dbname, user, pwd, port):
		self.host = host
		self.dbname = dbname
		self.user = user
		self.pwd = pwd
		self.port = port

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host=crawler.settings.get('MYSQL_HOST'),
			dbname=crawler.settings.get('MYSQL_DBNAME'),
			user=crawler.settings.get('MYSQL_USER'),
			pwd=crawler.settings.get('MYSQL_PASSWD'),
			port=crawler.settings.get('MYSQL_PORT')
		)

	def open_spider(self, spider):
		self.connect = pymysql.connect(host=self.host, db=self.dbname, user=self.user, passwd=self.pwd, port=self.port,
									   charset='utf8', use_unicode=True)
		# 通过cursor执行增删查改
		self.cursor = self.connect.cursor()

	def process_item(self, item, spider):
		try:
			# 插入数据
			# 注意修改表名。。
			self.cursor.execute(
				"""insert into traditional_zc500_payout_info(series, hot_cold, opening_time, M1 ,M2, M3, M4, M5, M6, \
M7, M8, M9, M10, M11, M12, M13, M14, 14games_sales, 9games_sales, last_accumulated, first_prize_num, first_prize, \
payout_num, payout_prize, second_prize_num, second_prize, 9games_num, 9games_prize, 9games_payout_num, 9games_payout_prize, \
source) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
				(item['series'], item['hot_cold'], item['opening_time'], item['M1'], item['M2'], item['M3'], item['M4'],
				 item['M5'], item['M6'], item['M7'], item['M8'], item['M9'], item['M10'], item['M11'], item['M12'],
				 item['M13'], item['M14'], item['sfxl'], item['rjxl'], item['jcgc'], item['ydjzs'], item['ydjdzjj'],
				 item['pjzs'], item['pjdzjj'], item['edjzs'], item['edjdzjj'], item['rjzs'], item['rjdzjj'],
				 item['rjpjzs'], item['rjpjdzjj'], item['source']))
			self.connect.commit()

		except Exception as error:
			spider.logger.error(error)
		return item

	def close_spider(self, spider):
		self.connect.close()


class zcExponentialMysqlPipeline(object):
	def __init__(self, host, dbname, user, pwd, port):
		self.host = host
		self.dbname = dbname
		self.user = user
		self.pwd = pwd
		self.port = port

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host=crawler.settings.get('MYSQL_HOST'),
			dbname=crawler.settings.get('MYSQL_DBNAME'),
			user=crawler.settings.get('MYSQL_USER'),
			pwd=crawler.settings.get('MYSQL_PASSWD'),
			port=crawler.settings.get('MYSQL_PORT')
		)

	def open_spider(self, spider):
		self.connect = pymysql.connect(host=self.host, db=self.dbname, user=self.user, passwd=self.pwd, port=self.port,
									   charset='utf8', use_unicode=True)
		# 通过cursor执行增删查改
		self.cursor = self.connect.cursor()

	def process_item(self, item, spider):
		try:
			# 插入数据
			# 注意修改表名。。
			self.cursor.execute(
				"""insert into traditional_zc500_exponential(series, num, league, match_, company, win, draw, lose, \
H_WaterLevel, handicap, A_WaterLevel, source) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
				(item['series'], item['num'], item['league'], item['match'], item['company'], item['win'], item['draw'],
				 item['lose'], item['H_WaterLevel'], item['handicap'], item['A_WaterLevel'], item['source']))
			self.connect.commit()

		except Exception as error:
			spider.logger.error(error, '..', item['source'])
		return item

	def close_spider(self, spider):
		self.connect.close()

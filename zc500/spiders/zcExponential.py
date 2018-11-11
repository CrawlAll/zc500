# -*- coding: utf-8 -*-
import scrapy
from zc500.items import Zc500Item


class ZcexponentialSpider(scrapy.Spider):
	name = 'zcExponential'
	allowed_domains = ['500.com']
	start_urls = ['http://zx.500.com/zc/odds_sfc.php']

	def parse(self, response):
		series_list = response.xpath("//select[@id='expect']/option").xpath("string(.)").extract()
		for i in range(len(series_list[3:])):
			page_num = series_list[i]
			detailUrl = 'http://zx.500.com/zc/odds_sfc.php?expect=' + page_num
			yield scrapy.Request(url=detailUrl, callback=self.second_parse)

	# 详细页
	def second_parse(self, response):
		item = Zc500Item()
		source = response.url
		item['source'] = source
		item['series'] = source[-5:]

		table_list = response.xpath("//div[@id='n1']/table")
		# 最新的有些没及时更新，所以存在 没有的情况
		if table_list == 0:
			yield item
		# 一般情况下会有14场
		else:
			for j in xrange(len(table_list)):
				num = j + 1
				item['num'] = num
				table_num = "//div[@id='n1']/table[%s]" % num

				# 表格左侧数据
				league = response.xpath(table_num + "//dl[@class='sfc-zc-dz']/dt/a/b").xpath("string(.)").extract()
				item['league'] = league[0].replace(' ', '') if league else None
				match = response.xpath(table_num + "//dl[@class='sfc-zc-dz']/dd[1]").xpath("string(.)").extract()
				item['match'] = match[0] if match else None

				# 表格中间及右侧数据
				tr_list = response.xpath(table_num + "/tbody/tr")
				for m in range(len(tr_list)):
					tr_num = table_num + "/tbody/tr[%s]" % (m + 1)
					company = response.xpath(tr_num + "/td[1]").xpath("string(.)").extract()
					item['company'] = company[0] if company else None
					win = response.xpath(tr_num + "/td[2]").xpath("string(.)").extract()
					win_ = win[0] if win else 0
					item['win'] = 0 if win_ == '' else win_
					draw = response.xpath(tr_num + "/td[3]").xpath("string(.)").extract()
					draw_ = draw[0] if draw else 0
					item['draw'] = 0 if draw_ == '' else draw_
					lose = response.xpath(tr_num + "/td[4]").xpath("string(.)").extract()
					lose_ = lose[0] if lose else 0
					item['lose'] = 0 if lose_ == '' else lose_
					H_WaterLevel = response.xpath(tr_num + "/td[5]").xpath("string(.)").extract()
					H_WaterLevel_ = H_WaterLevel[0] if H_WaterLevel else 0
					item['H_WaterLevel'] = 0 if H_WaterLevel_ == '' else H_WaterLevel_
					handicap = response.xpath(tr_num + "/td[6]").xpath("string(.)").extract()
					item['handicap'] = handicap[0] if handicap else None
					A_WaterLevel = response.xpath(tr_num + "/td[7]").xpath("string(.)").extract()
					A_WaterLevel_ = A_WaterLevel[0] if A_WaterLevel else 0
					item['A_WaterLevel'] = 0 if A_WaterLevel_ == '' else A_WaterLevel_
					yield item

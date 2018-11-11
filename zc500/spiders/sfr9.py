# -*- coding: utf-8 -*-
import re
import scrapy
from zc500.items import Zc500Item


class Sfr9Spider(scrapy.Spider):
	name = 'sfr9'
	allowed_domains = ['500.com']
	start_urls = ['http://zx.500.com/zc/lskj.shtml?sfcall']

	# 第一层
	def parse(self, response):
		detailUrl_list = response.xpath("//table[@class='sfc-tb-a sfc-tb-d']/tbody/tr/td/a/@href").extract()
		for i in range(len(detailUrl_list)):
			item = Zc500Item()

			# 第二层的url
			detailUrl = 'http:' + detailUrl_list[i].encode('utf-8')

			repead_xpath = "//table[@class='sfc-tb-a sfc-tb-d']/tbody/tr[%s]" % (i + 1)
			item['series'] = response.xpath(repead_xpath + "/td[1]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M1'] = response.xpath(repead_xpath + "/td[2]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M2'] = response.xpath(repead_xpath + "/td[3]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M3'] = response.xpath(repead_xpath + "/td[4]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M4'] = response.xpath(repead_xpath + "/td[5]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M5'] = response.xpath(repead_xpath + "/td[6]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M6'] = response.xpath(repead_xpath + "/td[7]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M7'] = response.xpath(repead_xpath + "/td[8]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M8'] = response.xpath(repead_xpath + "/td[9]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M9'] = response.xpath(repead_xpath + "/td[10]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M10'] = response.xpath(repead_xpath + "/td[11]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M11'] = response.xpath(repead_xpath + "/td[12]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M12'] = response.xpath(repead_xpath + "/td[13]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M13'] = response.xpath(repead_xpath + "/td[14]").xpath('string(.)').extract()[0].encode('utf-8')
			item['M14'] = response.xpath(repead_xpath + "/td[15]").xpath('string(.)').extract()[0].encode('utf-8')
			item['hot_cold'] = response.xpath(repead_xpath + "/td[16]").xpath('string(.)').extract()[0].encode('utf-8')
			item['opening_time'] = response.xpath(repead_xpath + "/td[22]").xpath('string(.)').extract()[0].encode(
				'utf-8')

			yield scrapy.Request(url=detailUrl, meta={'meta_1': item}, callback=self.second_parse)

	# 第二层
	def second_parse(self, response):
		meta_1 = response.meta['meta_1']
		item = Zc500Item()
		item['series'] = meta_1['series']
		item['M1'], item['M2'], item['M3'], item['M4'] = meta_1['M1'], meta_1['M2'], meta_1['M3'], meta_1['M4']
		item['M5'], item['M6'], item['M7'], item['M8'] = meta_1['M5'], meta_1['M6'], meta_1['M7'], meta_1['M8']
		item['M9'], item['M10'], item['M11'] = meta_1['M9'], meta_1['M10'], meta_1['M11']
		item['M12'], item['M13'], item['M14'] = meta_1['M12'], meta_1['M13'], meta_1['M14']
		item['hot_cold'], item['opening_time'] = meta_1['hot_cold'], meta_1['opening_time']

		# 第一个table
		sfxl = response.xpath("//table[1]//tr[4]/td/span[1]").xpath('string(.)').extract()
		sfxl = sfxl[0].encode('utf-8').replace('元', '').replace(',', '') if sfxl else None
		item['sfxl'] = sfxl
		rjxl = response.xpath("//table[1]//tr[4]/td/span[2]").xpath('string(.)').extract()
		rjxl = rjxl[0].encode('utf-8').replace('元', '').replace(',', '') if rjxl else None
		item['rjxl'] = rjxl
		jcgc = response.xpath("//table[1]//tr[4]/td/span[3]").xpath('string(.)').extract()
		jcgc = jcgc[0].encode('utf-8').replace('元', '').replace(',', '') if jcgc else None
		item['jcgc'] = jcgc

		# 第二个table
		tr_list = response.xpath('//table[2]//tr').extract()
		for tr in tr_list[2:-1]:
			tr = tr.encode('utf-8')
			td_list = re.findall(r'<td>(.*?)</td>', tr)
			if tr.find('奖') != -1:
				if tr.find('等') != -1:
					# 一等奖
					if tr.find('一') != -1:
						ydjzs = td_list[1]
						item['ydjzs'] = ydjzs.replace(',', '')
						ydjdzjj = td_list[2]
						item['ydjdzjj'] = ydjdzjj.replace(',', '')
					# 二等奖
					elif tr.find('二') != -1:
						edjzs = td_list[1]
						item['edjzs'] = edjzs.replace(',', '')
						edjdzjj = td_list[2]
						item['edjdzjj'] = edjdzjj.replace(',', '')
				elif tr.find('派奖') != -1:
					# 任九派奖
					if tr.find('任九派奖') != -1:
						rjpjzs = td_list[1]
						item['rjpjzs'] = rjpjzs.replace(',', '')
						rjpjdzjj = td_list[2]
						item['rjpjdzjj'] = rjpjdzjj.replace(',', '')
					# 派奖
					else:
						pjzs = td_list[1]
						item['pjzs'] = pjzs.replace(',', '')
						pjdzjj = td_list[2]
						item['pjdzjj'] = pjdzjj.replace(',', '')
			# 任九
			elif tr.find('任九') != 1:
				rjzs = td_list[1]
				item['rjzs'] = rjzs.replace(',', '')
				rjdzjj = td_list[2]
				item['rjdzjj'] = rjdzjj.replace(',', '')

		# 增加字典中不存在的键的默认值
		item['ydjzs'] = item.get('ydjzs', None)
		item['ydjdzjj'] = item.get('ydjdzjj', None)
		item['pjzs'] = item.get('pjzs', None)
		item['pjdzjj'] = item.get('pjdzjj', None)
		item['edjzs'] = item.get('edjzs', None)
		item['edjdzjj'] = item.get('edjdzjj', None)
		item['rjzs'] = item.get('rjzs', None)
		item['rjdzjj'] = item.get('rjdzjj', None)
		item['rjpjzs'] = item.get('rjpjzs', None)
		item['rjpjdzjj'] = item.get('rjpjdzjj', None)

		item['source'] = response.url

		yield item

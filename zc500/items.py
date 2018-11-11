# -*- coding: utf-8 -*-
import scrapy


class Zc500Item(scrapy.Item):
	# sfr9
	# 从第一层获取
	# 1、期号
	series = scrapy.Field()
	# 2、第1场
	M1 = scrapy.Field()
	# 3、第2场
	M2 = scrapy.Field()
	# 4、第3场
	M3 = scrapy.Field()
	# 5、第4场
	M4 = scrapy.Field()
	# 6、第5场
	M5 = scrapy.Field()
	# 7、第6场
	M6 = scrapy.Field()
	# 8、第7场
	M7 = scrapy.Field()
	# 9、第8场
	M8 = scrapy.Field()
	# 10、第9场
	M9 = scrapy.Field()
	# 11、第10场
	M10 = scrapy.Field()
	# 12、第11场
	M11 = scrapy.Field()
	# 13、第12场
	M12 = scrapy.Field()
	# 14、第13场
	M13 = scrapy.Field()
	# 15、第14场
	M14 = scrapy.Field()
	# 16、赛果冷热统计
	hot_cold = scrapy.Field()
	# 17、开奖时间
	opening_time = scrapy.Field()
	# 从第二层获取
	# 1、本期足彩胜负销量
	sfxl = scrapy.Field()
	# 2、本期任九销量
	rjxl = scrapy.Field()
	# 3、足彩胜负彩奖池滚存
	jcgc = scrapy.Field()
	# 4、一等奖注数
	ydjzs = scrapy.Field()
	# 5、一等奖单注奖金
	ydjdzjj = scrapy.Field()
	# 6、派奖注数
	pjzs = scrapy.Field()
	# 7、派奖单注奖金
	pjdzjj = scrapy.Field()
	# 8、二等奖注数
	edjzs = scrapy.Field()
	# 9、二等奖单注奖金
	edjdzjj = scrapy.Field()
	# 10、任九注数
	rjzs = scrapy.Field()
	# 11、任九单注奖金
	rjdzjj = scrapy.Field()
	# 12、任九派奖注数
	rjpjzs = scrapy.Field()
	# 13、任九派奖单注奖金
	rjpjdzjj = scrapy.Field()
	# 14、该数据来源的url
	source = scrapy.Field()

	# zcExponential
	# 1、期号series 同15行
	# 2、场号
	num = scrapy.Field()
	# 3、联赛
	league = scrapy.Field()
	# 4、比赛
	match = scrapy.Field()
	# 5、博彩公司
	company = scrapy.Field()
	# 6、标胜
	win = scrapy.Field()
	# 7、标平
	draw = scrapy.Field()
	# 8、标负
	lose = scrapy.Field()
	# 9、主队水位home
	H_WaterLevel = scrapy.Field()
	# 10、让球
	handicap = scrapy.Field()
	# 11、客队水位away
	A_WaterLevel = scrapy.Field()
	# 12、该数据来源source 同76行

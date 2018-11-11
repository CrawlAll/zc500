# 项目说明

### 一.zc500
- 该项目下有两个爬虫文件
1. zc500/zc500/spiders/sfr9

    - 该爬虫由下面链接进入第一层，链接如下
    - http://zx.500.com/zc/lskj.shtml?sfcall
    - 爬取的是 足彩胜负(任选9场)及子链接下的页面
    - 子链接e.g.http://kaijiang.500.com/shtml/sfc/17194.shtml
2. zc500/zc500/spiders/zcExponential

    - 该爬虫实际为一层，只是先从第一页，获取全部所要爬取的期号，链接如下
    - http://zx.500.com/zc/odds_sfc.php
    - 之后的链接大概如下
    - http://zx.500.com/zc/odds_sfc.php?expect=17195

### 二、入库字段说明
    sfr9
    # 从第一层获取            
    1、期号serie                2、第1场M1            
    3、第2场M2                  4、第3场M3            
    5、第4场M4                  6、第5场M5            
    7、第6场M6                  8、第7场M7            
    9、第8场M8                  10、第9场M9            
    11、第10场M10               12、第11场M11            
    13、第12场M12               14、第13场M13            
    15、第14场M14               16、赛果冷热统计hot_cold
    17、开奖时间opening_time
    # 从第二层获取
    1、本期足彩胜负销量sfxl      2、本期销量rjxl
    3、足彩胜负彩奖池滚存jcgc    4、一等奖注数ydjzs
    5、一等奖单注奖金ydjdzjj     6、派奖注数pjzs
    7、派奖单注奖金pjdzjj        8、二等奖注数edjzs
    9、二等奖单注奖金edjdzjj     10、任九注数rjzs
    11、任九单注奖金rjdzjj       12、任九派奖注数rjpjzs
    13、任九派奖单注奖金rjpjdzjj 14、该数据来源的urlsource            
    
    zcExponential
    1、期号series                2、场号num
    3、联赛league                4、比赛match
    5、博彩公司company           6、标胜win
    7、标平draw                  8、标负lose
    9、主队水位homeH_WaterLevel  10、让球handicap
    11、客队水位awayA_WaterLevel 12、该数据来源source



### 三、备注
- 因为有两个爬虫文件，开启爬虫时注意修改settings
- 具体的是 数据库表名 ITEM_PIPELINES LOG_FILE
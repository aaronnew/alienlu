# alienlu
aliexpress为速卖通关键字搜索爬虫，利用了selenium和phatomjs模拟js点击进行爬取


scrapy12306为12306抢票脚本，利用scrapy对12306服务器发送查票请求，设置为0.1s一次，如果查到有票以后会调用Login函数进行登录购买，验证码使用第三方打码。


scrapyguahao为深圳网上医院挂号脚本，同样利用scrapy对91160进行查询请求，1秒一次，查到可以挂号后会调用login函数进行预约等级，验证码为第三方打码。

2017/08/27
增加snkrs中国一键下单的脚本
增加apple一键下单的脚本

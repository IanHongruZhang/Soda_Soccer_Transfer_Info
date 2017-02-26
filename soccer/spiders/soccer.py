from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from soccer.items import SoccerItem
from bs4 import BeautifulSoup
import re
from scrapy import FormRequest #起模拟登录作用的一个包

class myspider(CrawlSpider):

    name = 'soccer'
    allowed_domains = ['sodasoccer.com'] #限定爬行域名范围
    start_urls = ['http://www.sodasoccer.com/summary/transfer/index.shtml']  #爬虫入口
    ###编写爬虫规则！
    rules = (Rule(LinkExtractor(allow = ('transfer\/\index+(\w?)+.shtml')),callback = 'parse_item', follow = True),
             )

    def parse_item(self,response):
        html_page = BeautifulSoup(response.text,'lxml')
        total = html_page.find("table",class_ = 'paitable2').find_all('tr',{'align':"center"})
        list_total_1 = []
        for item in total:
            k = item.get_text().strip()
            list_total_1.append(k)
        list_total_2 = []
        for item in list_total_1:
            item_1 = re.split('\n',item) #去掉空格，必须用正则的方法去掉空格
            list_total_2.extend(item_1)
        list_total_2 = list_total_2[6:] #剪去前面不要的元素

        item_t = SoccerItem() #引入items.py里的类
        #使用暴力方法
        #由于表的行是固定的，列表中的元素进11位，就能得到下一个元素
        #把名字计入列表之中
        list_transfer_from = []
        list_transfer_to = []
        list_transfer_name = []
        list_transfer_date = []
        list_transfer_model = []
        list_transfer_fee = []

        for tf in list_total_2[7::11]:
            list_transfer_from.append(tf)

        for tt in list_total_2[10::11]:
            list_transfer_to.append(tt)

        for name in list_total_2[4::11]:
            list_transfer_name.append(name)

        for date in list_total_2[0::11]: #转会日期
            list_transfer_date.append(date)

        for model in list_total_2[1::11]:
            list_transfer_model.append(model)

        for fee in list_total_2[2::11]:
            list_transfer_fee.append(fee)


        list_total_3 = zip(list_transfer_from,list_transfer_to,list_transfer_name,list_transfer_date,list_transfer_model,list_transfer_fee)
        for tf,tt,name,date,model,fee in list_total_3:
            item_t['transfer_from'] = tf
            item_t['transfer_to'] = tt
            item_t['transfer_name'] = name
            item_t['transfer_date'] = date
            item_t['transfer_model'] = model
            item_t['transfer_fee'] = fee
            yield item_t

        '''
        for tf in list_transfer_from:
            item_t['transfer_from'] = tf

        for tt in list_transfer_to:
            item_t['transfer_to'] = tt
            yield item_t
            #print(tt)
            #item_t['transfer_to'] = tt
            #return item_t
        '''


        '''
        for name in list_total_2[4::11]:
            item_t['transfer_name'] = name

        for tf in list_total_2[7::11]:
            item_t['transfer_from'] = tf

        for date in list_total_2[0::11]: #转会日期
            item_t['transfer_date'] = date
            #pass

        for model in list_total_2[1::11]:
            #print(model)
            item_t['transfer_model'] = model
            #pass

        for fee in list_total_2[2::11]:
            #print(fee)
            item_t['transfer_fee'] = fee

        for tt in list_total_2[10::11]:
            item_t['transfer_to'] = tt
            yield item_t'''
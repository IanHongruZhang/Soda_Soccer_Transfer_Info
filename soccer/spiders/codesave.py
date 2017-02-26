'''
html_soup = BeautifulSoup(response.text,'lxml')
page_total = html_soup.find('div',class_ = 'g_b1').find_all('tr',{'align':'center'})
list_total = []
for i in page_total:
    k = i.get_text().strip()
    list_total.append(k)

list_single = []
for item in list_total:
    item1 = item.split('\n',100)
    list_single.append(item1)

print(list_single)

#item = SoccerItem()
#item['url'] = response.url
#return item


def parse_item(self,response):
    #print(response.url)
    pass

Rule(LinkExtractor(allow = ('transfer\/\d+.shtml')),callback= 'parse_item',follow = True),
'''
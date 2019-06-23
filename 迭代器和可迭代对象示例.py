import requests
from lxml import etree
import city_dict
from collections.abc import Iterable,Iterator

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getwea(self,city):
        if city in city_dict.dt:
            url = 'http://www.weather.com.cn/weather/{}.shtml'.format(city_dict.dt[city])
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            html = etree.HTML(r.text)    
            xrl_date = 'string(.//li[contains(@class,"sky")][1]/h1)'
            xrl_wea =  'string(.//li[contains(@class,"sky")][1]/p[@class="wea"])'
            xrl_tem =  'string(.//li[contains(@class,"sky")][1]/p[@class="tem"])'
            date = html.xpath(xrl_date).strip()
            weaInfo = html.xpath(xrl_wea).strip()
            temInfo = html.xpath(xrl_tem).strip()
            return city+':'+date+weaInfo+temInfo

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getwea(city)


class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

ts = WeatherIterable(['北京', '上海', '天津', '镇江', '重庆'])
for i in ts:
    print(i)


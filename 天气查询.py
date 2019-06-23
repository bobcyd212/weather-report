import requests
from lxml import etree
import city_dict

while True:
    city = input('请输入城市,空格退出:').strip()
    if not city:
        print('感谢使用！')
        break
    dt = city_dict.dt #347个主要城市
    if city not in dt:
        print('输入城市无法查询，请选择其他城市')
        city = input('请输入城市:')
    riqi = int(input('今日天气请输入1，明日天气请输入2，后天输入3，以此类推可查询7日:'))
    url = 'http://www.weather.com.cn/weather/{}.shtml'.format(dt[city])
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)    
    xrl_date = 'string(.//li[contains(@class,"sky")][{}]/h1)'.format(riqi)
    xrl_wea =  'string(.//li[contains(@class,"sky")][{}]/p[@class="wea"])'.format(riqi)
    xrl_tem =  'string(.//li[contains(@class,"sky")][{}]/p[@class="tem"])'.format(riqi)
    date = html.xpath(xrl_date).strip()
    weaInfo = html.xpath(xrl_wea).strip()
    temInfo = html.xpath(xrl_tem).strip()
    print(date,weaInfo,temInfo)

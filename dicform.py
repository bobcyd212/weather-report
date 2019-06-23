import re
lst = input('请输入需要划分的城市名:').strip()
p = re.compile(r"[\u4e00-\u9f5a]{2}")
cty = ','.join(p.findall(lst))
print(cty)
provDic={'黑龙江': 101050101, '吉林': 101060101, '辽宁': 101070101, '内蒙古': 101080101, '河北': 101090101, '山西': 101100101,
         '陕西': 101110101,'山东': 101120101, '新疆': 101130101, '西藏': 101140101, '青海': 101150101, '甘肃': 101160101,
         '宁夏': 101170101,'河南': 101180101, '江苏': 101190101, '湖北': 101200101, '浙江': 101210101, '安徽': 101220101,
         '福建': 101230101,'江西':101240101,'湖南': 101250101,'贵州': 101260101,'四川': 101270101,'广东': 101280101,
         '云南': 101290101,'广西': 101300101,'海南': 101310101}
def dicform(lst,num):
    dt = {lst[i]:num+i*100 for i in range(len(lst))}
    return dt

city = input('请手动输入城市名列表:').strip()
cityLst = city.split(',')
province = input('请输入省份').strip()

if province in provDic:
    num = provDic[province]
    gs = dicform(cityLst,num)
    print(gs)





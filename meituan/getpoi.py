# coding=utf-8
import csv
import time
import requests
import json
from getip import getip
import pymysql
from get_cookies import get_cookie

ci = '20'
city = '广州'
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="li123456..", db="lys", charset="utf8")
cursor = db.cursor()


# 区域店铺id ct_Poi cateName抓取，传入参数为区域id
def crow_id(areaid, cookie, uuid, ua):
    id_list = []
    url = 'https://meishi.meituan.com/i/api/channel/deal/list'
    head = {'Host': 'meishi.meituan.com',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'http://meishi.meituan.com/i/?ci=' + ci + '&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
            'User-Agent': ua,
            'Cookie': cookie
            }
    p = {'http': 'http://' + getip()}
    data = {"uuid": uuid, "version": "8.3.3", "platform": 3, "app": "",
            "partner": 126, "riskLevel": 1, "optimusCode": 10,
            "originUrl": "http://meishi.meituan.com/i/?ci=" + ci + "&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1",
            "offset": 0, "limit": 15, "cateId": 17, "lineId": 0, "stationId": 0, "areaId": areaid, "sort": "default",
            "deal_attr_23": "", "deal_attr_24": "", "deal_attr_25": "", "poi_attr_20043": "", "poi_attr_20033": ""}
    r = requests.post(url, headers=head, data=data, proxies=p)
    print(r.text)
    result = json.loads(r.text)
    if "data" not in result:
        return False
    totalcount = result['data']['poiList']['totalCount']  # 获取该分区店铺总数，计算出要翻的页数
    datas = result['data']['poiList']['poiInfos']
    print(len(datas), totalcount)
    for d in datas:
        d_list = ['', '', '', '', '', '']
        d_list[0] = d['name']
        d_list[1] = d['cateName']
        d_list[2] = d['poiid']
        d_list[3] = d['ctPoi']
        d_list[4] = d['areaName']
        d_list[5] = city
        id_list.append(d_list)
    # print(id_list)
    # 将数据保存到本地csv
    # with open('mt_id.csv', 'a', newline='', encoding='gb18030')as f:
    # 	write = csv.writer(f)
    try:
        for i in id_list:
            # write.writerow(i)
            save(i)
        db.commit()
    except Exception as e:
        print("写入发生了异常:", e)
        db.rollback()
    # 开始爬取第2页到最后一页
    offset = 0
    if totalcount > 15:
        totalcount -= 15
        while offset < totalcount:
            id_list = []
            offset += 15
            m = offset / 15 + 1
            print('Page:%d' % m)
            # 构造post请求参数，通过改变offset实现翻页
            data2 = {"uuid": uuid, "version": "8.3.3", "platform": 3, "app": "",
                     "partner": 126, "riskLevel": 1, "optimusCode": 10,
                     "originUrl": "http://meishi.meituan.com/i/?ci=" + ci + "&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1",
                     "offset": offset, "limit": 15, "cateId": 17, "lineId": 0, "stationId": 0, "areaId": areaid,
                     "sort": "default",
                     "deal_attr_23": "", "deal_attr_24": "", "deal_attr_25": "", "poi_attr_20043": "",
                     "poi_attr_20033": ""}
            try:
                r = requests.post(url, headers=head, data=data2, proxies=p)
                print(r.text)
                result = json.loads(r.text)
                if "data" not in result:
                    getip(1)
                    return False
                datas = result['data']['poiList']['poiInfos']
                print(len(datas))
                for d in datas:
                    d_list = ['', '', '', '', '', '']
                    d_list[0] = d['name']
                    d_list[1] = d['cateName']
                    d_list[2] = d['poiid']
                    d_list[3] = d['ctPoi']
                    d_list[4] = d['areaName']
                    d_list[5] = city
                    id_list.append(d_list)
                # 保存到本地
                # with open('mt_id.csv', 'a', newline='', encoding='gb18030')as f:
                # 	write = csv.writer(f)
                # 	for i in id_list:
                # 		write.writerow(i)
                try:
                    for i in id_list:
                        # write.writerow(i)
                        save(i)

                except Exception as e:
                    print("写入发生了异常:", e)
                    db.rollback()
                time.sleep(1)
            except Exception as e:
                print(e)
    return True


def save(res):
    name = res[0]
    category = res[1]
    poiid = res[2]
    ctpoi = res[3]
    areaname = res[4]
    city = res[5]
    sql = """
		insert into meituan(name,category,poiid,ctpoi,areaname,city) values('{}','{}','{}','{}','{}','{}')
	""".format(name, category, poiid, ctpoi, areaname, city)
    cursor.execute(sql)
    db.commit()


if __name__ == '__main__':
    # 直接将html代码中区域的信息复制出来，南澳新区的数据需要处理下，它下面没有分区
    a = {
        "areaObj": {
	"22": [{
		"id": 22,
		"name": "全部",
		"regionName": "天河区",
		"count": 557
	}, {
		"id": 7782,
		"name": "体育中心",
		"regionName": "体育中心",
		"count": 18
	}, {
		"id": 7784,
		"name": "时尚天河",
		"regionName": "时尚天河",
		"count": 10
	}, {
		"id": 7783,
		"name": "天河城/体育西",
		"regionName": "天河城/体育西",
		"count": 28
	}, {
		"id": 1177,
		"name": "燕岭",
		"regionName": "燕岭",
		"count": 12
	}, {
		"id": 1380,
		"name": "天河客运站",
		"regionName": "天河客运站",
		"count": 28
	}, {
		"id": 717,
		"name": "棠下",
		"regionName": "棠下",
		"count": 44
	}, {
		"id": 1164,
		"name": "东圃",
		"regionName": "东圃",
		"count": 95
	}, {
		"id": 1490,
		"name": "龙洞",
		"regionName": "龙洞",
		"count": 53
	}, {
		"id": 714,
		"name": "天河北/广州东站",
		"regionName": "天河北/广州东站",
		"count": 20
	}, {
		"id": 715,
		"name": "岗顶/龙口",
		"regionName": "岗顶/龙口",
		"count": 30
	}, {
		"id": 716,
		"name": "跑马场",
		"regionName": "跑马场",
		"count": 6
	}, {
		"id": 5199,
		"name": "梅花园/天平架",
		"regionName": "梅花园/天平架",
		"count": 5
	}, {
		"id": 7791,
		"name": "花城汇/高德置地",
		"regionName": "花城汇/高德置地",
		"count": 20
	}, {
		"id": 9651,
		"name": "小新塘",
		"regionName": "小新塘",
		"count": 19
	}, {
		"id": 13162,
		"name": "员村",
		"regionName": "员村",
		"count": 19
	}, {
		"id": 13163,
		"name": "华景新城",
		"regionName": "华景新城",
		"count": 7
	}, {
		"id": 13875,
		"name": "正佳广场",
		"regionName": "正佳广场",
		"count": 24
	}, {
		"id": 14319,
		"name": "岑村/火炉山",
		"regionName": "岑村/火炉山",
		"count": 8
	}, {
		"id": 14391,
		"name": "五山",
		"regionName": "五山",
		"count": 9
	}, {
		"id": 14405,
		"name": "车陂",
		"regionName": "车陂",
		"count": 26
	}, {
		"id": 15110,
		"name": "兴盛路/猎德",
		"regionName": "兴盛路/猎德",
		"count": 24
	}, {
		"id": 15112,
		"name": "珠江新城",
		"regionName": "珠江新城",
		"count": 8
	}, {
		"id": 18528,
		"name": "石牌/百脑汇",
		"regionName": "石牌/百脑汇",
		"count": 18
	}, {
		"id": 18529,
		"name": "天河公园/上社",
		"regionName": "天河公园/上社",
		"count": 23
	}],
	"23": [{
		"id": 23,
		"name": "全部",
		"regionName": "越秀区",
		"count": 153
	}, {
		"id": 1065,
		"name": "中山二三路/东山口",
		"regionName": "中山二三路/东山口",
		"count": 14
	}, {
		"id": 1066,
		"name": "五羊新城",
		"regionName": "五羊新城",
		"count": 12
	}, {
		"id": 721,
		"name": "东风中路/越秀公园",
		"regionName": "东风中路/越秀公园",
		"count": 2
	}, {
		"id": 1070,
		"name": "麓湖公园周边",
		"regionName": "麓湖公园周边",
		"count": 7
	}, {
		"id": 722,
		"name": "中山六路",
		"regionName": "中山六路",
		"count": 9
	}, {
		"id": 723,
		"name": "火车站/人民北路",
		"regionName": "火车站/人民北路",
		"count": 4
	}, {
		"id": 1276,
		"name": "海珠广场",
		"regionName": "海珠广场",
		"count": 3
	}, {
		"id": 719,
		"name": "北京路商业区",
		"regionName": "北京路商业区",
		"count": 52
	}, {
		"id": 720,
		"name": "沿江路沿线/二沙岛",
		"regionName": "沿江路沿线/二沙岛",
		"count": 8
	}, {
		"id": 7775,
		"name": "东风东/杨箕",
		"regionName": "东风东/杨箕",
		"count": 7
	}, {
		"id": 19656,
		"name": "瑶台",
		"regionName": "瑶台",
		"count": ""
	}, {
		"id": 19682,
		"name": "建设六马路",
		"regionName": "建设六马路",
		"count": 9
	}, {
		"id": 19683,
		"name": "淘金",
		"regionName": "淘金",
		"count": 3
	}, {
		"id": 19684,
		"name": "黄花岗",
		"regionName": "黄花岗",
		"count": 2
	}, {
		"id": 19685,
		"name": "环市东路/区庄",
		"regionName": "环市东路/区庄",
		"count": 4
	}, {
		"id": 19686,
		"name": "动物园南门",
		"regionName": "动物园南门",
		"count": 2
	}, {
		"id": 21631,
		"name": "东山口/农林下路",
		"regionName": "东山口/农林下路",
		"count": ""
	}, {
		"id": 21642,
		"name": "中华广场",
		"regionName": "中华广场",
		"count": 3
	}],
	"24": [{
		"id": 24,
		"name": "全部",
		"regionName": "海珠区",
		"count": 306
	}, {
		"id": 1494,
		"name": "江南西",
		"regionName": "江南西",
		"count": 36
	}, {
		"id": 727,
		"name": "滨江路沿线",
		"regionName": "滨江路沿线",
		"count": 25
	}, {
		"id": 725,
		"name": "江南大道沿线",
		"regionName": "江南大道沿线",
		"count": 32
	}, {
		"id": 1179,
		"name": "工业大道沿线",
		"regionName": "工业大道沿线",
		"count": 27
	}, {
		"id": 726,
		"name": "新港西路沿线",
		"regionName": "新港西路沿线",
		"count": 16
	}, {
		"id": 1165,
		"name": "客村/赤岗",
		"regionName": "客村/赤岗",
		"count": 60
	}, {
		"id": 1178,
		"name": "东晓南路沿线",
		"regionName": "东晓南路沿线",
		"count": 49
	}, {
		"id": 8961,
		"name": "琶洲",
		"regionName": "琶洲",
		"count": 20
	}],
	"25": [{
		"id": 25,
		"name": "全部",
		"regionName": "荔湾区",
		"count": 163
	}, {
		"id": 1067,
		"name": "芳村",
		"regionName": "芳村",
		"count": 31
	}, {
		"id": 730,
		"name": "中山七八路",
		"regionName": "中山七八路",
		"count": 23
	}, {
		"id": 1971,
		"name": "恒宝广场",
		"regionName": "恒宝广场",
		"count": ""
	}, {
		"id": 731,
		"name": "沙面",
		"regionName": "沙面",
		"count": 6
	}, {
		"id": 729,
		"name": "上下九商业区",
		"regionName": "上下九商业区",
		"count": 58
	}, {
		"id": 7540,
		"name": "康王路",
		"regionName": "康王路",
		"count": 7
	}, {
		"id": 7669,
		"name": "西村西场",
		"regionName": "西村西场",
		"count": 6
	}, {
		"id": 8925,
		"name": "西城都荟",
		"regionName": "西城都荟",
		"count": ""
	}, {
		"id": 23262,
		"name": "滘口",
		"regionName": "滘口",
		"count": ""
	}, {
		"id": 25088,
		"name": "坦尾/河沙",
		"regionName": "坦尾/河沙",
		"count": 3
	}],
	"26": [{
		"id": 26,
		"name": "全部",
		"regionName": "白云区",
		"count": 673
	}, {
		"id": 734,
		"name": "机场路沿线",
		"regionName": "机场路沿线",
		"count": 34
	}, {
		"id": 1180,
		"name": "白云大道沿线",
		"regionName": "白云大道沿线",
		"count": 39
	}, {
		"id": 1493,
		"name": "新市",
		"regionName": "新市",
		"count": 44
	}, {
		"id": 735,
		"name": "三元里",
		"regionName": "三元里",
		"count": 23
	}, {
		"id": 733,
		"name": "广园新村",
		"regionName": "广园新村",
		"count": 10
	}, {
		"id": 1491,
		"name": "同德围",
		"regionName": "同德围",
		"count": 27
	}, {
		"id": 1181,
		"name": "同和/京溪",
		"regionName": "同和/京溪",
		"count": 60
	}, {
		"id": 1492,
		"name": "罗冲围/金沙洲",
		"regionName": "罗冲围/金沙洲",
		"count": 30
	}, {
		"id": 5193,
		"name": "嘉禾/人和",
		"regionName": "嘉禾/人和",
		"count": 40
	}, {
		"id": 5196,
		"name": "永泰",
		"regionName": "永泰",
		"count": 27
	}, {
		"id": 7535,
		"name": "嘉裕太阳城",
		"regionName": "嘉裕太阳城",
		"count": 5
	}, {
		"id": 7536,
		"name": "五号停机坪",
		"regionName": "五号停机坪",
		"count": 7
	}, {
		"id": 7537,
		"name": "黄石",
		"regionName": "黄石",
		"count": 23
	}, {
		"id": 7539,
		"name": "万达广场",
		"regionName": "万达广场",
		"count": 11
	}, {
		"id": 15984,
		"name": "黄边",
		"regionName": "黄边",
		"count": 13
	}, {
		"id": 16022,
		"name": "石井",
		"regionName": "石井",
		"count": 40
	}, {
		"id": 16091,
		"name": "钟落潭",
		"regionName": "钟落潭",
		"count": 16
	}, {
		"id": 17078,
		"name": "江高",
		"regionName": "江高",
		"count": 23
	}, {
		"id": 17256,
		"name": "均禾",
		"regionName": "均禾",
		"count": 46
	}, {
		"id": 18064,
		"name": "太和镇",
		"regionName": "太和镇",
		"count": 46
	}, {
		"id": 25072,
		"name": "白云绿地中心",
		"regionName": "白云绿地中心",
		"count": 1
	}, {
		"id": 26659,
		"name": "凯德广场",
		"regionName": "凯德广场",
		"count": 6
	}, {
		"id": 27976,
		"name": "白云国际机场",
		"regionName": "白云国际机场",
		"count": ""
	}, {
		"id": 37939,
		"name": "嘉禾望岗",
		"regionName": "嘉禾望岗",
		"count": 37
	}],
	"274": [{
		"id": 274,
		"name": "全部",
		"regionName": "番禺区",
		"count": 513
	}, {
		"id": 1182,
		"name": "市桥",
		"regionName": "市桥",
		"count": 74
	}, {
		"id": 9023,
		"name": "市桥南",
		"regionName": "市桥南",
		"count": 22
	}, {
		"id": 1461,
		"name": "番禺广场",
		"regionName": "番禺广场",
		"count": 28
	}, {
		"id": 1184,
		"name": "大学城",
		"regionName": "大学城",
		"count": 40
	}, {
		"id": 9024,
		"name": "沙湾镇",
		"regionName": "沙湾镇",
		"count": 15
	}, {
		"id": 1183,
		"name": "大石",
		"regionName": "大石",
		"count": 65
	}, {
		"id": 5187,
		"name": "洛溪",
		"regionName": "洛溪",
		"count": 41
	}, {
		"id": 7541,
		"name": "长隆/南村/万达",
		"regionName": "长隆/南村/万达",
		"count": 88
	}, {
		"id": 7542,
		"name": "钟村",
		"regionName": "钟村",
		"count": 56
	}, {
		"id": 9276,
		"name": "石基",
		"regionName": "石基",
		"count": 26
	}, {
		"id": 14179,
		"name": "石楼",
		"regionName": "石楼",
		"count": 16
	}, {
		"id": 18905,
		"name": "南浦",
		"regionName": "南浦",
		"count": 15
	}, {
		"id": 23275,
		"name": "广州南站",
		"regionName": "广州南站",
		"count": 2
	}],
	"737": [{
		"id": 737,
		"name": "全部",
		"regionName": "黄埔区",
		"count": 169
	}, {
		"id": 8029,
		"name": "大沙地",
		"regionName": "大沙地",
		"count": 38
	}, {
		"id": 8030,
		"name": "文冲",
		"regionName": "文冲",
		"count": 10
	}, {
		"id": 8031,
		"name": "鱼珠",
		"regionName": "鱼珠",
		"count": 1
	}, {
		"id": 8032,
		"name": "科学城/萝岗高德汇",
		"regionName": "科学城/萝岗高德汇",
		"count": 5
	}, {
		"id": 8033,
		"name": "中心城",
		"regionName": "中心城",
		"count": 24
	}, {
		"id": 8034,
		"name": "开发区东区",
		"regionName": "开发区东区",
		"count": 28
	}, {
		"id": 8035,
		"name": "开发区西区",
		"regionName": "开发区西区",
		"count": 2
	}, {
		"id": 8797,
		"name": "生活区/南岗",
		"regionName": "生活区/南岗",
		"count": 16
	}, {
		"id": 17692,
		"name": "长洲岛",
		"regionName": "长洲岛",
		"count": 3
	}, {
		"id": 22706,
		"name": "万达广场",
		"regionName": "万达广场",
		"count": 16
	}, {
		"id": 38999,
		"name": "联和联世广场",
		"regionName": "联和联世广场",
		"count": 1
	}],
	"738": [{
		"id": 738,
		"name": "全部",
		"regionName": "花都区",
		"count": 213
	}, {
		"id": 5882,
		"name": "新世纪广场",
		"regionName": "新世纪广场",
		"count": 9
	}, {
		"id": 5883,
		"name": "梯面",
		"regionName": "梯面",
		"count": ""
	}, {
		"id": 5884,
		"name": "花山",
		"regionName": "花山",
		"count": 7
	}, {
		"id": 5885,
		"name": "炭步",
		"regionName": "炭步",
		"count": ""
	}, {
		"id": 5886,
		"name": "赤坭",
		"regionName": "赤坭",
		"count": ""
	}, {
		"id": 5887,
		"name": "狮岭",
		"regionName": "狮岭",
		"count": 27
	}, {
		"id": 5888,
		"name": "花东",
		"regionName": "花东",
		"count": 1
	}, {
		"id": 5889,
		"name": "雅瑶",
		"regionName": "雅瑶",
		"count": 1
	}, {
		"id": 13356,
		"name": "北站/建设路",
		"regionName": "北站/建设路",
		"count": 7
	}, {
		"id": 13357,
		"name": "花都广场",
		"regionName": "花都广场",
		"count": 22
	}, {
		"id": 13362,
		"name": "大润发",
		"regionName": "大润发",
		"count": 30
	}, {
		"id": 13715,
		"name": "建设北路",
		"regionName": "建设北路",
		"count": 22
	}, {
		"id": 13904,
		"name": "花都体育场",
		"regionName": "花都体育场",
		"count": 13
	}, {
		"id": 13905,
		"name": "秀全公园",
		"regionName": "秀全公园",
		"count": 1
	}, {
		"id": 14053,
		"name": "饮食风情街",
		"regionName": "饮食风情街",
		"count": 7
	}, {
		"id": 16090,
		"name": "白云国际机场",
		"regionName": "白云国际机场",
		"count": 14
	}, {
		"id": 23248,
		"name": "莲塘",
		"regionName": "莲塘",
		"count": ""
	}, {
		"id": 36192,
		"name": "雅居乐锦城/保利花城",
		"regionName": "雅居乐锦城/保利花城",
		"count": 5
	}, {
		"id": 36194,
		"name": "骏壹万邦",
		"regionName": "骏壹万邦",
		"count": 5
	}, {
		"id": 39346,
		"name": "马溪",
		"regionName": "马溪",
		"count": ""
	}, {
		"id": 39659,
		"name": "美林湖",
		"regionName": "美林湖",
		"count": ""
	}],
	"739": [{
		"id": 739,
		"name": "全部",
		"regionName": "增城市",
		"count": 166
	}, {
		"id": 13071,
		"name": "万达广场",
		"regionName": "万达广场",
		"count": 22
	}, {
		"id": 9181,
		"name": "太阳城/凯旋门",
		"regionName": "太阳城/凯旋门",
		"count": 17
	}, {
		"id": 7718,
		"name": "新塘大润发/新好景",
		"regionName": "新塘大润发/新好景",
		"count": 21
	}, {
		"id": 9178,
		"name": "东汇城/人人乐",
		"regionName": "东汇城/人人乐",
		"count": 9
	}, {
		"id": 9180,
		"name": "荔城挂绿/泰富广场",
		"regionName": "荔城挂绿/泰富广场",
		"count": 1
	}, {
		"id": 9504,
		"name": "白水寨/派潭",
		"regionName": "白水寨/派潭",
		"count": 1
	}, {
		"id": 13070,
		"name": "新塘广场",
		"regionName": "新塘广场",
		"count": 8
	}, {
		"id": 13113,
		"name": "凤凰城",
		"regionName": "凤凰城",
		"count": 12
	}, {
		"id": 16723,
		"name": "佰乐广场",
		"regionName": "佰乐广场",
		"count": 1
	}, {
		"id": 27311,
		"name": "朱村镇",
		"regionName": "朱村镇",
		"count": 1
	}, {
		"id": 27313,
		"name": "中新镇",
		"regionName": "中新镇",
		"count": 7
	}, {
		"id": 27483,
		"name": "沙埔镇",
		"regionName": "沙埔镇",
		"count": 4
	}, {
		"id": 27485,
		"name": "永和镇",
		"regionName": "永和镇",
		"count": 16
	}, {
		"id": 37286,
		"name": "合汇城广场",
		"regionName": "合汇城广场",
		"count": 1
	}, {
		"id": 38530,
		"name": "挂绿广场/泰富广场",
		"regionName": "挂绿广场/泰富广场",
		"count": 11
	}, {
		"id": 39909,
		"name": "敏捷锦绣广场",
		"regionName": "敏捷锦绣广场",
		"count": 4
	}],
	"740": [{
		"id": 740,
		"name": "全部",
		"regionName": "从化市",
		"count": 67
	}, {
		"id": 13069,
		"name": "温泉镇",
		"regionName": "温泉镇",
		"count": 4
	}, {
		"id": 13150,
		"name": "街口/新世纪广场",
		"regionName": "街口/新世纪广场",
		"count": 21
	}, {
		"id": 13153,
		"name": "江埔",
		"regionName": "江埔",
		"count": 1
	}, {
		"id": 13157,
		"name": "欣荣宏广场",
		"regionName": "欣荣宏广场",
		"count": 21
	}, {
		"id": 15240,
		"name": "商贸城",
		"regionName": "商贸城",
		"count": 5
	}, {
		"id": 15242,
		"name": "碧水湾/碧水新村",
		"regionName": "碧水湾/碧水新村",
		"count": ""
	}, {
		"id": 16273,
		"name": "太平镇/太平商业街",
		"regionName": "太平镇/太平商业街",
		"count": 5
	}, {
		"id": 17630,
		"name": "旺城",
		"regionName": "旺城",
		"count": 2
	}, {
		"id": 23258,
		"name": "溪头村",
		"regionName": "溪头村",
		"count": ""
	}, {
		"id": 25818,
		"name": "鳌头",
		"regionName": "鳌头",
		"count": ""
	}, {
		"id": 26381,
		"name": "良口镇",
		"regionName": "良口镇",
		"count": ""
	}],
	"1068": [{
		"id": 1068,
		"name": "全部",
		"regionName": "南沙区",
		"count": 76
	}, {
		"id": 13845,
		"name": "黄阁镇",
		"regionName": "黄阁镇",
		"count": 4
	}, {
		"id": 13848,
		"name": "金洲商业街",
		"regionName": "金洲商业街",
		"count": 3
	}, {
		"id": 13850,
		"name": "华汇广场",
		"regionName": "华汇广场",
		"count": 7
	}, {
		"id": 13853,
		"name": "板头",
		"regionName": "板头",
		"count": 3
	}, {
		"id": 15265,
		"name": "东涌镇",
		"regionName": "东涌镇",
		"count": 7
	}, {
		"id": 15267,
		"name": "大岗",
		"regionName": "大岗",
		"count": 11
	}, {
		"id": 15269,
		"name": "珠江旧镇",
		"regionName": "珠江旧镇",
		"count": 3
	}, {
		"id": 18624,
		"name": "百万葵园/十九涌",
		"regionName": "百万葵园/十九涌",
		"count": ""
	}, {
		"id": 18626,
		"name": "大涌",
		"regionName": "大涌",
		"count": ""
	}, {
		"id": 18628,
		"name": "榄核镇",
		"regionName": "榄核镇",
		"count": 2
	}, {
		"id": 18630,
		"name": "鱼窝头",
		"regionName": "鱼窝头",
		"count": 4
	}, {
		"id": 19803,
		"name": "万顷沙镇",
		"regionName": "万顷沙镇",
		"count": 3
	}, {
		"id": 25709,
		"name": "南沙万达广场",
		"regionName": "南沙万达广场",
		"count": 16
	}]
}

    }
    res = get_cookie()
    cookie = res[1]
    uuid = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}["uuid"]
    ua = res[2]
    datas = a['areaObj']
    b = datas.values()
    area_list = []
    for data in b:
        for d in data[1:]:
            area_list.append(d)  # 将每个区域信息保存到列表，元素是字典
    l = 0
    # print(len(area_list))
    old = time.time()

    for i in area_list:
        # print(i)

        l += 1
        print('开始抓取第%d个区域：' % l, i['regionName'], '店铺总数：', i['count'])
        # if i['regionName'] == "回龙观":
        #     print(area_list.index(i))
        try:
            # pass
            aa = crow_id(i['id'], cookie, uuid, ua)
            if aa:
                now = time.time() - old
                print(i['name'], '抓取完成！', '时间:%d' % now)
            else:
                res = get_cookie(1)
                cookie = res[1]
                uuid = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}["uuid"]
                ua = res[2]
        except Exception as e:
            print(e)

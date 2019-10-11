import requests
from fake_useragent import UserAgent
ua =UserAgent()
url ="https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
headers ={
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'referer':'https://qun.qq.com/member.html',
    'cache-control':'no-cache',
    'content-length':'49',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent':ua.random,
    'origin':'https://qun.qq.com',
    'pragma':'no-cache',
    'x-requested-with':'XMLHttpRequest'
}
cookie ='RK=/2hJnxD8S1; ptcz=3cd088b9d9033403e5dde1b90f49b20b3c6b789be4023a28c9fc64f7081e8dd6; UM_distinctid=16b926b66d6494-0557faecb664d-43450521-15f900-16b926b66d73f6; UM_distinctid=16b9861d7e1aa-08767b0ed8d4f3-43450521-15f900-16b9861d7e22fa; pgv_pvid=3614164490; pgv_pvi=8595558400; _gcl_au=1.1.1908180433.1562208075; _ga=GA1.2.1122246799.1562208076; pt_235db4a7=uid=utOGnoApX5LEb3Iy70n/Ug&nid=1&vid=jfcICKfEyxsA5FfLth97MA&vn=1&pvn=1&sact=1562208075551&to_flag=0&pl=0KzaISwJA-wYoyVB1nkjpQ*pt*1562208075551; ied_qq=o1462063555; uin=o1462063555; p_uin=o1462063555; traceid=588d518693; pgv_si=s6327396352; _qpsvr_localtk=0.30455141350287995; ptisp=ctc; pgv_info=ssid=s7654831872; ts_last=qun.qq.com/member.html; ts_uid=8027596625; CNZZDATA1272960370=66749414-1561526372-https%253A%252F%252Fqun.qq.com%252F%7C1564047500; skey=@upI2QWDIf; pt4_token=oJpR-YPP5q0ep6Iq53eGFWmwmb0MJON5HFGl66VPfPo_; p_skey=z5ImpNyCBnpZg30zVQI*3J9RzbxwF5w8OLcWgW5--7I_; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin'
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
data = {
    'gc':'176483233',
    'st':'50',
    'end':'70',
    'sort':'0',
    'bkn':'1072091840'
}

res = requests.post(url,headers=headers,cookies=cookies,data=data)
print(res.text)
# json=eval(res.text)
# for i in json["mems"]:
#     print(i["uin"])
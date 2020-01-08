def make(header_str=''):

    headers=header_str.split('\n')
    headers_dict={i.split(':')[0].strip():i.split(':')[1].strip() for i in headers}
    return headers_dict
if __name__=="__main__":
    aa = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: UM_distinctid=16f8461957873-038e695ce3b107-43450521-1aeaa0-16f846195795d6; CNZZDATA1274292051=1168808616-1561524422-%7C1578470362
    Host: www.xd0.com
    Pragma: no-cache
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"""
    print(make(aa))
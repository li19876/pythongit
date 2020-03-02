def make(header_str=''):

    headers=header_str.split('\n')
    # return headers
    headers_dict={i.split(': ')[0].strip():i.split(': ')[1].strip() for i in headers}
    return headers_dict
if __name__=="__main__":
    header = """:authority: szftbz.1688.com
:method: GET
:path: /fragment/contactinfo.htm?page_type=contactinfo&apps=%5B%7B%22appName%22%3A%22winport_public_dialog%22%7D%2C%7B%22appName%22%3A%22couponLayer%22%7D%2C%7B%22appName%22%3A%22collectWinport%22%7D%2C%7B%22app_key%22%3A%22323eaa73b6824fe79311ee945897f6f0%22%2C%22appName%22%3A%22supplierInfoSmall%22%2C%22segment_id%22%3A%22site_content%22%2C%22layout_type%22%3A%22s5m0%22%2C%22region_type%22%3A%22small%22%7D%2C%7B%22appName%22%3A%22collectWinport%22%2C%22segment_id%22%3A%22site_content%22%2C%22layout_type%22%3A%22s5m0%22%2C%22region_type%22%3A%22small%22%7D%5D&_=1579074637817
:scheme: https
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: cna=0/WZFcFaezkCAWovfr4ENWUt; ali_ab=106.47.78.72.1562208840496.4; ali_apache_id=11.186.201.1.1562208857741.702363.9; lid=tb76332162; cookie2=69afb1b3eacec698b700af3d3498e1b3; hng=CN%7Czh-CN%7CCNY%7C156; t=5eddbd8e9b6a418ad0e05addcfb94c53; _tb_token_=e354181795816; __cn_logon__=false; alicnweb=homeIdttS%3D47202860487398943810735359923784582780%7Ctouch_tb_at%3D1579072552312%7ChomeIdttSAction%3Dtrue; UM_distinctid=16fa80f79ab4c8-03c5dc0cd7d548-43450521-1aeaa0-16fa80f79acc6e; taklid=fd4ae90a549a404f9726d73d0539aa51; _csrf_token=1579072581234; ad_prefer="2020/01/15 15:17:32"; h_keys="%u673a%u68b0"; ali_beacon_id=106.47.84.167.1579072708597.419715.1; isg=BNPTDQnyieTVAEYzH2hVSLbRYlf9iGdKbx_bJoXwnvIpBPOmDVy_m79dPnRqpL9C; l=cBSsvxSVqPwR6IB0BOfwZuI8av_9wIRb4sPzw4_gQICP_LCW511PWZDeQITXCnGVp64HR3umks4gBeYBqBBFb0IqlNDEb
pragma: no-cache
referer: https://szftbz.1688.com/page/contactinfo.htm?spm=a2615.2177701.autotrace-topNav.8.17c952f2KKpJ4o
user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
x-requested-with: XMLHttpRequest"""
    print(make(header))
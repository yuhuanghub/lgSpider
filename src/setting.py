# -*- coding: utf-8 -*-

# headers
headers = {
    'Host': 'www.lagou.com',
    'Connection': 'keep-alive',
    'Content-Length': '23',
    'Origin': 'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
    'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

# cookies
cookies = {' gate_login_token': '6db827717ef052067b99f6d4693bf91337377d4a1867c8622ae0a3d491368eb2', ' TG-TRACK-CODE': 'index_navigation', ' showExpriedIndex': '1', ' SEARCH_ID': 'eb191f9b6129463094dcd2f625b2a956', ' hasDeliver': '0', ' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1536583850', ' _putrc': 'A423713BBCF0A43C123F89F2B170EADC', ' index_location_city': '%E6%88%90%E9%83%BD', ' LGUID': '20180825225323-9d290488-a876-11e8-a55c-525400f775ce', ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1536418766,1536494658,1536583841', ' login': 'true', ' PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPncXC2Dd1e4_G556Am-_Gdcc9oqf1_peSZCCq8-YZ_i%26wd%3D%26eqid%3D88cae80800001049000000055b9668aa', 'user_trace_token': '20180825225316-8f43b66c-d767-4dac-b8e0-67c9c99e88c7', ' PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F', ' LG_LOGIN_USER_ID': 'cf16a7efc3312e80f1a4c7a42972081fd5b55a45a0c99f402dad361c4627e44b', ' LGSID': '20180910205054-27a4d8c8-b4f8-11e8-b62b-5254005c3644', ' unick': '%E5%96%BB%E9%BB%84', ' JSESSIONID': 'ABAAABAAADEAAFI7492B7A1F7A1356227E9875142185DF1', ' showExpriedMyPublish': '1', ' LGRID': '20180910205103-2d4b3cca-b4f8-11e8-8d51-525400f775ce', ' _gat': '1', ' PRE_UTM': '', ' _gid': 'GA1.2.359501752.1536583840', ' _ga': 'GA1.2.192130662.1535208794', ' showExpriedCompanyHome': '1', ' PRE_HOST': 'www.baidu.com'}



# IP池
# 0(pay) or 1(free) or 2(None)
TAGIP = 0

# IP
IP = []

# UA
UA = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0;\
       Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; 360SE)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
      'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 \
      (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) \
      Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) \
      Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; \
      .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
      .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',

      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) \
      Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0',

      'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) \
      Version/5.0.2 Mobile/8C148 Safari/6533.18.5',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)']

CITY = ['成都']
POSITION = ['Java']

SCHOOL = {'gx':'全职', 'needAddtionalResult': 'false', 'isSchoolJob': '1', 'xl':'大专'}
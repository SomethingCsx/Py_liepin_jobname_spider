import requests
import time

key=input('输入你想搜索的岗位')
for i in range(0,10):
    url='https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "content-length": "505",
        "content-type": "application/json;charset=UTF-8",
        "cookie": "XSRF-TOKEN=6SZcBGRYQx6i2WIHtx3apQ; __gc_id=a49b5150eaf74d5c8077d93047cebb08; _ga=GA1.1.185437421.1776767561; __uuid=1776767560822.07; __sessionId=1776767560844.92; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1776767561; HMACCOUNT=D254B8FDE0AFDF71; acw_tc=7b3975b817767694564028565e88c771505bad6bf4518f364841910922b5b1; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1776769460; __session_seq=20; __tlg_event_seq=101; _ga_54YTJKWN86=GS2.1.s1776767560$o1$g1$t1776769713$j55$l0$h0",
        "host": "api-c.liepin.com",
        "origin": "https://www.liepin.com",
        "referer": "https://www.liepin.com/",
        "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "x-client-type": "web",
        "x-fscp-bi-stat": '{"location":"https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=java&suggestTag=&workYearCode=0&compId=&compName=&compTag=&industry=&salaryCode=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&ckId=kkip4qej05c02oxyh0tjvxx2rpmg4o69&skId=kkip4qej05c02oxyh0tjvxx2rpmg4o69&fkId=kkip4qej05c02oxyh0tjvxx2rpmg4o69&scene=input&sfrom=search_job_pc&suggestId="}',
        "x-fscp-fe-version": "",
        "x-fscp-std-info": '{"client_id": "40108"}',
        "x-fscp-trace-id": "9dac0987-7999-4e0a-ae08-40b8e9528977",
        "x-fscp-version": "1.1",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "6SZcBGRYQx6i2WIHtx3apQ"
    }
    data = {
        'data': {
            'mainSearchPcConditionForm': {
                'city': '410',
                'dq': '410',
                'currentPage': i,
                'pageSize': 40,
                'key': key,
                'workYearCode': '0'
            },
            'passThroughForm': {
                'scene': 'input',
                'skId': '',
                'fkId': '',
                'ckId': '7zelke07j6isq6mrvdk8kdohz400uswb'
            },
        },
    }
    res = requests.post(url=url, headers=headers, json=data)
    rest = res.json()
    for j in rest['data']['data']['jobCardList']:
        print(j['job']['title'])
        time.sleep(1)
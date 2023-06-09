REQ_OPTIONS = {
    "wexin_request_qrcode":{
        "req_url": "https://open.weixin.qq.com/connect/qrconnect?appid=wx4411fdc32430ce58&scope=snsapi_login&redirect_uri=https%3A%2F%2Faqy.lgb360.com%2F%23%2Flogin&state=123456",
        "req_type": "get",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": False,
        "header":{
            "Host": "open.weixin.qq.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-dest": "iframe",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "wexin_request_uuid":{
        "req_url": "https://open.weixin.qq.com",
        "req_type": "get",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": False,
        "not_decode": True,
        "header":{
            "Host": "open.weixin.qq.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-dest": "image",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://open.weixin.qq.com/connect/qrconnect?appid=wx4411fdc32430ce58&scope=snsapi_login&redirect_uri=https%3A%2F%2Faqy.lgb360.com%2F%23%2Flogin&state=123456"
        },
    },
    "wexin_confirm_request_uuid":{
        "req_url": "https://open.weixin.qq.com/connect/confirm?uuid=",
    },
    "wexin_poll_confirm_request_uuid":{
        "req_url": "https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid=",
        "req_type": "get",
        "re_try": 1,
        "re_time": 1,
        "s_time": 0.1,
        "is_json": False,
        "not_decode": False,
        "header":{
            "Host": "lp.open.weixin.qq.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-dest": "script",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://open.weixin.qq.com/"
        },
    },
    "login":{
        "req_url": "https://aqy.lgb360.com/aqy/wechat/accountLogin?code=",
        "req_url_suffix": "&type=3",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "not_decode": False,
        "header":{
            "Host": "aqy.lgb360.com",
            "Origin": "https://aqy.lgb360.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "competition":{
        "req_url": "https://aqy.lgb360.com/aqy/regist/competition",
        "req_type": "get",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "not_decode": False,
        "header":{
            "Host": "aqy.lgb360.com",
            "Origin": "https://aqy.lgb360.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "token": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "memberId": "",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "start":{
        "req_url": "https://aqy.lgb360.com/aqy/ques/startCompetition",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "not_decode": False,
        "header":{
            "Host": "aqy.lgb360.com",
            "Origin": "https://aqy.lgb360.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "token": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "memberId": "",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "answer": {
        "req_url": "https://aqy.lgb360.com/aqy/ques/answerQues",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "not_decode": False,
        "header":{
            "Host": "aqy.lgb360.com",
            "Origin": "https://aqy.lgb360.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "token": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "memberId": "",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "submitcompetition": {  # 答题结束提交接口
        "req_url": "https://aqy.lgb360.com/aqy/ques/submitCompetition",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "header":{
            "Host": "aqy.lgb360.com",
            "Origin": "https://aqy.lgb360.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "token": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "memberId": "",
            "Connection": "Keep-Alive",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ko;q=0.6",
            "Referer": "https://aqy.lgb360.com/"
        },
    },
    "getdrawsurplusnum": {  # 查询抽奖次数接口
        "req_url": "https://aqy-app.lgb360.com/aqy/prize/getDrawSurplusNum",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "header": {
            "Host": "aqy-app.lgb360.com",
            "accept": "application/json, text/plain, */*",
            "token": "",
            "User-Agent": "",
            "memberId": "",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://aqy-app.lgb360.com",
            "x-requested-with": "com.hxak.liangongbao",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        },
    },
     "drawprize": {  # 自动抽奖
        "req_url": "https://aqy-app.lgb360.com/aqy/prize/drawPrize",
        "req_type": "post",
        "re_try": 10,
        "re_time": 3,
        "s_time": 0.1,
        "is_json": True,
        "header": {
            "Host": "aqy-app.lgb360.com",
            "accept": "application/json, text/plain, */*",
            "token": "",
            "User-Agent": "",
            "memberId": "",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://aqy-app.lgb360.com",
            "x-requested-with": "com.hxak.liangongbao",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        },
    }
}

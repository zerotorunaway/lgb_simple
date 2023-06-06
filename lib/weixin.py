#coding:utf8
import json
import re
import copy
import time
from lib.req_url import REQ_OPTIONS
from PIL import Image
from io import BytesIO

def wx_login(http_client):
    res = http_client.send(REQ_OPTIONS['wexin_request_qrcode'])  #获取二维码src
    qrcode_href = re.findall(r'web_qrcode_img" src="/(.*?)"/>',res)[0]
    qrcode_uuid = qrcode_href.split('/')[-1]
    qrcode_req_option = copy.deepcopy(REQ_OPTIONS['wexin_request_uuid'])
    qrcode_req_option['req_url'] += '/' + qrcode_href
    res = http_client.send(qrcode_req_option)
    image = Image.open(BytesIO(res))
    image.show()
    wexin_poll_confirm_request_uuid_url = copy.deepcopy(REQ_OPTIONS['wexin_poll_confirm_request_uuid'])
    for _ in range(100):
        time.sleep(1)
        current_milli_time = lambda: str(int(round(time.time() * 1000)))
        wexin_poll_confirm_request_uuid_url['req_url'] += qrcode_uuid + '&_=' + current_milli_time()
        res = http_client.send(wexin_poll_confirm_request_uuid_url)
        if not isinstance(res, str) or 'window.wx_errcode=405;window.wx_code=' not in res: continue
        wx_code = re.findall("wx_code='(.*?)'",res)[0]
        scan_qrcode_sucess = True
        print('扫描登录成功')
        break
    assert scan_qrcode_sucess, "微信扫码超时,退出登录"
    login_option = copy.deepcopy(REQ_OPTIONS['login'])
    login_option['req_url'] += wx_code + login_option['req_url_suffix']
    token_dict = http_client.send(login_option)
    return token_dict


def record_users(token_dict):
    #持久化写入     
    token = token_dict.get("data").get("uidtok")
    memberId = token_dict.get("data").get("unionId")
    user_info = {'USER': memberId, 'PWD': token}
    with open('config/record_users.json', 'r') as f:
        text = ''.join(f.readlines())
    name  = input("请输答题人名字")
    if text == '':
        data = {user_info['USER']:[user_info['PWD'],name]}
        with open('config/record_users.json', 'w') as f:
            f.write(json.dumps(data))
    else:
        user_data = json.loads(text)
        user_data[user_info['USER']] = ['',name]
        user_data[user_info['USER']][0] = user_info["PWD"]
        data = json.dumps(user_data)
        with open('config/record_users.json', 'w') as f:
            f.write(data)
        


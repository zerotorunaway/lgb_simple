from lib.weixin import *
from lib.lgb import *
from lib.http_utils import HTTPClient
import json

def get_users():
    with open('config/record_users.json', 'rb') as f:
        text = b''.join(f.readlines()).decode('utf8')
        if text == '':
            return []
        else:
            user_data = json.loads(text)
            users = []
            for user in user_data.keys():
                users.append({
                    'USER':user, 
                    'PWD': user_data[user][0],
                    'NAME':user_data[user][1]
                })
    return users


if __name__== "__main__":
    http_client = HTTPClient()
    print("请选择方式:\n1.更新用户扫码信息\n2.直接执行")
    choice = input()
    users = get_users()
    if choice == '1' or users == []:
        token_dict = wx_login(http_client)
        status = token_dict.get("status")
        if status == 20000:
            record_users(token_dict)
        else:
            print("微信登录失败！")
    else:
        for user in users:
            logger.info(user['NAME'])
            http_client = HTTPClient()
            http_client.token = user['PWD']
            http_client.memberId = user['USER']
            result_dict = start_paper(http_client)
            if result_dict == False:
                try:
                    auto_lottery(http_client)
                except:
                    pass
                continue
            test_paper(http_client,result_dict)
            auto_lottery(http_client)


    

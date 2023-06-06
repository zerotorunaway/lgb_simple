import requests,re
def get_question_bank():
    res = {}
    url = "https://bitbucket.org/liangongbao/lgb/src/master/content"
    req = requests.get(url)
    version = re.findall(r'"https://bitbucket.org/liangongbao/lgb/commits/(.*?)"',req.content.decode('utf8'))[0]
    url = f"https://bitbucket.org/!api/2.0/repositories/liangongbao/lgb/src/{version}/content"
    question_text= requests.get(url).content.decode('utf8')
    question_list = question_text.split('\n')[2:]
    for question in question_list:
        t_a = question.split('。',1)
        title = t_a[0] + '。'
        answer = t_a[1]
        title = title.replace('题目:','')
        res[title] = answer
    return res
QUESTION_BANK  = get_question_bank()
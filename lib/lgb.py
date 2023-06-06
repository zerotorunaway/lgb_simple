import time,random,json
from lib.req_url import REQ_OPTIONS
from lib.get_question_bank import QUESTION_BANK
from loguru import logger
ANSWER_QUES_NUM = 0 
MIN_TIME = 1
MAX_TIME = 3
logger.add('lgb.log')

def find_anwser(result_dict):
    if "data" in result_dict.keys():
        content = result_dict["data"]["ques"]["content"]
        """"
        {'result': {'msg': '成功'}, 'data': {'ques': {'quesNo': 1, 'options': ['对', '错'], 'quesTypeStr': '判断题', 'quesId': 'OCxF4aqWZF-eDCwY', 'content': '在作业过程中职工对于用人单位任何指挥都应无条件服从。'}, 'remainder': 13}}
        """
        try:
            answer = QUESTION_BANK[content].split(',')
        except:
            logger.debug(content+'题库缺失，请手动答题')
            return None,content
        return answer,content
    else:
        return '',''

def start_paper(http_client):
    result_dict = http_client.send(REQ_OPTIONS['competition'])
    if result_dict.get('result').get('code') == 100:
        logger.debug(http_client.memberId+'失效,请重新扫描登录')
        return False
    if 'isAnswered' in result_dict.get('data'):
        logger.info(http_client.memberId+"每天只能挑战一次哦~")
        return False
    memberId = http_client.memberId
    userCode = result_dict['data']['userCode']
    points = result_dict['data']['points']
    logger.info(f"wxid:{memberId},userid:{userCode},points:{points}")
    result_dict = http_client.send(REQ_OPTIONS['start'], data={})
    msg = result_dict.get("result").get("msg")
    code = result_dict.get("result").get("code")
    if msg == "您今日挑战已完成，明天再来挑战吧！" or code == 9:
        print("您今日挑战已完成，明天再来挑战吧！")
        return False
    return result_dict

def submit_paper(http_client):
    result_dict = http_client.send(REQ_OPTIONS['submitcompetition'], data={})
    logger.info('本次答对题目数：'+ str(result_dict.get('data').get("correctNum")))

def test_paper(http_client,result_dict):
    while(1):
        data = result_dict.get("data")
        if data:
            ques = data.get("ques")
            if not ques:
                print("<------恭喜您，满分！！！------>")
                submit_paper(http_client)
                break
            else:
                quesId = ques.get("quesId")
                answerOptions = ques.get("options")
        else:
            print("======程序执行结束======")
            submit_paper(http_client)
            break
        answer  = find_anwser(result_dict)[0]
        content = find_anwser(result_dict)[1]
        if answer:
            data = {"quesId": "%s" % quesId, "answerOptions": answer}
        else:
            show_subject(content,answerOptions)
            while(1):
                choice = input("请输入正确选项：\n ")
                if choice not in ["1",'2','3','4','12','13','14','23','24','34','123','124','134','234','1234']:
                    continue
                else:
                    break
            answer_data = return_answer(choice,answerOptions)
            data = {"quesId": "%s" % quesId, "answerOptions": ["%s" % answer_data]}
            logger.debug("<--randomAnswer-->", answerOptions[0])
        result_dict = http_client.send(
            REQ_OPTIONS['answer'], data=json.dumps(data))
        time.sleep(random.randint(MIN_TIME, MAX_TIME))

def auto_lottery(http_client):
    result_dict = http_client.send(
        REQ_OPTIONS['getdrawsurplusnum'], data={})
    surplusNum = int(result_dict.get('data').get('surplusNum'))
    if surplusNum == 0:
        logger.info("您的抽奖次数已用完！")
    for i in range(surplusNum):
        result_dict = http_client.send(REQ_OPTIONS['drawprize'], data={})
        data = result_dict.get('data')
        if not data:  # 无数据
            logger.info("您的抽奖次数已用完！")
            return
        prizeName = data.get('prizeName')
        logger.info('第%s次抽奖获得:' % (i+1)+ str(prizeName))
        time.sleep(random.randint(MIN_TIME, MAX_TIME))


def return_answer( answer_match, answerOptions):
    tmp = []
    for v in answer_match:
        tmp.append(answerOptions[v-1])
    return tmp

def show_subject(content,answerOptions):
    logger.warning(content)
    for i in range(len(answerOptions)):
        logger.warning(f"{i+1}、{answerOptions[i]}")



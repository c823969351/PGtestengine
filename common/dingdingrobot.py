from dingtalkchatbot.chatbot import DingtalkChatbot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f59535ecc4bd8647c71290957e49efa3b8434ed6f5b3117f617b065d5a6bb03a'
secret = '***'

dingding = DingtalkChatbot(webhook,secret=secret,pc_slide=True,fail_notice=True)

<<<<<<< HEAD
dingding .send_text('PG测试机器人',is_at_all=False)
=======
dingding .send_text('猜猜我是谁',is_at_all=False)
>>>>>>> 5684c234810a919d880e217e418679c411e7d6d9

from dingtalkchatbot.chatbot import DingtalkChatbot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f59535ecc4bd8647c71290957e49efa3b8434ed6f5b3117f617b065d5a6bb03a'
secret = 'SEC4d9eea43714470401d9d926412188201f39e027f92b8c16caf8a82e2e61fe26f'

dingding = DingtalkChatbot(webhook,secret=secret,pc_slide=True,fail_notice=True)

dingding .send_text('猜猜我是谁',is_at_all=False)
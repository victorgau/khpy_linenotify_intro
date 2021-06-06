from settings import LINE_NOTIFY_TOKEN
from linenotify import Notify

# 欲傳送的訊息內容
message = 'Hello World!'

Notify(LINE_NOTIFY_TOKEN, message)
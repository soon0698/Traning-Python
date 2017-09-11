import praw # http://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
import config
import time

def bot_login(): 
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "soon0698's dog comment responder v0.1")
    print("로그인(정보 획득) 완료!") 
    return r

def run_bot(r):
    print("25개의 코멘트를 검색합니다.")
    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body:
            print("해당 검색어를 찾았습니다. 코멘트 아이디 : " + comment.id)
            comment.reply("나도 좋아해! [여기](http://imgur.com/gallery/TUQvrsV)에도 하나 있지!")
            print(comment.id + "의 코멘트에 응답했습니다!")
    print("10초간 대기합니다.")
    time.sleep(10)

r = bot_login()
while True:
    run_bot(r)

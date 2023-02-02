from wapp_to_json import wapp_to_json
import json

chat = json.loads(wapp_to_json("chat.txt"))

def usr_messages(name):
    user_msg = []
    for i in chat:
        if i["Sender"] == name:
            user_msg.append(i)
    return user_msg

def most_used_word(messages):
    word_list = {}
    for i in messages:
        words = i["Message"].split()
        for x in words:
            try:
                q = word_list[x]
                word_list.update({x : q + 1 })
            except:
                word_list.update({x : 1})

    sorted_word_list = sorted(word_list.items(), key=lambda x:x[1])
    muw = sorted_word_list[-1]
    return [sorted_word_list, muw]

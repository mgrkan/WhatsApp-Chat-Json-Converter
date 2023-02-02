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

def search_word(word, messages, pretty_print):
    msg_including_word = []
    for i in messages:
        if word in i["Message"]:
            date = "{}/{}/{}".format(i["Day"], i["Month"], i["Year"])
            del i["Day"]
            del i["Month"]
            del i["Year"]
            del i["Hour"]
            highlighted = i["Message"].replace(word, '|{}|'.format(word))
            i.update({"Message": highlighted})
            i.update({"Date": date})
            msg_including_word.append(i)
    if pretty_print:
        for i in msg_including_word:
            print(i, "\n")
    return msg_including_word
    

from help_dialogs import message_sent, quest_confirm_reject_handler, quest_message_help
from Replicas.Quest_says import Quest_says

version = "1.0"


def chap2(req_save, command, intent, user_id):
    req_save['save'] = ''
    text = Quest_says['']['text']
    tts = Quest_says['']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)

def chap2_3_2_2_2_1_x(req_save, command, intent, user_id):
    if "" in intent:
        text = Quest_says['']['text']
        tts = Quest_says['']['tts']
        req_save['save'] = ''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "" in intent:
        text = Quest_says['']['text']
        tts = Quest_says['']['tts']
        req_save['save'] = ''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def chap2_3_end(req_save, command, intent, user_id):
    if "" in intent:
        text = Quest_says['']['text']
        tts = Quest_says['']['tts']
        req_save['save'] = ''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)



def chap2_7_x(req_save, command, intent, user_id):
    text = Quest_says['']['text']
    tts = Quest_says['']['tts']
    text_reject = Quest_says['']['text']
    tts_reject = Quest_says['']['tts']
    new_save = {'accept': '', 'reject': ''}
    return quest_confirm_reject_handler(req_save, "", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="")


def chap2_7_1(req_save, command, intent, user_id):
    text = Quest_says['']['text']
    tts = Quest_says['']['tts']
    new_save = {'accept': '', 'reject': ''}
    return quest_confirm_reject_handler(req_save, "", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)
from Replicas.Quest_says import Quest_says
from help_dialogs import message_sent, quest_confirm_reject_handler, quest_message_help

version = "1.0"

def quest(req_save, command, intent, user_id):
    req_save['save'] = 'quest_2'
    req_save['chapter'] = 'quest'
    text = Quest_says['quest']['text']
    tts = Quest_says['quest']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def quest_2(req_save, command, intent, user_id):
    text = Quest_says['quest_2']['text']
    tts = Quest_says['quest_2']['tts']
    new_save = {'accept': 'quest_3', 'reject': ''}
    return quest_confirm_reject_handler(req_save, "quest_2", intent, text_commands=intent, text=text, tts=tts, new_save=new_save)


def quest_3(req_save, command, intent, user_id):
    if "quest_3" in intent:
        text = Quest_says['quest_3']['text']
        tts = Quest_says['quest_3']['tts']
        req_save['save'] = 'quest_4_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest_4_x(req_save, command, intent, user_id):
    if "quest_4_x.DEACTIVE" in intent:
        text = Quest_says['quest_4_1x']['text']
        tts = Quest_says['quest_4_1x']['tts']
        req_save['save'] = 'quest_5_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest_4_x.RESUME" in intent:
        text = Quest_says['quest_4_x']['text']
        tts = Quest_says['quest_4_x']['tts']
        req_save['save'] = 'quest_5_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest_5_x(req_save, command, intent, user_id):
    if "quest_5_x.OUT" in intent:
        text = Quest_says['quest_5_1x']['text']
        tts = Quest_says['quest_5_1x']['tts']
        req_save['save'] = 'quest_6_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest_5_x.HELP" in intent:
        text = Quest_says['quest_5_x']['text']
        tts = Quest_says['quest_5_x']['tts']
        req_save['save'] = 'quest_6_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest_6_x(req_save, command, intent, user_id):
    text = Quest_says['quest_6_x']['text']
    tts = Quest_says['quest_6_x']['tts']
    text_reject = Quest_says['quest_6_1x']['text']
    tts_reject = Quest_says['quest_6_1x']['tts']
    new_save = {'accept': 'quest_7_x', 'reject': 'quest_end'}
    return quest_confirm_reject_handler(req_save, "quest_6_x.OUT", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="quest_6_x.NOT_OUT")


def quest_7_x(req_save, command, intent, user_id):
    if "quest_7_x.DEATH" in intent:
        text = Quest_says['quest_7_1x']['text']
        tts = Quest_says['quest_7_1x']['tts']
        req_save['save'] = 'quest_end'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest_7_x.LIFE" in intent:
        text = Quest_says['quest_7_x']['text']
        tts = Quest_says['quest_7_x']['tts']
        req_save['save'] = 'quest_8_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest_8_x(req_save, command, intent, user_id):
    if "quest_8_x.SEARCH" in intent:
        text = Quest_says['quest_8_x']['text']
        tts = Quest_says['quest_8_x']['tts']

        req_save["inventory"]['weapon']["sword"]["rust"]["activity"] = True
        req_save["other"]['Map'] = True

        req_save['save'] = 'quest_9'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest_8_x.BIND" in intent:
        text = Quest_says['quest_8_1x']['text']
        tts = Quest_says['quest_8_1x']['tts']

        req_save["inventory"]['weapon']["sword"]["rust"]["activity"] = True
        req_save["other"]['Map'] = True

        req_save['save'] = 'quest_9'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest_9(req_save, command, intent, user_id):
    if "quest_9" in intent:
        text = Quest_says['quest_9']['text']
        tts = Quest_says['quest_9']['tts']
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)

def quest_end(req_save, command, intent, user_id):
    if "chap2_3_end" in intent:
        text = Quest_says['Home']['text']
        tts = Quest_says['Home']['tts']
        req_save['save'] = 'Home'
        req_save['chapter'] = 'Home'
        req_save['other']['Quests']['quest'] = True
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)
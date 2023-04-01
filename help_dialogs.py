from Replicas.dictionary import main_data
from dialogs import message_sent, message_sent_with_card
from Replicas.Quest_tips import Quest_tips


def message_help(req_save, version):
    text = main_data[req_save["save"]]['text']
    tts = main_data[req_save["save"]]['tts']
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": False,
            "buttons": main_data[req_save["save"]]['buttons']
        },
        "session_state": {
            "save": req_save["save"],
            "chapter": req_save["chapter"],
            "name": req_save["name"],
            "health": req_save["health"],
            "power": req_save["power"],
            "mana": req_save["mana"],
            "stamina": req_save["stamina"],
            "score": req_save["score"],
            "inventory": req_save["inventory"],
            "other": req_save["other"]
        },
        "version": version
    }
    return response

def quest_message_help(req_save, version):
    text = Quest_tips[req_save["save"]]['text']
    tts = Quest_tips[req_save["save"]]['tts']
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": False,
            "buttons": Quest_tips[req_save["save"]]['buttons']
        },
        "session_state": {
            "save": req_save["save"],
            "chapter": req_save["chapter"],
            "name": req_save["name"],
            "health": req_save["health"],
            "power": req_save["power"],
            "mana": req_save["mana"],
            "stamina": req_save["stamina"],
            "score": req_save["score"],
            "inventory": req_save["inventory"],
            "other": req_save["other"]
        },
        "version": version
    }
    return response

def quest_confirm_reject_handler(req_save, command, intent, text_commands, text, tts, version="1.0",
                           reject_enable=False,
                           reject_commands=None, new_save=None, text_reject='', tts_reject='', reject_command=''):
    if reject_enable:
        reject_command = command if reject_command == '' else reject_command
        if "YANDEX.REJECT" in intent or reject_command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif "YANDEX.REJECT" not in intent and reject_command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)
    else:
        if ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)

def confirm_reject_handler(req_save, command, intent, text_commands, text, tts, version="1.0",
                           reject_enable=False,
                           reject_commands=None, new_save=None, text_reject='', tts_reject='', reject_command=''):
    if reject_enable:
        reject_command = command if reject_command == '' else reject_command
        if "YANDEX.REJECT" in intent or reject_command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif "YANDEX.REJECT" not in intent and reject_command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)
    else:
        if ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)
        
        
        
        
def confirm_reject_handler_with_card(req_save, command, intent, text_commands, text, tts, version="1.0",
                           reject_enable=False,
                           reject_commands=None, new_save=None, text_reject='', tts_reject='', card={}):
    if reject_enable:
        if "YANDEX.REJECT" in intent or command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text_reject, tts=tts_reject, save=save, version=version, card=card)
        elif "YANDEX.REJECT" not in intent and command in reject_commands:
            save = {
                "save": new_save['reject'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text_reject, tts=tts_reject, save=save, version=version, card=card)
        elif ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text, tts=tts, save=save, version=version, card=card)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text, tts=tts, save=save, version=version, card=card)
        else:
            return message_help(req_save, version)
    else:
        if ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text, tts=tts, save=save, version=version, card=card)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "chapter": req_save["chapter"],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "stamina": req_save["stamina"],
                "score": req_save["score"],
                "inventory": req_save["inventory"],
                "other": req_save["other"]
            }
            return message_sent_with_card(text=text, tts=tts, save=save, version=version, card=card)
        else:
            return message_help(req_save, version)
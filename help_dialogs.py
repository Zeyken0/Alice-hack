from dictionary import main_data
from dialogs import message_sent


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
            "name": req_save["name"],
            "health": req_save["health"],
            "power": req_save["power"],
            "mana": req_save["mana"],
            "score": req_save["score"]
        },
        "version": version
    }
    return response


def confirm_reject_handler(req_save, command, intent, text_commands, text, tts, version="1.0",
                           reject_enable=False,
                           reject_commands=None, new_save=None, text_reject='', tts_reject=''):
    if reject_enable:
        if "YANDEX.REJECT" in intent or command in reject_commands:
            save = {
                "save": new_save['reject'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif "YANDEX.REJECT" not in intent and command in reject_commands:
            save = {
                "save": new_save['reject'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text_reject, tts=tts_reject, save=save, version=version)
        elif ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)
    else:
        if ("YANDEX.CONFIRM" in intent) or (command in text_commands):
            save = {
                "save": new_save['accept'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        elif ("YANDEX.CONFIRM" not in intent) and (command in text_commands):
            save = {
                "save": new_save['accept'],
                "name": req_save["name"],
                "health": req_save["health"],
                "power": req_save["power"],
                "mana": req_save["mana"],
                "score": req_save["score"]
            }
            return message_sent(text=text, tts=tts, save=save, version=version)
        else:
            return message_help(req_save, version)


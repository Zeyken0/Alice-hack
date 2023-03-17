from config import *
from dialogs import d_start_0, message_sent
version = "1.01"


def start(event, context):
    command = event['request']['command']
    intent = event["request"]["intents"]
    if command == "":
        if COLLECTION.count_documents({"id": event["session"]["application"]["application_id"]}) == 0:
            user = {
                "id": event["session"]["application"]["application_id"],
                "name": "",
                "save": "",
                "step": [""]
            }
            COLLECTION.insert_one(user)
            text = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            tts = "Добро пожаловать в Сагу Битв и Приключений. sil <[200]> Ты готов начать?"
            return d_start_0(text, tts, version)
        elif COLLECTION.find_one({"id": event["session"]["application"]["application_id"]})["save"] == "":
            text = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            tts = "Добро пожаловать в Сагу Битв и Приключений. sil <[200]> Ты готов начать?"
            return d_start_0(text, tts, version)
        else:
            text = "Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"
            tts = "Рады тебя снова видеть в Саге Битв и Приключений. sil <[200]> Ты готов продолжить?"
            save = COLLECTION.find_one({"id": event["session"]["application"]["application_id"]})["save"]
            return message_sent(text=text,tts=tts,version=version,save=save)
    elif intent["YANDEX.HELP"]:
        req_save = event["request"]["state"]["session"]["text"]
        if req_save == "start":
            text = 'Выберите один из следующих вариантов:\n'
            tts = 'Выберите один из следующих вариантов:\n'
            save = {
                "value": 1,
                "text": "start"
            }
            return message_sent(text, tts, version, save)
        elif req_save == "start_1":
            pass
    elif command == "выход":
        text = 'Удачи!!'
        tts = 'Удачи!!'
        save = {
            "value": 1,
            "text": "start"
        }
        message_sent(text, tts, version, save, end_session=True)
    elif command:
        req_save = event["request"]["state"]["session"]["text"]
        if req_save == "start":
            start_1(event, req_save, command, intent)
        elif req_save == "start_1":
            pass


def start_1(event, req_save, command, intent):
    if intent["YANDEX.CONFIRM"]:
        save = {
            "value": 2,
            "text": "start_1"
        }
        text = "В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли."
        tts = "В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли."
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
            },
            "session_state": {
                save
            },
            "version": version
        }
        return response
    else:
        pass


#event = {
#    "meta": {
#        "locale": "ru-RU",
#        "timezone": "UTC",
#        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
#        "interfaces": {
#            "screen": {},
#            "payments": {},
#            "account_linking": {}
#        }
#    },
#    "session": {
#        "message_id": 0,
#        "session_id": "49926f4e-5329-4fa5-b49b-fbbd5e69467d",
#        "skill_id": "b2735f27-2dcf-4c5a-ad8c-a08d78959ad0",
#        "user": {
#            "user_id": "9499CE22F35C42BAF046A5D7EB1A15ABEAC69D1D6FA94CC37F7AF136D04C2AAE"
#        },
#        "application": {
#            "application_id": "0DB5208CDBB88CF3DE5F460F91E3C39D651CB3324CC6003D58E031B9BEFFAEAC"
#        },
#        "user_id": "0DB5208CDBB88CF3DE5F460F91E3C39D651CB3324CC6003D58E031B9BEFFAEAC",
#        "new": True
#    },
#    "request": {
#        "command": "",
#        "original_utterance": "",
#        "nlu": {
#            "tokens": [],
#            "entities": [],
#            "intents": {}
#        },
#        "markup": {
#            "dangerous_context": False
#        },
#        "type": "SimpleUtterance"
#    },
#    "state": {
#        "session": {},
#        "user": {},
#        "application": {}
#    },
#    "version": "1.0"
#}
# start(event, '1')

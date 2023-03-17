from config import *
from dialogs import d_start_0, message_sent
version = "1.0"


def start(event, context):
    command = event['request']['command']
    intent = event["request"]['nlu']["intents"]
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
    elif command == "выход":
        text = 'Удачи!!'
        tts = 'Удачи!!'
        save = {
            "value": 1,
            "text": "start"
        }
        message_sent(text, tts, version, save, end_session=True)
    elif command:
        try:
            if intent["YANDEX.HELP"]:
                try:
                    req_save = event["state"]["session"]["text"]
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
                except KeyError:
                    req_save = " "
        except KeyError:
            try:
                req_save = event["request"]["state"]["session"]["text"]
                if req_save == "start":
                    start_1(event, req_save, command, intent)
                elif req_save == "start_1":
                    pass
            except KeyError:
                req_save = " "


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

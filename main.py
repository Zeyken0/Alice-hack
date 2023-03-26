import chapter_1
from config import *
from dialogs import message_sent, d_start_0

version = "1.0"


# Сделать сохранения

def start(event, context):
    command = event['request']['command']
    intent = event["request"]['nlu']["intents"]
    user_id = event["session"]["user"]["user_id"]
    if command == "":
        if COLLECTION.count_documents({"id": user_id}) == 0:
            user = {
                "id": user_id,
                "name": "default",
                "save": "",
                "health": 6,
                "power": 2,
                "mana": 0,
                "inventory": {},
                "other": {"trader": False, "knife": False}
            }
            COLLECTION.insert_one(user)
            text = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
            tts = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
            return d_start_0(text, tts, version)
        elif COLLECTION.find_one({"id": user_id})["save"] == "":
            text = '''"Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"'''
            tts = '''"Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"'''
            return d_start_0(text, tts, version)
        else:
            text = '''"Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"'''
            tts = '''"Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"'''
            save = COLLECTION.find_one({"id": user_id})["save"]
            return message_sent(text=text, tts=tts, version=version, save=save)
    elif command == "выход":
        text = 'Удачи!!'
        tts = 'Удачи!!'
        save = ""
        return message_sent(text, tts, version, save, end_session=True)
    else:
        req_save = {
            "save": event["state"]["session"]["save"],
            "name": event["state"]["session"]["name"],
            "health": event["state"]["session"]["health"],
            "power": event["state"]["session"]["power"],
            "mana": event["state"]["session"]["mana"],
            "score": event["state"]["session"]["score"],
            "inventory": event["state"]["session"]["inventory"],
            "other": event["state"]["session"]["other"],
        }
        saves = {
            "start": chapter_1.start_1,
            "start_1": chapter_1.start_2,
            "start_2": chapter_1.start_3,
            "start_3": chapter_1.chap,
            "start_3_1": chapter_1.chap,
            "chap": chapter_1.chap_1,
            "chap_1": chapter_1.chap_2,
            "chap_1_1": chapter_1.chap_2,
            "chap_2": chapter_1.chap_3,
            "chap_3": chapter_1.chap_4,
            "chap_4_1": chapter_1.chap_4_1_1,
            "chap_4_1_1": chapter_1.chap_4_1_x,
            "chap_4_1_2": chapter_1.chap_5,
            "chap_4_1_3": chapter_1.chap_4_1_3_x,
            "chap_4_1_3_1": chapter_1.chap_4_1_3_x_end,
            "chap_4_1_3_2": chapter_1.chap_4_1_3_x_end,
            "chap_4_1_3_3": chapter_1.chap_5_1,
            "chap_4_1_4": chapter_1.chap_5,
            "chap_4_1_7": chapter_1.chap_5,
            "chap_4_1_0": chapter_1.chap_5,
            "chap_4_2": chapter_1.chap_4_2_1,
            "chap_4_1_3_4": chapter_1.chap_5,
            "chap_5": chapter_1.chap_5_1,
            "chap_5_1": chapter_1.chap_6,
            "chap_6": chapter_1.chap_6_x,
            "chap_6_1": chapter_1.chap_6_0_x,
            "chap_6_2": chapter_1.chap_6_0_x,
            "chap_6_0": chapter_1.chap_7,
            "chap_6_0_1": chapter_1.chap_7,
            "chap_7": chapter_1.chap_7_x,
            "chap_7_1": chapter_1.chap_8,
            "chap_7_2": chapter_1.chap_7_end,
            "chap_7_3": chapter_1.chap_7_end,
            "chap_7_0": chapter_1.chap_7_end,
            "chap_8": chapter_1.chap_9,
            "chap_9": chapter_1.chap_10,
            "chap_10": chapter_1.chap_10_x,
            "chap_10_1": chapter_1.chap_11_x,
            "chap_10_2": chapter_1.chap_11_x,
            "chap_10_0": chapter_1.chap_11_x,
            "chap_11": chapter_1.chap_12_x,
            "chap_11_1": chapter_1.chap_11_1,
            "chap_11_2": chapter_1.chap_11_2_1,
            "chap_11_2_1": chapter_1.chap_14,
            "chap_12": chapter_1.chap_13,
            "chap_12_1": chapter_1.chap_13_1,
            "chap_13": chapter_1.chap_13,
            "chap_13_0": chapter_1.chap_14,
            "chap_13_4": chapter_1.chap_14,
            "chap_14": chapter_1.chap_15,
            "chap_15": chapter_1.chap_15,
            "chap_17": chapter_1.chap_13_0,
            "chap_13_2": chapter_1.chap_13_2,
            "chap_18": chapter_1.chap_18,
            "chap_13_3": chapter_1.chap_13_3,
            "chap_16": chapter_1.chap_16,
            "chap_11_0": chapter_1.chap_16,
            "chap_18_1": chapter_1.chap_18_1,
            "chap_18_2": chapter_1.chap_18_2,
            "chap_19": chapter_1.chap_19,
            "chap_19_1": chapter_1.chap_19_1,
            "chap_19_2": chapter_1.chap_19_2,
            "chap_19_3": chapter_1.chap_19_3,
            "chap_19_1_1": chapter_1.chap_19_1_1,
            "chap_21": chapter_1.chap_21_x,
            "chap_20": chapter_1.chap_21,
            "chap_21_1": chapter_1.chap_21_1,
            "chap_21_2": chapter_1.chap_21_2,
            "chap_22": chapter_1.chap_22,
            "chap_22_1": chapter_1.chap_22_1,
            "chap_22_2": chapter_1.chap_22_2,
            "chap_24": chapter_1.chap_24,
            "chap_23": chapter_1.chap_23,
            "chap_23_2": chapter_1.chap_23_2,
            "chap_24_1": chapter_1.chap_24_1,
            "chap_24_2": chapter_1.chap_24_2,
            "chap_25": chapter_1.chap_25,
            "chap_25_1": chapter_1.chap_25_1,
            "chap_25_2": chapter_1.chap_25_2,
            "chap_25_1_2": chapter_1.chap_25_1_2
        }
        if req_save["save"] in saves:
            return saves[req_save["save"]](req_save, command, intent, user_id)
        else:
            return message_sent(text="чо", tts="чо", version=version, save=req_save)

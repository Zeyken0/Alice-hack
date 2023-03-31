import chapter_1
import chapter_2
from Quests import quests
from config import *
from dialogs import message_sent, d_start_0

version = "1.0"
chapter1 = {
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
    "chap_17": chapter_1.chap_17,
    "chap_13_2": chapter_1.chap_13_2,
    "chap_18": chapter_1.chap_18,
    "chap_18_0": chapter_1.chap_18_0,
    "chap_13_3": chapter_1.chap_13_3,
    "chap_16": chapter_1.chap_16,
    "chap_11_0": chapter_1.chap_17,
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
    "chap_25_1_2": chapter_1.chap_25_1_2,
    "chap2": chapter_2.chap2,
}

chapter2 = {
    "chap2_1_x": chapter_2.chap2_1_x,
    "chap2_2": chapter_2.chap2_2,
    "chap2_3_x": chapter_2.chap2_3_x,
    "chap2_3_1x": chapter_2.chap2_3_1x,
    "chap2_3_2x": chapter_2.chap2_3_2x,
    "chap2_3_3x": chapter_2.chap2_3_3x,
    "chap_2_3_1_1x": chapter_2.chap2_3_end,
    "chap_2_3_1_2x": chapter_2.chap2_3_end,
    "chap2_3_2_2": chapter_2.chap2_3_2_2,
    "chap2_3_2_2_2_0": chapter_2.chap2_3_2_2_2_0,
    "chap2_3_2_2_2_1_0": chapter_2.chap2_3_2_2_2_1_0,
    "chap2_3_2_2_2_1x": chapter_2.chap2_3_2_2_2_1x,
    "chap2_3_2_2_2_1_x": chapter_2.chap2_3_2_2_2_1_x,
    "chap2_3_2_2_2_1_1x": chapter_2.chap2_3_end,
    "chap2_3_2_2_2_1_2": chapter_2.chap2_3_2_2_2_1_2,
    "chap2_3_3_1x": chapter_2.chap2_3_end,
    "chap2_3_3_1": chapter_2.chap2_3_3_1,
    "chap2_3_3_2": chapter_2.chap2_3_3_2,
    "chap2_3_3_2_x": chapter_2.chap2_3_3_2_x,
    "chap2_3_3_2_1x": chapter_2.chap2_3_end,
    "chap2_3_3_2_1": chapter_2.chap2_3_3_2_1,
    "chap2_3_3_2_2": chapter_2.chap2_3_3_2_2,
    "chap2_3_3_2_2_x": chapter_2.chap2_3_3_2_2_x,
    "chap2_3_3_2_2_1x": chapter_2.chap2_3_end,
    "chap2_3_2_1_x": chapter_2.chap2_3_2_1_x,
    "chap2_3_2_1_2": chapter_2.chap2_3_2_1_2,
    "chap2_3_2_1_2_x": chapter_2.chap2_3_2_1_2_x,
    "chap2_3_2_1_2_1x": chapter_2.chap2_3_end,
    "chap2_3_2_1_2_0x": chapter_2.chap2_3_2_1_2_0x,
    "chap2_3_2_1_2_2": chapter_2.chap2_3_2_1_2_2,
    "chap2_3_2_1_2_2_x": chapter_2.chap2_3_2_1_2_2_x,
    "chap2_3_2_1_2_2_1x": chapter_2.chap2_3_end,
    "chap2_3_0": chapter_2.chap2_3_0,
    "chap2_4": chapter_2.chap2_4,
    "chap2_5": chapter_2.chap2_5,
    "chap2_6": chapter_2.chap2_6,
    "chap2_7": chapter_2.chap2_7,
    "chap2_7_1": chapter_2.chap2_7_1,
    "chap2_7_2": chapter_2.chap2_7_2_fight,
    "chap2_9": chapter_2.chap2_9,
    "chap2_10": chapter_2.chap2_10,
    "chap2_11": chapter_2.chap2_11,
    "chap2_12": chapter_2.chap2_12,
    "chap2_13_x": chapter_2.chap2_13_x,
    "chap2_13_2_x": chapter_2.chap2_13_2_x,
    "chap2_14": chapter_2.chap2_14,
    "chap2_15_x": chapter_2.chap2_15_x,
    "chap2_15_x_x": chapter_2.chap2_15_x_x,
    "chap2_16_x": chapter_2.chap2_16_x,
    "chap2_16_3x_x": chapter_2.chap2_16_3x_x,
    "chap2_17": chapter_2.chap2_17,
    "chap2_18_x": chapter_2.chap2_18_x,
    "chap2_19": chapter_2.chap2_19,
    "chap2_20": chapter_2.chap2_20,
    "chap2_21": chapter_2.chap2_21,
    "chap2_22": chapter_2.chap2_22,
}

quest = {
    "quest_2": quests.quest_2,
    "quest_3": quests.quest_3,
    "quest_4_x": quests.quest_4_x,
    "quest_5_x": quests.quest_5_x,
    "quest_6_x": quests.quest_6_x,
    "quest_7_x": quests.quest_7_x,
    "quest_end": quests.quest_end,
    "quest_8_x": quests.quest_8_x,
    "quest_9": quests.quest_9
}

quest2 = {

}

def start(event, context):
    command = event['request']['command']
    original_utterance = event['request']['original_utterance']
    intent = event["request"]['nlu']["intents"]
    user_id = event["session"]["user"]["user_id"]
    if original_utterance == "":
        if COLLECTION.count_documents({"id": user_id}) == 0:
            USER["user_id"] = user_id
            COLLECTION.insert_one(USER)
            text = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
            tts = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
            return d_start_0(text, tts, version)
        elif COLLECTION.find_one({"id": user_id})["save"] == "":
            text = '''"Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"'''
            tts = '''"Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"'''
            return d_start_0(text, tts, version)
        else:
            save = {
                "save": COLLECTION.find_one({"id": user_id})["save"],
                "name": COLLECTION.find_one({"id": user_id})["name"],
                "chapter": COLLECTION.find_one({"id": user_id})["chapter"],
                "health": COLLECTION.find_one({"id": user_id})["health"],
                "power": COLLECTION.find_one({"id": user_id})["power"],
                "mana": COLLECTION.find_one({"id": user_id})["mana"],
                "stamina": 100,
                "score": COLLECTION.find_one({"id": user_id})["score"],
                "inventory": COLLECTION.find_one({"id": user_id})["inventory"],
                "other": COLLECTION.find_one({"id": user_id})["other"],
            }

            text = '''Рады тебя снова видеть в Саге Битв и Приключений. Загрузить последнее сохранение или начать игру сначала?'''
            tts = '''Рады тебя снова видеть в Саге Битв и Приключений. Загрузить последнее сохранение или начать игру сначала?'''
            return message_sent(text=text, tts=tts, version=version, save=save)
    elif "EXIT" in intent:
        req_save = {
            "save": event["state"]["session"]["save"],
            "chapter": event["state"]["session"]["chapter"],
            "name": event["state"]["session"]["name"],
            "health": event["state"]["session"]["health"],
            "power": event["state"]["session"]["power"],
            "mana": event["state"]["session"]["mana"],
            "stamina": event["state"]["session"]["stamina"],
            "score": event["state"]["session"]["score"],
            "inventory": event["state"]["session"]["inventory"],
            "other": event["state"]["session"]["other"],
        }
        text = 'Ждем тебя снова!'
        tts = 'Ждем тебя снова!'
        return message_sent(text, tts, version, req_save, end_session=True)
    else:
        req_save = {
            "save": event["state"]["session"]["save"],
            "chapter": event["state"]["session"]["chapter"],
            "name": event["state"]["session"]["name"],
            "health": event["state"]["session"]["health"],
            "power": event["state"]["session"]["power"],
            "mana": event["state"]["session"]["mana"],
            "stamina": event["state"]["session"]["stamina"],
            "score": event["state"]["session"]["score"],
            "inventory": event["state"]["session"]["inventory"],
            "other": event["state"]["session"]["other"],
        }
        if "RESTART" in intent:
            req_save['save'] = 'RESTART' + req_save['save']
            text = "Вы уверены, что хотите начать игру сначала? Весь прогресс будет потерян!"
            tts = "Вы уверены, что хотите начать игру сначала? Весь прогресс будет потерян!"
            return message_sent(text=text, tts=tts, version=version, save=req_save)


        # ЖЕЛАТЕЛЬНО СОЗДАТЬ НОВЫЙ ФАЙЛ И ПОМЕСТИТЬ ЭТО ТУДА. ТУТ ПРОВЕРКИ ФУНКЦИИ В НОВЫЙ ФАЙЛ


        # ВЕРНУТЬСЯ В УБЕЖИЩЕ
        elif "HOME" in intent and req_save["other"]["Menu"]:
            if req_save["save"] == "quest_9":
                text = ''' '''
                tts = ''' '''
                req_save['save'] = 'Home'
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            elif req_save["save"] == "quest2_8":
                # Хочешь получить больше заданий - обращайся ко мне (Гаврила)
                text = ''' '''
                tts = ''' '''
                req_save['save'] = 'Home'
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                return message_sent(text="Сейчас вы не можете вернуться в убежище!", tts="Сейчас вы не можете вернуться в убежище!", version=version, save=req_save)

        # ТОП ИГРОКОВ
        elif "TOP" in intent:
            score = COLLECTION.find().sort("score", -1)
            for x in score:
                pass

        # ОТКРЫТЬ ИНВЕНТАРЬ
        elif "INVENTORY" in intent and req_save["other"]["Menu"]:
            pass

        # НАДЕТЬ БРОНЮ
        elif "надеть" in command and req_save["other"]["Menu"]:
            pass

        # ВЗЯТЬ ОРУЖИЕ
        elif "взять" in command and req_save["other"]["Menu"]:
            pass

        elif "NEWQUESTS" in intent and req_save["other"]["Menu"]:
            # Сейчас для тебя новых заданий нет, но ты можешь отправиться в колизей бесконечных битв
            if req_save["save"] == "Home":
                text = '''Пока для вас нет новых заданий.'''
                tts = '''Пока для вас нет новых заданий.'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = '''Чтобы посмотреть новые задания, вернитесь в убежище!'''
                tts = '''Чтобы посмотреть новые задания, вернитесь в убежище!'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

        # СОХРАНЕНИЕ ИГРЫ
        elif "SAVEGAME" in intent and req_save['save'] == "Home":
            COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap2_11', "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
            text = '''Игра успешно сохранена!'''
            tts = '''Игра успешно сохранена!'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)

        # ХАРАКТЕРИСТИКИ ПОЛЬЗОВАТЕЛЯ
        elif "INSPECT" in intent and req_save["other"]["Menu"]:
            pass

        # КНИГА ЗАКЛИНАНИЙ ЗАКРЫТА
        elif "BOOK" in intent and req_save["other"]["Book"]['active']:
            if not req_save["other"]["Book"]['opened']:
                text = '''Вы не можете открыть книгу.'''
                tts = '''Вы не можете открыть книгу.'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

        # КОМАНДЫ
        elif "COMMANDS" in intent and req_save["other"]["Menu"]:
            text = ''' '''
            tts = ''' '''
            return message_sent(text=text, tts=tts, version=version, save=req_save)

        # ОТКРЫТЬ КНИГУ КВЕСТОВ
        elif "QUESTS" in intent and req_save["other"]["Menu"]:
            if req_save['other']['Quests']['quest']:
                text = ''' '''
                tts = ''' '''
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            elif req_save['other']['Quests']['quest2']:
                text = ''' '''
                tts = ''' '''
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            elif req_save['other']['Quests']['quest'] and req_save['other']['Quests']['quest2']:
                text = '''У вас нет квестов. Чтобы получить новые задания, скажите "Новые задания"'''
                tts = '''У вас нет квестов. Чтобы получить новые задания, скажите "Новые задания"'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = ''' '''
                tts = ''' '''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

        elif req_save['save'] == "RESTART":
            if "YANDEX.COMPLETE" in intent:
                USER["user_id"] = user_id
                COLLECTION.update_one({"id": user_id}, {"$set": USER})
                text = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
                tts = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'''
                return d_start_0(text, tts, version)
            elif "YANDEX.REJECT" in intent:
                req_save['save'] = req_save['save'].replace("RESTART", "")
                text = '''Загрузка... Для продолжения скажите "Начать"'''
                tts = '''Загрузка... sil <[500]> Для продолжения скажите "Начать'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

        # КВЕСТЫ
        elif req_save['save'] == "Home":
            if "отправиться на поиски приключений" in command:
                return quest['quest'](req_save, command, intent, user_id)
            elif "открыть магический потенциал" in command:
                return quest2['quest2'](req_save, command, intent, user_id)

        elif req_save["chapter"] == "chapter_1":
            if req_save["save"] in chapter1:
                return chapter1[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="чо", tts="чо", version=version, save=req_save)

        elif req_save["chapter"] == "chapter_2":
            if req_save["save"] in chapter2:
                return chapter2[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="чо", tts="чо", version=version, save=req_save)

        elif req_save["chapter"] == "quest":
            if req_save["save"] in quest:
                return quest[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="чо", tts="чо", version=version, save=req_save)

        elif req_save["chapter"] == "quest2":
            if req_save["save"] in quest2:
                return quest2[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="чо", tts="чо", version=version, save=req_save)

        # МЕНЮ
        else:
            text = ''' '''
            tts = ''' '''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
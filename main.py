from config import *
from dialogs import message_sent, d_start_0, message_sent_with_card
import pymongo

version = "1.0"

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
                text = '''Вы улучшили свое максимальное здоровье!'''
                tts = '''Вы улучшили свое максимальное здоровье!'''
                req_save['health'] = 20
                req_save['save'] = 'Home'
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            elif req_save["save"] == "quest2_8":
                text = '''Хочешь получить больше квестов? Скажи "Новые задания"'''
                tts = '''Хочешь получить больше квестов? Скажи "Новые задания"'''
                req_save['mana'] = 100
                req_save['save'] = 'Home'
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                return message_sent(text="Сейчас вы не можете вернуться в убежище!", tts="Сейчас вы не можете вернуться в убежище!", version=version, save=req_save)

        # ТОП ИГРОКОВ (ДОДЕЛАТЬ)
        elif "TOP" in intent:
            top = COLLECTION.find().sort("score", pymongo.DESCENDING).limit(10)
            text = 'Топ пользователей\n'
            tts = 'Топ пользователей'
            for i in top:
                NAME = i['name']
                SCORE = i['score']
                text = text + "Имя: " + NAME + '\n' + "Очки: " + str(SCORE) + '\n'
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Здоровье",
                        "description": f"{req_save['health']}",
                    },
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Сила",
                        "description": f"{req_save['power']}",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Мана",
                        "description": f"{req_save['mana']}",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # ОТКРЫТЬ ИНВЕНТАРЬ (ДОДЕЛАТЬ)
        elif "INVENTORY" in intent and req_save["other"]["Menu"]:
            text = "Ваш Инвентарь"
            tts = f""
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Здоровье",
                        "description": f"{req_save['health']}",
                    },
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Сила",
                        "description": f"{req_save['power']}",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Мана",
                        "description": f"{req_save['mana']}",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # НАДЕТЬ БРОНЮ
        elif "надеть" in command and req_save["other"]["Menu"]:
            thing_map = {
                "потрепанный шлем": ["helmet", "broken"],
                "потрепанный нагрудник": ["chest", "broken"],
                "потрепанные поножи": ["shorts", "broken"],
                "потрепанные ботинки": ["boots", "broken"]
            }

            thing_key = thing_map.get(command.replace("надеть", ""))
            if not thing_key:
                text = "Вы не можете надеть этот предмет!"
                tts = "Вы не можете надеть этот предмет!"
                return message_sent(text=text, tts=tts, version=version, save=req_save)

            inventory_item = req_save["inventory"]["armor"][thing_key[0]][thing_key[1]]
            if not inventory_item["activity"]:
                text = "У вас нет этого предмета в инвентаре!"
                tts = "У вас нет этого предмета в инвентаре!"
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            if inventory_item["is_gear"]:
                text = "Вы уже одели " + inventory_item["name"]
                tts = "Вы уже одели " + inventory_item["name"]
                return message_sent(text=text, tts=tts, version=version, save=req_save)

            inventory_item["is_gear"] = True
            text = "Вы одели " + inventory_item["name"]
            tts = "Вы одели " + inventory_item["name"]
            return message_sent(text=text, tts=tts, version=version, save=req_save)


        # ВЗЯТЬ ОРУЖИЕ
        elif "взять" in command and req_save["other"]["Menu"]:
            thing_map = {
                "самодельный топор": ["axe", "broken"],
                "потрескавшийся меч": ["sword", "broken"],
                "ржавый меч": ["sword", "rust"],
            }

            thing_key = thing_map.get(command.replace("взять", ""))
            if not thing_key:
                text = "Вы не можете взять этот предмет!"
                tts = "Вы не можете взять этот предмет!"
                return message_sent(text=text, tts=tts, version=version, save=req_save)

            inventory_item = req_save["inventory"]["weapon"][thing_key[0]][thing_key[1]]
            if not inventory_item["activity"]:
                text = "У вас нет этого предмета в инвентаре!"
                tts = "У вас нет этого предмета в инвентаре!"
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            if inventory_item["is_gear"]:
                text = "Вы уже одели " + inventory_item["name"]
                tts = "Вы уже одели " + inventory_item["name"]
                return message_sent(text=text, tts=tts, version=version, save=req_save)

            inventory_item["is_gear"] = True
            text = "Вы взяли " + inventory_item["name"]
            tts = "Вы взяли " + inventory_item["name"]
            return message_sent(text=text, tts=tts, version=version, save=req_save)

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
            text = "Ваши характеристики"
            tts = f"Ваши характеристики Здоровье: {req_save['health']} Сила: {req_save['power']} Мана: {req_save['mana']}"
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": Health_icon,
                        "title": "Здоровье",
                        "description": f"{req_save['health']}",
                    },
                    {
                        "image_id": Power_icon,
                        "title": "Сила",
                        "description": f"{req_save['power']}",
                    },

                    {
                        "image_id": Mana_icon,
                        "title": "Мана",
                        "description": f"{req_save['mana']}",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # КНИГА ЗАКЛИНАНИЙ ЗАКРЫТА
        elif "BOOK" in intent and req_save["other"]["Book"]['active']:
            if not req_save["other"]["Book"]['opened']:
                text = '''Вы не можете открыть книгу.'''
                tts = '''Вы не можете открыть книгу.'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

        # КОМАНДЫ
        elif "COMMANDS" in intent and req_save["other"]["Menu"]:
            text = "Команды"
            tts = 'Команды: Вернуться в убежище. Инвентарь. Надеть "Название доспеха". Взять "Название предмета". Сохранить игру. Осмотреть себя. Открыть книгу квестов. Название квеста. Новые квесты. Топ Игроков. Начать заново '
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Вернуться в убежище",
                        "description": "Возвращение в убежище",
                    },
                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Инвентарь",
                        "description": "Открытие инвентаря",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": 'Надеть "Название доспеха"',
                        "description": "Надеть доспех",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": 'Взять "Название предмета"',
                        "description": "Взять предмет",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Сохранить игру",
                        "description": "Сохранение игры",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Осмотреть себя",
                        "description": "Посмотреть свои характеристики",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Открыть книгу квестов",
                        "description": "Все ваши доступные квесты",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Название квеста",
                        "description": "Запустить определенный квест",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Новые квесты",
                        "description": "Все новые квесты",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Топ Игроков",
                        "description": "Шкала лидеров",
                    },

                    {
                        "image_id": "1030494/628705743a5ab80c90ea",
                        "title": "Начать заново",
                        "description": "Начать игру сначала",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # ОТКРЫТЬ КНИГУ КВЕСТОВ
        elif "QUESTS" in intent and req_save["other"]["Menu"]:
            if req_save['other']['Quests']['quest']:
                text = 'Текущие квесты:'
                tts = 'Текущие квесты: Открыть магический потенциал. sil <[300]> Для подробного описания квеста, произнесите его название!'
                card = {
                    "type": "ItemsList",
                    "header": {
                        "text": text,
                    },
                    "items": [
                        {
                            "image_id": "1030494/628705743a5ab80c90ea",
                            "title": "Открыть магический потенциал",
                            "description": "Магия - это очень круто",
                        },
                    ],
                    "footer": {
                        "text": "Для подробного описания квеста, произнесите его название!",
                    }
                }
                return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
            elif req_save['other']['Quests']['quest'] and req_save['other']['Quests']['quest2']:
                text = '''У вас нет квестов. Чтобы получить новые задания, скажите "Новые задания"'''
                tts = '''У вас нет квестов. Чтобы получить новые задания, скажите "Новые задания"'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = 'Текущие квесты:'
                tts = 'Текущие квесты: Отправиться на поиски приключений sil <[200]> Открыть магический потенциал. sil <[300]> Для подробного описания квеста, произнесите его название!'
                card = {
                    "type": "ItemsList",
                    "header": {
                        "text": text,
                    },
                    "items": [
                        {
                            "image_id": "1030494/628705743a5ab80c90ea",
                            "title": "Отправиться на поиски приключений",
                            "description": "Захватывающие приключения ждут вас!",
                        },

                        {
                            "image_id": "1030494/628705743a5ab80c90ea",
                            "title": "Открыть магический потенциал",
                            "description": "Магия - это очень круто",
                        },
                    ],
                    "footer": {
                        "text": "Для подробного описания квеста, произнесите его название!",
                    }
                }
                return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

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
                return message_sent(text="Ошибка!", tts="Ошибка!", version=version, save=req_save)

        elif req_save["chapter"] == "chapter_2":
            if req_save["save"] in chapter2:
                return chapter2[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="Ошибка!", tts="Ошибка!", version=version, save=req_save)

        elif req_save["chapter"] == "quest":
            if req_save["save"] in quest:
                return quest[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="Ошибка!", tts="Ошибка!", version=version, save=req_save)

        elif req_save["chapter"] == "quest2":
            if req_save["save"] in quest2:
                return quest2[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="Ошибка!", tts="Ошибка!", version=version, save=req_save)

        # МЕНЮ
        else:
            text = ''' '''
            tts = ''' '''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
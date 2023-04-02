from config import *
from dialogs import message_sent, d_start_0, message_sent_with_card
import pymongo

Health_icon = "1030494/f96c26a03ebbba705608"
Power_icon = "213044/4d285fda066e9ae61952"
Mana_icon = "997614/844a30f69150fb050ed6"
Stamina_icon = "1540737/7e3905e7d3c850e8d514"

version = "1.0"

def start(event, context):
    command = event['request']['command']
    original_utterance = event['request']['original_utterance']
    intent = event["request"]['nlu']["intents"]
    user_id = event["session"]["user"]["user_id"]
    if original_utterance == "":
        if COLLECTION.count_documents({"id": user_id}) == 0:
            USER["id"] = user_id
            COLLECTION.insert_one(USER)
            text = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы узнать больше, скажи "Что ты умеешь?", если ты готов скажи "Начать"'''
            tts = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы узнать больше, скажи "Что ты умеешь?", если ты готов скажи "Начать"'''
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
    elif original_utterance == "ping":
        text = '1'
        tts = '1'
        save = {
            "save": "",
            "name": "",
            "chapter": "",
            "health": "",
            "power": "",
            "mana": "",
            "stamina": "",
            "score": "",
            "inventory": "",
            "other": "",
        }
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

        if "RESTART" in req_save['save']:
            if "YANDEX.CONFIRM" in intent:
                USER["id"] = user_id
                COLLECTION.update_one({"id": user_id}, {"$set": USER})
                text = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы узнать больше, скажи "Что ты умеешь?", если ты готов скажи "Начать"'''
                tts = '''Добро пожаловать в Сагу Битв и Приключений. Чтобы узнать больше, скажи "Что ты умеешь?", если ты готов скажи "Начать"'''
                return d_start_0(text, tts, version)
            elif "YANDEX.REJECT" in intent:
                req_save['save'] = req_save['save'].replace("RESTART", "")
                text = '''Загрузка... Для продолжения скажите "Начать"'''
                tts = '''Загрузка... sil <[500]> Для продолжения скажите "Начать'''
                return message_sent(text=text, tts=tts, version=version, save=req_save)

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

        elif "start_1.HELP" in intent:
            text = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. \nВ конце почти каждого сообщения пишутся варианты ответов. Для продолжения ответь на них! Не бойся ошибаться, мы тебе поможем!\nРекомендуем этот навык для людей старше 12 лет.'
            tts = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. sil <[100]> В конце почти каждого сообщения пишутся варианты ответов. Для продолжения ответь на них! Не бойся ошибаться, мы тебе поможем! Рекомендуем этот навык для людей старше 12 лет.'
            return message_sent(text=text, tts=tts, save=req_save, version=version)

        # ТОП ИГРОКОВ
        elif "TOP" in intent:
            COLLECTION.update_one({"id": user_id}, {
                "$set": {"score": req_save['score']}})
            top = COLLECTION.find().sort("score", pymongo.DESCENDING).limit(10)
            text = f'Топ пользователей. У вас {req_save["score"]} очков'
            tts = f'Топ пользователей. У вас {req_save["score"]} очков '
            top_5 = []
            for i in top:
                NAME = i['name']
                SCORE = i['score']
                top_5.append({"name": NAME, "score": SCORE})
                tts += top_5[-1]['name'] + ' ' + str(top_5[-1]['score']) + ' очков. '
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1030494/8fe25497ac8140cccf83",
                        "title": top_5[0]['name'],
                        "description": f"{top_5[0]['score']} очков",
                    },
                    {
                        "image_id": "1030494/8fe25497ac8140cccf83",
                        "title": top_5[1]['name'],
                        "description": f"{top_5[1]['score']} очков",
                    },

                    {
                        "image_id": "1030494/8fe25497ac8140cccf83",
                        "title": top_5[2]['name'],
                        "description": f"{top_5[2]['score']} очков",
                    },

                    {
                        "image_id": "1030494/8fe25497ac8140cccf83",
                        "title": top_5[3]['name'],
                        "description": f"{top_5[3]['score']} очков",
                    },

                    {
                        "image_id": "1030494/8fe25497ac8140cccf83",
                        "title": top_5[4]['name'],
                        "description": f"{top_5[4]['score']} очков",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # ОТКРЫТЬ ИНВЕНТАРЬ
        elif "INVENTORY" in intent and req_save["other"]["Menu"]:
            text = "Ваш Инвентарь"
            tts = '''Ваш Инвентарь: Потрёпанный шлем(НАДЕТО). Потрёпанный нагрудник(НАДЕТО). Потрепанныe поножи(НАДЕТО). Потрепанныe ботинки(НАДЕТО). Ржавый меч(ЭКИПИРОВАННО)'''
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1656841/2a225a1720673653ec8d",
                        "title": "Потрёпанный шлем",
                        "description": "НАДЕТО",
                    },
                    {
                        "image_id": "1540737/946ec67f38c0544f558f",
                        "title": "Потрёпанный нагрудник",
                        "description": "НАДЕТО",
                    },

                    {
                        "image_id": "1656841/21dfdcc14e529a221aa9",
                        "title": "Потрепанныe поножи",
                        "description": "НАДЕТО",
                    },

                    {
                        "image_id": "1521359/5178b1c867cd8f6aaae8",
                        "title": "Потрепанныe ботинки",
                        "description": "НАДЕТО",
                    },

                    {
                        "image_id": "1652229/92a5ce83c25b42fc1093",
                        "title": "Ржавый меч",
                        "description": "ЭКИПИРОВАННО",
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
            text = "Вы уже одели " + inventory_item["name"]
            tts = "Вы уже одели " + inventory_item["name"]
            return message_sent(text=text, tts=tts, version=version, save=req_save)

            #if not inventory_item["activity"]:
            #    text = "У вас нет этого предмета в инвентаре!"
            #    tts = "У вас нет этого предмета в инвентаре!"
            #    return message_sent(text=text, tts=tts, version=version, save=req_save)
            #if inventory_item["is_gear"]:
            #    text = "Вы уже одели " + inventory_item["name"]
            #    tts = "Вы уже одели " + inventory_item["name"]
            #    return message_sent(text=text, tts=tts, version=version, save=req_save)
#
            #inventory_item["is_gear"] = True
            #text = "Вы одели " + inventory_item["name"]
            #tts = "Вы одели " + inventory_item["name"]
            #return message_sent(text=text, tts=tts, version=version, save=req_save)


        # ВЗЯТЬ ОРУЖИЕ
        elif "взять" in command and req_save["other"]["Menu"]:
            thing_map = {
                "самодельный топор": ["axe", "broken"],
                "потрескавшийся меч": ["sword", "broken"],
                "ржавый меч": ["sword", "rust"],
            }

            thing_key = thing_map.get(command.replace("взять", ""))
            #if not thing_key:
            #    text = "Вы не можете взять этот предмет!"
            #    tts = "Вы не можете взять этот предмет!"
            #    return message_sent(text=text, tts=tts, version=version, save=req_save)

            inventory_item = req_save["inventory"]["weapon"][thing_key[0]][thing_key[1]]
            if not inventory_item["activity"]:
                text = "У вас нет этого предмета в инвентаре!"
                tts = "У вас нет этого предмета в инвентаре!"
                return message_sent(text=text, tts=tts, version=version, save=req_save)
            if inventory_item["is_gear"]:
                text = "Вы уже одели " + inventory_item["name"]
                tts = "Вы уже одели " + inventory_item["name"]
                return message_sent(text=text, tts=tts, version=version, save=req_save)

            #inventory_item["is_gear"] = True
            #text = "Вы взяли " + inventory_item["name"]
            #tts = "Вы взяли " + inventory_item["name"]
            #return message_sent(text=text, tts=tts, version=version, save=req_save)

        elif "NEWQUESTS" in intent and req_save["other"]["Menu"]:
            # Сейчас для тебя новых заданий нет, но ты можешь отправиться в колизей бесконечных битв
            if req_save["save"] == "Home":
                text = '''Пока для вас нет новых заданий. Но ты можешь испытать свои силы в Клубе Сражений, сказав "Клуб Сражений"'''
                tts = '''Пока для вас нет новых заданий. Но ты можешь испытать свои силы в Клубе Сражений, сказав "Клуб Сражений"'''
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
            tts = 'Команды: Сохранить игру. Открыть книгу квестов. Название квеста запускает этот квест. Новые квесты. Топ Игроков.'
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "937455/c823bb7292f5eb3c5a1c",
                        "title": "Сохранить игру",
                        "description": "Сохранение игры",
                    },

                    {
                        "image_id": "1540737/6502f97f78a5caba4501",
                        "title": "Открыть книгу квестов",
                        "description": "Все ваши доступные квесты",
                    },

                    {
                        "image_id": "1652229/79d1a66270b81c3ccfec",
                        "title": "Название квеста",
                        "description": "Запустить определенный квест",
                    },

                    {
                        "image_id": "1521359/51202f121bbb70bffe42",
                        "title": "Новые квесты",
                        "description": "Все новые квесты",
                    },

                    {
                        "image_id": "1533899/9c469be57347db74750d",
                        "title": "Топ Игроков",
                        "description": "Шкала лидеров",
                    },
                ]
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

        # ОТКРЫТЬ КНИГУ КВЕСТОВ
        elif "QUESTS" in intent and req_save["other"]["Menu"]:
            if req_save['other']['Quests']['quest'] and not req_save['other']['Quests']['quest2']:
                text = 'Текущие квесты:'
                tts = 'Текущие квесты: Открыть магический потенциал. sil <[300]> Для подробного описания квеста, произнесите его название!'
                card = {
                    "type": "ItemsList",
                    "header": {
                        "text": text,
                    },
                    "items": [
                        {
                            "image_id": "213044/87de8dcc08f0eee9426b",
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
                            "image_id": "1540737/752a35762b13e455b445",
                            "title": "Отправиться на поиски приключений",
                            "description": "Захватывающие приключения ждут вас!",
                        },

                        {
                            "image_id": "213044/87de8dcc08f0eee9426b",
                            "title": "Открыть магический потенциал",
                            "description": "Магия - это очень круто",
                        },
                    ],
                    "footer": {
                        "text": "Для подробного описания квеста, произнесите его название!",
                    }
                }
                return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
        # КВЕСТЫ
        if req_save['save'] == "Home":
            if "отправиться на поиски приключений" in command:
                if req_save['other']['Quests']['quest']:
                    text = '''Вы уже прошли это задание!'''
                    tts = '''Вы уже прошли это задание!'''
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                return quest['quest'](req_save, command, intent, user_id)
            elif "открыть магический потенциал" in command:
                if req_save['other']['Quests']['quest2']:
                    text = '''Вы уже прошли это задание!'''
                    tts = '''Вы уже прошли это задание!'''
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                return quest2['quest2'](req_save, command, intent, user_id)
            elif "клуб сражений" in command:
                return infinity['inf'](req_save, command, intent, user_id)

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

        elif req_save["chapter"] == "inf":
            if req_save["save"] in infinity:
                return infinity[req_save["save"]](req_save, command, intent, user_id)
            else:
                return message_sent(text="Ошибка!", tts="Ошибка!", version=version, save=req_save)


        text = '''Для просмотра команд, скажите "Посмотреть команды"'''
        tts = '''Для просмотра команд, скажите "Посмотреть команды"'''
        req_save['save'] = 'Home'
        req_save['mana'] = 100
        req_save['stamina'] = 100
        return message_sent(text=text, tts=tts, version=version, save=req_save)
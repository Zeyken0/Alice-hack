from dialogs import message_sent, message_sent_with_card
from help_dialogs import message_help, confirm_reject_handler, confirm_reject_handler_with_card
from config import *
from Replicas.alice_says import alice_dict
import random

version = "1.0"


def start_1(req_save, command, intent, user_id):
    if "start_1.START" in intent:
        req_save['save'] = 'start_1'
        text = alice_dict['start_1']['text']
        tts = alice_dict['start_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "start_1.HELP" in intent:
        text = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. \nРекомендуем этот навык для людей старше 12 лет.'
        tts = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. Рекомендуем этот навык для людей старше 12 лет.'
        req_save['save'] = 'start'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.REJECT" in intent:
        text = 'А всё так хорошо начиналось'
        tts = 'А всё так хорошо начиналось'
        return message_sent(text=text, tts=tts, save=req_save, version=version, end_session=True)
    else:
        text = 'Такие подсказки будут доступны на протяжении квеста:\n' \
               'Отлично! \n' \
               'Чтобы начать игру, скажите "Начать"'
        tts = 'Такие подсказки будут доступны на протяжении квеста:\n' \
              'Отлично! \n' \
              'Чтобы начать игру, скажите "Начать"'
        req_save['save'] = 'start'
        buttons = [{
                    "title": 'Что ты умеешь?',
                    "hide": True
                },
                {
                    "title":"Начать",
                    "hide": True
                }]
        return message_sent(text=text, tts=tts, save=req_save, version=version, buttons = buttons)


def start_2(req_save, command, intent, user_id):
    COMMANDS_1 = ['']
    req_save["power"] = 2
    req_save["health"] = 6
    text = alice_dict['start_2']['text']
    tts = alice_dict['start_2']['tts']
    text_REJECT = '''Сегодня вы не поехали на рынок. Весь вечер вы пытались найти хоть кусочек хлеба ,но безуспешно.
Обстоятельства вынудили вас отправиться на рынок. На рынке, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении.
Проследовать за полицией или попробовать сбежать?'''
    tts_REJECT = '''Сегодня вы не поехали на рынок. 
Весь вечер вы пытались найти хоть кусочек хлеба ,но безуспешно.
Обстоятельства вынудили вас отправиться на рынок. На рынке, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении.
Проследовать за полицией или попробовать сбежать?'''
    new_save = {'accept': 'start_2', 'reject': 'start_2'}
    return confirm_reject_handler(req_save, "start_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save,reject_enable=True,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT, reject_commands=COMMANDS_1)


def start_3(req_save, command, intent, user_id):
    if "start_3.POLICE" in intent:
        text = alice_dict['start_3']['text']
        tts = alice_dict['start_3']['tts']
        req_save["save"] = 'start_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "start_3.RUN" in intent:
        text_REJECT = alice_dict['start_3_1']['text']
        tts_REJECT = alice_dict['start_3_1']['tts']
        req_save["save"] = 'start_3_1'
        return message_sent(text=text_REJECT, tts=tts_REJECT, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap(req_save, command, intent, user_id):
    text = alice_dict['chap']['text']
    tts = alice_dict['chap']['tts']
    new_save = {'accept': 'chap', 'reject': ''}
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
        ],
        "footer": {
            "text": "Для того, чтобы сделать свой досуг более интересным, выберите, чем заняться: спортом или отдыхом в виде сна.",
        }
    }
    return confirm_reject_handler_with_card(req_save, "chap", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, card= card)


def chap_1(req_save, command, intent, user_id):
    text = alice_dict['chap_1']['text']
    tts = alice_dict['chap_1']['tts']

    text_1 = alice_dict['chap_1_1']['text']
    tts_1 = alice_dict['chap_1_1']['tts']
    if "chap_1.SPORT" in intent:
        req_save["power"] = 4
        req_save["save"] = "chap_1"
        a = random.randint(0, 2)
        if a == 0:
            text = alice_dict['chap_1']['text_2']
            tts = alice_dict['chap_1']['tts_2']
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
                ],
                "footer": {
                    "text": "Продолжить мотать срок?",
                }
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
        else:
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
                ],
                "footer": {
                    "text": "Продолжить мотать срок?",
                }
            }
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
    elif "chap_1.SLEEP" in intent:
        req_save["health"] = 10
        req_save["save"] = "chap_1_1"
        a = random.randint(0, 2)
        if a == 0:
            text_1 = alice_dict['chap_1_1']['text_2']
            tts_1 = alice_dict['chap_1_1']['tts_2']
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text_1,
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
                ],
                "footer": {
                    "text": "Продолжить мотать срок?",
                }
            }
            return message_sent_with_card(text=text_1, tts=tts_1, save=req_save, version=version, card=card)
        else:
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text_1,
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
                ],
                "footer": {
                    "text": "Продолжить мотать срок?",
                }
            }
            return message_sent_with_card(text=text_1, tts=tts_1, save=req_save, version=version, card=card)
    else:
        return message_help(req_save, version)


def chap_2(req_save, command, intent, user_id):
    text = alice_dict["chap_2"]['text']
    tts = alice_dict["chap_2"]['tts']
    new_save = {'accept': 'chap_2', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_3(req_save, command, intent, user_id):
    text = alice_dict['chap_3_1']['text']
    tts = alice_dict['chap_3_1']['tts']
    text_REJECT = alice_dict['chap_3']['text']
    tts_REJECT = alice_dict['chap_3']['tts']
    new_save = {'accept': 'chap_3', 'reject': 'chap_3'}
    return confirm_reject_handler(req_save, "chap_3.WORK", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=intent,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT, reject_command="chap_3.NOT_WORK")


def chap_4(req_save, command, intent, user_id):
    if "chap_4.TRUE" in intent:
        req_save["save"] = "chap_4_1"
        text = alice_dict['chap_4_1']['text']
        tts = alice_dict['chap_4_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_4.LIE" in intent:
        req_save["health"] -= 2
        req_save["save"] = "chap_4_2"
        text = alice_dict['chap_4_2']['text']
        tts = alice_dict['chap_4_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_1(req_save, command, intent, user_id):
    text = alice_dict['chap_4_1_1']['text']
    tts = alice_dict['chap_4_1_1']['tts']
    new_save = {'accept': 'chap_4_1_1', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_4_1_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_4_1_x(req_save, command, intent, user_id):
    if "chap_4_1_x.RUN" in intent:
        req_save["save"] = "chap_4_1_2"
        req_save["health"] -= 1
        text = alice_dict['chap_4_1_2']['text']
        tts = alice_dict['chap_4_1_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_4_1_x.SHOUT" in intent:
        req_save["save"] = "chap_4_1_4"
        req_save["health"] -= 3
        text = alice_dict['chap_4_1_4']['text']
        tts = alice_dict['chap_4_1_4']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_4_1_x.HIT" in intent:
        if req_save["power"] == 4:
            req_save["save"] = "chap_4_1_3"
            text = alice_dict['chap_4_1_3']['text']
            tts = alice_dict['chap_4_1_3']['tts']
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            req_save["save"] = "chap_4_1_7"
            req_save["health"] -= 2
            text = alice_dict['chap_4_1_7']['text']
            tts = alice_dict['chap_4_1_7']['tts']
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_2_1(req_save, command, intent, user_id):
    text = alice_dict['chap_4_2_1']['text']
    tts = alice_dict['chap_4_2_1']['tts']
    new_save = {'accept': 'chap_5', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_4_2_1", intent, text_commands=intent, text=text, tts=tts, new_save=new_save)


def chap_4_1_3_x(req_save, command, intent, user_id):
    if "chap_4_1_3_x.POLICE" in intent:
        req_save["save"] = "chap_4_1_3_1"
        text = alice_dict['chap_4_1_3_1']['text']
        tts = alice_dict['chap_4_1_3_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_4_1_3_x.LEAVE" in intent:
        req_save["save"] = "chap_4_1_3_2"
        text = alice_dict['chap_4_1_3_2']['text']
        tts = alice_dict['chap_4_1_3_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_4_1_3_x.REMOVE" in intent:
        req_save["save"] = "chap_4_1_3_3"
        text = alice_dict['chap_4_1_3_3']['text']
        tts = alice_dict['chap_4_1_3_3']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_3_x_end(req_save, command, intent, user_id):
    text = alice_dict['start_1']['text']
    tts = alice_dict['start_1']['tts']
    new_save = {'accept': 'start_1', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_4_1_3_x_end", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_5(req_save, command, intent, user_id):
    text = alice_dict['chap_5']['text']
    tts = alice_dict['chap_5']['tts']
    text_REJECT = '''Охранник приводит вас в чувства. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов.\n
Вам нужно восстановить силы. Лечь спать?'''
    tts_REJECT = '''Охранник приводит вас в чувства. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов.\n
Вам нужно восстановить силы. Лечь спать?'''
    new_save = {'accept': 'chap_5', 'reject': 'chap_5'}
    return confirm_reject_handler(req_save, "chap_5.WAKE_UP", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=intent,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT, reject_command="chap_5.NOT_WAKE_UP")


def chap_5_1(req_save, command, intent, user_id):
    text = alice_dict['chap_5_1']['text']
    tts = alice_dict['chap_5_1']['tts']
    text_reject = '''Вы проявляли прекрасную выдержку, но уютная домашняя атмосфера тюрьмы заставила вас уснуть через 20 минут.
В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере.
Мотать срок?'''
    tts_reject = '''Вы проявляли прекрасную выдержку, но уютная домашняя атмосфера тюрьмы заставила вас уснуть через 20 минут.
        В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере.
    Мотать срок?'''
    new_save = {'accept': 'chap_5_1', 'reject': 'chap_5_1'}
    return confirm_reject_handler(req_save, "chap_5_1.SLEEP", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=intent,
                                  text_reject=text_reject, tts_reject=tts_reject, reject_command="chap_5_1.REJECT")


def chap_6(req_save, command, intent, user_id):
    text = alice_dict['chap_6']['text']
    tts = alice_dict['chap_6']['tts']
    new_save = {'accept': 'chap_6', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_6", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_6_x(req_save, command, intent, user_id):
    text = alice_dict['chap_6_1']['text']
    tts = alice_dict['chap_6_1']['tts']
    text_reject = alice_dict['chap_6_2']['text']
    tts_reject = alice_dict['chap_6_2']['tts']
    new_save = {'accept': 'chap_6_1', 'reject': 'chap_6_2'}
    return confirm_reject_handler(req_save, "chap_6_x.WATCH", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap_6_x.RESUME")


def chap_6_0_x(req_save, command, intent, user_id):
    if "chap_6_0_x.HELP" in intent:
        req_save["save"] = 'chap_6_0'
        req_save["other"]["trader"] = True
        text = alice_dict['chap_6_0']['text']
        tts = alice_dict['chap_6_0']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_6_0_x.RESUME" in intent:
        req_save["save"] = 'chap_6_0_1'
        text = alice_dict['chap_6_0_1']['text']
        tts = alice_dict['chap_6_0_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7(req_save, command, intent, user_id):
    text = alice_dict['chap_7']['text']
    tts = alice_dict['chap_7']['tts']
    new_save = {'accept': 'chap_7', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_7", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_7_x(req_save, command, intent, user_id):
    if "chap_7_x.HELP" in intent:
        if req_save["health"] > 3:
            req_save["save"] = "chap_7_1"
            text = alice_dict['chap_7_1']['text']
            tts = alice_dict['chap_7_1']['tts']
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            req_save["save"] = "chap_7_2"
            text = alice_dict['chap_7_2']['text']
            tts = alice_dict['chap_7_2']['tts']
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_7_x.RESUME" in intent:
        req_save["save"] = "chap_7_3"
        text = alice_dict['chap_7_3']['text']
        tts = alice_dict['chap_7_3']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7_end(req_save, command, intent, user_id):
    if "chap_7_end" in intent:
        req_save["save"] = 'start_1'
        text = alice_dict['start_1']['text']
        tts = alice_dict['start_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = "chap_7_0"
        return message_help(req_save, version)


def chap_8(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": req_save['save'], "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
    COMMANDS_REJECT = ['']
    text= '''После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.\n
Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за  последствия своих действий.\n
Сохранение игры... Прогресс сохранен.\n
Желаете продолжить?'''
    tts='''После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.
Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за  последствия своих действий.
Сохранение игры... Прогресс сохранен.
Желаете продолжить?'''
    text_REJECT= alice_dict['chap_7_end']['text']
    tts_REJECT= alice_dict['chap_7_end']['tts']
    new_save = {'accept': 'chap_8', 'reject': 'chap_7_end'}
    return confirm_reject_handler(req_save, "chap_8", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap_9(req_save, command, intent, user_id):
    text = alice_dict['chap_9']['text']
    tts = alice_dict['chap_9']['tts']
    new_save = {'accept': 'chap_9', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_9", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_10(req_save, command, intent, user_id):
    # проверка на имя
    req_save["save"] = 'chap_10'
    req_save["name"] = command
    text = alice_dict['chap_10']['text'] + command + alice_dict['chap_10']['text_1']
    tts = alice_dict['chap_10']['tts']
    return message_sent(text=text, tts=tts, save=req_save, version=version)


def chap_10_x(req_save, command, intent, user_id):
    if "chap_10_x.WHY" in intent:
        text = alice_dict['chap_10_1']['text']
        tts = alice_dict['chap_10_1']['tts']
        req_save["save"] = "chap_10_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_10_x.HOW" in intent:
        text = alice_dict['chap_10_2']['text']
        tts = alice_dict['chap_10_2']['tts']
        req_save["save"] = "chap_10_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_x(req_save, command, intent, user_id):
    if "chap_11_x.CAFETERIA" in intent:
        if req_save['other']['trader']:
            text = alice_dict['chap_11_1']['text']
            tts = alice_dict['chap_11_1']['tts']
            req_save['save'] = 'chap_11_1'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = alice_dict['chap_11_2']['text']
            tts = alice_dict['chap_11_2']['tts']
            req_save['save'] = 'chap_11_2'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_11_x.JOB" in intent:
        text = alice_dict['chap_11']['text']
        tts = alice_dict['chap_11']['tts']
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_2_1(req_save, command, intent, user_id):
    req_save["other"]["knife"] = True
    text = alice_dict['chap_11_2_1']['text']
    tts = alice_dict['chap_11_2_1']['tts']
    new_save = {'accept': 'chap_11_2_1', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_11_2_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_11_1(req_save, command, intent, user_id):
    text = alice_dict['chap_14']['text']
    tts = alice_dict['chap_14']['tts']
    req_save["other"]["knife"] = True
    new_save = {'accept': 'chap_14', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_11_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_14(req_save, command, intent, user_id):
    if "chap_14.LOOK_AROUND" in intent:
        req_save["save"] = "chap_15"
        text = alice_dict['chap_15']['text']
        tts = alice_dict['chap_15']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_14.JOB" in intent:
        text = alice_dict['chap_11']['text']
        tts = alice_dict['chap_11']['tts']
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_15(req_save, command, intent, user_id):
    text = alice_dict['chap_11']['text']
    tts = alice_dict['chap_11']['tts']
    new_save = {'accept': 'chap_11', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_15", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_12_x(req_save, command, intent, user_id):
    if "chap_12_x.MAKE" in intent:
        req_save["save"] = "chap_12"
        text = alice_dict['chap_12']['text']
        tts = alice_dict['chap_12']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_12_x.LOOK_AROUND" in intent:
        text = alice_dict['chap_12_1']['text']
        tts = alice_dict['chap_12_1']['tts']
        req_save["save"] = "chap_12_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13(req_save, command, intent, user_id):
    if ("YANDEX.CONFIRM" in intent) or ("chap_13" in intent):
        if req_save["other"]["trader"]:
            text = 'На полу вы заметили моток веревки. Вы взяли его с собой. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На полу вы заметили моток веревки. Вы взяли его с собой. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = 'На полу вы заметили моток веревки. Вы взяли его с собой. \nПойти в столовую?'
            tts = 'На полу вы заметили моток веревки. Вы взяли его с собой. Пойти в столовую?'
            if req_save["other"]["trader"]:
                req_save["save"] = "chap_13_3"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
            else:
                req_save["save"] = "chap_16"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif ("YANDEX.CONFIRM" not in intent) and ("chap_13" in intent):
        if req_save["other"]["trader"]:
            text = 'На полу вы заметили моток веревки. Вы взяли его с собой. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На полу вы заметили моток веревки. Вы взяли его с собой. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = 'На полу вы заметили моток веревки. Вы взяли его с собой. \nПойти в столовую?'
            tts = 'На полу вы заметили моток веревки. Вы взяли его с собой. Пойти в столовую?'
            if req_save["other"]["trader"]:
                req_save["save"] = "chap_13_3"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
            else:
                req_save["save"] = "chap_16"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_1(req_save, command, intent, user_id):
    if ("YANDEX.CONFIRM" in intent) or ("chap_13_1" in intent):
        if req_save["other"]["knife"]:
            text = 'На токарном станке вы изготовили рукоять. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На токарном станке вы изготовили рукоять. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18_0"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = 'На токарном станке вы изготовили рукоять.\nПойти в столовую? '
            tts = 'На токарном станке вы изготовили рукоять. Пойти в столовую?'
            if req_save["other"]["trader"]:
                req_save["save"] = "chap_13_3"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
            else:
                req_save["save"] = "chap_16"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif ("YANDEX.CONFIRM" not in intent) and ("chap_13_1" in intent):
        if req_save["other"]["knife"]:
            text = 'На токарном станке вы изготовили рукоять. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На токарном станке вы изготовили рукоять. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18_0"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = 'На токарном станке вы изготовили рукоять.\nПойти в столовую? '
            tts = 'На токарном станке вы изготовили рукоять. Пойти в столовую?'
            if req_save["other"]["trader"]:
                req_save["save"] = "chap_13_3"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
            else:
                req_save["save"] = "chap_16"
                return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_0(req_save, command, intent, user_id):
    if "chap_13_0" in intent:
        text = alice_dict['chap_18']['text']
        tts = alice_dict['chap_18']['tts']
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_2(req_save, command, intent, user_id):
    if req_save['other']['trader']:
        text = alice_dict['chap_13_3']['text']
        tts = alice_dict['chap_13_3']['tts']
        req_save["save"] = 'chap_13_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        text = alice_dict['chap_16']['text']
        tts = alice_dict['chap_16']['tts']
        req_save["save"] = 'chap_16'
        return message_sent(text=text, tts=tts, save=req_save, version=version)


def chap_13_3(req_save, command, intent, user_id):
    if "chap_13_3" in intent:
        req_save["save"] = "chap_13_4"
        text = alice_dict['chap_13_4']['text']
        tts = alice_dict['chap_13_4']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_4(req_save, command, intent, user_id):
    if "chap_13_4" in intent:
        text = alice_dict['chap_18']['text']
        tts = alice_dict['chap_18']['tts']
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_16(req_save, command, intent, user_id):
    text = alice_dict['chap_16']['text']
    tts = alice_dict['chap_16']['tts']
    new_save = {'accept': 'chap_17', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_16", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_17(req_save, command, intent, user_id):
    if "chap_17" in intent:
        req_save["save"] = 'chap_18_0'
        text = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        tts = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = 'chap_11_0'
        return message_help(req_save, version)


def chap_18_0(req_save, command, intent, user_id):
    text = alice_dict['chap_18']['text']
    tts = alice_dict['chap_18']['tts']
    new_save = {'accept': 'chap_18', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_18_0", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_18(req_save, command, intent, user_id):
    if "chap_18.CHECK" in intent:
        text = alice_dict['chap_18_1']['text']
        tts = alice_dict['chap_18_1']['tts']
        req_save["save"] = 'chap_18_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_18.RUN" in intent:
        text = alice_dict['chap_18_2']['text']
        tts = alice_dict['chap_18_2']['tts']
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_1(req_save, command, intent, user_id):
    if "chap_18_1.LOOK_AROUND" in intent:
        text = alice_dict['chap_19']['text']
        tts = alice_dict['chap_19']['tts']
        req_save["save"] = 'chap_19'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_18_1.RUN" in intent:
        text = alice_dict['chap_18_2']['text']
        tts = alice_dict['chap_18_2']['tts']
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_2(req_save, command, intent, user_id):
    if "chap_18_2" in intent:
        text = alice_dict['chap_21']['text']
        tts = alice_dict['chap_21']['tts']
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19(req_save, command, intent, user_id):
    if "chap_19.TABLE" in intent:
        text = alice_dict['chap_19_1']['text']
        tts = alice_dict['chap_19_1']['tts']
        req_save["save"] = 'chap_19_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_19.FLOOR" in intent:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_19.BED" in intent:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_1(req_save, command, intent, user_id):
    if "chap_19_1.WALLET" in intent:
        text = alice_dict['chap_19_1_1']['text']
        tts = alice_dict['chap_19_1_1']['tts']
        req_save["save"] = 'chap_19_1_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_19_1.FLOOR" in intent:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_19_1.BED" in intent:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_2(req_save, command, intent, user_id):
    text = alice_dict['chap_19_3']['text']
    tts = alice_dict['chap_19_3']['tts']
    new_save = {'accept': 'chap_19_3', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_19_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_19_1_1(req_save, command, intent, user_id):
    if "chap_19_1_1.FLOOR" in intent:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_19_1_1.BED" in intent:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_3(req_save, command, intent, user_id):
    text = alice_dict['chap_20']['text']
    tts = alice_dict['chap_20']['tts']
    new_save = {'accept': 'chap_20', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_19_3", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_21(req_save, command, intent, user_id):
    if "chap_21" in intent:
        text = alice_dict['chap_21']['text']
        tts = alice_dict['chap_21']['tts']
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_x(req_save, command, intent, user_id):
    text = alice_dict['chap_21_1']['text']
    tts = alice_dict['chap_21_1']['tts']
    text_reject = alice_dict['chap_21_2']['text']
    tts_reject = alice_dict['chap_21_2']['tts']
    new_save = {'accept': 'chap_21_1', 'reject': 'chap_21_2'}
    return confirm_reject_handler(req_save, "chap_21_x.HIDE", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap_21_x.REJECT")


def chap_21_1(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_9'}})
    text = alice_dict['chap_9']['text']
    tts = alice_dict['chap_9']['tts']
    new_save = {'accept': 'chap_9', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_21_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)

def chap_21_2(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22', "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
    text= '''Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.\n
Начать побег сейчас или во время обеда?'''
    tts='''Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня. Начать побег сейчас или во время обеда?'''
    new_save = {'accept': 'chap_22', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_21_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_22(req_save, command, intent, user_id):
    if "chap_22.DINNER" in intent:
        text = alice_dict['chap_22_1']['text']
        tts = alice_dict['chap_22_1']['tts']
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_22.NOW" in intent:
        text = alice_dict['chap_22_2']['text']
        tts = alice_dict['chap_22_2']['tts']
        req_save['save'] = 'chap_22_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_22_1(req_save, command, intent, user_id):
    text = alice_dict['chap_24']['text']
    tts = alice_dict['chap_24']['tts']
    card = {
        "type": "ItemsList",
        "header": {
            "text": text,
        },
        "items": [
            {
                "image_id": "1030494/628705743a5ab80c90ea",
                "title": "Самодельный топор",
                "description": "Хорош для всех рубящих ударов",
            },
            {
                "image_id": "1030494/628705743a5ab80c90ea",
                "title": "Самодельная кирка",
                "description": "Хорошо подходит для копания шахт",
            },
        ],
        "footer": {
            "text": "Необходимо определить, что изготовить - самодельный топор или самодельную кирку.",
            }
        }
    new_save = {'accept': 'chap_24', 'reject': ''}
    return confirm_reject_handler_with_card(req_save, "chap_22_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save, card=card)


def chap_22_2(req_save, command, intent, user_id):
    if "chap_22_2.ENTER" in intent:
        text = alice_dict['chap_23_2']['text']
        tts = alice_dict['chap_23_2']['tts']
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_22_2.LOOK_AROUND" in intent:
        text = alice_dict['chap_23']['text']
        tts = alice_dict['chap_23']['tts']
        req_save['save'] = 'chap_23'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23(req_save, command, intent, user_id):
    if "chap_23.ENTER" in intent:
        text = alice_dict['chap_23_2']['text']
        tts = alice_dict['chap_23_2']['tts']
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_23.DINNER" in intent:
        text = alice_dict['chap_22_1']['text']
        tts = alice_dict['chap_22_1']['tts']
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23_1(req_save, command, intent, user_id):  # == chap_22_1
    if "chap_23_1" in intent:
        text = alice_dict['chap_24']['text']
        tts = alice_dict['chap_24']['tts']
        req_save['save'] = 'chap_24'
        card = {
        "type": "ItemsList",
        "header": {
            "text": text,
        },
        "items": [
            {
                "image_id": "1030494/628705743a5ab80c90ea",
                "title": "Самодельный топор",
                "description": "Хорош для всех рубящих ударов",
            },
            {
                "image_id": "1030494/628705743a5ab80c90ea",
                "title": "Самодельная кирка",
                "description": "Хорошо подходит для копания шахт",
            },
        ],
        "footer": {
            "text": "Необходимо определить, что изготовить - самодельный топор или самодельную кирку.",
            }
        }
        return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
    else:
        return message_help(req_save, version)  # можно удалить


def chap_23_2(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22'}})
    text = alice_dict['chap_22']['text']
    tts = alice_dict['chap_22']['tts']
    new_save = {'accept': 'chap_22', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_23_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_24(req_save, command, intent, user_id):
    if "chap_24.PICKAXE" in intent:
        text = alice_dict['chap_24_1']['text']
        tts = alice_dict['chap_24_1']['tts']
        req_save['save'] = 'chap_24_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_24.AXE" in intent:
        text = alice_dict['chap_24_2']['text']
        tts = alice_dict['chap_24_2']['tts']
        req_save['save'] = 'chap_24_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24_1(req_save, command, intent, user_id):
    text = alice_dict['chap_25']['text']
    tts = alice_dict['chap_25']['tts']
    new_save = {'accept': 'chap_25', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_24_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_24_2(req_save, command, intent, user_id):
    text = alice_dict['chap_25']['text']
    tts = alice_dict['chap_25']['tts']
    new_save = {'accept': 'chap_25', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_24_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_25(req_save, command, intent, user_id):
    text = alice_dict['chap_25_1']['text']
    tts = alice_dict['chap_25_1']['tts']
    text_reject = alice_dict['chap_25_2']['text']
    tts_reject = alice_dict['chap_25_2']['tts']
    new_save = {'accept': 'chap_25_1', 'reject': 'chap_23_2'}
    return confirm_reject_handler(req_save, "chap_25.CONFIRM", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap_25.REJECT")


def chap_25_1(req_save, command, intent, user_id):
    if "chap_25_1.BREAK" in intent:
        req_save['save'] = 'chap_23_2'
        text = alice_dict['chap_25_1']['text']
        tts = alice_dict['chap_25_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "chap_25_1.WAIT" in intent:
        req_save['save'] = 'chap_25_1_2'
        text = alice_dict['chap_25_1_2']['text']
        tts = alice_dict['chap_25_1_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_1_1(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22'}})
    text = alice_dict['chap_22']['text']
    tts = alice_dict['chap_22']['tts']
    new_save = {'accept': 'chap_22', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_25_1_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap_25_1_2(req_save, command, intent, user_id):
    if "chap_25_1_2" in intent:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": req_save['save'], "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
        text = '''Добро пожаловать во вторую главу "Приключения только начинаются!".
        Неизвестно, сколько часов вы уже бежите.
        Хотите остановиться?'''
        tts = '''Добро пожаловать во вторую главу "Приключения только начинаются!".
        Неизвестно, сколько часов вы уже бежите.
        Хотите остановиться?'''
        req_save['save'] = 'chap2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_2(req_save, command, intent, user_id):
    text = alice_dict['chap_22']['text']
    tts = alice_dict['chap_22']['tts']
    req_save["save"] = 'chap_22'
    new_save = {'accept': 'chap_22', 'reject': ''}
    return confirm_reject_handler(req_save, "chap_25_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)
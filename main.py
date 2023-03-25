import re
from urllib import request
from config import *
from dialogs import message_sent, d_start_0
from help_dialogs import message_help, confirm_reject_handler

version = "1.0"


# Сделать сохранения, сделать ifы

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
            text = 'Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'
            tts = 'Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'
            return d_start_0(text, tts, version)
        elif COLLECTION.find_one({"id": user_id})["save"] == "":
            text = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            tts = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            return d_start_0(text, tts, version)
        else:
            text = "Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"
            tts = "Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"
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
        if req_save["save"] == "start":
            return start_1(req_save, command, intent)

        elif req_save["save"] == "start_1":
            return start_2(req_save, command, intent)

        elif req_save["save"] == "start_2":
            return start_3(req_save, command, intent)

        elif req_save["save"] == "start_3" or req_save["save"] == "start_3_1":
            return chap(req_save, command, intent)

        elif req_save["save"] == "chap":
            return chap_1(req_save, command, intent)

        elif req_save["save"] == "chap_1" or req_save["save"] == "chap_1_1":
            return chap_2(req_save, command, intent)

        elif req_save["save"] == "chap_2":
            return chap_3(req_save, command, intent)

        elif req_save["save"] == "chap_3":
            return chap_4(req_save, command, intent)

        elif req_save["save"] == "chap_4_1":
            return chap_4_1_1(req_save, command, intent)

        elif req_save["save"] == "chap_4_1_1":
            return chap_4_1_x(req_save, command, intent)

        elif req_save["save"] == "chap_4_1_2" or req_save["save"] == "chap_4_1_4" or req_save["save"] == "chap_4_1_7" or req_save["save"] == "chap_4_1_0":
            return chap_5(req_save, command, intent)

        elif req_save["save"] == "chap_4_1_3":
            return chap_4_1_3_x(req_save, command, intent)

        elif req_save["save"] == "chap_4_2":
            return chap_4_2_1(req_save, command, intent)

        elif req_save["save"] == "chap_4_1_3_1" or req_save["save"] == "chap_4_1_3_2":
            return start_1(req_save, command, intent)

        elif req_save["save"] == "chap_4_1_3_3" or req_save["save"] == "chap_4_2_1" or req_save["save"] == "chap_5":
            return chap_5_1(req_save, command, intent)

        elif req_save["save"] == "chap_5_1":
            return chap_6(req_save, command, intent)

        elif req_save["save"] == "chap_6":
            return chap_6_x(req_save, command, intent)

        elif req_save["save"] == "chap_6_1" or req_save["save"] == "chap_6_2":
            return chap_6_0_x(req_save, command, intent)

        elif req_save["save"] == "chap_6_0" or req_save["save"] == "chap_6_0_1":
            return chap_7(req_save, command, intent)

        elif req_save["save"] == "chap_7":
            return chap_7_x(req_save, command, intent)

        elif req_save["save"] == "chap_7_1":
            return chap_8(req_save, command, intent)

        elif req_save["save"] == "chap_7_2" or req_save["save"] == "chap_7_3" or req_save["save"] == "chap_7_0":
            return chap_7_end(req_save, command, intent)

        elif req_save["save"] == "chap_8":
            return chap_9(req_save, command, intent)

        elif req_save["save"] == "chap_9":
            return chap_10(req_save, command, intent)

        elif req_save["save"] == "chap_10":
            return chap_10_x(req_save, command, intent)

        elif req_save["save"] == "chap_10_1" or req_save["save"] == "chap_10_2" or req_save["save"] == "chap_10_0":
            return chap_11_x(req_save, command, intent)

        elif req_save["save"] == "chap_11_2_1" or req_save["save"] == "chap_14":
            return chap_14(req_save, command, intent)

        elif req_save["save"] == "chap_11_2":
            return chap_11_2_1(req_save, command, intent)

        elif req_save["save"] == "chap_11":
            return chap_12_x(req_save, command, intent)

        elif req_save["save"] == "chap_11_1":
            return chap_11_1(req_save, command, intent)

        elif req_save["save"] == "chap_15":
            return chap_15(req_save, command, intent)

        elif req_save["save"] == "chap_12":
            return chap_13(req_save, command, intent)

        elif req_save["save"] == "chap_12_1":
            return chap_13_1(req_save, command, intent)

        elif req_save["save"] == "chap_13":
            return chap_13(req_save, command, intent)

        elif req_save["save"] == "chap_13_0" or req_save["save"] == "chap_13_4" or req_save["save"] == "chap_17" :
            return chap_13_0(req_save, command, intent)

        elif req_save["save"] == "chap_13_2":
            return chap_13_2(req_save, command, intent)

        elif req_save["save"] == "chap_18":
            return chap_18(req_save, command, intent)

        elif req_save["save"] == "chap_13_3":
            return chap_13_3(req_save, command, intent)

        elif req_save["save"] == "chap_16" or req_save["save"] == "chap_11_0":
            return chap_16(req_save, command, intent)

        elif req_save["save"] == "chap_18_1":
            return chap_18_1(req_save, command, intent)

        elif req_save["save"] == "chap_18_2":
            return chap_18_2(req_save, command, intent)

        elif req_save["save"] == "chap_19":
            return chap_19(req_save, command, intent)

        elif req_save["save"] == "chap_19_1":
            return chap_19_1(req_save, command, intent)

        elif req_save["save"] == "chap_19_2":
            return chap_19_2(req_save, command, intent)

        elif req_save["save"] == "chap_19_3":
            return chap_19_3(req_save, command, intent)

        elif req_save["save"] == "chap_19_1_1":
            return chap_19_1_1(req_save, command, intent)

        elif req_save["save"] == "chap_21":
            return chap_21_x(req_save, command, intent)

        elif req_save["save"] == "chap_20":
            return chap_21(req_save, command, intent)

        elif req_save["save"] == "chap_21_1":
            return chap_21_1(req_save, command, intent)

        elif req_save["save"] == "chap_21_2":
            return chap_21_2(req_save, command, intent)

        elif req_save["save"] == "chap_22":
            return chap_22(req_save, command, intent)

        elif req_save["save"] == "chap_22_1":
            return chap_22_1(req_save, command, intent)

        elif req_save["save"] == "chap_22_2":
            return chap_22_2(req_save, command, intent)

        elif req_save["save"] == "chap_24":
            return chap_24(req_save, command, intent)

        elif req_save["save"] == "chap_23":
            return chap_23(req_save, command, intent)

        elif req_save["save"] == "chap_23_2":
            return chap_23_2(req_save, command, intent)

        elif req_save["save"] == "chap_24_1":
            return chap_24_1(req_save, command, intent)

        elif req_save["save"] == "chap_24_2":
            return chap_24_2(req_save, command, intent)

        elif req_save["save"] == "chap_25":
            return chap_25(req_save, command, intent)

        elif req_save["save"] == "chap_25_1":
            return chap_25_1(req_save, command, intent)

        elif req_save["save"] == "chap_25_2":
            return chap_25_2(req_save, command, intent)

        elif req_save["save"] == "chap25_1_2":
            return chap_25_1_2(req_save, command, intent)

        else:
            return message_sent(text="чо", tts="чо", version=version, save=req_save)


def start_1(req_save, command, intent):
    COMMANDS = ['начать', 'вперед']
    text = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли. Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений. Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'
    tts = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли. Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений. Сегодня вам нужно пойти торговать на рынке.'
    new_save = {'accept': 'start_1', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def start_2(req_save, command, intent):
    COMMANDS = ['пойти на рынок', 'отправиться на рынок', 'рынок', 'пошли']
    text = 'Но однажды, когда вы были на рынке, чтобы продать свой урожай, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении. Проследовать за полицией или попробовать сбежать?'
    tts = 'Но однажды, когда вы были на рынке, чтобы продать свой урожай, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении. Проследовать за полицией или попробовать сбежать?'
    new_save = {'accept': 'start_2', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def start_3(req_save, command, intent):
    COMMANDS = ['пойти с полицией', 'полиция', 'пойти', 'проследовать', 'полицией', 'пройти', 'пошли', 'иду']
    COMMANDS_REJECT = ['сбежать', 'убежать', 'бег', 'побег']

    text = 'Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Мотать срок?'
    tts = 'Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Мотать срок?'
    text_REJECT = 'Вас догоняет один из полицейских и заламывает руки. Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Вы потеряли 1 единицу здоровья. Мотать срок?'
    tts_REJECT = "Вас догоняет один из полицейских и заламывает руки. Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Вы потеряли 1 единицу здоровья. Мотать срок?"
    new_save = {'accept': 'start_3', 'reject': 'start_3_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap(req_save, command, intent):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи']
    text = 'В тюрьме вы понимаете, что жизнь здесь не так проста, как казалась. Вы оказываетесь среди преступников, которые ненавидят вас и считают "мелким фермером". Они издеваются над вами, отбирают еду и уважают только тех, кто сильнее и жестче. Здоровье: 6/10 Сила: 2 Мана: 0 Для того, чтобы сделать свой досуг более интересным, выберите, чем заняться: спортом или отдыхом в виде сна.'
    tts = 'В тюрьме вы понимаете, что жизнь здесь не так проста, как казалась. Вы оказываетесь среди преступников, которые ненавидят вас и считают "мелким фермером". Они издеваются над вами, отбирают еду и уважают только тех, кто сильнее и жестче. Здоровье: 6 из 10 sil <[200]> Сила: 2 sil <[200]> Мана: 0 sil <[200]> Для того, чтобы сделать свой досуг более интересным, выберите, чем заняться: спортом или отдыхом в виде сна.'
    new_save = {'accept': 'chap', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_1(req_save, command, intent):
    COMMANDS = ['спорт']
    COMMANDS_1 = ['спать']

    text = 'Среди различных вариантов занятий, доступных вам в тюрьме, вы решили заняться спортом. Здоровье: 6/10 Сила: 4 Мана: 0 Продолжить мотать срок?'
    tts = 'Среди различных вариантов занятий, доступных вам в тюрьме, вы решили заняться спортом. Здоровье: 6/10 Сила: 4 Мана: 0 Продолжить мотать срок?'

    text_1 = 'Вы были вынуждены приспосабливаться к жизни за решеткой, но вы были слишком измучены, чтобы сосредоточиться на чем-то другом, кроме как на сне. Здоровье: 10/10 Сила: 2 Мана: 0 Продолжить мотать срок?'
    tts_1 = 'Вы были вынуждены приспосабливаться к жизни за решеткой, но вы были слишком измучены, чтобы сосредоточиться на чем-то другом, кроме как на сне. Здоровье: 10/10 Сила: 2 Мана: 0 Продолжить мотать срок?'
    if command in COMMANDS:
        req_save["power"] = 4
        req_save["save"] = "chap_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_1:
        req_save["health"] = 10
        req_save["save"] = "chap_1_1"
        return message_sent(text=text_1, tts=tts_1, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_2(req_save, command, intent):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи']
    text = 'Наступает день выбора работы. Вам достается работа в мастерской. Начать работать?'
    tts = 'Наступает день выбора работы. Вам достается работа в мастерской. Начать работать?'
    new_save = {'accept': 'chap_2', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_3(req_save, command, intent):
    COMMANDS = ['']
    COMMANDS_REJECT = ['']

    text = 'Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?". Соврать или отказаться?'
    tts = 'Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?". Соврать или отказаться?'
    text_REJECT = 'Вас толкает начальник и грозит посадить в карцер, вы отправляетесь на работу Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?". Соврать или отказаться?'
    tts_REJECT = 'Вас толкает начальник и грозит посадить в карцер, вы отправляетесь на работу Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?". Соврать или отказаться?'
    new_save = {'accept': 'chap_3', 'reject': 'chap_3'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap_4(req_save, command, intent):
    COMMANDS_TRUE = ['отказаться']
    COMMANDS_LIE = ['солгать']
    if command in COMMANDS_TRUE:
        req_save["save"] = "chap_4_1"
        text = 'Преступник: "Ты думаешь, что можешь отказаться от меня? Я сделаю твою жизнь адом, если ты не будешь слушаться меня". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        tts = 'Преступник: "Ты думаешь, что можешь отказаться от меня? Я сделаю твою жизнь адом, если ты не будешь слушаться меня". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_LIE:
        req_save["health"] -= 2
        req_save["save"] = "chap_4_2"
        text = 'Вы решаете соврать и согласиться с предложением преступника. Преступник резко поднялся со стула и подошел к вам, ухмыляясь. Вы попытались отойти назад, но он настиг вас и ударил рукой. Минус 2 единицы здоровья. Преступник: "Ты думал, что я не пойму, что ты врешь, мелкий? Я тебя здесь научу говорить правду, это первое и последнее предупреждение". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        tts = 'Вы решаете соврать и согласиться с предложением преступника. Преступник резко поднялся со стула и подошел к вам, ухмыляясь. Вы попытались отойти назад, но он настиг вас и ударил рукой. Минус 2 единицы здоровья. Преступник: "Ты думал, что я не пойму, что ты врешь, мелкий? Я тебя здесь научу говорить правду, это первое и последнее предупреждение". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_1(req_save, command, intent):
    COMMANDS = ['']
    text = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость и решаете вернуться в свою камеру для отдыха. Вы открываете дверь своей камеры и видите, что там уже находятся двое заключенных, один из которых был тот преступник, которому вы отказали в помощи. Вы понимаете, что они настроены решительно и не будут договариваться с вами. Что лучше сделать: "Ударить заключенного", "Убежать", "Закричать".'
    tts = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость и решаете вернуться в свою камеру для отдыха. Вы открываете дверь своей камеры и видите, что там уже находятся двое заключенных, один из которых был тот преступник, которому вы отказали в помощи. Вы понимаете, что они настроены решительно и не будут договариваться с вами. Что лучше сделать: "Ударить заключенного", "Убежать", "Закричать"'
    new_save = {'accept': 'chap_4_1_1', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_4_1_x(req_save, command, intent):
    COMMANDS_RUN = ['убежать']
    COMMANDS_HIT = ['ударить']
    COMMANDS_SHOUT = ['закричать']
    if command in COMMANDS_RUN:
        req_save["save"] = "chap_4_1_2"
        req_save["health"] -= 1
        text = 'Вы резко поворачиваетесь, чтобы убежать, но один из заключенных быстро подбегает к вам и хватает за руку. Вы пытаетесь вырваться, но он удерживает вас и начинает толкать к стене. Вы чувствуете удар в голову, и все исчезает перед глазами. Минус 1 единица здоровья. Очнуться?'
        tts = 'Вы резко поворачиваетесь, чтобы убежать, но один из заключенных быстро подбегает к вам и хватает за руку. Вы пытаетесь вырваться, но он удерживает вас и начинает толкать к стене. Вы чувствуете удар в голову, и все исчезает перед глазами. Минус 1 единица здоровья. Очнуться?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_SHOUT:
        req_save["save"] = "chap_4_1_4"
        req_save["health"] -= 3
        text = 'Вы попытаетесь закричать, чтобы привлечь внимание охранников, но один из заключенных быстро закрывает вам рот. Вы начинаете чувствовать себя задыхающимся и беспомощным, пытаясь освободиться от его хватки. Другой заключенный в это время начинает обыскивать ваши карманы и забирает все ценности. Вы теряете сознание. Минус 3 единицы здоровья. Очнуться?'
        tts = 'Вы попытаетесь закричать, чтобы привлечь внимание охранников, но один из заключенных быстро закрывает вам рот. Вы начинаете чувствовать себя задыхающимся и беспомощным, пытаясь освободиться от его хватки. Другой заключенный в это время начинает обыскивать ваши карманы и забирает все ценности. Вы теряете сознание. Минус 3 единицы здоровья. Очнуться?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_HIT:
        if req_save["power"] == 4:  # Поменять на показатель здоровья / силы
            req_save["save"] = "chap_4_1_3"
            text = 'Ваши занятия спортом не прошли даром: вы бьете одного заключенного, тот сразу же теряет сознание. Другой преступник, увидев это, убегает. Вы думаете, что нужно сделать с заключенным, находящимся в отключке. Теперь что-то нужно сделать с заключенным: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру".'
            tts = 'Ваши занятия спортом не прошли даром: вы бьете одного заключенного, тот сразу же теряет сознание. Другой преступник, увидев это, убегает. Вы думаете, что нужно сделать с заключенным, находящимся в отключке. Теперь что-то нужно сделать с заключенным: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру"'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            req_save["save"] = "chap_4_1_7"
            req_save["health"] -= 2
            text = '''
            Вы чувствуете, что вам нужно защитить себя и быстро делаете решительный шаг, пытаясь ударить преступника, 
            которому отказали в помощи. Однако он быстро увернулся, и вы промахнулись, 
            потеряв при этом равновесие и ударившись головой. Вы теряете сознание. 
            Минус 2 единицы здоровья. Очнуться?
            '''
            tts = "Вы чувствуете, что вам нужно защитить себя и быстро делаете решительный шаг, пытаясь ударить преступника, которому отказали в помощи. Однако он быстро увернулся, и вы промахнулись, потеряв при этом равновесие и ударившись головой. Вы теряете сознание. Минус 2 единицы здоровья. Очнуться?"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_2_1(req_save, command, intent):
    COMMANDS = ['']
    text = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость. Вы направляетесь на перекличку, а затем решаете вернуться в свою камеру, чтобы отдохнуть. Лечь спать?'
    tts = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость. Вы направляетесь на перекличку, а затем решаете вернуться в свою камеру, чтобы отдохнуть. Лечь спать?'
    new_save = {'accept': 'chap_5_1', 'reject': 'chap_5_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_4_1_3_x(req_save, command, intent): 
    COMMANDS_1 = ['охрана']
    COMMANDS_2 = ['оставить']
    COMMANDS_3 = ['убрать']
    if command in COMMANDS_1:
        req_save["save"] = "chap_4_1_3_1"
        text = 'Вы зовете охрану. Вас обвиняют в нападении на заключенного, и теперь вы находитесь в карцере. Начать сначала?'
        tts = 'Вы зовете охрану. Вас обвиняют в нападении на заключенного, и теперь вы находитесь в карцере. Начать сначала?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save["save"] = "chap_4_1_3_2"
        text = 'Мимо вашей камеры проходит охранник, увидев лежачего заключенного, вас обвиняют в нападении, теперь вы находитесь в карцере. Начать сначала?'
        tts = 'Мимо вашей камеры проходит охранник, увидев лежачего заключенного, вас обвиняют в нападении, теперь вы находитесь в карцере. Начать сначала?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        req_save["save"] = "chap_4_1_3_3"
        text = 'Вы осматриваетесь вокруг и не замечаете охранников, решаете перенести заключенного в другую камеру. Но когда вы выходите на перекличку, надзиратели находят одного из заключенных без сознания и обвиняют владельца камеры в нападении на него. Вам нужно восстановить силы. Лечь спать?'
        tts = 'Вы осматриваетесь вокруг и не замечаете охранников, решаете перенести заключенного в другую камеру. Но когда вы выходите на перекличку, надзиратели находят одного из заключенных без сознания и обвиняют владельца камеры в нападении на него. Вам нужно восстановить силы. Лечь спать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_5(req_save, command, intent):
    COMMANDS = ['очнуться']
    if command in COMMANDS:
        req_save["save"] = "chap_5"
        text = 'Когда вы приходите в сознание, вы лежите на полу в своей камере. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов. Вам нужно восстановить силы. Лечь спать?'
        tts = 'Когда вы приходите в сознание, вы лежите на полу в своей камере. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов. Вам нужно восстановить силы. Лечь спать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = "chap_4_1_0"
        return message_help(req_save, version)


def chap_5_1(req_save, command, intent):
    COMMANDS = ['спать']
    if command in COMMANDS:
        req_save["save"] = "chap_5_1"
        text = 'В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере. Мотать срок.'
        tts = 'В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере. Мотать срок.'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_6(req_save, command, intent):  # Без сохранения
    COMMANDS = ['']
    text = 'Однажды, работая в мастерской, вы слышите крик заключенного из соседней камеры. Что думаете, стоит ли посмотреть?'
    tts = 'Однажды, работая в мастерской, вы слышите крик заключенного из соседней камеры. Что думаете, стоит ли посмотреть?'
    new_save = {'accept': 'chap_6', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_6_x(req_save, command, intent):  # Без сохранения
    COMMANDS_1 = ['посмотреть']
    COMMANDS_2 = ['продолжить']
    text = 'Вы решили посмотреть, что происходит в соседней камере, и замечаете, что двое других заключенных избивают третьего. Помочь или продолжить работать?'
    tts = 'Вы решили посмотреть, что происходит в соседней камере, и замечаете, что двое других заключенных избивают третьего. Помочь или продолжить работать?'
    text_reject = 'Вы продолжаете работать, но крик усиливается. Помочь или продолжить работать?'
    tts_reject = 'Вы продолжаете работать, но крик усиливается. Помочь или продолжить работать?'
    new_save = {'accept': 'chap_6_1', 'reject': 'chap_6_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts, reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject, tts_reject=tts_reject, new_save=new_save)


def chap_6_0_x(req_save, command, intent):  # Без сохранения
    COMMANDS_1 = ['помочь']
    COMMANDS_2 = ['продолжить работать', 'работать']
    if command in COMMANDS_1:
        req_save["save"] = 'chap_6_0'
        req_save["other"]["trader"] = True
        text = "Решив, что нельзя оставлять человека в опасности вы отправились в мастерскую и взяв тяжелый предмет вернулись в его камеру. Пригрозив нападавшим вы заставили их отойти от заключенного. Они бросаются к выходу, и вы оказываетесь наедине с заключенным, которого они избивали." \
               "Оказалось, что он был торговцем, который тайно занимался торговлей внутри тюрьмы. Он благодарит вас за помощь и говорит, что готов оказать вам любую услугу, если вы будете когда-нибудь в чем-то нуждаться." \
               "Продолжить мотать срок?"
        tts = "Решив, что нельзя оставлять человека в опасности вы отправились в мастерскую и взяв тяжелый предмет вернулись в его камеру. Пригрозив нападавшим вы заставили их отойти от заключенного. Они бросаются к выходу, и вы оказываетесь наедине с заключенным, которого они избивали." \
              "Оказалось, что он был торговцем, который тайно занимался торговлей внутри тюрьмы. Он благодарит вас за помощь и говорит, что готов оказать вам любую услугу, если вы будете когда-нибудь в чем-то нуждаться." \
              "Продолжить мотать срок?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save["save"] = 'chap_6_0_1'
        text = "Вы решаете продолжить работу. Крик прекращается, и, оглянувшись назад, вы видите, как надзиратель уводит двух заключенных, а за ними на носилках несут третьего." \
               "Продолжить мотать срок?"
        tts = "Вы решаете продолжить работу. Крик прекращается, и, оглянувшись назад, вы видите, как надзиратель уводит двух заключенных, а за ними на носилках несут третьего." \
              "Продолжить мотать срок?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7(req_save, command, intent):
    COMMANDS = ['продолжить мотать']
    text = 'В течение следующих месяцев ничего интересного не происходило, однако однажды во время обеда заключенные начали избивать другого заключенного.' \
           'Помочь заключенному?'
    tts = 'В течение следующих месяцев ничего интересного не происходило, однако однажды во время обеда заключенные начали избивать другого заключенного.' \
          'Помочь заключенному?'
    new_save = {'accept': 'chap_7', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_7_x(req_save, command, intent):
    COMMANDS_TRUE = ['помочь']
    COMMANDS_FALSE = ['продолжить смотреть']
    if command in COMMANDS_TRUE:
        if req_save["health"] > 3:
            req_save["save"] = "chap_7_1"
            text = 'Вы вмешались в драку, но это не привело к ничему хорошему, в результате заключенные начали бить и вас.' \
                   'Вы теряете 3 единицы здоровья.' \
                   'Отправиться в лазарет?'
            tts = 'Вы вмешались в драку, но это не привело к ничему хорошему, в результате заключенные начали бить и вас.' \
                  'Вы теряете 3 единицы здоровья.' \
                  'Отправиться в лазарет?'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            req_save["save"] = "chap_7_2"
            text = "Вы вмешались в драку, но это не привело к ничему хорошему, в результате заключенные начали бить и вас." \
                   "Вы теряете 3 единицы здоровья и погибаете." \
                   "Начать сначала?"
            tts = "Вы вмешались в драку, но это не привело к ничему хорошему, в результате заключенные начали бить и вас." \
                  "Вы теряете 3 единицы здоровья и погибаете." \
                  "Начать сначала?"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_FALSE:
        req_save["save"] = "chap_7_3"
        text = "Вы не вмешиваетесь в драку, но появились надзиратели, которые посчитали, что вы являетесь соучастником, и отправили вас в карцер." \
               "Начать сначала?"
        tts = "Вы не вмешиваетесь в драку, но появились надзиратели, которые посчитали, что вы являетесь соучастником, и отправили вас в карцер." \
              "Начать сначала?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7_end(req_save, command, intent): 
    COMMANDS_TRUE = ['начать сначала']
    if command in COMMANDS_TRUE:
        req_save["save"] = 'start_1'
        text = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.' \
               'Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.' \
               'Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'
        tts = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.' \
              'Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.' \
              'Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = "chap_7_0"
        return message_help(req_save, version)


def chap_8(req_save, command, intent):
    # СОХРАНЕНИЕ
    COMMANDS = ['отправиться в лазарет']
    COMMANDS_REJECT = ['']
    text = 'После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.' \
           'Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за последствия своих действий.' \
           'Сохранение игры... Прогресс сохранен.' \
           'Желаете продолжить?'
    tts = 'После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.' \
          'Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за последствия своих действий.' \
          'Сохранение игры... Прогресс сохранен.' \
          'Желаете продолжить?'
    text_REJECT = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.' \
                  'Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.' \
                  'Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'
    tts_REJECT = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.' \
                 'Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.' \
                 'Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'
    new_save = {'accept': 'chap_8', 'reject': 'start_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap_9(req_save, command, intent):
    COMMANDS_TRUE = ['продолжить']
    text = "Через некоторое время вас выписывают из лазарета, и вы отправляетесь обратно в свою камеру, " \
           "но замечаете, что заработанные вами деньги пропали." \
           "Опечаленный, вы садитесь на койку и не понимаете, что делать дальше. Вдруг в камеру заходит заключенный, садиться напротив вас и говорит: 'Спасибо за то, что вмешался в драку. Можешь ли ты сказать мне свое имя?'"
    tts = "Через некоторое время вас выписывают из лазарета, и вы отправляетесь обратно в свою камеру, " \
          "но замечаете, что заработанные вами деньги пропали." \
          "Опечаленный, вы садитесь на койку и не понимаете, что делать дальше. Вдруг в камеру заходит заключенный, садиться напротив вас и говорит: 'Спасибо за то, что вмешался в драку. Можешь ли ты сказать мне свое имя?'"
    new_save = {'accept': 'chap_9', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_TRUE, text=text, tts=tts, new_save=new_save)


def chap_10(req_save, command, intent):
    # проверка на имя
    req_save["save"] = 'chap_10'
    req_save["name"] = command
    text = f'"Приятно познакомиться, {req_save["name"]}. Меня зовут Михаил. Я знаю, как мы можем выбраться отсюда", - говорит Михаил, глядя на вас загадочным взглядом.'
    tts = f'"Приятно познакомиться, {req_save["name"]}. Меня зовут Михаил. Я знаю, как мы можем выбраться отсюда", - говорит Михаил, глядя на вас загадочным взглядом.'
    return message_sent(text=text, tts=tts, save=req_save, version=version)


def chap_10_x(req_save, command, intent):
    COMMANDS_1 = ['почему ты хочешь помочь мне']
    COMMANDS_2 = ['и как же']
    if command in COMMANDS_1:
        text = '"Ты помог мне, а я помогу тебе. Для начала тебе нужно принести мне рукоятку, железную заточку и веревку. С их помощью мы сможем сделать самодельную кирку. Когда найдешь все предметы, заходи ко мне в камеру. Мы начнем планировать побег".' \
               'Куда стоит пойти первым делом? В столовую или на работу.'
        tts = '"Ты помог мне, а я помогу тебе. Для начала тебе нужно принести мне рукоятку, железную заточку и ' \
              'веревку. С их помощью мы сможем сделать самодельную кирку. Когда найдешь все предметы, заходи ко мне в ' \
              'камеру. Мы начнем планировать побег".' \
              'Куда стоит пойти первым делом? В столовую или на работу.'
        req_save["save"] = "chap_10_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = '"Для начала тебе нужно принести мне рукоятку, железную заточку и веревку. С их помощью мы сможем сделать самодельную кирку. Когда найдешь все предметы, заходи ко мне в камеру. Мы начнем планировать побег".'
        tts = '"Для начала тебе нужно принести мне рукоятку, железную заточку и веревку. С их помощью мы сможем сделать самодельную кирку. Когда найдешь все предметы, заходи ко мне в камеру. Мы начнем планировать побег".'
        req_save["save"] = "chap_10_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_x(req_save, command, intent):
    COMMANDS_1 = ['пойти в столовую']
    COMMANDS_2 = ['пойти на работу']
    if command in COMMANDS_1:
        if req_save['other']['trader']:
            text = "Зайдя в столовую вы видите торговца, которому спасли жизнь. Хотите подойти к нему?"
            tts = "Зайдя в столовую вы видите торговца, которому спасли жизнь. Хотите подойти к нему?"
            req_save['save'] = 'chap_11_1'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            text = 'Вы подходите к заключенному, чтобы спросить про железную заточку. Заключенный отвечает: "Да, я могу продать тебе заточку." Если вы решите купить заточку, то вы потратите все свои деньги, но у вас нет другого выбора.' \
                   'Вы готовы купить заточку?'
            tts = 'Вы подходите к заключенному, чтобы спросить про железную заточку. Заключенный отвечает: "Да, я могу продать тебе заточку." Если вы решите купить заточку, то вы потратите все свои деньги, но у вас нет другого выбора.' \
                  'Вы готовы купить заточку?'
            req_save['save'] = 'chap_11_2'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
        tts = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_2_1(req_save, command, intent):
    COMMANDS_1 = ['купить заточку']
    if command in COMMANDS_1:
        req_save["other"]["knife"] = True
        req_save["save"] = 'chap_11_2_1'
        text = 'Вы купили заточку. Теперь осталось достать только веревку и рукоятку.' \
               'Хотите осмотреться или пойти на работу?'
        tts = 'Вы купили заточку. Теперь осталось достать только веревку и рукоятку.' \
              'Хотите осмотреться или пойти на работу?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_1(req_save, command, intent):
    COMMANDS_1 = ['подойти к торговцу']
    text = 'Вы спросили у торговца, сможет ли он достать железную заточку. Торговец ответил: "Конечно, это малая услуга для моего спасителя".' \
           ' Затем он отдал ее вам. Теперь осталось достать только веревку и рукоятку. Хотите осмотреться или пойти на работу'
    tts = 'Вы спросили у торговца, сможет ли он достать железную заточку. Торговец ответил: "Конечно, это малая услуга для моего спасителя".' \
          ' Затем он отдал ее вам. Теперь осталось достать только веревку и рукоятку. Хотите осмотреться или пойти на работу'
    req_save["other"]["knife"] = True
    new_save = {'accept': 'chap_14', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  new_save=new_save)


def chap_14(req_save, command, intent):
    COMMANDS_1 = ['осмотреться']
    COMMANDS_2 = ['пойти на работу']
    if command in COMMANDS_1:
        req_save["save"] = "chap_15"
        text = 'Вы внимательно осмотрелись, но не заметили ничего ценного.' \
               'Отправиться на работу?'
        tts = 'Вы внимательно осмотрелись, но не заметили ничего ценного.' \
              'Отправиться на работу?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
        tts = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = 'chap_14'
        return message_help(req_save, version)


def chap_15(req_save, command, intent):
    COMMANDS = ['пойти на работу']
    text = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
    tts = 'Вы пришли в мастерскую. Хотите осмотреться или сделать рукоятку?'
    new_save = {'accept': 'chap_11', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_12_x(req_save, command, intent):
    COMMANDS_1 = ['сделать рукоятку']
    COMMANDS_2 = ['осмотреться']
    if command in COMMANDS_1:
        req_save["save"] = "chap_12"
        text = 'На токарном станке вы изготовили рукоять.' \
               'Осмотреться?'
        tts = 'На токарном станке вы изготовили рукоять.' \
              'Осмотреться?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'На полу вы заметили моток веревки. Вы взяли его с собой.' \
               'Начать делать рукоятку?'
        tts = 'На полу вы заметили моток веревки. Вы взяли его с собой.' \
              'Начать делать рукоятку?'
        req_save["save"] = "chap_12_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13(req_save, command, intent):
    COMMANDS_1 = ['осмотреться']
    if ("YANDEX.CONFIRM" in intent) or (command in COMMANDS_1):
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
    elif ("YANDEX.CONFIRM" not in intent) and (command in COMMANDS_1):
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


def chap_13_1(req_save, command, intent):
    COMMANDS_1 = ['начать']
    if ("YANDEX.CONFIRM" in intent) or (command in COMMANDS_1):
        if req_save["other"]["knife"]:
            text = 'На токарном станке вы изготовили рукоять. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На токарном станке вы изготовили рукоять. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18"
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
    elif ("YANDEX.CONFIRM" not in intent) and (command in COMMANDS_1):
        if req_save["other"]["knife"]:
            text = 'На токарном станке вы изготовили рукоять. \nВсе предметы собраны! Отправиться к Михаилу?'
            tts = 'На токарном станке вы изготовили рукоять. Все предметы собраны! Отправиться к Михаилу?'
            req_save["save"] = "chap_18"
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

def chap_13_0(req_save, command, intent):
    COMMANDS = ['отправиться к михаилу']
    if command in COMMANDS:
        text = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания.' \
               'Проверить пульс или убежать?'
        tts = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания.' \
              'Проверить пульс или убежать?'
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_2(req_save, command, intent):
    if req_save['other']['trader']:
        text = "Когда вы зашли в столовую, вы заметили торговца, которому вы спасли жизнь. Хотите подойти к нему?"
        tts = "Когда вы зашли в столовую, вы заметили торговца, которому вы спасли жизнь. Хотите подойти к нему?"
        req_save["save"] = 'chap_13_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        text = 'Вы подходите к заключенному, чтобы спросить про железную заточку. Заключенный отвечает: "Да, я могу продать тебе заточку." ' \
               'Если вы решите купить заточку, то вы потратите все свои деньги, но у вас нет другого выбора.' \
               'Вы готовы купить заточку?'
        tts = 'Вы подходите к заключенному, чтобы спросить про железную заточку. Заключенный отвечает: "Да, я могу продать тебе заточку." ' \
              'Если вы решите купить заточку, то вы потратите все свои деньги, но у вас нет другого выбора.' \
              'Вы готовы купить заточку?'
        req_save["save"] = 'chap_16'
        return message_sent(text=text, tts=tts, save=req_save, version=version)


def chap_13_3(req_save, command, intent):
    COMMANDS = ['подойти к торговцу']
    if command in COMMANDS:
        req_save["save"] = "chap_13_4"
        text = 'Вы спросили у торговца, сможет ли он достать железную заточку. Торговец ответил: "Конечно, это малая услуга для моего спасителя". Затем он отдал ее вам.' \
               'Все предметы собраны. Отправляемся к Михаилу?'
        tts = 'Вы спросили у торговца, сможет ли он достать железную заточку. Торговец ответил: "Конечно, это малая услуга для моего спасителя". Затем он отдал ее вам.' \
              'Все предметы собраны. Отправляемся к Михаилу?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_4(req_save, command, intent):
    COMMANDS = ['отправиться к михаилу']
    if command in COMMANDS:
        text = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания. \nПроверить пульс или убежать?'
        tts = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания. Проверить пульс или убежать?'
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_16(req_save, command, intent):
    COMMANDS = ['купить заточку']
    if command in COMMANDS:
        req_save["save"] = 'chap_17'
        text = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        tts = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = 'chap_11_0'
        return message_help(req_save, version)


def chap_17(req_save, command, intent): # chap_13_0 такой же
    COMMANDS = ['отправиться к михаилу']
    if command in COMMANDS:
        text = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания.' \
               'Проверить пульс или убежать?'
        tts = 'Вы заходите в камеру к Михаилу и замечаете, что он лежит на полу без сознания.' \
              'Проверить пульс или убежать?'
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18(req_save, command, intent):
    COMMANDS_1 = ['проверить пульс']
    COMMANDS_2 = ['убежать']
    if command in COMMANDS_1:
        text = 'Вы решаете проверить пульс у Михаила. Однако, пульс отсутствует, и вы осознаете, что Михаил умер.' \
               'Убежать или осмотреть комнату?'
        tts = 'Вы решаете проверить пульс у Михаила. Однако, пульс отсутствует, и вы осознаете, что Михаил умер.' \
              'Убежать или осмотреть комнату?'
        req_save["save"] = 'chap_18_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Вы начинаете бежать, но спотыкаетесь и замечаете листок, лежащий под кроватью. Вы решаете взять его с собой. По прибытии в камеру вы обнаруживаете, что это план побега.' \
               'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
        tts = 'Вы начинаете бежать, но спотыкаетесь и замечаете листок, лежащий под кроватью. Вы решаете взять его с собой. По прибытии в камеру вы обнаруживаете, что это план побега.' \
              'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_1(req_save, command, intent):
    COMMANDS_1 = ['осмотреть комнату']
    COMMANDS_2 = ['убежать']
    if command in COMMANDS_1:
        text = 'Где наилучшим образом начать искать - в тумбочке, на полу или в кровати?'
        tts = 'Где наилучшим образом начать искать - в тумбочке, на полу или в кровати?'
        req_save["save"] = 'chap_19'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Вы начинаете бежать, но спотыкаетесь и замечаете листок, лежащий под кроватью. Вы решаете взять его с собой. По прибытии в камеру вы обнаруживаете, что это план побега.' \
               'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
        tts = 'Вы начинаете бежать, но спотыкаетесь и замечаете листок, лежащий под кроватью. Вы решаете взять его с собой. По прибытии в камеру вы обнаруживаете, что это план побега.' \
              'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_2(req_save, command, intent):
    COMMANDS = ['спрятать под одеждой', 'оставить в камере']
    if command in COMMANDS:
        text = 'Вы направляетесь на перекличку, но надзиратель замечает отсутствие Михаила. Это приводит к объявлению об обыске, после которого всех заключенных отводят обратно в камеры.' \
               'Перепрятать предметы?'
        tts = 'Вы направляетесь на перекличку, но надзиратель замечает отсутствие Михаила. Это приводит к объявлению об обыске, после которого всех заключенных отводят обратно в камеры.' \
              'Перепрятать предметы?'
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19(req_save, command, intent):
    COMMANDS_1 = ['искать в тумбочке']
    COMMANDS_2 = ['искать на полу']
    COMMANDS_3 = ['искать в кровати']
    if command in COMMANDS_1:
        text = 'В тумбочке вы находите кошелек Михаила.' \
               'Взять его с собой или продолжить искать на полу либо в кровати?'
        tts = 'В тумбочке вы находите кошелек Михаила.' \
              'Взять его с собой или продолжить искать на полу либо в кровати?'
        req_save["save"] = 'chap_19_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'На полу вы ничего не нашли.' \
               'Обыскать кровать?'
        tts = 'На полу вы ничего не нашли.' \
              'Обыскать кровать?'
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
               'Желаете вернуться в камеру?'
        tts = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
              'Желаете вернуться в камеру?'
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_1(req_save, command, intent):
    COMMANDS_1 = ['взять кошелек']
    COMMANDS_2 = ['искать на полу']
    COMMANDS_3 = ['искать в кровати']
    if command in COMMANDS_1:
        text = 'Вы берете кошелек Михаила.' \
               'Где продолжить искать - на полу или в кровати?'
        tts = 'Вы берете кошелек Михаила.' \
              'Где продолжить искать - на полу или в кровати?'
        req_save["save"] = 'chap_19_1_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'На полу вы ничего не нашли.' \
               'Обыскать кровать?'
        tts = 'На полу вы ничего не нашли.' \
              'Обыскать кровать?'
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
               'Желаете вернуться в камеру?'
        tts = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
              'Желаете вернуться в камеру?'
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_2(req_save, command, intent):
    COMMANDS_3 = ['искать в кровати']
    if command in COMMANDS_3:
        text = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
               'Желаете вернуться в камеру?'
        tts = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
              'Желаете вернуться в камеру?'
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_1_1(req_save, command, intent):
    COMMANDS_2 = ['искать на полу']
    COMMANDS_3 = ['искать в кровати']
    if command in COMMANDS_2:
        text = 'На полу вы ничего не нашли.' \
               'Обыскать кровать?'
        tts = 'На полу вы ничего не нашли.' \
              'Обыскать кровать?'
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
               'Желаете вернуться в камеру?'
        tts = 'Вы использовали железную заточку, чтобы разрезать матрас, и заметили там листок с чертежами.' \
              'Желаете вернуться в камеру?'
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_3(req_save, command, intent):
    COMMANDS = ['вернуться в камеру']
    text = 'После возвращения в камеру вы изучаете листок и осознаете, что это план побега.' \
           'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
    tts = 'После возвращения в камеру вы изучаете листок и осознаете, что это план побега.' \
          'Пришло время для вечерней переклички. Что лучше - спрятать предметы под одежду или оставить их в камере?'
    new_save = {'accept': 'chap_20', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_21(req_save, command, intent):
    COMMANDS = ['спрятать под одеждой', 'оставить в камере']
    if command in COMMANDS:
        text = 'Вы направляетесь на перекличку, но надзиратель замечает отсутствие Михаила. Это приводит к объявлению об обыске, после которого всех заключенных отводят обратно в камеры.' \
               'Перепрятать предметы?'
        tts = 'Вы направляетесь на перекличку, но надзиратель замечает отсутствие Михаила. Это приводит к объявлению об обыске, после которого всех заключенных отводят обратно в камеры.' \
              'Перепрятать предметы?'
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_x(req_save, command, intent):
    COMMANDS_1 = ['да']
    COMMANDS_2 = ['нет']
    if command in COMMANDS_1:
        text = 'Вы начинаете прятать предметы, но охранник замечает вас и вы отправляетесь в карцер.' \
               'Загрузить последнее сохранение?'
        tts = 'Вы начинаете прятать предметы, но охранник замечает вас и вы отправляетесь в карцер.' \
              'Загрузить последнее сохранение?'
        req_save["save"] = 'chap_21_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Охранник мчится мимо вашей камеры, и тревога заканчивается. Вы замечаете, как Михаила уносят на носилках куда-то.' \
               'Вы ошеломлены произошедшим, хотите лечь спать?'
        tts = 'Охранник мчится мимо вашей камеры, и тревога заканчивается. Вы замечаете, как Михаила уносят на носилках куда-то.' \
              'Вы ошеломлены произошедшим, хотите лечь спать?'
        req_save["save"] = 'chap_21_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_1(req_save, command, intent):
    COMMANDS = ['загрузить последнее сохранение']
    if command in COMMANDS:
        text = 'Через некоторое время вас выписывают из лазарета, и вы отправляетесь обратно в свою камеру, но замечаете, что заработанные вами деньги пропали.' \
               'Опечаленный, вы садитесь на койку и не понимаете, что делать дальше. Вдруг в камеру заходит заключенный, садиться напротив вас и говорит: "Спасибо за то, что вмешался в драку. Можешь ли ты сказать мне свое имя?"'
        tts = 'Через некоторое время вас выписывают из лазарета, и вы отправляетесь обратно в свою камеру, но замечаете, что заработанные вами деньги пропали.' \
              'Опечаленный, вы садитесь на койку и не понимаете, что делать дальше. Вдруг в камеру заходит заключенный, садиться напротив вас и говорит: "Спасибо за то, что вмешался в драку. Можешь ли ты сказать мне свое имя?"'
        req_save["save"] = 'chap_9'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_2(req_save, command, intent):
    COMMANDS = ['сохранить игру']
    if command in COMMANDS:
        text = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
               'Начать побег сейчас или во время обеда?'
        tts = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
              'Начать побег сейчас или во время обеда?'
        req_save['save'] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_22(req_save, command, intent):
    COMMANDS_1 = ['начать побег в обед']
    COMMANDS_2 = ['начать побег сейчас']
    if command in COMMANDS_1:
        text = 'В обеденное время вы отправляетесь к месту, указанному на плане. К вашему удивлению, вы обнаруживаете, что тайная комната, вырытая Михаилом, находится в самом заметном месте, за картиной.' \
               'Войти в комнату?'
        tts = 'В обеденное время вы отправляетесь к месту, указанному на плане. К вашему удивлению, вы обнаруживаете, что тайная комната, вырытая Михаилом, находится в самом заметном месте, за картиной.' \
              'Войти в комнату?'
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Просматривая план побега, вы понимаете, что тайная комната, прорытая Михаилом, находится за картиной, которая выставлена на самом видном месте. Вы приходите к месту входа в комнату.' \
               'Осмотреться или войти в комнату?'
        tts = 'Просматривая план побега, вы понимаете, что тайная комната, прорытая Михаилом, находится за картиной, которая выставлена на самом видном месте. Вы приходите к месту входа в комнату.' \
              'Осмотреться или войти в комнату?'
        req_save['save'] = 'chap_22_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_22_1(req_save, command, intent):
    COMMANDS = ['войти в комнату']
    text = 'Вы отодвигаете картину, осторожно пролезаете в комнату и обнаруживаете решетку, которая ведет в канализацию. Чтобы создать что-то полезное вы решаете использовать имеющиеся у вас железную заточку, веревку и рукоятку' \
           'Необходимо определить, что изготовить - самодельный топор или самодельную кирку.' \
           'Список:' \
           '* Самодельный топор' \
           'Хорош для всех рубящих ударов' \
           '* Самодельная кирка' \
           'Хорошо подходит для компания шахт'
    tts = 'Вы отодвигаете картину, осторожно пролезаете в комнату и обнаруживаете решетку, которая ведет в канализацию. Чтобы создать что-то полезное вы решаете использовать имеющиеся у вас железную заточку, веревку и рукоятку' \
          'Необходимо определить, что изготовить - самодельный топор или самодельную кирку.' \
          'Список:' \
          '* Самодельный топор' \
          'Хорош для всех рубящих ударов' \
          '* Самодельная кирка' \
          'Хорошо подходит для компания шахт'
    new_save = {'accept': 'chap_24', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_22_2(req_save, command, intent):
    COMMANDS_1 = ['войти в комнату']
    COMMANDS_2 = ['осмотреться']
    if command in COMMANDS_1:
        text = 'Вы решаете отодвинуть картину, но к сожалению, охранник замечает вас и сажает в карцер. Загрузить последнее сохранение?'
        tts = 'Вы решаете отодвинуть картину, но к сожалению, охранник замечает вас и сажает в карцер. Загрузить последнее сохранение?'
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Вы осматриваетесь и не замечаете охранников. Войти в комнату или вернуться в обед?'
        tts = 'Вы осматриваетесь и не замечаете охранников. Войти в комнату или вернуться в обед?'
        req_save['save'] = 'chap_23'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23(req_save, command, intent):
    COMMANDS_1 = ['войти в комнату']
    COMMANDS_2 = ['вернуться в обед']
    if command in COMMANDS_1:
        text = 'Вы решаете отодвинуть картину, но к сожалению, охранник замечает вас и сажает в карцер. Загрузить последнее сохранение?'
        tts = 'Вы решаете отодвинуть картину, но к сожалению, охранник замечает вас и сажает в карцер. Загрузить последнее сохранение?'
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'В обеденное время вы вернулись к месту, указанному на плане. Войти в комнату?'
        tts = 'В обеденное время вы вернулись к месту, указанному на плане. Войти в комнату?'
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23_1(req_save, command, intent): # == chap_22_1
    COMMANDS = ['войти в комнату']
    if command in COMMANDS:
        text = 'Вы отодвигаете картину, осторожно пролезаете в комнату и обнаруживаете решетку, которая ведет в канализацию. Чтобы создать что-то полезное вы решаете использовать имеющиеся у вас железную заточку, веревку и рукоятку' \
               'Необходимо определить, что изготовить - самодельный топор или самодельную кирку.' \
               'Список:' \
               '* Самодельный топор' \
               'Хорош для всех рубящих ударов' \
               '* Самодельная кирка' \
               'Хорошо подходит для компания шахт'
        tts = 'Вы отодвигаете картину, осторожно пролезаете в комнату и обнаруживаете решетку, которая ведет в канализацию. Чтобы создать что-то полезное вы решаете использовать имеющиеся у вас железную заточку, веревку и рукоятку' \
              'Необходимо определить, что изготовить - самодельный топор или самодельную кирку.' \
              'Список:' \
              '* Самодельный топор' \
              'Хорош для всех рубящих ударов' \
              '* Самодельная кирка' \
              'Хорошо подходит для компания шахт'
        req_save['save'] = 'chap_24'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version) # можно удалить


def chap_23_2(req_save, command, intent):
    COMMANDS = ['загрузить последнее сохранение']
    if command in COMMANDS:
        req_save['save'] = 'chap_22'
        text = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня. Начать побег сейчас или во время обеда?'
        tts = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня. Начать побег сейчас или во время обеда?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24(req_save, command, intent):
    COMMANDS_1 = ['сделать кирку']
    COMMANDS_2 = ['сделать топор']
    if command in COMMANDS_1:
        text = 'Вы изготовили кирку и принимаетесь ломать решетку. Однако, сразу после первого удара веревка, держащая железную затычку, рвется. Вы быстро связываете концы веревок и изготавливаете топор' \
               'Продолжить ломать решетку?'
        tts = 'Вы изготовили кирку и принимаетесь ломать решетку. Однако, сразу после первого удара веревка, держащая железную затычку, рвется. Вы быстро связываете концы веревок и изготавливаете топор' \
              'Продолжить ломать решетку?'
        req_save['save'] = 'chap_24_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Изготовленный топор отлично подойдет для разрушения решетки. Начать ломать решетку?'
        tts = 'Изготовленный топор отлично подойдет для разрушения решетки. Начать ломать решетку?'
        req_save['save'] = 'chap_24_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24_1(req_save, command, intent):
    COMMANDS = ['продолжить ломать решетку']
    if command in COMMANDS:
        text = 'Вы начинаете бить решетку самодельным топором, звук постепенно усиливается. После нескольких ударов прутья решетки ломаются, вы их загибаете и пролезаете в канализационный тоннель.' \
               'Звук ломающейся решетки привлек внимание охраны, и вы услышали звук сирены. Стоит ли бежать из города?'
        tts = 'Вы начинаете бить решетку самодельным топором, звук постепенно усиливается. После нескольких ударов прутья решетки ломаются, вы их загибаете и пролезаете в канализационный тоннель.' \
              'Звук ломающейся решетки привлек внимание охраны, и вы услышали звук сирены. Стоит ли бежать из города?'
        req_save['save'] = 'chap_25'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24_2(req_save, command, intent):
    COMMANDS = ['начать ломать решетку']
    text = 'Вы начинаете бить решетку самодельным топором, звук постепенно усиливается. После нескольких ударов прутья решетки ломаются, вы их загибаете и пролезаете в канализационный тоннель.' \
           'Звук ломающейся решетки привлек внимание охраны, и вы услышали звук сирены. Стоит ли бежать из города?'
    tts = 'Вы начинаете бить решетку самодельным топором, звук постепенно усиливается. После нескольких ударов прутья решетки ломаются, вы их загибаете и пролезаете в канализационный тоннель.' \
          'Звук ломающейся решетки привлек внимание охраны, и вы услышали звук сирены. Стоит ли бежать из города?'
    new_save = {'accept': 'chap_25', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_25(req_save, command, intent):
    COMMANDS_1 = ['да']
    COMMANDS_2 = ['нет']
    text = 'Вы вылезаете из канализации и бежите к воротам города, но они оказываются тщательно запертыми.' \
           'Подождать пока ворота откроют или попробовать сломать замок самодельным топором?'
    tts = 'Вы вылезаете из канализации и бежите к воротам города, но они оказываются тщательно запертыми.' \
          'Подождать пока ворота откроют или попробовать сломать замок самодельным топором?'
    text_reject = 'Вы решаете остаться в городе, но из-за вашей формы заключенного вас замечает житель и сообщает полиции. Вас задерживают и осуждают на казнь.' \
           'Хотите ли вы загрузить последнее сохранение?'
    tts_reject = 'Вы решаете остаться в городе, но из-за вашей формы заключенного вас замечает житель и сообщает полиции. Вас задерживают и осуждают на казнь.' \
          'Хотите ли вы загрузить последнее сохранение?'
    new_save = {'accept': 'chap_25_1', 'reject': 'chap_23_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts, reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject, tts_reject=tts_reject, new_save=new_save)


def chap_25_1(req_save, command, intent):
    COMMANDS_1 = ['сломать']
    COMMANDS_2 = ['ждать']
    if command in COMMANDS_1:
        req_save['save'] = 'chap_23_2'
        text = 'Вы начинаете ломать замок своим самодельным топором, но вас замечает полиция и приговаривает к казни.' \
               'Загрузить последнее сохранение?'
        tts = 'Вы начинаете ломать замок своим самодельным топором, но вас замечает полиция и приговаривает к казни.' \
              'Загрузить последнее сохранение?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save['save'] = 'chap_25_1_2'
        text = 'Вы прячетесь в кустах. Внезапно ворота открываются и в город заезжает какой-то разбойник. Это ваш шанс сбежать. Вы быстро выходите из кустов и убегаете из города в неизвестном направлении.' \
               'Сохранить игру?'
        tts = 'Вы прячетесь в кустах. Внезапно ворота открываются и в город заезжает какой-то разбойник. Это ваш шанс сбежать. Вы быстро выходите из кустов и убегаете из города в неизвестном направлении.' \
              'Сохранить игру?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_1_1(req_save, command, intent):
    COMMANDS = ['загрузить последнее сохранение']
    if command in COMMANDS:
        text = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
               'Начать побег сейчас или во время обеда?'
        tts = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
              'Начать побег сейчас или во время обеда?'
        req_save["save"] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version) # == chap_23_2


def chap_25_1_2(req_save, command, intent):
    COMMANDS = ['сохранить игру']
    if command in COMMANDS:
        text = 'Поздравляем, вы успешно завершили 1 главу!!!!' \
               'Спасибо за игру (2 глава находится на тестировании)'
        tts = 'Поздравляем, вы успешно завершили 1 главу!!!!' \
              'Спасибо за игру (2 глава находится на тестировании)'
        req_save['save'] = 'start'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_2(req_save, command, intent):
    COMMANDS = ['загрузить последнее сохранение']
    if command in COMMANDS:
        text = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
               'Начать побег сейчас или во время обеда?'
        tts = 'Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.' \
              'Начать побег сейчас или во время обеда?'
        req_save["save"] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version) # == chap_23_2

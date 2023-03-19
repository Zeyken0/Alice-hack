from config import *
from dialogs import message_sent, d_start_0
from help_dialogs import message_help
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
                "health": "",
                "power": "",
                "mane": "",
                "inventory": [""],
                "other": [""]
            }
            COLLECTION.insert_one(user)
            text = 'Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'
            tts = 'Добро пожаловать в Сагу Битв и Приключений. Чтобы пройти обучение скажи "Пройти обучение", если ты готов скажи "Начать"'
            return d_start_0(text, tts, version)
        elif COLLECTION.find_one({"id": event["session"]["application"]["application_id"]})["save"] == "":
            text = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            tts = "Добро пожаловать в Сагу Битв и Приключений. Ты готов начать?"
            return d_start_0(text, tts, version)
        else:
            text = "Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"
            tts = "Рады тебя снова видеть в Саге Битв и Приключений. Ты готов продолжить?"
            save = COLLECTION.find_one({"id": event["session"]["application"]["application_id"]})["save"]
            return message_sent(text=text,tts=tts,version=version,save=save)
    elif command == "выход":
        text = 'Удачи!!'
        tts = 'Удачи!!'
        save = ""
        return message_sent(text, tts, version, save, end_session=True)
    else:
        req_save = event["state"]["session"]["save"]
        if "YANDEX.HELP" in intent:
            if intent["YANDEX.HELP"]:
                return message_help(req_save, version)

            elif req_save == "start":
                return start_1(req_save, command, intent)

            elif req_save == "start_1":
                return start_2(req_save, command, intent)

            elif req_save == "start_2":
                return start_3(req_save, command, intent)

            elif req_save == "start_3" or req_save == "start_3_1":
                return chap(req_save, command, intent)

            elif req_save == "chap":
                return chap_1(req_save, command, intent)

            elif req_save == "chap_1" or req_save == "chap_1_1":
                return chap_2(req_save, command, intent)

            elif req_save == "chap_2":
                return chap_3(req_save, command, intent)

            elif req_save == "chap_3":
                return chap_4(req_save, command, intent)

            elif req_save == "chap_4_1":
                return chap_4_1_1(req_save, command, intent)

            elif req_save == "chap_4_1_1":
                return chap_4_1_x(req_save, command, intent)

            elif req_save == "chap_4_1_2" or req_save == "chap_4_1_4" or req_save == "chap_4_1_7":
                return chap_5(req_save, command, intent)

            elif req_save == "chap_4_1_3":
                return chap_4_1_3_x(req_save, command, intent)

            elif req_save == "chap_4_2":
                return chap_4_2_1(req_save, command, intent)

            elif req_save == "chap_5" or req_save == "chap_4_2_1":
                return chap_5_1(req_save, command, intent)
        else:
            if req_save == "start":
                return start_1(req_save, command, intent)

            elif req_save == "start_1":
                return start_2(req_save, command, intent)

            elif req_save == "start_2":
                return start_3(req_save, command, intent)

            elif req_save == "start_3" or req_save == "start_3_1":
                return chap(req_save, command, intent)

            elif req_save == "chap":
                return chap_1(req_save, command, intent)

            elif req_save == "chap_1" or req_save == "chap_1_1":
                return chap_2(req_save, command, intent)

            elif req_save == "chap_2":
                return chap_3(req_save, command, intent)

            elif req_save == "chap_3":
                return chap_4(req_save, command, intent)

            elif req_save == "chap_4_1":
                return chap_4_1_1(req_save, command, intent)

            elif req_save == "chap_4_1_1":
                return chap_4_1_x(req_save, command, intent)

            elif req_save == "chap_4_1_2" or req_save == "chap_4_1_4" or req_save == "chap_4_1_7":
                return chap_5(req_save, command, intent)

            elif req_save == "chap_4_1_3":
                return chap_4_1_3_x(req_save, command, intent)

            elif req_save == "chap_4_2":
                return chap_4_2_1(req_save, command, intent)

            elif req_save == "chap_5" or req_save == "chap_4_2_1":
                return chap_5_1(req_save, command, intent)


def start_1(req_save, command, intent):
    COMMANDS = ['начать', 'перед']
    text = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли. \nВы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений. \n Сегодня вам нужно пойти торговать на рынке.'
    tts = 'В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли. Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений. Сегодня вам нужно пойти торговать на рынке.'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "start_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
            req_save = "start_1"
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def start_2(req_save, command, intent):
    COMMANDS = ['пойти на рынок', 'отправиться на рынок', 'рынок', 'пошли']
    text = 'Но однажды, когда вы были на рынке, чтобы продать свой урожай, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении. Проследовать за полицией или попробовать сбежать?'
    tts = 'Но однажды, когда вы были на рынке, чтобы продать свой урожай, вы стали свидетелем ограбления. Вы попытались остановить преступников, но они сбежали. На следующий день к вам приходит полиция и обвиняет вас в ограблении. Проследовать за полицией или попробовать сбежать?'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "start_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "start_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def start_3(req_save, command, intent):
    COMMANDS = ['пойти с полицией', 'полиция', 'пойти', 'проследовать', 'полицией', 'пройти', 'пошли', 'иду']
    COMMANDS_REJECT = ['сбежать', 'убежать', 'бег', 'побег']

    text = 'Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Мотать срок?'
    tts = 'Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Мотать срок?'
    text_REJECT = 'Вас догоняет один из полицейских и заламывает руки. Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Вы потеряли 1 единицу здоровья Мотать срок?'
    tts_REJECT = "Вас догоняет один из полицейских и заламывает руки. Вы были арестованы и обвинены в ограблении, хотя вы ничего не делали. Вас посадили в тюрьму, и началась ваша борьба за справедливость и свободу. Вы потеряли 1 единицу здоровья Мотать срок?"
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "start_3"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "start_3"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.REJECT" in intent or command in COMMANDS_REJECT:
        req_save = "start_3_1"
        return message_sent(text=text_REJECT, tts=tts_REJECT, save=req_save, version=version)
    elif "YANDEX.REJECT" not in intent and command in COMMANDS_REJECT:
        req_save = "start_3_1"
        return message_sent(text=text_REJECT, tts=tts_REJECT, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap(req_save, command, intent):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи']
    text = 'В тюрьме вы понимаете, что жизнь здесь не так проста, как казалась. Вы оказываетесь среди преступников, которые ненавидят вас и считают "мелким фермером". Они издеваются над вами, отбирают еду и уважают только тех, кто сильнее и жестче. Здоровье: 6/10 Сила: 2 Мана: 0 Для того, чтобы сделать свой досуг более интересным, выберите, чем заняться: спортом или отдыхом в виде сна.'
    tts = 'В тюрьме вы понимаете, что жизнь здесь не так проста, как казалась. Вы оказываетесь среди преступников, которые ненавидят вас и считают "мелким фермером". Они издеваются над вами, отбирают еду и уважают только тех, кто сильнее и жестче. Здоровье: 6 из 10 sil <[200]> Сила: 2 sil <[200]> Мана: 0 sil <[200]> Для того, чтобы сделать свой досуг более интересным, выберите, чем заняться: спортом или отдыхом в виде сна.'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "chap"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "chap"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_1(req_save, command, intent):
    COMMANDS = ['спорт']
    COMMANDS_1 = ['спать']

    text = 'Среди различных вариантов занятий, доступных вам в тюрьме, вы решили заняться спортом. Здоровье: 6/10 Сила: 4 Мана: 0 Продолжить мотать срок?'
    tts = 'Среди различных вариантов занятий, доступных вам в тюрьме, вы решили заняться спортом. Здоровье: 6/10 Сила: 4 Мана: 0 Продолжить мотать срок?'

    text_1 = 'Вы были вынуждены приспосабливаться к жизни за решеткой, но вы были слишком измучены, чтобы сосредоточиться на чем-то другом, кроме как на сне. Здоровье: 10/10 Сила: 2 Мана: 0 Продолжить мотать срок?'
    tts_1 = 'Вы были вынуждены приспосабливаться к жизни за решеткой, но вы были слишком измучены, чтобы сосредоточиться на чем-то другом, кроме как на сне. Здоровье: 10/10 Сила: 2 Мана: 0 Продолжить мотать срок?'
    if command in COMMANDS:
        #COLLECTION.update_one()
        req_save = "chap_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_1:
        #COLLECTION.update_one()
        req_save = "chap_1_1"
        return message_sent(text=text_1, tts=tts_1, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_2(req_save, command, intent):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи']
    text = 'Наступает день выбора работы. Вам достается работа в мастерской. Начать работать?'
    tts = 'Наступает день выбора работы. Вам достается работа в мастерской. Начать работать?'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "chap_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "chap_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_3(req_save, command, intent):
    COMMANDS = ['']
    COMMANDS_REJECT = ['']

    text = 'Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?" Соврать или отказаться?'
    tts = 'Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?" Соврать или отказаться?'
    text_REJECT = 'Вас толкает начальник и грозит посадить в карцер, вы отправляетесь на работу Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?" Соврать или отказаться?'
    tts_REJECT = 'Вас толкает начальник и грозит посадить в карцер, вы отправляетесь на работу Вы начинаете работу и слышите, как открывается дверь мастерской. Там оказывается какой-то заключенный, который обращается к вам: "Эй, ты, мелкий фермер! Ты здесь, чтобы работать и зарабатывать, или быть нашим рабом? Посмотри на этот нож. У меня есть свои способы получить, что я хочу, и ты можешь лишь повиноваться мне. Так что, будешь слушаться или тебе придется пожалеть о своем решении?" Соврать или отказаться?'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "chap_3"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "chap_3"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.REJECT" in intent or command in COMMANDS_REJECT:
        req_save = "chap_3"
        return message_sent(text=text_REJECT, tts=tts_REJECT, save=req_save, version=version)
    elif "YANDEX.REJECT" not in intent and command in COMMANDS_REJECT:
        req_save = "chap_3"
        return message_sent(text=text_REJECT, tts=tts_REJECT, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_4(req_save, command, intent):
    COMMANDS_TRUE = ['отказаться']
    COMMANDS_LIE = ['солгать']
    if command in COMMANDS_TRUE:
        req_save = "chap_4_1"
        text = 'Преступник: "Ты думаешь, что можешь отказаться от меня? Я сделаю твою жизнь адом, если ты не будешь слушаться меня". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        tts = 'Преступник: "Ты думаешь, что можешь отказаться от меня? Я сделаю твою жизнь адом, если ты не будешь слушаться меня". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_LIE:
        req_save = "chap_4_2"
        text = 'Вы решаете соврать и согласиться с предложением преступника. Преступник резко поднялся со стула и подошел к вам, ухмыляясь. Вы попытались отойти назад, но он настиг вас и ударил рукой. Минус 2 единицы здоровья. Преступник: "Ты думал, что я не пойму, что ты врешь, мелкий? Я тебя здесь научу говорить правду, это первое и последнее предупреждение". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        tts = 'Вы решаете соврать и согласиться с предложением преступника. Преступник резко поднялся со стула и подошел к вам, ухмыляясь. Вы попытались отойти назад, но он настиг вас и ударил рукой. Минус 2 единицы здоровья. Преступник: "Ты думал, что я не пойму, что ты врешь, мелкий? Я тебя здесь научу говорить правду, это первое и последнее предупреждение". Преступник уходит. Вы ошеломлены произошедшим, закончить работать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_4_1_1(req_save, command, intent):
    COMMANDS = ['']
    text = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость и решаете вернуться в свою камеру для отдыха. Вы открываете дверь своей камеры и видите, что там уже находятся двое заключенных, один из которых был тот преступник, которому вы отказали в помощи. Вы понимаете, что они настроены решительно и не будут договариваться с вами. Что лучше сделать: "Ударить заключенного", "Убежать", "Закричать"'
    tts = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость и решаете вернуться в свою камеру для отдыха. Вы открываете дверь своей камеры и видите, что там уже находятся двое заключенных, один из которых был тот преступник, которому вы отказали в помощи. Вы понимаете, что они настроены решительно и не будут договариваться с вами. Что лучше сделать: "Ударить заключенного", "Убежать", "Закричать"'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "chap_4_1_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "chap_4_1_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_x(req_save, command, intent):
    COMMANDS_RUN = ['убежать']
    COMMANDS_HIT = ['ударить']
    COMMANDS_SHOUT = ['закричать']
    if command in COMMANDS_RUN:
        req_save = "chap_4_1_2"
        text = 'Вы резко поворачиваетесь, чтобы убежать, но один из заключенных быстро подбегает к вам и хватает за руку. Вы пытаетесь вырваться, но он удерживает вас и начинает толкать к стене. Вы чувствуете удар в голову, и все исчезает перед глазами. Минус 1 единица здоровья. Очнуться?'
        tts = 'Вы резко поворачиваетесь, чтобы убежать, но один из заключенных быстро подбегает к вам и хватает за руку. Вы пытаетесь вырваться, но он удерживает вас и начинает толкать к стене. Вы чувствуете удар в голову, и все исчезает перед глазами. Минус 1 единица здоровья. Очнуться?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_SHOUT:
        req_save = "chap_4_1_4"
        text = 'Вы попытаетесь закричать, чтобы привлечь внимание охранников, но один из заключенных быстро закрывает вам рот. Вы начинаете чувствовать себя задыхающимся и беспомощным, пытаясь освободиться от его хватки. Другой заключенный в это время начинает обыскивать ваши карманы и забирает все ценности. Вы теряете сознание. Минус 3 единицы здоровья. Очнуться?'
        tts = 'Вы попытаетесь закричать, чтобы привлечь внимание охранников, но один из заключенных быстро закрывает вам рот. Вы начинаете чувствовать себя задыхающимся и беспомощным, пытаясь освободиться от его хватки. Другой заключенный в это время начинает обыскивать ваши карманы и забирает все ценности. Вы теряете сознание. Минус 3 единицы здоровья. Очнуться?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_HIT:
        if 4 == 4:
            req_save = "chap_4_1_3"
            text = 'Ваши занятия спортом не прошли даром: вы бьете одного заключенного, тот сразу же теряет сознание. Другой преступник, увидев это, убегает. Вы думаете, что нужно сделать с заключенным, находящимся в отключке. Теперь что-то нужно сделать с заключенным: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру"'
            tts = 'Ваши занятия спортом не прошли даром: вы бьете одного заключенного, тот сразу же теряет сознание. Другой преступник, увидев это, убегает. Вы думаете, что нужно сделать с заключенным, находящимся в отключке. Теперь что-то нужно сделать с заключенным: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру"'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
        else:
            req_save = "chap_4_1_7"
            text = 'Вы чувствуете, что вам нужно защитить себя и быстро делаете решительный шаг, пытаясь ударить преступника, которому отказали в помощи. Однако он быстро увернулся, и вы промахнулись, потеряв при этом равновесие и ударившись головой. Вы теряете сознание. Минус 2 единицы здоровья. Очнуться?'
            tts = 'Вы чувствуете, что вам нужно защитить себя и быстро делаете решительный шаг, пытаясь ударить преступника, которому отказали в помощи. Однако он быстро увернулся, и вы промахнулись, потеряв при этом равновесие и ударившись головой. Вы теряете сознание. Минус 2 единицы здоровья. Очнуться?'
            return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_4_2_1(req_save, command, intent):
    COMMANDS = ['']
    text = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость. Вы направляетесь на перекличку, а затем решаете вернуться в свою камеру, чтобы отдохнуть. Лечь спать?'
    tts = 'После тяжелого дня работы в мастерской вы чувствуете сильную усталость. Вы направляетесь на перекличку, а затем решаете вернуться в свою камеру, чтобы отдохнуть. Лечь спать?'
    if "YANDEX.CONFIRM" in intent or command in COMMANDS:
        req_save = "chap_5_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif "YANDEX.CONFIRM" not in intent and command in COMMANDS:
        req_save = "chap_5_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_4_1_3_x(req_save, command, version):
    COMMANDS_1 = ['охрана']
    COMMANDS_2 = ['оставить']
    COMMANDS_3 = ['убрать']
    if command in COMMANDS_1:
        req_save = "chap_4_1_3_1"
        text = 'Вы зовете охрану. Вас обвиняют в нападении на заключенного, и теперь вы находитесь в карцере. Начать сначала?'
        tts = 'Вы зовете охрану. Вас обвиняют в нападении на заключенного, и теперь вы находитесь в карцере. Начать сначала?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save = "chap_4_1_3_2"
        text = 'Мимо вашей камеры проходит охранник, увидев лежачего заключенного, вас обвиняют в нападении, теперь вы находитесь в карцере. Начать сначала?'
        tts = 'Мимо вашей камеры проходит охранник, увидев лежачего заключенного, вас обвиняют в нападении, теперь вы находитесь в карцере. Начать сначала?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        req_save = "chap_4_1_3_3"
        text = 'Вы осматриваетесь вокруг и не замечаете охранников, решаете перенести заключенного в другую камеру. Но когда вы выходите на перекличку, надзиратели находят одного из заключенных без сознания и обвиняют владельца камеры в нападении на него. Вам нужно восстановить силы. Лечь спать?'
        tts = 'Вы осматриваетесь вокруг и не замечаете охранников, решаете перенести заключенного в другую камеру. Но когда вы выходите на перекличку, надзиратели находят одного из заключенных без сознания и обвиняют владельца камеры в нападении на него. Вам нужно восстановить силы. Лечь спать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)

def chap_5(req_save, command, intent):
    COMMANDS = ['очнуться']
    if command in COMMANDS:
        req_save = "chap_5"
        text = 'Когда вы приходите в сознание, вы лежите на полу в своей камере. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов. Вам нужно восстановить силы. Лечь спать?'
        tts = 'Когда вы приходите в сознание, вы лежите на полу в своей камере. Вам кажется, что прошло несколько часов, но вы не уверены. Вы пытаетесь подняться, но чувствуете резкую боль в голове и ощущение тошноты. Открыв глаза, вы замечаете, что на вашем лице красуется синяк, а на ваших руках видны следы ударов. Вам нужно восстановить силы. Лечь спать?'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help("chap_4_1_0", version)

def chap_5_1(req_save, command, intent):
    COMMANDS = ['спать']
    if command in COMMANDS:
        req_save = "chap_5_1"
        text = 'В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере. Мотать срок.'
        tts = 'В течение следующих дней вы стараетесь держаться подальше от других заключенных, опасаясь повторной атаки. Вы также продолжаете работать и складывать деньги в своей камере. Мотать срок.'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)






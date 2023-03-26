from dialogs import message_sent, d_start_0
from help_dialogs import message_help, confirm_reject_handler
from config import *
from alice_says import alice_dict

version = "1.0"


def start_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['начать', 'вперед', 'поехали', 'начинай', 'быстрее', 'ну', 'да', 'давай', 'ага', 'начнем', 'я готов']
    COMMANDS_2 = ['что ты умеешь', 'что ты умеешь', 'что ты', 'что ты', 'че умеешь', 'что ты', 'как', 'не понимаю', 'что ты делаешь', 'делаешь что']
    if command in COMMANDS_1:
        req_save['save'] = 'start_1'
        text = alice_dict['start_1']['text']
        tts = alice_dict['start_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. \nРекомендуем этот навык для людей старше 12 лет.'
        tts = 'Навык - пошаговый квест, в рамках которого вы будете погружаться в захватывающий мир приключений и сражений. Вы играете главного героя, обычного фермера, который однажды решает отправиться на рынок, чтобы продать свои товары. Там он замечает грабителей и решает остановить их. Однако на следующий день его обвиняют в краже, и герой попадает в тюрьму, где ему приходится выживать любыми способами. В конце концов, герой выбирается из тюрьмы, и начинаются его приключения за городом. Рекомендуем этот навык для людей старше 12 лет.'
        req_save['save'] = 'start'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in intent['YANDEX.REJECT']:
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
        return message_sent(text=text, tts=tts, save=req_save, version=version)


def start_2(req_save, command, intent, user_id):
    COMMANDS = ['отправиться на рынок', 'сходить на рынок', 'пойти на рынок', 'поехать на рынок', 'зайти на рынок', 'рынок', 'пошли', 'пойти']
    req_save["power"] = 2
    req_save["health"] = 6
    text = alice_dict['start_2']['text']
    tts = alice_dict['start_2']['tts']
    new_save = {'accept': 'start_2', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def start_3(req_save, command, intent, user_id):
    COMMANDS = ['пойти с полицией', 'полиция', 'пойти', 'проследовать', 'полицией', 'пройти', 'пошли', 'иду', 'отправиться за полицией', 'проследовать за полицией']
    COMMANDS_REJECT = ['сбежать', 'убежать', 'бег', 'побег', 'валим', 'уходим', 'бежим', 'убегай', 'беги', 'побежали', 'сбежать от полиции']

    text = alice_dict['start_3']['text']
    tts = alice_dict['start_3']['tts']
    text_REJECT = alice_dict['start_3_1']['text']
    tts_REJECT = alice_dict['start_3_1']['tts']
    new_save = {'accept': 'start_3', 'reject': 'start_3_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap(req_save, command, intent, user_id):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи', 'мотай', 'мотай срок']
    text = alice_dict['chap']['text']
    tts = alice_dict['chap']['tts']
    new_save = {'accept': 'chap', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_1(req_save, command, intent, user_id):
    COMMANDS = ['спорт', 'заняться спортом', 'заняться', 'спортом', 'спортсмен']
    COMMANDS_1 = ['спать', 'лечь', 'лечь спать', 'давай поспи', 'лечь поспать', 'спи', 'сон', 'ляг', 'отдохнуть']

    text = alice_dict['chap_1']['text']
    tts = alice_dict['chap_1']['tts']

    text_1 = alice_dict['chap_1_1']['text']
    tts_1 = alice_dict['chap_1_1']['tts']
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


def chap_2(req_save, command, intent, user_id):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи', 'мотай', 'мотай срок', 'продолжить', 'продолжить мотать срок']
    text = alice_dict["chap_2"]['text']
    tts = alice_dict["chap_2"]['tts']
    new_save = {'accept': 'chap_2', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_3(req_save, command, intent, user_id):
    COMMANDS = ['начать', 'работать', 'работай', 'начни', 'начинай', 'начинай работать', 'начать работать']
    COMMANDS_REJECT = ['не хочу', 'не буду работать', 'не буду', 'работа для слабых']

    text = alice_dict['chap_3_1']['text']
    tts = alice_dict['chap_3_1']['tts']
    text_REJECT = alice_dict['chap_3']['text']
    tts_REJECT = alice_dict['chap_3']['tts']
    new_save = {'accept': 'chap_3', 'reject': 'chap_3'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap_4(req_save, command, intent, user_id):
    COMMANDS_TRUE = ['отказаться', 'отказываюсь', 'я отказываюсь']
    COMMANDS_LIE = ['солгать', 'соврать', 'лгать', 'совру', 'врать', 'обману', 'обман', 'солгу']
    if command in COMMANDS_TRUE:
        req_save["save"] = "chap_4_1"
        text = alice_dict['chap_4_1']['text']
        tts = alice_dict['chap_4_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_LIE:
        req_save["health"] -= 2
        req_save["save"] = "chap_4_2"
        text = alice_dict['chap_4_2']['text']
        tts = alice_dict['chap_4_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_1(req_save, command, intent, user_id):
    COMMANDS = ['закончить', 'заканчивай', 'кончить', 'кончай', 'прекращай', 'прекрати', 'прекратить', 'прекратить', 'хватит', 'достаточно']
    text = alice_dict['chap_4_1_1']['text']
    tts = alice_dict['chap_4_1_1']['tts']
    new_save = {'accept': 'chap_4_1_1', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_4_1_x(req_save, command, intent, user_id):
    COMMANDS_RUN = ['убежать', 'убегай', 'беги', 'вали', 'валим', 'уходим', 'уйти', 'бежать', 'бег']
    COMMANDS_HIT = ['ударить', 'ударить заключенного', 'вломить', 'вломить заключенному', 'ударить зека', 'ударить первого']
    COMMANDS_SHOUT = ['закричать', 'кричать', 'кричи', 'орать', 'позвать охрану', 'крик', 'кричи', 'закричу']
    if command in COMMANDS_RUN:
        req_save["save"] = "chap_4_1_2"
        req_save["health"] -= 1
        text = alice_dict['chap_4_1_2']['text']
        tts = alice_dict['chap_4_1_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_SHOUT:
        req_save["save"] = "chap_4_1_4"
        req_save["health"] -= 3
        text = alice_dict['chap_4_1_4']['text']
        tts = alice_dict['chap_4_1_4']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_HIT:
        if req_save["power"] == 4:  # Поменять на показатель здоровья / силы
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
    COMMANDS = ['закончить', 'заканчивай', 'кончить', 'кончай', 'прекращай', 'прекрати', 'прекратить', 'прекратить', 'хватит', 'достаточно']
    text = alice_dict['chap_4_2_1']['text']
    tts = alice_dict['chap_4_2_1']['tts']
    new_save = {'accept': 'chap_5_1', 'reject': 'chap_5_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_4_1_3_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['охрана', 'позвать охрану', 'позвать', 'звать', 'зову']
    COMMANDS_2 = ['оставить', 'оставить в камере', 'в камере', 'оставить тут', 'пусть лежит', 'пусть остается']
    COMMANDS_3 = ['убрать', 'убрать в соседнюю камеру', 'убрать в камеру', 'убрать в соседнюю', 'в соседнюю', 'в камеру', 'в соседнюю камеру']
    if command in COMMANDS_1:
        req_save["save"] = "chap_4_1_3_1"
        text = alice_dict['chap_4_1_3_1']['text']
        tts = alice_dict['chap_4_1_3_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save["save"] = "chap_4_1_3_2"
        text = alice_dict['chap_4_1_3_2']['text']
        tts = alice_dict['chap_4_1_3_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        req_save["save"] = "chap_4_1_3_3"
        text = alice_dict['chap_4_1_3_3']['text']
        tts = alice_dict['chap_4_1_3_3']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_4_1_3_x_end(req_save, command, intent, user_id):
    COMMANDS = ['начать сначала', 'заново', 'сначала', 'начать', 'начинай', 'да']
    if command in COMMANDS:
        req_save["save"] = "start_1"
        text = alice_dict['start_1']['text']
        tts = alice_dict['start_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_5(req_save, command, intent, user_id):
    COMMANDS = ['очнуться', 'очнись', 'встать', 'проснуться', 'да', 'ага', 'давай']
    if command in COMMANDS:
        req_save["save"] = "chap_5"
        text = alice_dict['chap_5']['text']
        tts = alice_dict['chap_5']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = "chap_4_1_0"
        return message_help(req_save, version)


def chap_5_1(req_save, command, intent, user_id):
    COMMANDS = ['спать', 'лечь', 'лечь спать', 'ложись спать', 'спать я сказал', 'начать спать', 'лечь поспать']
    text = alice_dict['chap_5_1']['text']
    tts = alice_dict['chap_5_1']['tts']
    new_save = {'accept': 'chap_5_1', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_6(req_save, command, intent, user_id):  # Без сохранения
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи', 'мотай', 'мотай срок']
    text = alice_dict['chap_6']['text']
    tts = alice_dict['chap_6']['tts']
    new_save = {'accept': 'chap_6', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_6_x(req_save, command, intent, user_id):  # Без сохранения
    COMMANDS_1 = ['посмотреть', 'смотреть', 'что там', 'смотри', 'посмотрю']
    COMMANDS_2 = ['продолжить', 'продолжай', 'не смотри', 'не смотреться', 'не надо', 'вперед', 'не отвлекаться']
    text = alice_dict['chap_6_1']['text']
    tts = alice_dict['chap_6_1']['tts']
    text_reject = alice_dict['chap_6_2']['text']
    tts_reject = alice_dict['chap_6_2']['tts']
    new_save = {'accept': 'chap_6_1', 'reject': 'chap_6_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap_6_0_x(req_save, command, intent, user_id):  # Без сохранения
    COMMANDS_1 = ['помочь', 'помочь заключенному', 'помочь зеку']
    COMMANDS_2 = ['продолжить работать', 'работать', 'продолжить', 'продолжай', 'работай', 'дальше']
    if command in COMMANDS_1:
        req_save["save"] = 'chap_6_0'
        req_save["other"]["trader"] = True
        text = alice_dict['chap_6_0']['text']
        tts = alice_dict['chap_6_0']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save["save"] = 'chap_6_0_1'
        text = alice_dict['chap_6_0_1']['text']
        tts = alice_dict['chap_6_0_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7(req_save, command, intent, user_id):
    COMMANDS = ['мотать срок', 'мотать', 'срок', 'продолжи', 'мотай', 'мотай срок', 'продолжить', 'продолжить мотать', 'продолжить мотать срок']
    text = alice_dict['chap_7']['text']
    tts = alice_dict['chap_7']['tts']
    new_save = {'accept': 'chap_7', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_7_x(req_save, command, intent, user_id):
    COMMANDS_TRUE = ['помочь', 'помочь заключенному', 'помочь зеку', 'да', 'конечно', 'ага']
    COMMANDS_FALSE = ['продолжить смотреть', 'продолжить', 'смотреть', 'пусть', 'смотреть дальше', 'смотри', 'я продолжу смотреть']
    if command in COMMANDS_TRUE:
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
    elif command in COMMANDS_FALSE:
        req_save["save"] = "chap_7_3"
        text = alice_dict['chap_7_3']['text']
        tts = alice_dict['chap_7_3']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_7_end(req_save, command, intent, user_id):
    COMMANDS_TRUE = ['начать сначала', 'заново', 'сначала', 'начать', 'начинай', 'да']
    if command in COMMANDS_TRUE:
        req_save["save"] = 'start_1'
        text = alice_dict['start_1']['text']
        tts = alice_dict['start_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = "chap_7_0"
        return message_help(req_save, version)


def chap_8(req_save, command, intent, user_id):
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": req_save['save'], "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
    COMMANDS = ['отправиться в лазарет', 'в лазарет', 'лазарет', 'отправиться', 'пойти', 'поползти', 'в лазарет', 'в больничку']
    COMMANDS_REJECT = ['']
    text= '''После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.\n
                Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за  последствия своих действий.\n
                Сохранение игры... Прогресс сохранен.\n
                Желаете продолжить?'''
    tts='''После того, как заключенные начали бить вас, надзиратели немедленно вмешались и разогнали драку. Они отвели вас в лазарет, где вам была оказана необходимая медицинская помощь.
               Вы чувствовали себя очень плохо и были обескуражены произошедшим. Вы понимали, что вмешательство в драку было ошибкой, и теперь вам придется отвечать за  последствия своих действий.
               Сохранение игры... Прогресс сохранен.
               Желаете продолжить?'''
    text_REJECT= '''В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.\n
                Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.\n
                Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'''
    tts_REJECT= '''В магическом мире, который окутан злом, люди выживают только за огромными стенами замков. Вокруг них бродят опасные монстры, готовые напасть на любого, кто попадется у них на пути. Однако, несмотря на опасности, внутри замков процветает жизнь, и люди делают все, чтобы защитить свои земли.
               Вы, герой нашего рассказа, жили на ферме, которую наследовали от своих предков. Ваша семья занималась земледелием и животноводством уже несколько поколений.
               Сегодня вам нужно пойти торговать на рынке. Пойти на рынок?'''
    new_save = {'accept': 'chap_8', 'reject': 'start_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save, reject_enable=True, reject_commands=COMMANDS_REJECT,
                                  text_reject=text_REJECT, tts_reject=tts_REJECT)


def chap_9(req_save, command, intent, user_id):
    COMMANDS_TRUE = ['продолжить', 'продолжай', 'давай', 'желаю', 'начинай', 'давай уже']
    text = alice_dict['chap_9']['text']
    tts = alice_dict['chap_9']['tts']
    new_save = {'accept': 'chap_9', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_TRUE, text=text, tts=tts,
                                  new_save=new_save)


def chap_10(req_save, command, intent, user_id):
    # проверка на имя
    req_save["save"] = 'chap_10'
    req_save["name"] = command
    text = alice_dict['chap_10']['text']
    tts = alice_dict['chap_10']['tts']
    return message_sent(text=text, tts=tts, save=req_save, version=version)


def chap_10_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['почему ты хочешь помочь мне', 'почему', 'зачем', 'зачем ты хочешь помочь мне', 'и почему', 'и зачем', 'а зачем', 'а почему']
    COMMANDS_2 = ['и как же', 'как', 'и как', 'как же', 'ну и как', 'что дальше', 'дальше']
    if command in COMMANDS_1:
        text = alice_dict['chap_10_1']['text']
        tts = alice_dict['chap_10_1']['tts']
        req_save["save"] = "chap_10_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_10_2']['text']
        tts = alice_dict['chap_10_2']['tts']
        req_save["save"] = "chap_10_2"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['пойти в столовую', 'в столовую', 'столовая', 'столовка']
    COMMANDS_2 = ['пойти на работу', 'работу', 'на работу', 'работа']
    if command in COMMANDS_1:
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
    elif command in COMMANDS_2:
        text = alice_dict['chap_11']['text']
        tts = alice_dict['chap_11']['tts']
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_2_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['купить заточку', 'купить', 'заточку', 'покупаю', 'покупай', 'покупай заточку']
    if command in COMMANDS_1:
        req_save["other"]["knife"] = True
        req_save["save"] = 'chap_11_2_1'
        text = alice_dict['chap_11_2_1']['text']
        tts = alice_dict['chap_11_2_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_11_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['подойти к торговцу', 'подойти', 'подойди', 'иди', 'давай', 'ну', 'пошли уже', 'пошли', 'к торговцу']
    text = alice_dict['chap_14']['text']
    tts = alice_dict['chap_14']['tts']
    req_save["other"]["knife"] = True
    new_save = {'accept': 'chap_14', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  new_save=new_save)


def chap_14(req_save, command, intent, user_id):
    COMMANDS_1 = ['осмотреться', 'хочу осмотреться', 'осмотрюсь', 'осмотрись', 'посмотреть']
    COMMANDS_2 = ['пойти на работу', 'работу', 'на работу', 'работа']
    if command in COMMANDS_1:
        req_save["save"] = "chap_15"
        text = alice_dict['chap_15']['text']
        tts = alice_dict['chap_15']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_11']['text']
        tts = alice_dict['chap_11']['tts']
        req_save['save'] = 'chap_11'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = 'chap_14'
        return message_help(req_save, version)


def chap_15(req_save, command, intent, user_id):
    COMMANDS = ['пойти на работу', 'работу', 'на работу', 'работа']
    text = alice_dict['chap_11']['text']
    tts = alice_dict['chap_11']['tts']
    new_save = {'accept': 'chap_11', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_12_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['сделать рукоятку', 'сделать', 'делать', 'рукоятку', 'начать', 'рукоять', 'сделать рукоять']
    COMMANDS_2 = ['осмотреться', 'хочу осмотреться', 'осмотрюсь', 'осмотрись', 'посмотреть']
    if command in COMMANDS_1:
        req_save["save"] = "chap_12"
        text = alice_dict['chap_12']['text']
        tts = alice_dict['chap_12']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_12_1']['text']
        tts = alice_dict['chap_12_1']['tts']
        req_save["save"] = "chap_12_1"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13(req_save, command, intent, user_id):
    COMMANDS_1 = ['осмотреться', 'хочу осмотреться', 'осмотрюсь', 'осмотрись', 'посмотреть']
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


def chap_13_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['начать', 'вперед', 'поехали', 'начинай', 'быстрее', 'ну']
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


def chap_13_0(req_save, command, intent, user_id):
    COMMANDS = ['отправиться к михаилу', 'к михаилу', 'к михе', 'отправиться', 'к михалычу', 'михаилу', 'отправиться к мише', 'мише']
    if command in COMMANDS:
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
    COMMANDS = ['подойти к торговцу', 'подойти', 'подойди', 'иди', 'давай', 'ну', 'пошли уже', 'пошли', 'к торговцу']
    if command in COMMANDS:
        req_save["save"] = "chap_13_4"
        text = alice_dict['chap_13_4']['text']
        tts = alice_dict['chap_13_4']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_13_4(req_save, command, intent, user_id):
    COMMANDS = ['отправиться к михаилу', 'к михаилу', 'к михе', 'отправиться', 'к михалычу', 'михаилу', 'отправиться к мише', 'мише']
    if command in COMMANDS:
        text = alice_dict['chap_18']['text']
        tts = alice_dict['chap_18']['tts']
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_16(req_save, command, intent, user_id):
    COMMANDS = ['купить заточку', 'купить', 'заточку', 'покупаю', 'покупай', 'покупай заточку']
    if command in COMMANDS:
        req_save["save"] = 'chap_17'
        text = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        tts = "Вы купили заточку. Все предметы собраны. Отправляемся к Михаилу?"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        req_save["save"] = 'chap_11_0'
        return message_help(req_save, version)


def chap_17(req_save, command, intent, user_id):  # chap_13_0 такой же
    COMMANDS = ['отправиться к михаилу', 'к михаилу', 'к михе', 'отправиться', 'к михалычу', 'михаилу', 'отправиться к мише', 'мише']
    if command in COMMANDS:
        text = alice_dict['chap_18']['text']
        tts = alice_dict['chap_18']['tts']
        req_save["save"] = 'chap_18'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18(req_save, command, intent, user_id):
    COMMANDS_1 = ['проверить пульс', 'проверить', 'пульс', 'проверю пульс', 'проверь пульс']
    COMMANDS_2 = ['убежать', 'убегай', 'беги', 'вали', 'валим', 'уходим', 'уйти', 'бежать', 'бег']
    if command in COMMANDS_1:
        text = alice_dict['chap_18_1']['text']
        tts = alice_dict['chap_18_1']['tts']
        req_save["save"] = 'chap_18_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_18_2']['text']
        tts = alice_dict['chap_18_2']['tts']
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['осмотреть комнату', 'осмотреть', 'осмотреться', 'посмотреть', 'посмотреть комнату', 'комнату']
    COMMANDS_2 = ['убежать', 'убегай', 'беги', 'вали', 'валим', 'уходим', 'уйти', 'бежать', 'бег']
    if command in COMMANDS_1:
        text = alice_dict['chap_19']['text']
        tts = alice_dict['chap_19']['tts']
        req_save["save"] = 'chap_19'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_18_2']['text']
        tts = alice_dict['chap_18_2']['tts']
        req_save["save"] = 'chap_18_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_18_2(req_save, command, intent, user_id):
    COMMANDS = ['спрятать под одеждой', 'оставить в камере', 'под одеждой', 'в камере', 'спрятать в камере', 'спрятать под кроватью', 'прятать', 'оставить']
    if command in COMMANDS:
        text = alice_dict['chap_21']['text']
        tts = alice_dict['chap_21']['tts']
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19(req_save, command, intent, user_id):
    COMMANDS_1 = ['искать в тумбочке', 'тумбочка', 'в тумбочке', 'тумбе', 'тумба']
    COMMANDS_2 = ['искать на полу', 'пол', 'на полу']
    COMMANDS_3 = ['искать в кровати', 'в кровати', 'кровать']
    if command in COMMANDS_1:
        text = alice_dict['chap_19_1']['text']
        tts = alice_dict['chap_19_1']['tts']
        req_save["save"] = 'chap_19_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['взять кошелек', 'взять', 'кошелек', 'конечно брать', 'да', 'давай', 'берем', 'лишним не будет']
    COMMANDS_2 = ['искать на полу', 'пол', 'на полу']
    COMMANDS_3 = ['искать в кровати', 'в кровати', 'кровать']
    if command in COMMANDS_1:
        text = alice_dict['chap_19_1_1']['text']
        tts = alice_dict['chap_19_1_1']['tts']
        req_save["save"] = 'chap_19_1_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_2(req_save, command, intent, user_id):
    COMMANDS_3 = ['искать в кровати', 'в кровати', 'кровать', 'да', 'ага', 'давай']
    if command in COMMANDS_3:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_1_1(req_save, command, intent, user_id):
    COMMANDS_2 = ['искать на полу', 'на полу', 'пол']
    COMMANDS_3 = ['искать в кровати', 'в кровати', 'кровать', 'на кровати']
    if command in COMMANDS_2:
        text = alice_dict['chap_19_2']['text']
        tts = alice_dict['chap_19_2']['tts']
        req_save["save"] = 'chap_19_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_3:
        text = alice_dict['chap_19_3']['text']
        tts = alice_dict['chap_19_3']['tts']
        req_save["save"] = 'chap_19_3'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_19_3(req_save, command, intent, user_id):
    COMMANDS = ['вернуться в камеру', 'вернуться', 'в камеру', 'быстрее', 'камеру', 'камера']
    text = alice_dict['chap_20']['text']
    tts = alice_dict['chap_20']['tts']
    new_save = {'accept': 'chap_20', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_21(req_save, command, intent, user_id):
    COMMANDS = ['спрятать под одеждой', 'оставить в камере', 'под одеждой', 'в камере', 'спрятать в камере', 'спрятать под кроватью', 'прятать', 'оставить', 'под одежду']
    if command in COMMANDS:
        text = alice_dict['chap_21']['text']
        tts = alice_dict['chap_21']['tts']
        req_save["save"] = "chap_21"
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['перепрятать']
    COMMANDS_2 = ['не хочу']
    text = alice_dict['chap_21_1']['text']
    tts = alice_dict['chap_21_1']['tts']
    text_reject = alice_dict['chap_21_2']['text']
    tts_reject = alice_dict['chap_21_2']['tts']
    new_save = {'accept': 'chap_21_1', 'reject': 'chap_21_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap_21_1(req_save, command, intent, user_id):
    COMMANDS = ['загрузить последнее сохранение', 'загрузить', 'последнее', 'загружай', 'загрухи сохранение', 'загрузить сохранение']
    if command in COMMANDS:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_9'}})
        text = alice_dict['chap_9']['text']
        tts = alice_dict['chap_9']['tts']
        req_save["save"] = 'chap_9'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_21_2(req_save, command, intent, user_id):
    COMMANDS = ['сохранить игру', 'сохранить']
    if command in COMMANDS:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22', "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
        text= '''Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня.\n
                Начать побег сейчас или во время обеда?'''
        tts='''Вы не выспались и бодрствовали всю ночь из-за кошмаров. Однако, вы понимаете, что это ваш последний день в тюрьме, и принимаете решение сбежать сегодня. Начать побег сейчас или во время обеда?'''
        req_save['save'] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_22(req_save, command, intent, user_id):
    COMMANDS_1 = ['начать побег в обед', 'в обед', 'побег в обед', 'обед']
    COMMANDS_2 = ['начать побег сейчас', 'сейчас', 'побег сейчас', 'начать сейчас']
    if command in COMMANDS_1:
        text = alice_dict['chap_22_1']['text']
        tts = alice_dict['chap_22_1']['tts']
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_22_2']['text']
        tts = alice_dict['chap_22_2']['tts']
        req_save['save'] = 'chap_22_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_22_1(req_save, command, intent, user_id):
    COMMANDS = ['войти в комнату', 'войти', 'в комнату', 'комната', 'зайти в комнату', 'зайти']
    text = alice_dict['chap_24']['text']
    tts = alice_dict['chap_24']['tts']
    new_save = {'accept': 'chap_24', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_22_2(req_save, command, intent, user_id):
    COMMANDS_1 = ['войти в комнату', 'войти', 'в комнату', 'комната', 'зайти в комнату', 'зайти']
    COMMANDS_2 = ['осмотреться', 'хочу осмотреться', 'осмотрюсь', 'осмотрись', 'посмотреть']
    if command in COMMANDS_1:
        text = alice_dict['chap_23_2']['text']
        tts = alice_dict['chap_23_2']['tts']
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_23']['text']
        tts = alice_dict['chap_23']['tts']
        req_save['save'] = 'chap_23'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23(req_save, command, intent, user_id):
    COMMANDS_1 = ['войти в комнату', 'войти', 'в комнату', 'комната', 'зайти в комнату', 'зайти']
    COMMANDS_2 = ['вернуться в обед', 'вернуться', 'в обед', 'обед', 'не сейчас']
    if command in COMMANDS_1:
        text = alice_dict['chap_23_2']['text']
        tts = alice_dict['chap_23_2']['tts']
        req_save['save'] = 'chap_23_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_22_1']['text']
        tts = alice_dict['chap_22_1']['tts']
        req_save['save'] = 'chap_22_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_23_1(req_save, command, intent, user_id):  # == chap_22_1
    COMMANDS = ['войти в комнату', 'войти', 'в комнату', 'комната', 'зайти в комнату', 'зайти']
    if command in COMMANDS:
        text = alice_dict['chap_24']['text']
        tts = alice_dict['chap_24']['tts']
        req_save['save'] = 'chap_24'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)  # можно удалить


def chap_23_2(req_save, command, intent, user_id):
    COMMANDS = ['загрузить последнее сохранение', 'загрузить', 'загружай', 'сохранение', 'последнее сохранение']
    if command in COMMANDS:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22'}})
        req_save['save'] = 'chap_22'
        text = alice_dict['chap_22']['text']
        tts = alice_dict['chap_22']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24(req_save, command, intent, user_id):
    COMMANDS_1 = ['сделать кирку', 'лучше кирку', 'кирку']
    COMMANDS_2 = ['сделать топор', 'топор', 'лучше топор']
    if command in COMMANDS_1:
        text = alice_dict['chap_24_1']['text']
        tts = alice_dict['chap_24_1']['tts']
        req_save['save'] = 'chap_24_1'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        text = alice_dict['chap_24_2']['text']
        tts = alice_dict['chap_24_2']['tts']
        req_save['save'] = 'chap_24_2'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_24_1(req_save, command, intent, user_id):
    COMMANDS = ['продолжить ломать решетку', 'продолжить', 'продолжить ломать', 'ломать решетку', 'продолжай']
    text = alice_dict['chap_25']['text']
    tts = alice_dict['chap_25']['tts']
    new_save = {'accept': 'chap_25', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_24_2(req_save, command, intent, user_id):
    COMMANDS = ['начать ломать решетку', 'начать', 'начать ломать', 'ломать решетку']
    text = alice_dict['chap_25']['text']
    tts = alice_dict['chap_25']['tts']
    new_save = {'accept': 'chap_25', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap_25(req_save, command, intent, user_id):
    COMMANDS_1 = ['стоит', 'конечно', 'уходим из города', 'из города']
    COMMANDS_2 = ['не стоит', 'остаться', 'не надо', 'остаюсь', 'а я останусь']
    text = alice_dict['chap_25_1']['text']
    tts = alice_dict['chap_25_1']['tts']
    text_reject = alice_dict['chap_25_2']['text']
    tts_reject = alice_dict['chap_25_2']['tts']
    new_save = {'accept': 'chap_25_1', 'reject': 'chap_23_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap_25_1(req_save, command, intent, user_id):
    COMMANDS_1 = ['сломать', 'ломать', 'начать ломать', 'попробовать сломать']
    COMMANDS_2 = ['ждать', 'лучше ждать', 'подождать', 'жду', 'лучше подождать']
    if command in COMMANDS_1:
        req_save['save'] = 'chap_23_2'
        text = alice_dict['chap_25_1']['text']
        tts = alice_dict['chap_25_1']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    elif command in COMMANDS_2:
        req_save['save'] = 'chap_25_1_2'
        text = alice_dict['chap_25_1_2']['text']
        tts = alice_dict['chap_25_1_2']['tts']
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_1_1(req_save, command, intent, user_id):
    COMMANDS = ['загрузить последнее сохранение', 'загрузить', 'последнее', 'сохранение', 'последнее сохранение']
    if command in COMMANDS:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap_22'}})
        text = alice_dict['chap_22']['text']
        tts = alice_dict['chap_22']['tts']
        req_save["save"] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)  # == chap_23_2


def chap_25_1_2(req_save, command, intent, user_id):
    COMMANDS = ['сохранить игру', 'сохранить', 'сохраняй']
    if command in COMMANDS:
        COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": req_save['save'], "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
        text = 'Поздравляем, вы успешно завершили 1 главу!!!!' \
               'Спасибо за игру (2 глава находится на тестировании)'
        tts = 'Поздравляем, вы успешно завершили 1 главу!!!!' \
              'Спасибо за игру (2 глава находится на тестировании)'
        req_save['save'] = 'start'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)


def chap_25_2(req_save, command, intent, user_id):
    COMMANDS = ['загрузить последнее сохранение', 'загрузить', 'последнее', 'сохранение', 'последнее сохранение']
    if command in COMMANDS:
        text = alice_dict['chap_22']['text']
        tts = alice_dict['chap_22']['tts']
        req_save["save"] = 'chap_22'
        return message_sent(text=text, tts=tts, save=req_save, version=version)
    else:
        return message_help(req_save, version)  # == chap_23_2

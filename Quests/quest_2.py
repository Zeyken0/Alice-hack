from help_dialogs import message_sent, quest_confirm_reject_handler, quest_message_help
from Replicas.Quest_says import Quest_says
import random

version = "1.0"


def quest2(req_save, command, intent, user_id):
    req_save['save'] = 'quest2_x'
    text = Quest_says['quest2']['text']
    tts = Quest_says['quest2']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def quest2_x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        if req_save['other']['Map']:
            text = Quest_says['quest2_2']['text']
            tts = Quest_says['quest2_2']['tts']
            req_save['save'] = 'quest2_3_x'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = Quest_says['quest2_1']['text']
            tts = Quest_says['quest2_1']['tts']
            req_save['save'] = 'quest2_1_1'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_1_1(req_save, command, intent, user_id):
    req_save['save'] = 'Home'
    text = Quest_says['quest2_1_1']['text']
    tts = Quest_says['quest2_1_1']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def quest2_3_x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = Quest_says['quest2_3']['text']
        tts = Quest_says['quest2_3']['tts']
        req_save['save'] = 'quest2_4_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.REJECT" in intent or "" in intent:
        text = 'Вы вернулись в убежище'
        tts = 'Вы вернулись в убежище'
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_4_x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = Quest_says['quest2_4_1x']['text']
        tts = Quest_says['quest2_4_1x']['tts']
        req_save['save'] = 'quest2_5x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.REJECT" in intent or "" in intent:
        text = Quest_says['quest2_4_x']['text']
        tts = Quest_says['quest2_4_x']['tts']
        req_save['save'] = 'quest2_4_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_4_1x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = Quest_says['quest2_4_1x']['text']
        tts = Quest_says['quest2_4_1x']['tts']
        req_save['save'] = 'quest2_fight_n1'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_fight_n1(req_save, command, intent, user_id):
    if "" in intent:  # лёгкая
        damage = random.randint(1, 3)
        text = ""
        tts = ""
        enemy_answer = random.randint(1, 100)
        if enemy_answer < 35:  # temniy shit
            text += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
            tts += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
        elif enemy_answer > 65:
            text += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
            tts += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
            req_save['health'] -= 3  # black arrow
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                text = Quest_says['quest2_5_x']['text']
                tts = Quest_says['quest2_5_x']['tts']
                req_save['save'] = 'quest2_6'
            elif req_save['health'] <= 0:
                text = Quest_says['quest2_5_1x']['text']
                tts = Quest_says['quest2_5_1x']['tts']
                req_save['save'] = 'quest2_end'
        else:
            text += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''
            tts += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''  # proklatie slabosti
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "" in intent:  # тяжелая
        if req_save['stamina'] > 40:
            damage = random.randint(2, 5)
            text = ""
            tts = ""
            enemy_answer = random.randint(1, 100)
            if enemy_answer < 35:  # temniy shit
                text += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
                tts += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
            elif enemy_answer > 65:
                text += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                tts += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                req_save['health'] -= 3  # black arrow
                req_save['other']['enemy']['health'] -= damage
                if req_save['other']['enemy']['health'] <= 0:
                    text = Quest_says['quest2_5_x']['text']
                    tts = Quest_says['quest2_5_x']['tts']
                    req_save['save'] = 'quest2_6'
                elif req_save['health'] <= 0:
                    text = Quest_says['quest2_5_1x']['text']
                    tts = Quest_says['quest2_5_1x']['tts']
                    req_save['save'] = 'quest2_end'
            else:
                text += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''
                tts += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''  # proklatie slabosti
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "" in intent:
        text = '''Вы восстановили 40 очков.
Но противник зря времени не терял и нанес вам удар жезлом. -2 единицы здоровья.'''
        tts = '''Вы восстановили 40 очков.
Но противник зря времени не терял и нанес вам удар жезлом. -2 единицы здоровья.'''
        req_save['health'] -= 2
        if req_save['health'] <= 0:
            text = Quest_says['quest2_5_1x']['text']
            tts = Quest_says['quest2_5_1x']['tts']
            req_save['save'] = 'quest2_end'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


# ВОТ ЗДЕСЬ ДОДЕЛАТЬ
def quest2_end(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = 'Вы вернулись в убежище'
        tts = 'Вы вернулись в убежище'
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_6(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = Quest_says['quest2_6']['text']
        tts = Quest_says['quest2_6']['tts']
        req_save['save'] = 'quest2_7'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_7(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        text = Quest_says['quest2_7']['text']
        tts = Quest_says['quest2_7']['tts']
        req_save['save'] = 'quest2_8'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_8(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "" in intent:
        req_save['other']['Book']['active'] = True
        req_save['save'] = 'Home'
        text = Quest_says['quest2_8']['text']
        tts = Quest_says['quest2_8']['tts']
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)

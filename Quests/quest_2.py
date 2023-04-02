from pymongo import MongoClient

from help_dialogs import message_sent, quest_confirm_reject_handler, quest_message_help
from Replicas.Quest_says import Quest_says
import random

version = "1.0"


def quest2(req_save, command, intent, user_id):
    req_save['save'] = 'quest2_x'
    req_save['chapter'] = 'quest2'
    text = Quest_says['quest2']['text']
    tts = Quest_says['quest2']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def quest2_x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_x.CONFIRM" in intent:
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
    if "YANDEX.CONFIRM" in intent or "quest2_3_x" in intent:
        text = Quest_says['quest2_3']['text']
        tts = Quest_says['quest2_3']['tts']
        req_save['save'] = 'quest2_4_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.REJECT" in intent:
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
        req_save['save'] = 'quest2_fight_n1'
        req_save['health'] = 20
        req_save['stamina'] = 100
        req_save['other']['enemy']['health'] = 15
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.REJECT" in intent or "" in intent:
        text = Quest_says['quest2_4_x']['text']
        tts = Quest_says['quest2_4_x']['tts']
        req_save['save'] = 'quest2_4_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_4_1x(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_4_1x" in intent:
        text = Quest_says['quest2_4_1x']['text']
        tts = Quest_says['quest2_4_1x']['tts']
        req_save['save'] = 'quest2_fight_n1'
        req_save['health'] = 20
        req_save['stamina'] = 100
        req_save['other']['enemy']['health'] = 15
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_fight_n1(req_save, command, intent, user_id):
    if "quest2_fight.EASY" in intent:  # лёгкая
        if req_save['stamina'] > 15:
            req_save['stamina'] -= 15
            damage = random.randint(1, 3)
            text = "Вы нанесли Нечестивому " + str(damage) + ' урона. '
            tts = "Вы нанесли Нечестивому " + str(damage) + ' урона. '
            enemy_answer = random.randint(1, 100)
            req_save['other']['enemy']['health'] -= damage
            if enemy_answer < 35:  # temniy shit
                req_save['other']['enemy']['health'] += damage
                text += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
                tts += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
            elif enemy_answer > 65:
                text += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                tts += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                req_save['health'] -= 3  # black arrow
            else:
                text += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''
                tts += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''  # proklatie slabosti
            if req_save['other']['enemy']['health'] <= 0:
                text = Quest_says['quest2_5_x']['text']
                tts = Quest_says['quest2_5_x']['tts']
                req_save['save'] = 'quest2_6'
            elif req_save['health'] <= 0:
                text = Quest_says['quest2_5_1x']['text']
                tts = Quest_says['quest2_5_1x']['tts']
                req_save['save'] = 'quest2_end'
            text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
            tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest2_fight" in intent:  # тяжелая
        if req_save['stamina'] > 40:
            req_save['stamina'] -= 40
            damage = random.randint(2, 5)
            text = "Вы нанесли Нечестивому " + str(damage) + ' урона. '
            tts = "Вы нанесли Нечестивому " + str(damage) + ' урона. '
            enemy_answer = random.randint(1, 100)
            req_save['other']['enemy']['health'] -= damage
            if enemy_answer < 35:  # temniy shit
                req_save['other']['enemy']['health'] += damage
                text += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
                tts += '''Нечестивый поднимает руку и создаёт из тёмной энергии щит, который защищает его от атаки.'''
            elif enemy_answer > 65:
                text += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                tts += '''Нечестивый поднимает свой жезл и произносит заклинание "Темная стрела", направляя стрелу на вас. -3 единицы здоровья'''
                req_save['health'] -= 3  # black arrow
            else:
                text += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''
                tts += '''Нечестивый касается вас своим жезлом и произносит заклинание "Проклятие слабости", вызывая у вас чувство слабости.'''  # proklatie slabosti
            if req_save['other']['enemy']['health'] <= 0:
                text = Quest_says['quest2_5_x']['text']
                tts = Quest_says['quest2_5_x']['tts']
                req_save['save'] = 'quest2_6'
            elif req_save['health'] <= 0:
                text = Quest_says['quest2_5_1x']['text']
                tts = Quest_says['quest2_5_1x']['tts']
                req_save['save'] = 'quest2_end'
            text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
            tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest2_fight.RELAX" in intent:
        text = '''Вы восстановили 40 очков.
Но противник зря времени не терял и нанес вам удар жезлом. -2 единицы здоровья.'''
        tts = '''Вы восстановили 40 очков.
Но противник зря времени не терял и нанес вам удар жезлом. -2 единицы здоровья.'''
        req_save['health'] -= 2
        req_save['stamina'] = min(100, req_save['stamina'] + 40)
        if req_save['health'] <= 0:
            text = Quest_says['quest2_5_1x']['text']
            tts = Quest_says['quest2_5_1x']['tts']
            req_save['save'] = 'quest2_end'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


# ВОТ ЗДЕСЬ ДОДЕЛАТЬ
def quest2_end(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_end" in intent:
        text = 'Вы вернулись в убежище'
        tts = 'Вы вернулись в убежище'
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_6(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_6" in intent:
        req_save['score'] += random.randint(10, 16)
        text = Quest_says['quest2_6']['text']
        tts = Quest_says['quest2_6']['tts']
        req_save['save'] = 'quest2_7'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_7(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_7" in intent:
        text = Quest_says['quest2_7']['text']
        tts = Quest_says['quest2_7']['tts']
        req_save['save'] = 'quest2_8'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)


def quest2_8(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "quest2_8" in intent:
        req_save['other']['Book']['active'] = True
        req_save['other']['Quests']['quest2'] = True
        req_save['save'] = 'Home'
        text = Quest_says['quest2_8']['text']
        tts = Quest_says['quest2_8']['tts']
        CLUSTER = MongoClient("mongodb+srv://Alisa:pasword@alisa.cayawc6.mongodb.net/?retryWrites=true&w=majority")
        DB = CLUSTER["AlisaBase"]
        COLLECTION = DB["users"]
        COLLECTION.update_one({"id": user_id}, {
            "$set": {"name": req_save['name'], "save": req_save['save'], "chapter": req_save['chapter'],
                     "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return quest_message_help(req_save, version)

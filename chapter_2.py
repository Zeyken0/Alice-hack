from dialogs import message_sent, d_start_0, message_sent_with_card
from help_dialogs import message_help, confirm_reject_handler, confirm_reject_handler_with_card
from config import *
from alice_says import alice_dict
import random

version = "1.0"


def chap2(req_save, command, intent, user_id):
    req_save['save'] = 'chap2_1_x'
    text = alice_dict['2_chap']['text']
    tts = alice_dict['2_chap']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_1_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['остановиться']
    COMMANDS_2 = ['не остановиться']
    text = alice_dict['2_chap_1_x']['text']
    tts = alice_dict['2_chap_1_x']['tts']
    text_reject = alice_dict['2_chap_1_1x']['text']
    tts_reject = alice_dict['2_chap_1_1x']['tts']
    new_save = {'accept': 'chap2_2', 'reject': 'chap2_2'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_2(req_save, command, intent, user_id):
    COMMANDS = ['осмотреть себя']
    if command in COMMANDS:
        text = alice_dict['2_chap_2']['text']
        tts = alice_dict['2_chap_2']['tts']
        req_save['save'] = 'chap2_3_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['влево']
    COMMANDS_2 = ['вперед']
    COMMANDS_3 = ['вправо']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_1x']['text']
        tts = alice_dict['2_chap_3_1x']['tts']
        req_save['save'] = 'chap2_3_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2x']['text']
        tts = alice_dict['2_chap_3_2x']['tts']
        req_save['save'] = 'chap2_3_2x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_3:
        text = alice_dict['2_chap_3_3x']['text']
        tts = alice_dict['2_chap_3_3x']['tts']
        req_save['save'] = 'chap2_3_3x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_1x(req_save, command, intent, user_id):
    COMMANDS_1 = ['идти']
    COMMANDS_2 = ['осмотреться']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_1_1x']['text']
        tts = alice_dict['2_chap_3_1_1x']['tts']
        req_save['save'] = 'chap_2_3_1_1x'  # вернуть на последнее сохранение
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_1_2x']['text']
        tts = alice_dict['2_chap_3_1_2x']['tts']
        req_save['save'] = 'chap2_3_1_2x'  # вернуть на последнее сохранение
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3x(req_save, command, intent, user_id):
    COMMANDS_1 = ['резко']
    COMMANDS_2 = ['медленно']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_3_1x']['text']
        tts = alice_dict['2_chap_3_3_1x']['tts']
        req_save['save'] = 'chap2_3_3_1x'  # вернуть на последнее сохранение
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_3x']['text']
        tts = alice_dict['2_chap_3_3x']['tts']
        req_save['save'] = 'chap2_3_3_1'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_1(req_save, command, intent, user_id):
    COMMANDS = ['плыть', 'прощупывать дно палкой']
    if command in COMMANDS:
        text = alice_dict['2_chap_3_3_1']['text']
        tts = alice_dict['2_chap_3_3_1']['tts']
        req_save['save'] = 'chap2_3_3_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2(req_save, command, intent, user_id):
    COMMANDS = ['идти дальше']
    text = alice_dict['2_chap_3_3_2']['text']
    tts = alice_dict['2_chap_3_3_2']['tts']
    new_save = {'accept': 'chap2_3_3_2_x', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_3_2_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['перепрыгнуть']
    COMMANDS_2 = ['мост']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_3_2_1x']['text']
        tts = alice_dict['2_chap_3_3_2_1x']['tts']
        req_save['save'] = 'chap2_3_3_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_3_2_x']['text']
        tts = alice_dict['2_chap_3_3_2_x']['tts']
        req_save['save'] = 'chap2_3_3_2_1'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_1(req_save, command, intent, user_id):
    COMMANDS = ['инвентарь']
    if command in COMMANDS:
        text = alice_dict['2_chap_3_3_2_1']['text']
        tts = alice_dict['2_chap_3_3_2_1']['tts']
        req_save['save'] = 'chap2_3_3_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_2(req_save, command, intent, user_id):
    COMMANDS = ['взять самодельный топор']
    if command in COMMANDS:
        text = alice_dict['2_chap_3_3_2_2']['text']
        tts = alice_dict['2_chap_3_3_2_2']['tts']
        req_save['save'] = 'chap2_3_3_2_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_2_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['отправиться']
    COMMANDS_2 = ['не отправиться']
    text = alice_dict['2_chap_3_3_2_2_x']['text']
    tts = alice_dict['2_chap_3_3_2_2_x']['tts']
    text_reject = alice_dict['2_chap_3_3_2_2_1x']['text']
    tts_reject = alice_dict['2_chap_3_3_2_2_1x']['tts']
    new_save = {'accept': 'chap2_3_0', 'reject': 'chap2_3_3_2_2_1x'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_3_2x(req_save, command, intent, user_id):
    COMMANDS_1 = ['сразиться']
    COMMANDS_2 = ['пройти мимо']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_1x']['text']
        tts = alice_dict['2_chap_3_2_1x']['tts']
        req_save['save'] = 'chap2_3_2_1_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_x']['text']
        tts = alice_dict['2_chap_3_2_x']['tts']
        req_save['save'] = 'chap2_3_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['инвентарь']
    COMMANDS_2 = ['взять самодельный топор']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_1_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2(req_save, command, intent, user_id):
    COMMANDS_2 = ['взять самодельный топор']
    if command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['прикинуться мертвым']
    COMMANDS_2 = ['продолжить']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_1_2_x']['text']
        tts = alice_dict['2_chap_3_2_1_2_x']['tts']
        req_save['save'] = 'chap2_3_2_1_2_0x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_0x(req_save, command, intent, user_id):
    COMMANDS_1 = ['продолжить']
    COMMANDS_2 = ['встать']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_1_2_1']['text']
        tts = alice_dict['2_chap_3_2_1_2_1']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_2(req_save, command, intent, user_id):
    COMMANDS = ['хочу']
    text = alice_dict['2_chap_3_2_1_2_2']['text']
    tts = alice_dict['2_chap_3_2_1_2_2']['tts']
    new_save = {'accept': 'chap2_3_2_1_2_2_x', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_2_1_2_2_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['лечь спать']
    COMMANDS_2 = ['продолжить']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_1_2_2_1x']['text']
        tts = alice_dict['2_chap_3_2_1_2_2_1x']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_1_2_2_x']['text']
        tts = alice_dict['2_chap_3_2_1_2_2_x']['tts']
        req_save['save'] = 'chap2_3_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2(req_save, command, intent, user_id):
    COMMANDS = ['спустить']
    text = alice_dict['2_chap_3_2_2']['text']
    tts = alice_dict['2_chap_3_2_2']['tts']
    new_save = {'accept': 'chap2_3_2_2_2_0', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_2_2_2_0(req_save, command, intent, user_id):
    COMMANDS_1 = ['лечь спать']
    COMMANDS_2 = ['обыскать шлюпку']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_2_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_2_2']['text']
        tts = alice_dict['2_chap_3_2_2_2']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1x(req_save, command, intent, user_id):
    COMMANDS_1 = ['лечь спать']
    COMMANDS_2 = ['перекусить']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_2_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_2_2_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['остаться']
    COMMANDS_2 = ['выпрыгнуть']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_2_2_2_1_x']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_x']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2_2_2_1_1x']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1x']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_end(req_save, command, intent, user_id):
    COMMANDS = ['загрузить последнее сохранение']
    if command in COMMANDS:
        text = alice_dict['2_chap']['text']
        tts = alice_dict['2_chap']['tts']
        req_save['save'] = 'chap2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_0(req_save, command, intent, user_id):
    COMMANDS = ['инвентарь']
    if command in COMMANDS:
        text = alice_dict['2_chap_3_2_2_2_1_0']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_0']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_2(req_save, command, intent, user_id):
    COMMANDS = ['взять самодельный топор']
    if command in COMMANDS:
        text = alice_dict['2_chap_3_2_2_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_2']['tts']
        req_save['save'] = 'chap2_3_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_0(req_save, command, intent, user_id):
    COMMANDS = ['очнуться', 'лечь спать']
    text = alice_dict['2_chap_3_0']['text']
    tts = alice_dict['2_chap_3_0']['tts']
    new_save = {'accept': 'chap2_4', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_4(req_save, command, intent, user_id):
    COMMANDS = ['познакомиться']
    text = alice_dict['2_chap_4']['text']
    tts = alice_dict['2_chap_4']['tts']
    new_save = {'accept': 'chap2_5', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_5(req_save, command, intent, user_id):
    COMMANDS = ['помочь']
    text = alice_dict['2_chap_5']['text']
    tts = alice_dict['2_chap_5']['tts']
    new_save = {'accept': 'chap2_6', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_6(req_save, command, intent, user_id):
    COMMANDS = ['открыть инвентарь']
    text = alice_dict['2_chap_6']['text']
    tts = alice_dict['2_chap_6']['tts']
    new_save = {'accept': 'chap2_7', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_7(req_save, command, intent, user_id):
    gear_dict = {  # ДОПИСАТЬ ВЕЩИ!!!! НЕТУ ПРОВЕРКИ НА ОРУЖИЕ
        'Потрепанный шлем': ('helmet',),
        'Потрепанный нагрудник': ('chest',)
    }
    all_items_boolean = False
    for gear, keys in gear_dict.items():
        if gear in command:
            if keys[0] == 'axe' or keys[0] == 'sword':
                req_save["other"]['weapon'][keys[0]]["broken"]["activity"] = True
                req_save["other"]['weapon'][keys[0]]["broken"]["is_gear"] = True
                break
            else:
                req_save["other"]['armor'][keys[0]]["broken"]["activity"] = True
                req_save["other"]['armor'][keys[0]]["broken"]["is_gear"] = True
                break
        if req_save["other"]['armor'][keys[0]]["broken"]["is_gear"]:
            all_items_boolean = True
        else:
            all_items_boolean = False
    if all_items_boolean:
        COMMANDS = ['']
        text = alice_dict['2_chap_7']['text']
        tts = alice_dict['2_chap_7']['tts']
        new_save = {'accept': 'chap2_7_x', 'reject': ''}
        return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                      new_save=new_save)


def chap2_7_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['']
    COMMANDS_2 = ['']
    text = alice_dict['2_chap_7_2']['text']
    tts = alice_dict['2_chap_7_2']['tts']
    text_reject = alice_dict['2_chap_7_1']['text']
    tts_reject = alice_dict['2_chap_7_1']['tts']
    new_save = {'accept': 'chap2_7_2_fight', 'reject': 'chap2_7_1'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_7_1(req_save, command, intent, user_id):
    COMMANDS = ['отправиться в пещеру']
    text = alice_dict['2_chap_7_2']['text']
    tts = alice_dict['2_chap_7_2']['tts']
    new_save = {'accept': 'chap2_7_2_fight', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_7_2_fight(req_save, command, intent, user_id):
    COMMANDS_1 = ['мощная атака']
    COMMANDS_2 = ['слабая атака']
    COMMANDS_3 = ['отдохнуть']
    if command in COMMANDS_1:
        if req_save['stamina'] < 30:
            text = 'Вы устали, можете немного отдохнуть или ударить лёгкой атакой'
            tts = 'Вы устали, можете немного отдохнуть или ударить лёгкой атакой'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            if random.random() < 0.5:  # v1 тяжелая
                text = 'Тяжелая атака v1(-0)'
                tts = 'Тяжелая атака v1(-0)'
                if random.random() < 0.5:
                    text += 'Ответ v1(-0)'
                    tts += 'Ответ v1(-0)'
                else:
                    text += 'Ответ v2(-4)'
                    tts += 'Ответ v2(-4)'
                    req_save['health'] -= 4
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = 'Тяжелая атака v2(-4)'
                tts = 'Тяжелая атака v2(-4)'
                if random.random() < 0.5:
                    text += 'Ответ v1(-0)'
                    tts += 'Ответ v1(-0)'
                else:
                    text += 'Ответ v2(-4)'
                    tts += 'Ответ v2(-4)'
                    req_save['health'] -= 4
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        if req_save['stamina'] < 15:
            text = 'Вы слишком устали, вам нужно отдохнуть'
            tts = 'Вы слишком устали, вам нужно отдохнуть'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            if random.random() < 0.5:  # v1 лёгкая
                text = 'Лёгкая атака v1(-0)'
                tts = 'Лёгкая атака v1(-0)'
                if random.random() < 0.5:
                    text += 'Ответ v1(-0)'
                    tts += 'Ответ v1(-0)'
                else:
                    text += 'Ответ v2(-4)'
                    tts += 'Ответ v2(-4)'
                    req_save['health'] -= 4
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = 'Лёгкая атака v2(-2)'
                tts = 'Лёгкая атака v2(-2)'
                if random.random() < 0.5:
                    text += 'Ответ v1(-0)'
                    tts += 'Ответ v1(-0)'
                else:
                    text += 'Ответ v2(-4)'
                    tts += 'Ответ v2(-4)'
                    req_save['health'] -= 4
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_3:
        if req_save['stamina'] > 60:
            text = 'Вы хорошо отдохнули'
            tts = 'Вы хорошо отдохнули'
            req_save['health'] -= 2
            req_save['stamina'] = 100
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            req_save['health'] -= 2
            req_save['stamina'] += 40
            text = 'Вы немного отдышались'
            tts = 'Вы немного отдышались'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help('2_chap_7_2', version)


def chap2_9(req_save, command, intent, user_id):
    COMMANDS = ['расспросить']
    text = alice_dict['2_chap_9']['text']
    tts = alice_dict['2_chap_9']['tts']
    new_save = {'accept': 'chap2_10', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_10(req_save, command, intent, user_id):
    COMMANDS = ['начать убираться']
    text = alice_dict['2_chap_10']['text']
    tts = alice_dict['2_chap_10']['tts']
    new_save = {'accept': 'chap2_11', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_11(req_save, command, intent, user_id):
    COMMANDS = ['лечь спать', 'загрузить последнее сохранение']
    text = alice_dict['2_chap_11']['text']
    tts = alice_dict['2_chap_11']['tts']
    new_save = {'accept': 'chap2_12', 'reject': ''}
    # СОХРАНЕНИЕ
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_12(req_save, command, intent, user_id):
    COMMANDS = ['пойти поесть']
    text = alice_dict['2_chap_12']['text']
    tts = alice_dict['2_chap_12']['tts']
    new_save = {'accept': 'chap2_13_x', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_13_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['ягоды']
    COMMANDS_2 = ['рыба']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_13_1']['text']
        tts = alice_dict['2_chap_13_1']['tts']
        req_save['save'] = 'chap2_14'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_13_2']['text']
        tts = alice_dict['2_chap_13_2']['tts']
        req_save['save'] = 'chap2_13_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_13_2_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['пожарить']
    COMMANDS_2 = ['не жарить']
    text = alice_dict['2_chap_13_2_1']['text']
    tts = alice_dict['2_chap_13_2_1']['tts']
    text_reject = alice_dict['2_chap_13_2_2']['text']
    tts_reject = alice_dict['2_chap_13_2_2']['tts']
    new_save = {'accept': 'chap2_14', 'reject': 'chap2_14'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_14(req_save, command, intent, user_id):
    COMMANDS = ['осмотреться']
    text = alice_dict['2_chap_14']['text']
    tts = alice_dict['2_chap_14']['tts']
    new_save = {'accept': 'chap2_15_x', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_15_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['прикоснуться']
    COMMANDS_2 = ['не прикасаться']
    text = alice_dict['2_chap_15_x']['text']
    tts = alice_dict['2_chap_15_x']['tts']
    text_reject = alice_dict['2_chap_15_1x']['text']
    tts_reject = alice_dict['2_chap_15_1x']['tts']
    new_save = {'accept': 'chap2_14', 'reject': 'chap2_14'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_15_x_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['подуть']
    COMMANDS_2 = ['не дуть']
    text = alice_dict['2_chap_15_x_x']['text']
    tts = alice_dict['2_chap_15_x_x']['tts']
    text_reject = alice_dict['2_chap_15_x_1x']['text']
    tts_reject = alice_dict['2_chap_15_x_1x']['tts']
    new_save = {'accept': 'chap2_16_x', 'reject': 'chap2_16_x'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


""" ЗДЕСЬ ХУЙНЯ, 
ВНИМАТЕЛЬНО ПОСМОТРЕТЬ ОПИСАНИЕ БЛОКОВ, ПЕРЕДЕЛАТЬ
"""


def chap2_16_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['земля']
    COMMANDS_2 = ['вода']
    COMMANDS_3 = ['огонь']
    water = req_save['other']['runes']['water']
    fire = req_save['other']['runes']['fire']
    terra = req_save['other']['runes']['earth']
    if command in COMMANDS_1:
        if terra and fire:
            text = alice_dict['2_chap_16_2x']['text'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            tts = alice_dict['2_chap_16_2x']['tts'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            req_save['save'] = 'chap2_17'
        elif not terra and fire:
            text = alice_dict['2_chap_16_2x']['text'] + '''Зажжешь руну земли?'''
            tts = alice_dict['2_chap_16_2x']['tts'] + '''Зажжешь руну земли?'''
            req_save['save'] = 'chap2_16_x'
        elif terra and not fire:
            text = alice_dict['2_chap_16_2x']['text'] + '''Зажжешь руну огня?'''
            tts = alice_dict['2_chap_16_2x']['tts'] + '''Зажжешь руну огня?'''
            req_save['save'] = 'chap2_16_x'
        else:
            text = 'Вторая руна зажжена! Использовать "Землю" или "Огонь"'
            tts = 'Вторая руна зажжена! Использовать "Землю" или "Огонь"'
            req_save['save'] = 'chap2_16_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_16_3x']
        tts = alice_dict['2_chap_16_3x']
        req_save['save'] = 'chap2_16_3x_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_3:
        if water and fire:
            text = alice_dict['2_chap_16_1x']['text'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            tts = alice_dict['2_chap_16_1x']['tts'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            req_save['save'] = 'chap2_17'
        elif not water and fire:
            text = alice_dict['2_chap_16_1x']['text'] + '''Зажжешь руну воды?'''
            tts = alice_dict['2_chap_16_1x']['tts'] + '''Зажжешь руну воды?'''
            req_save['save'] = 'chap2_16_x'
        elif water and not fire:
            text = alice_dict['2_chap_16_1x']['text'] + '''Зажжешь руну огня?'''
            tts = alice_dict['2_chap_16_1x']['tts'] + '''Зажжешь руну огня?'''
            req_save['save'] = 'chap2_16_x'
        else:
            text = 'Вторая руна зажжена! Использовать "Воду" или "Огонь".'
            tts = 'Вторая руна зажжена! Использовать "Воду" или "Огонь".'
            req_save['save'] = 'chap2_16_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_16_3x_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['сразиться']
    COMMANDS_2 = ['убежать']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_16_3x_1x']['text']
        tts = alice_dict['2_chap_16_3x_1x']['tts']
        req_save['save'] = 'chap2_11'  # загрузка последнего сохранения
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        water = req_save['other']['runes']['water']
        terra = req_save['other']['runes']['earth']
        if water and terra:
            text = alice_dict['2_chap_16_3x_x']['text'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            tts = alice_dict['2_chap_16_3x_x']['tts'] + '''Все руны загораются, но никаких изменений не происходит.
             Прикоснуться к стене?'''
            req_save['save'] = 'chap2_17'
        elif not water and terra:
            text = alice_dict['2_chap_16_3x_x']['text'] + '''Зажжешь руну воды?'''
            tts = alice_dict['2_chap_16_3x_x']['tts'] + '''Зажжешь руну воды?'''
            req_save['save'] = 'chap2_16_x'
        elif water and not terra:
            text = alice_dict['2_chap_16_3x_x']['text'] + '''Зажжешь руну земли?'''
            tts = alice_dict['2_chap_16_3x_x']['tts'] + '''Зажжешь руну земли?'''
            req_save['save'] = 'chap2_16_x'
        else:
            text = 'Вторая руна зажжена! Использовать "Землю" или "Воду".'
            tts = 'Вторая руна зажжена! Использовать "Землю" или "Воду".'
            req_save['save'] = 'chap2_16_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_17(req_save, command, intent, user_id):
    COMMANDS = ['']
    text = alice_dict['2_chap_17']['text']
    tts = alice_dict['2_chap_17']['tts']
    new_save = {'accept': 'chap2_18_x', 'reject': ''}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS, text=text, tts=tts,
                                  new_save=new_save)


def chap2_18_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['держать']
    COMMANDS_2 = ['не держать']
    text = '''Вы продолжаете держать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    tts = '''Вы продолжаете держать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    text_reject = '''"Вы пытаетесь убрать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    tts_reject = '''"Вы пытаетесь убрать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    new_save = {'accept': 'chap2_19', 'reject': 'chap2_19'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_19(req_save, command, intent, user_id):
    COMMANDS_1 = ['спросить']
    COMMANDS_2 = ['не спрашивать']
    text = alice_dict['2_chap_19']['text']
    tts = alice_dict['2_chap_19']['tts']
    text_reject = alice_dict['2_chap_19']['text']
    tts_reject = alice_dict['2_chap_19']['tts']
    new_save = {'accept': 'chap2_20', 'reject': 'chap2_20'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_20(req_save, command, intent, user_id):
    COMMANDS_1 = ['начать обучение магией']
    COMMANDS_2 = ['не начинать обучение магией']
    text = '''"Потрясающе, что ты остался жив! Тебе еще рано знать, что там. Начнем обучение Магии!".'''
    tts = '''"Потрясающе, что ты остался жив! Тебе еще рано знать, что там. Начнем обучение Магии!".'''
    text_reject = '''"Начнем обучение магии?".'''
    tts_reject = '''"Начнем обучение магии?".'''
    new_save = {'accept': 'chap2_21', 'reject': 'chap2_21'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_21(req_save, command, intent, user_id):
    text = '''"Отказы не принимаются!"
"Открытие магического потенциала требует осознанности и сосредоточенности. Важно научиться контролировать свои мысли и эмоции, чтобы не допустить их разрушительного влияния на магические практики.

 Вдохи играют важную роль в открытии магического потенциала, так как они помогают контролировать энергию в теле. Начни с глубокого дыхания, вдыхая и выдыхая медленно и равномерно. Сосредоточься на своем дыхании, постепенно осознавая свое тело.

 Глаза являются важным инструментом при открытии магического потенциала. Закрой глаза и представь себе живую картину, используя свою воображение. Визуализируй, как магическая энергия проникает в твои руки и тело. Руками ты можешь контролировать магическую энергию. Сосредоточься на своих руках, представив их как инструмент для магической работы. Попробуй выполнить медитативные движения, используя свои руки, чтобы улучшить свою концентрацию и контроль над энергией."

"Повтори за мной: глубоко вдохни, закрой глаза и представь, как магическая энергия проникает в твои руки и тело, выдыхай. Сделай вдох и сосредоточься на своих руках, представив их как инструмент для магической работы, выдыхай."'''
    tts = '''"Отказы не принимаются!"
"Открытие магического потенциала требует осознанности и сосредоточенности. Важно научиться контролировать свои мысли и эмоции, чтобы не допустить их разрушительного влияния на магические практики.

 Вдохи играют важную роль в открытии магического потенциала, так как они помогают контролировать энергию в теле. Начни с глубокого дыхания, вдыхая и выдыхая медленно и равномерно. Сосредоточься на своем дыхании, постепенно осознавая свое тело.

 Глаза являются важным инструментом при открытии магического потенциала. Закрой глаза и представь себе живую картину, используя свою воображение. Визуализируй, как магическая энергия проникает в твои руки и тело. Руками ты можешь контролировать магическую энергию. Сосредоточься на своих руках, представив их как инструмент для магической работы. Попробуй выполнить медитативные движения, используя свои руки, чтобы улучшить свою концентрацию и контроль над энергией."

"Повтори за мной: глубоко вдохни, закрой глаза и представь, как магическая энергия проникает в твои руки и тело, выдыхай. Сделай вдох и сосредоточься на своих руках, представив их как инструмент для магической работы, выдыхай."'''
    req_save['save'] = 'chap2_22'
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_22(req_save, command, intent, user_id):
    text = ''' После часа повторения упражнений. "На сегодня хватит. Не переусердствуй с упражнениями, они могут негативно повлиять на тебя!".

Поздравляем, с прохождением пролога! Открыта новая команда "Меню", тут ты сможешь посмотреть свои квесты и открытые способности и многое другое! Для продолжения скажи "Меню".'''
    tts = '''После часа повторения упражнений. "На сегодня хватит. Не переусердствуй с упражнениями, они могут негативно повлиять на тебя!".

Поздравляем, с прохождением пролога! Открыта новая команда "Меню", тут ты сможешь посмотреть свои квесты и открытые способности и многое другое! Для продолжения скажи "Меню".'''
    req_save['save'] = 'chap2_23'
    return message_sent(text=text, tts=tts, version=version, save=req_save)

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


def chap2_3x(req_save, command, intent, user_id):
    COMMANDS_1 = ['влево']
    COMMANDS_2 = ['вперед']
    COMMANDS_3 = ['вправо']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_1x']['text']
        tts = alice_dict['2_chap_3_1x']['tts']
        req_save['save'] = 'chap2_3_1_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_2x']['text']
        tts = alice_dict['2_chap_3_2x']['tts']
        req_save['save'] = 'chap2_3_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_3:
        text = alice_dict['2_chap_3_3x']['text']
        tts = alice_dict['2_chap_3_3x']['tts']
        req_save['save'] = 'chap2_3_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_1_x(req_save, command, intent, user_id):
    COMMANDS_1 = ['идти']
    COMMANDS_2 = ['осмотреться']
    if command in COMMANDS_1:
        text = alice_dict['2_chap_3_1_1x']['text']
        tts = alice_dict['2_chap_3_1_1x']['tts']
        req_save['save'] = 'chap2'  # вернуть на последнее сохранение
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif command in COMMANDS_2:
        text = alice_dict['2_chap_3_1_2x']['text']
        tts = alice_dict['2_chap_3_1_2x']['tts']
        req_save['save'] = 'chap2'  # вернуть на последнее сохранение
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)

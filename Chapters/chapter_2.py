from dialogs import message_sent, d_start_0, message_sent_with_card
from help_dialogs import message_help, confirm_reject_handler, confirm_reject_handler_with_card
from config import *
from Replicas.alice_says import alice_dict
import random

def chap2(req_save, command, intent, user_id):
    req_save['save'] = 'chap2_1_x'
    text = alice_dict['2_chap']['text']
    tts = alice_dict['2_chap']['tts']
    return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_1_x(req_save, command, intent, user_id):
    text = alice_dict['2_chap_1_x']['text']
    tts = alice_dict['2_chap_1_x']['tts']
    text_reject = alice_dict['2_chap_1_1x']['text']
    tts_reject = alice_dict['2_chap_1_1x']['tts']
    new_save = {'accept': 'chap2_2', 'reject': 'chap2_2'}
    return confirm_reject_handler(req_save, "chap2_1_x.STOP", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_1_x.NOT_STOP")


def chap2_2(req_save, command, intent, user_id): # СПИСОК
    if "chap2_2" in intent:
        text = alice_dict['2_chap_2']['text']
        tts = alice_dict['2_chap_2']['tts']
        req_save['save'] = 'chap2_3_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_x(req_save, command, intent, user_id):
    if "chap2_3_x.LEFT" in intent:
        text = alice_dict['2_chap_3_1x']['text']
        tts = alice_dict['2_chap_3_1x']['tts']
        req_save['save'] = 'chap2_3_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_x.CENTER" in intent:
        text = alice_dict['2_chap_3_2x']['text']
        tts = alice_dict['2_chap_3_2x']['tts']
        req_save['save'] = 'chap2_3_2x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_x.RIGHT" in intent:
        text = alice_dict['2_chap_3_3x']['text']
        tts = alice_dict['2_chap_3_3x']['tts']
        req_save['save'] = 'chap2_3_3x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_1x(req_save, command, intent, user_id):
    if "chap2_3_1x.GO" in intent:
        text = alice_dict['2_chap_3_1_1x']['text']
        tts = alice_dict['2_chap_3_1_1x']['tts']
        req_save['save'] = 'chap_2_3_1_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_1x.LOOK_AROUND" in intent:
        text = alice_dict['2_chap_3_1_2x']['text']
        tts = alice_dict['2_chap_3_1_2x']['tts']
        req_save['save'] = 'chap2_3_1_2x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3x(req_save, command, intent, user_id):
    if "chap2_3_3x.SHARPLY" in intent:
        text = alice_dict['2_chap_3_3_1x']['text']
        tts = alice_dict['2_chap_3_3_1x']['tts']
        req_save['save'] = 'chap2_3_3_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_3x.SLOWLY" in intent:
        text = alice_dict['2_chap_3_3x']['text']
        tts = alice_dict['2_chap_3_3x']['tts']
        req_save['save'] = 'chap2_3_3_1'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_1(req_save, command, intent, user_id):
    if "chap2_3_3_1" in intent:
        text = alice_dict['2_chap_3_3_1']['text']
        tts = alice_dict['2_chap_3_3_1']['tts']
        req_save['save'] = 'chap2_3_3_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2(req_save, command, intent, user_id):
    text = alice_dict['2_chap_3_3_2']['text']
    tts = alice_dict['2_chap_3_3_2']['tts']
    new_save = {'accept': 'chap2_3_3_2_x', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_3_3_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_3_2_x(req_save, command, intent, user_id):
    if "chap2_3_3_2_x.JUMP" in intent:
        text = alice_dict['2_chap_3_3_2_1x']['text']
        tts = alice_dict['2_chap_3_3_2_1x']['tts']
        req_save['save'] = 'chap2_3_3_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_3_2_x.BRIDGE" in intent:
        text = alice_dict['2_chap_3_3_2_x']['text']
        tts = alice_dict['2_chap_3_3_2_x']['tts']
        req_save['save'] = 'chap2_3_3_2_1'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_1(req_save, command, intent, user_id):
    if "chap2_3_3_2_1" in intent: ####################################################### СПИСОК
        text = alice_dict['2_chap_3_3_2_1']['text']
        tts = alice_dict['2_chap_3_3_2_1']['tts']
        req_save['save'] = 'chap2_3_3_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_2(req_save, command, intent, user_id):
    if "chap2_3_3_2_2" in intent:
        text = alice_dict['2_chap_3_3_2_2']['text']
        tts = alice_dict['2_chap_3_3_2_2']['tts']
        req_save['save'] = 'chap2_3_3_2_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_3_2_2_x(req_save, command, intent, user_id):
    text = alice_dict['2_chap_3_3_2_2_x']['text']
    tts = alice_dict['2_chap_3_3_2_2_x']['tts']
    text_reject = alice_dict['2_chap_3_3_2_2_1x']['text']
    tts_reject = alice_dict['2_chap_3_3_2_2_1x']['tts']
    new_save = {'accept': 'chap2_3_0', 'reject': 'chap2_3_3_2_2_1x'}
    return confirm_reject_handler(req_save, "chap2_3_3_2_2_x.GO", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_3_3_2_2_x.NOT_GO")


def chap2_3_2x(req_save, command, intent, user_id):
    if "chap2_3_2x.FIGHT" in intent:
        text = alice_dict['2_chap_3_2_1x']['text']
        tts = alice_dict['2_chap_3_2_1x']['tts']
        req_save['save'] = 'chap2_3_2_1_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2x.NOT_FIGHT" in intent:
        text = alice_dict['2_chap_3_2_x']['text']
        tts = alice_dict['2_chap_3_2_x']['tts']
        req_save['save'] = 'chap2_3_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_x(req_save, command, intent, user_id):
    if "chap2_3_2_1_x.INVENTORY" in intent: ######################################### СПИСОК
        text = alice_dict['2_chap_3_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_1_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_1_x.TAKE" in intent:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2(req_save, command, intent, user_id):
    if "chap2_3_2_1_2" in intent:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_x(req_save, command, intent, user_id):
    if "chap2_3_2_1_2_x.FEIGN" in intent:
        text = alice_dict['2_chap_3_2_1_2_x']['text']
        tts = alice_dict['2_chap_3_2_1_2_x']['tts']
        req_save['save'] = 'chap2_3_2_1_2_0x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_1_2_x.RESUME" in intent:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_0x(req_save, command, intent, user_id):
    if "chap2_3_2_1_2_0x.RESUME" in intent:
        text = alice_dict['2_chap_3_2_1_2_1']['text']
        tts = alice_dict['2_chap_3_2_1_2_1']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_1_2_0x.STAND_UP" in intent:
        text = alice_dict['2_chap_3_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_1_2']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_1_2_2(req_save, command, intent, user_id):
    text = alice_dict['2_chap_3_2_1_2_2']['text']
    tts = alice_dict['2_chap_3_2_1_2_2']['tts']
    new_save = {'accept': 'chap2_3_2_1_2_2_x', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_3_2_1_2_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_2_1_2_2_x(req_save, command, intent, user_id):
    if "chap2_3_2_1_2_2_x.SLEEP" in intent:
        text = alice_dict['2_chap_3_2_1_2_2_1x']['text']
        tts = alice_dict['2_chap_3_2_1_2_2_1x']['tts']
        req_save['save'] = 'chap2_3_2_1_2_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_1_2_2_x.RESUME" in intent:
        text = alice_dict['2_chap_3_2_1_2_2_x']['text']
        tts = alice_dict['2_chap_3_2_1_2_2_x']['tts']
        req_save['save'] = 'chap2_3_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2(req_save, command, intent, user_id):
    text = alice_dict['2_chap_3_2_2']['text']
    tts = alice_dict['2_chap_3_2_2']['tts']
    new_save = {'accept': 'chap2_3_2_2_2_0', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_3_2_2", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_3_2_2_2_0(req_save, command, intent, user_id):
    if "chap2_3_2_2_2_0.SLEEP" in intent:
        text = alice_dict['2_chap_3_2_2_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_2_2_0.FIND" in intent:
        text = alice_dict['2_chap_3_2_2_2']['text']
        tts = alice_dict['2_chap_3_2_2_2']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1x(req_save, command, intent, user_id):
    if "chap2_3_2_2_2_1x.SLEEP" in intent: #################################### СПИСОК
        text = alice_dict['2_chap_3_2_2_2_1_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_2_2_1x.EAT" in intent:
        text = alice_dict['2_chap_3_2_2_2_1']['text']
        tts = alice_dict['2_chap_3_2_2_2_1']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_x(req_save, command, intent, user_id):
    if "chap2_3_2_2_2_1_x.STAY" in intent:
        text = alice_dict['2_chap_3_2_2_2_1_x']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_x']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_3_2_2_2_1_x.JUMP" in intent:
        text = alice_dict['2_chap_3_2_2_2_1_1x']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_1x']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_end(req_save, command, intent, user_id):
    if "chap2_3_end" in intent:
        text = alice_dict['2_chap']['text']
        tts = alice_dict['2_chap']['tts']
        req_save['save'] = 'chap2_1x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_0(req_save, command, intent, user_id):
    if "chap2_3_end" in intent:
        text = alice_dict['2_chap_3_2_2_2_1_0']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_0']['tts']
        req_save['save'] = 'chap2_3_2_2_2_1_2'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_2_2_2_1_2(req_save, command, intent, user_id):
    if "chap2_3_2_2_2_1_2" in intent:
        text = alice_dict['2_chap_3_2_2_2_1_2']['text']
        tts = alice_dict['2_chap_3_2_2_2_1_2']['tts']
        req_save['save'] = 'chap2_3_0'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_3_0(req_save, command, intent, user_id):
    text = alice_dict['2_chap_3_0']['text']
    tts = alice_dict['2_chap_3_0']['tts']
    new_save = {'accept': 'chap2_4', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_3_0", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_4(req_save, command, intent, user_id):
    text = alice_dict['2_chap_4']['text']
    tts = alice_dict['2_chap_4']['tts']
    new_save = {'accept': 'chap2_5', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_4", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_5(req_save, command, intent, user_id):
    text = alice_dict['2_chap_5']['text']
    tts = alice_dict['2_chap_5']['tts']

    req_save["inventory"]['armor']["helmet"]["broken"]["activity"] = True
    req_save["inventory"]['armor']["chest"]["broken"]["activity"] = True
    req_save["inventory"]['armor']["shorts"]["broken"]["activity"] = True
    req_save["inventory"]['armor']["boots"]["broken"]["activity"] = True
    req_save["inventory"]['weapon']['sword']["broken"]["activity"] = True

    new_save = {'accept': 'chap2_6', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_5", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_6(req_save, command, intent, user_id):################################### СПИСОК
    text = alice_dict['2_chap_6']['text']
    tts = alice_dict['2_chap_6']['tts']
    new_save = {'accept': 'chap2_7', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_6", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)

def chap2_7(req_save, command, intent, user_id):
    gear_dict = {  # ПРОВЕРИТЬ
        'Потрепанный шлем': ('helmet',),
        'Потрепанный нагрудник': ('chest',),
        'Потрепанныe ботинки': ('boots',),
        'Потрепанныe поножи': ('shorts',),
        'Потрескавшийся меч': ('sword',),
    }
    all_items_boolean = False
    for gear, keys in gear_dict.items():
        if gear in command:
            if keys[0] == 'sword':
                req_save["inventory"]['weapon'][keys[0]]["broken"]["is_gear"] = True
                break
            else:
                req_save["inventory"]['armor'][keys[0]]["broken"]["is_gear"] = True
                break
        if req_save["inventory"]['armor'][keys[0]]["broken"]["is_gear"]:
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
    text = alice_dict['2_chap_7_2']['text']
    tts = alice_dict['2_chap_7_2']['tts']
    text_reject = alice_dict['2_chap_7_1']['text']
    tts_reject = alice_dict['2_chap_7_1']['tts']
    new_save = {'accept': 'chap2_7_2_fight', 'reject': 'chap2_7_1'}
    return confirm_reject_handler(req_save, "chap2_7_x.YES", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_7_x.NO")


def chap2_7_1(req_save, command, intent, user_id):
    text = alice_dict['2_chap_7_2']['text']
    tts = alice_dict['2_chap_7_2']['tts']
    new_save = {'accept': 'chap2_7_2_fight', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_7_1", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_7_2_fight(req_save, command, intent, user_id):
    if "chap2_7_2_fight.STRONG" in intent:
        if req_save['stamina'] < 30:
            text = 'Вы слишком устали, чтобы восстановить свою выносливость. Скажите: "Отдохнуть".'
            tts = 'Вы слишком устали, чтобы восстановить свою выносливость. Скажите: "Отдохнуть".'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            if random.random() < 0.5:
                text = 'Вы замахиваетесь мечем, но разбойник успевает увернуться. В ответ '
                tts = 'Вы замахиваетесь мечем, но разбойник успевает увернуться. В ответ '
                if random.random() < 0.5:
                    text += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.\n'
                    tts += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.'
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                else:
                    text += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.\n'
                    tts += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.'
                    req_save['health'] -= 4
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = 'Сделав замах мечом, вы нанесли удар с такой силой, что блок разбойника не выдержал и его наплечник был разрушен. В ответ '
                tts = 'Сделав замах мечом, вы нанесли удар с такой силой, что блок разбойника не выдержал и его наплечник был разрушен. В ответ '
                if random.random() < 0.5:
                    text += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.\n'
                    tts += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.'
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                else:
                    text += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.\n'
                    tts += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.'
                    req_save['health'] -= 4
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_7_2_fight.WEAK" in intent:
        if req_save['stamina'] < 15:
            text = 'Вы слишком устали, чтобы восстановить свою выносливость. Скажите: "Отдохнуть".'
            tts = 'Вы слишком устали, чтобы восстановить свою выносливость. Скажите: "Отдохнуть".'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            if random.random() < 0.5:
                text = 'Вы быстро поднимаете меч над головой, затем резко опускаете вниз, стараясь нанести удар по противнику, но тот уворачивается. В ответ '
                tts = 'Вы быстро поднимаете меч над головой, затем резко опускаете вниз, стараясь нанести удар по противнику, но тот уворачивается. В ответ '
                if random.random() < 0.5:
                    text += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.\n'
                    tts += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.'
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                else:
                    text += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.\n'
                    tts += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.'
                    req_save['health'] -= 4
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
            else:
                text = 'Вы наносите удар мечом, не замахиваясь, настолько быстро, что разбойник не успевает увернуться и получает удар. В ответ '
                tts = 'Вы наносите удар мечом, не замахиваясь, настолько быстро, что разбойник не успевает увернуться и получает удар. В ответ '
                if random.random() < 0.5:
                    text += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.\n'
                    tts += 'Разбойник замахивается мечом и направляет его в вашу сторону. Однако, вы умело увернулись, и меч разбойника не пробивает вашу броню, оставляя вас невредимым.'
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                else:
                    text += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.\n'
                    tts += 'Разбойник быстро подбегает к вам, размахивая своим мечом. Он приближается так близко, что вы чувствуете его дыхание на своем лице, и внезапно он резко направляет свой меч прямо к вашей груди. Вы пытаетесь увернуться, но он умело перехватывает ваше движение и пробивает вашу броню.'
                    req_save['health'] -= 4
                    text += 'Ваше здоровье: ' + req_save['health'] + '\n' + 'Выносливость: ' + req_save['stamina']
                    tts += 'Ваше здоровье: ' + req_save['health'] + 'Выносливость: ' + req_save['stamina']
                if req_save['health'] <= 5:
                    text = alice_dict['2_chap_8']['text']
                    tts = alice_dict['2_chap_8']['tts']
                    req_save['save'] = 'chap2_9'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
                else:
                    req_save['save'] = 'chap2_7_2_fight'
                    return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_7_2_fight.RELAX" in intent:
        if req_save['stamina'] > 60:
            req_save['health'] -= 2
            req_save['stamina'] = 100
            req_save['save'] = 'chap2_7_2_fight'
            text = f'Разбойник воспользовался вашим бездействием и нанес удар. \n Ваше здоровье: {req_save["health"]} \nВыносливость: {req_save["stamina"]}'
            tts = f'Разбойник воспользовался вашим бездействием и нанес удар. Ваше здоровье: {req_save["health"]} Выносливость: {req_save["stamina"]}'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            req_save['health'] -= 2
            req_save['stamina'] += 40
            text = f'Разбойник воспользовался вашим бездействием и нанес удар. \n Ваше здоровье: {req_save["health"]} \nВыносливость: {req_save["stamina"]}'
            tts = f'Разбойник воспользовался вашим бездействием и нанес удар. Ваше здоровье: {req_save["health"]} Выносливость: {req_save["stamina"]}'
            req_save['save'] = 'chap2_7_2_fight'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help('2_chap_7_2', version)


def chap2_9(req_save, command, intent, user_id):
    text = alice_dict['2_chap_9']['text']
    tts = alice_dict['2_chap_9']['tts']
    new_save = {'accept': 'chap2_10', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_9", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_10(req_save, command, intent, user_id):
    text = alice_dict['2_chap_10']['text']
    tts = alice_dict['2_chap_10']['tts']
    new_save = {'accept': 'chap2_11', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_10", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_11(req_save, command, intent, user_id):
    text = alice_dict['2_chap_11']['text']
    tts = alice_dict['2_chap_11']['tts']
    new_save = {'accept': 'chap2_12', 'reject': ''}
    COLLECTION.update_one({"id": user_id}, {"$set": {"name": req_save['name'], "save": 'chap2_11', "health": req_save["health"], "power": req_save["power"], "other": req_save["other"]}})
    return confirm_reject_handler(req_save, "chap2_11", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_12(req_save, command, intent, user_id):
    text = alice_dict['2_chap_12']['text']
    tts = alice_dict['2_chap_12']['tts']
    new_save = {'accept': 'chap2_13_x', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_12", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_13_x(req_save, command, intent, user_id):
    if "chap2_13_x.BERRIES" in intent:
        text = alice_dict['2_chap_13_1']['text']
        tts = alice_dict['2_chap_13_1']['tts']
        req_save['save'] = 'chap2_14'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_13_x.FISH" in intent:
        text = alice_dict['2_chap_13_2']['text']
        tts = alice_dict['2_chap_13_2']['tts']
        req_save['save'] = 'chap2_13_2_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)


def chap2_13_2_x(req_save, command, intent, user_id):
    text = alice_dict['2_chap_13_2_1']['text']
    tts = alice_dict['2_chap_13_2_1']['tts']
    text_reject = alice_dict['2_chap_13_2_2']['text']
    tts_reject = alice_dict['2_chap_13_2_2']['tts']
    new_save = {'accept': 'chap2_14', 'reject': 'chap2_14'}
    return confirm_reject_handler(req_save, "chap2_13_2_x.FRY", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_13_2_x.NOT_FRY")


def chap2_14(req_save, command, intent, user_id):
    text = alice_dict['2_chap_14']['text']
    tts = alice_dict['2_chap_14']['tts']
    new_save = {'accept': 'chap2_15_x', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_14", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_15_x(req_save, command, intent, user_id):
    text = alice_dict['2_chap_15_x']['text']
    tts = alice_dict['2_chap_15_x']['tts']
    text_reject = alice_dict['2_chap_15_1x']['text']
    tts_reject = alice_dict['2_chap_15_1x']['tts']
    new_save = {'accept': 'chap2_14', 'reject': 'chap2_14'}
    return confirm_reject_handler(req_save, "chap2_15_x.TOUCH", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_15_x.NOT_TOUCH")


def chap2_15_x_x(req_save, command, intent, user_id):
    text = alice_dict['2_chap_15_x_x']['text']
    tts = alice_dict['2_chap_15_x_x']['tts']
    text_reject = alice_dict['2_chap_15_x_1x']['text']
    tts_reject = alice_dict['2_chap_15_x_1x']['tts']
    new_save = {'accept': 'chap2_16_x', 'reject': 'chap2_16_x'}
    return confirm_reject_handler(req_save, "chap2_15_x_x.BLOW", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_15_x_x.NOT_BLOW")

def chap2_16_x(req_save, command, intent, user_id):
    water = req_save['other']['runes']['water']
    fire = req_save['other']['runes']['fire']
    terra = req_save['other']['runes']['earth']
    if "chap2_16_x.WATER" in intent:
        if water:
            text = 'Вы уже зажгли эту руну! Для продолжения вы можете использовать руну "Земля" или "Огонь"'
            tts = 'Вы уже зажгли эту руну! Для продолжения вы можете использовать руну "Земля" или "Огонь"'
            req_save['save'] = 'chap2_16_x'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
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
    elif "chap2_16_x.FIRE" in intent:
        text = alice_dict['2_chap_16_3x']
        tts = alice_dict['2_chap_16_3x']
        req_save['save'] = 'chap2_16_3x_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_16_x.EARTH" in intent:
        if terra:
            text = 'Вы уже зажгли эту руну! Для продолжения вы можете использовать руну "Вода" или "Огонь"'
            tts = 'Вы уже зажгли эту руну! Для продолжения вы можете использовать руну "Вода" или "Огонь"'
            req_save['save'] = 'chap2_16_x'
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        elif water and fire:
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
            text = alice_dict['2_chap_16_1x']['text'] + 'Вторая руна зажжена! Использовать "Воду" или "Огонь".'
            tts = alice_dict['2_chap_16_1x']['tts'] + 'Вторая руна зажжена! Использовать "Воду" или "Огонь".'
            req_save['save'] = 'chap2_16_x'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        return message_help(req_save, version)


def chap2_16_3x_x(req_save, command, intent, user_id):
    if "chap2_16_3x_x.FIGHT" in intent:
        text = alice_dict['2_chap_16_3x_1x']['text']
        tts = alice_dict['2_chap_16_3x_1x']['tts']
        req_save['save'] = 'chap2_11'  # загрузка последнего сохранения
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_16_3x_x.RUN" in intent:
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
    text = alice_dict['2_chap_17']['text']
    tts = alice_dict['2_chap_17']['tts']
    new_save = {'accept': 'chap2_18_x', 'reject': ''}
    return confirm_reject_handler(req_save, "chap2_17", intent, text_commands=intent, text=text, tts=tts,
                                  new_save=new_save)


def chap2_18_x(req_save, command, intent, user_id):
    text = '''Вы продолжаете держать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    tts = '''Вы продолжаете держать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    text_reject = '''"Вы пытаетесь убрать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    tts_reject = '''"Вы пытаетесь убрать руку, но внезапно происходит взрыв, который отбрасывает вас в другую сторону. Вы ударяетесь головой и теряете сознание.
Очнуться?'''
    new_save = {'accept': 'chap2_19', 'reject': 'chap2_19'}
    return confirm_reject_handler(req_save, "chap2_18_x.KEEP", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_18_x.NOT_KEEP")


def chap2_19(req_save, command, intent, user_id):
    text = alice_dict['2_chap_19']['text']
    tts = alice_dict['2_chap_19']['tts']
    text_reject = alice_dict['2_chap_19']['text']
    tts_reject = alice_dict['2_chap_19']['tts']
    new_save = {'accept': 'chap2_20', 'reject': 'chap2_20'}
    return confirm_reject_handler(req_save, "chap2_19.ASK", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_19.NOT_ASK")


def chap2_20(req_save, command, intent, user_id):
    text = '''"Потрясающе, что ты остался жив! Тебе еще рано знать, что там. Начнем обучение Магии!".'''
    tts = '''<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/cd168ef2-ca1f-49c1-aaaf-8c55787df6ef.opus">.'''
    text_reject = '''"Начнем обучение магии?".'''
    tts_reject = '''<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/7ee34ab0-0f47-4167-bd3e-f6d97e98ea18.opus">.'''
    new_save = {'accept': 'chap2_21', 'reject': 'chap2_21'}
    return confirm_reject_handler(req_save, "chap2_20.START", intent, text_commands=intent, text=text, tts=tts,
                                  reject_enable=True, reject_commands=intent, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save, reject_command="chap2_20.NOT_START")


def chap2_21(req_save, command, intent, user_id):
    COMMANDS_1 = ['']
    COMMANDS_2 = ['']
    text_reject = '''Отказы не принимаются!
"Открытие магического потенциала требует осознанности и сосредоточенности. Важно научиться контролировать свои мысли и эмоции, чтобы не допустить их разрушительного влияния на магические практики.

 Вдохи играют важную роль в открытии магического потенциала, так как они помогают контролировать энергию в теле. Начни с глубокого дыхания, вдыхая и выдыхая медленно и равномерно. Сосредоточься на своем дыхании, постепенно осознавая свое тело.

 Глаза являются важным инструментом при открытии магического потенциала. Закрой глаза и представь себе живую картину, используя свою воображение. Визуализируй, как магическая энергия проникает в твои руки и тело. Руками ты можешь контролировать магическую энергию. Сосредоточься на своих руках, представив их как инструмент для магической работы. Попробуй выполнить медитативные движения, используя свои руки, чтобы улучшить свою концентрацию и контроль над энергией."

"Повтори за мной: глубоко вдохни, закрой глаза и представь, как магическая энергия проникает в твои руки и тело, выдыхай. Сделай вдох и сосредоточься на своих руках, представив их как инструмент для магической работы, выдыхай."'''
    tts_reject = '''Отказы не принимаются!
<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/487f07a5-5773-47a9-bb27-137b7d56c715.opus">

 <speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/76470862-ebd8-4aa6-9cae-c37bcdc95612.opus">

<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/4ed27bbe-aea0-4654-9710-6e92c518e610.opus">'''

    text = '''
"Открытие магического потенциала требует осознанности и сосредоточенности. Важно научиться контролировать свои мысли и эмоции, чтобы не допустить их разрушительного влияния на магические практики.

Вдохи играют важную роль в открытии магического потенциала, так как они помогают контролировать энергию в теле. Начни с глубокого дыхания, вдыхая и выдыхая медленно и равномерно. Сосредоточься на своем дыхании, постепенно осознавая свое тело.

Глаза являются важным инструментом при открытии магического потенциала. Закрой глаза и представь себе живую картину, используя свою воображение. Визуализируй, как магическая энергия проникает в твои руки и тело. Руками ты можешь контролировать магическую энергию. Сосредоточься на своих руках, представив их как инструмент для магической работы. Попробуй выполнить медитативные движения, используя свои руки, чтобы улучшить свою концентрацию и контроль над энергией."

"Повтори за мной: глубоко вдохни, закрой глаза и представь, как магическая энергия проникает в твои руки и тело, выдыхай. Сделай вдох и сосредоточься на своих руках, представив их как инструмент для магической работы, выдыхай."'''
    tts = '''
<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/487f07a5-5773-47a9-bb27-137b7d56c715.opus">

 <speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/76470862-ebd8-4aa6-9cae-c37bcdc95612.opus">

<speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/4ed27bbe-aea0-4654-9710-6e92c518e610.opus">'''
    new_save = {'accept': 'chap2_22', 'reject': 'chap2_22'}
    return confirm_reject_handler(req_save, command, intent, text_commands=COMMANDS_1, text=text, tts=tts,
                                  reject_enable=True, reject_commands=COMMANDS_2, text_reject=text_reject,
                                  tts_reject=tts_reject, new_save=new_save)


def chap2_22(req_save, command, intent, user_id):
    text = ''' После часа повторения упражнений. "На сегодня хватит. Не переусердствуй с упражнениями, они могут негативно повлиять на тебя!".

Поздравляем, с прохождением пролога! Открыта новая команда "Меню", тут ты сможешь посмотреть свои квесты и открытые способности и многое другое! Для продолжения скажи "Меню".'''
    tts = '''После часа повторения упражнений. <speaker audio="dialogs-upload/b2735f27-2dcf-4c5a-ad8c-a08d78959ad0/3f36d6ec-4ab0-4e29-8b36-7195feb8916f.opus">.

Поздравляем, с прохождением пролога! Открыта новая команда "Меню", тут ты сможешь посмотреть свои квесты и открытые способности и многое другое! Для продолжения скажи "Меню".'''
    req_save['save'] = 'chap2_23'
    return message_sent(text=text, tts=tts, version=version, save=req_save)

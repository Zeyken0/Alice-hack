from dialogs import message_sent
from help_dialogs import message_help, confirm_reject_handler
from Replicas.alice_says import alice_dict

version = "1.0"


def chap2(req_save, command, intent, user_id):
    req_save['save'] = 'chap2_1_x'
    req_save['chapter'] = 'chapter_2'
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

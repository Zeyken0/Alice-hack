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
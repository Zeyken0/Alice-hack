from dialogs import message_sent, message_sent_with_card
import random

version = "1.0"

def inf(req_save, command, intent, user_id):
    req_save['save'] = 'inf_2'
    req_save['chapter'] = 'inf'
    text = '''Вы оказались перед входом в загадочный Клуб Сражений - место, где опытные бойцы и легендарные герои сражаются друг с другом, чтобы определить, кто из них достоин звания настоящего чемпиона. Здесь царит атмосфера схваток и волнения, и каждый, кто сюда приходит, должен быть готов к трудным испытаниям. Зайти?'''
    tts = '''Вы оказались перед входом в загадочный Клуб Сражений - место, где опытные бойцы и легендарные герои сражаются друг с другом, чтобы определить, кто из них достоин звания настоящего чемпиона. Здесь царит атмосфера схваток и волнения, и каждый, кто сюда приходит, должен быть готов к трудным испытаниям. Зайти?'''
    return message_sent(text=text, tts=tts, version=version, save=req_save)

def inf_2(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "inf_2" in intent:
        req_save['save'] = 'inf_3'
        if req_save['other']['infinity']['first']:
            text = 'После каждой победы вы получаете опыт.  Чтобы посмотреть ваш опыт скажите "Топ Игроков".'
            tts = 'После каждой победы вы получаете опыт. Чтобы посмотреть ваш опыт скажите "Топ Игроков". Ваши атаки: Удар сверху. урон три. выносливость двадцать. Легкая Атака. урон от одного до двух. выносливость 15. Тяжелая атака. урон от двух до четырех. выносливость 40. быстрый удар. урон 1. выносливость 10. Круговой удар. урон 5. выносливость 60'
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1540737/2752af94dc956ad540c7",
                        "title": "Легкая Атака",
                        "description": "Урон: 1-2\nВыносливость: 15",
                    },
                    {
                        "image_id": "1652229/446276eb50bb7e683075",
                        "title": "Тяжелая Атака",
                        "description": "Урон: 2-4\nВыносливость: 40",
                    },
                    {
                        "image_id": "937455/50c7f2b7c87ef40aed2e",
                        "title": "Удар Сверху",
                        "description": "Урон: 3\nВыносливость: 20",
                    },
                    {
                        "image_id": "213044/60b09c9d0c3b65543222",
                        "title": "Быстрый удар",
                        "description": "Урон: 1\nВыносливость: 10",
                    },
                    {
                        "image_id": "213044/b3924e221e84e06b6f93",
                        "title": "Круговой удар",
                        "description": "Урон: 5\nВыносливость: 60",
                    },
                ],
                "footer": {
                    "text": "Начать битву?",
                }
            }
            req_save['other']['infinity']['first'] = False
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
        else:
            text = '''Добро пожаловать. Начать битву?'''
            tts = '''Добро пожаловать. Начать битву?'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.REJECT" in intent:
        text = '''Вы вернулись в убежище'''
        tts = '''Вы вернулись в убежище'''
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        text = '''Вы оказались перед входом в загадочный Клуб Сражений. Для продолжения скажите зайти'''
        tts = '''Вы оказались перед входом в загадочный Клуб Сражений. Для продолжения скажите зайти'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)

def inf_3(req_save, command, intent, user_id):
    if "YANDEX.CONFIRM" in intent or "inf_3" in intent:
        text = 'Ваши Атаки'
        tts = 'Ваши атаки: Удар сверху. урон три. выносливость двадцать. Легкая Атака. урон от одного до двух. выносливость 15. Тяжелая атака. урон от двух до четырех. выносливость 40. быстрый удар. урон 1. выносливость 10. Круговой удар. урон 5. выносливость 60'
        card = {
            "type": "ItemsList",
            "header": {
                "text": text,
            },
            "items": [
                {
                    "image_id": "1540737/2752af94dc956ad540c7",
                    "title": "Легкая Атака",
                    "description": "Урон: 1-2\nВыносливость: 15",
                },
                {
                    "image_id": "1652229/446276eb50bb7e683075",
                    "title": "Тяжелая Атака",
                    "description": "Урон: 2-4\nВыносливость: 40",
                },
                {
                    "image_id": "937455/50c7f2b7c87ef40aed2e",
                    "title": "Удар Сверху",
                    "description": "Урон: 3\nВыносливость: 20",
                },
                {
                    "image_id": "213044/60b09c9d0c3b65543222",
                    "title": "Быстрый удар",
                    "description": "Урон: 1\nВыносливость: 10",
                },
                {
                    "image_id": "213044/b3924e221e84e06b6f93",
                    "title": "Круговой удар",
                    "description": "Урон: 5\nВыносливость: 60",
                },
            ],
            "footer": {
                "text": "Выберите атаку",
            }
        }
        req_save['health'] = 20
        req_save['stamina'] = 100
        req_save['save'] = 'inf_fight'
        names = ['Игорь', 'Николай', 'Владимир', 'Святослав', 'Дмитрий', 'Рагнар', 'Элдрик', 'Терранс', 'Лир', 'Ниро', 'Никита']
        random_name = random.choice(names)
        random_health = random.randint(10, 36)
        req_save['other']['enemy']['name'] = random_name
        req_save['other']['enemy']['health'] = random_health
        return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
    elif "YANDEX.REJECT" in intent:
        text = '''Вы вернулись в убежище'''
        tts = '''Вы вернулись в убежище'''
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        text = '''Для продолжения скажите: "Начать битву"'''
        tts = '''Для продолжения скажите: "Начать битву"'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)

def inf_fight(req_save, command, intent, user_id):
    if "chap2_7_2_fight.STRONG" in intent:
        if req_save['stamina'] > 39:
            req_save['stamina'] -= 40
            damage = random.randint(2, 5)
            text = f'''Вы нанесли {damage} урона. '''
            tts = f'''Вы нанесли {damage} урона. '''
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                score = random.randint(10, 26)
                req_save['score'] += score
                text += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                tts += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                req_save['save'] = 'inf_fight_end'
            attack = ['Темная метка', 'Смерть с небес', 'Огненный шар', 'Ледяная стрела', 'Электрический разряд', 'Щит',
                      'Рассечение', 'Выстрел в голову', 'Мощный удар', 'Танец теней', 'Кровавый вихрь', 'Разрыв',
                      'Исцеляющее прикосновение', 'Огненная ловушка', 'Удар щитом']
            random_attack = random.choice(attack)
            if random_attack == "Темная метка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус 2 урона'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус два урона'''
            elif random_attack == "Смерть с небес":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит 4 урона'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит четыре урона'''
            elif random_attack == "Огненный шар":
                enemy_damage = random.randint(4, 7)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
            elif random_attack == "Ледяная стрела":
                enemy_damage = random.randint(3, 6)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
            elif random_attack == "Электрический разряд":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
            elif random_attack == "Щит":
                req_save['other']['enemy']['health'] += damage
                text += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
                tts += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
            elif random_attack == "Рассечение":
                enemy_damage = 3
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
            elif random_attack == "Выстрел в голову":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
                tts += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
            elif random_attack == "Мощный удар":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
                tts += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
            elif random_attack == "Танец теней":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
                tts += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
            elif random_attack == "Кровавый вихрь":
                enemy_damage = random.randint(3, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
                tts += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
            elif random_attack == "Разрыв":
                enemy_damage = 6
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
            elif random_attack == "Исцеляющее прикосновение":
                req_save['other']['enemy']['health'] += 3
                text += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
                tts += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
            elif random_attack == "Огненная ловушка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
            elif random_attack == "Удар щитом":
                enemy_damage = 1
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
            if req_save['health'] <= 0:
                text += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы.'''
                tts += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы'''
                req_save['health'] = 20
                req_save['save'] = "Home"
            elif req_save['health'] > 0:
                text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
                tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "FAST_ATTACK" in intent:
        if req_save['stamina'] > 9:
            req_save['stamina'] -= 10
            damage = 1
            text = f'''Вы нанесли {damage} урона. '''
            tts = f'''Вы нанесли {damage} урона. '''
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                score = random.randint(10, 26)
                req_save['score'] += score
                text += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                tts += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                req_save['save'] = 'inf_fight_end'
            attack = ['Темная метка', 'Смерть с небес', 'Огненный шар', 'Ледяная стрела', 'Электрический разряд', 'Щит',
                      'Рассечение', 'Выстрел в голову', 'Мощный удар', 'Танец теней', 'Кровавый вихрь', 'Разрыв',
                      'Исцеляющее прикосновение', 'Огненная ловушка', 'Удар щитом']
            random_attack = random.choice(attack)
            if random_attack == "Темная метка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус 2 урона'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус два урона'''
            elif random_attack == "Смерть с небес":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит 4 урона'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит четыре урона'''
            elif random_attack == "Огненный шар":
                enemy_damage = random.randint(4, 7)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
            elif random_attack == "Ледяная стрела":
                enemy_damage = random.randint(3, 6)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
            elif random_attack == "Электрический разряд":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
            elif random_attack == "Щит":
                req_save['other']['enemy']['health'] += damage
                text += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
                tts += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
            elif random_attack == "Рассечение":
                enemy_damage = 3
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
            elif random_attack == "Выстрел в голову":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
                tts += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
            elif random_attack == "Мощный удар":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
                tts += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
            elif random_attack == "Танец теней":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
                tts += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
            elif random_attack == "Кровавый вихрь":
                enemy_damage = random.randint(3, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
                tts += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
            elif random_attack == "Разрыв":
                enemy_damage = 6
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
            elif random_attack == "Исцеляющее прикосновение":
                req_save['other']['enemy']['health'] += 3
                text += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
                tts += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
            elif random_attack == "Огненная ловушка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
            elif random_attack == "Удар щитом":
                enemy_damage = 1
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
            if req_save['health'] <= 0:
                text += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы.'''
                tts += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы'''
                req_save['health'] = 20
                req_save['save'] = "Home"
            elif req_save['health'] > 0:
                text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
                tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "quest2_fight.EASY" in intent:
        if req_save['stamina'] > 14:
            req_save['stamina'] -= 15
            damage = random.randint(1, 3)
            text = f'''Вы нанесли {damage} урона. '''
            tts = f'''Вы нанесли {damage} урона. '''
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                score = random.randint(10, 26)
                req_save['score'] += score
                text += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                tts += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                req_save['save'] = 'inf_fight_end'
            attack = ['Темная метка', 'Смерть с небес', 'Огненный шар', 'Ледяная стрела', 'Электрический разряд', 'Щит',
                      'Рассечение', 'Выстрел в голову', 'Мощный удар', 'Танец теней', 'Кровавый вихрь', 'Разрыв',
                      'Исцеляющее прикосновение', 'Огненная ловушка', 'Удар щитом']
            random_attack = random.choice(attack)
            if random_attack == "Темная метка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус 2 урона'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус два урона'''
            elif random_attack == "Смерть с небес":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит 4 урона'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит четыре урона'''
            elif random_attack == "Огненный шар":
                enemy_damage = random.randint(4, 7)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
            elif random_attack == "Ледяная стрела":
                enemy_damage = random.randint(3, 6)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
            elif random_attack == "Электрический разряд":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
            elif random_attack == "Щит":
                req_save['other']['enemy']['health'] += damage
                text += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
                tts += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
            elif random_attack == "Рассечение":
                enemy_damage = 3
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
            elif random_attack == "Выстрел в голову":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
                tts += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
            elif random_attack == "Мощный удар":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
                tts += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
            elif random_attack == "Танец теней":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
                tts += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
            elif random_attack == "Кровавый вихрь":
                enemy_damage = random.randint(3, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
                tts += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
            elif random_attack == "Разрыв":
                enemy_damage = 6
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
            elif random_attack == "Исцеляющее прикосновение":
                req_save['other']['enemy']['health'] += 3
                text += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
                tts += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
            elif random_attack == "Огненная ловушка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
            elif random_attack == "Удар щитом":
                enemy_damage = 1
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
            if req_save['health'] <= 0:
                text += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы.'''
                tts += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы'''
                req_save['health'] = 20
                req_save['save'] = "Home"
            elif req_save['health'] > 0:
                text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
                tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "TOP_ATTACK" in intent:
        if req_save['stamina'] > 19:
            req_save['stamina'] -= 20
            damage = 3
            text = f'''Вы нанесли {damage} урона. '''
            tts = f'''Вы нанесли {damage} урона. '''
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                score = random.randint(10, 26)
                req_save['score'] += score
                text += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                tts += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                req_save['save'] = 'inf_fight_end'
            attack = ['Темная метка', 'Смерть с небес', 'Огненный шар', 'Ледяная стрела', 'Электрический разряд', 'Щит',
                      'Рассечение', 'Выстрел в голову', 'Мощный удар', 'Танец теней', 'Кровавый вихрь', 'Разрыв',
                      'Исцеляющее прикосновение', 'Огненная ловушка', 'Удар щитом']
            random_attack = random.choice(attack)
            if random_attack == "Темная метка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус 2 урона'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус два урона'''
            elif random_attack == "Смерть с небес":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит 4 урона'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит четыре урона'''
            elif random_attack == "Огненный шар":
                enemy_damage = random.randint(4, 7)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
            elif random_attack == "Ледяная стрела":
                enemy_damage = random.randint(3, 6)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
            elif random_attack == "Электрический разряд":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
            elif random_attack == "Щит":
                req_save['other']['enemy']['health'] += damage
                text += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
                tts += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
            elif random_attack == "Рассечение":
                enemy_damage = 3
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
            elif random_attack == "Выстрел в голову":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
                tts += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
            elif random_attack == "Мощный удар":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
                tts += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
            elif random_attack == "Танец теней":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
                tts += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
            elif random_attack == "Кровавый вихрь":
                enemy_damage = random.randint(3, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
                tts += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
            elif random_attack == "Разрыв":
                enemy_damage = 6
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
            elif random_attack == "Исцеляющее прикосновение":
                req_save['other']['enemy']['health'] += 3
                text += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
                tts += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
            elif random_attack == "Огненная ловушка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
            elif random_attack == "Удар щитом":
                enemy_damage = 1
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
            if req_save['health'] <= 0:
                text += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы.'''
                tts += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы'''
                req_save['health'] = 20
                req_save['save'] = "Home"
            elif req_save['health'] > 0:
                text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
                tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "CIRCLE_ATTACK" in intent:
        if req_save['stamina'] > 59:
            req_save['stamina'] -= 60
            damage = 5
            text = f'''Вы нанесли {damage} урона. '''
            tts = f'''Вы нанесли {damage} урона. '''
            req_save['other']['enemy']['health'] -= damage
            if req_save['other']['enemy']['health'] <= 0:
                score = random.randint(10, 26)
                req_save['score'] += score
                text += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                tts += f''' {req_save['other']['enemy']['name']} проиграл. Вы получили {score} опыта. Вернуться в убежище или продолжить драку?'''
                req_save['save'] = 'inf_fight_end'
            attack = ['Темная метка', 'Смерть с небес', 'Огненный шар', 'Ледяная стрела', 'Электрический разряд', 'Щит',
                      'Рассечение', 'Выстрел в голову', 'Мощный удар', 'Танец теней', 'Кровавый вихрь', 'Разрыв',
                      'Исцеляющее прикосновение', 'Огненная ловушка', 'Удар щитом']
            random_attack = random.choice(attack)
            if random_attack == "Темная метка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус 2 урона'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} наносит вам рану, проникая в ваше тело темной энергией, минус два урона'''
            elif random_attack == "Смерть с небес":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит 4 урона'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Смерть с небес", вызывая молнию, которая бьет по вам и наносит четыре урона'''
            elif random_attack == "Огненный шар":
                enemy_damage = random.randint(2, 5)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Ignis Orbis!", формирует яркий шар из чистого огня и бросает его в вас, нанося значительный урон'''
            elif random_attack == "Ледяная стрела":
                enemy_damage = random.randint(2, 4)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
                tts += f'''{req_save['other']['enemy']['name']} произносит заклинание "Glacius Sagitta!",создавая острые стрелы из льда и запускает их в вас, нанося урон и замораживая вас на какое-то время.'''
            elif random_attack == "Электрический разряд":
                enemy_damage = random.randint(2, 4)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} вызывает мощный электрический разряд, поражающий всех врагов в зоне поражения, нанося урон и оглушая их на короткое время'''
            elif random_attack == "Щит":
                req_save['other']['enemy']['health'] += damage
                text += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
                tts += f'''Но {req_save['other']['enemy']['name']} создает прозрачный щит, который поглощающий весь урон'''
            elif random_attack == "Рассечение":
                enemy_damage = 3
                req_save['health'] -= enemy_damage
                text += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
                tts += f'''В ответ {req_save['other']['enemy']['name']} метко рассекает мечом броню, оставляя на вашем теле рану'''
            elif random_attack == "Выстрел в голову":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
                tts += f'''{req_save['other']['enemy']['name']} метко стреляет вам в шлем, нанося критический урон'''
            elif random_attack == "Мощный удар":
                enemy_damage = 4
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
                tts += f'''{req_save['other']['enemy']['name']} наносит мощный удар мечом, нанося большой урон, но расходуя большую часть своей энергии'''
            elif random_attack == "Танец теней":
                enemy_damage = random.randint(2, 4)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
                tts += f'''{req_save['other']['enemy']['name']} быстро двигается вокруг вас, нанося серию ударов мечом, которые почти невозможно блокировать'''
            elif random_attack == "Кровавый вихрь":
                enemy_damage = random.randint(2, 4)
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
                tts += f'''{req_save['other']['enemy']['name']} быстро крутит мечом, создавая вихрь из крови и металла, который наносит большой урон'''
            elif random_attack == "Разрыв":
                enemy_damage = 6
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает магическую волну, наносящую 6 урона'''
            elif random_attack == "Исцеляющее прикосновение":
                req_save['other']['enemy']['health'] += 3
                text += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
                tts += f'''Но {req_save['other']['enemy']['name']} направляет магическую энергию к своим ранам, и они быстро затягиваются. Восстанавливает 3 здоровья'''
            elif random_attack == "Огненная ловушка":
                enemy_damage = 2
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
                tts += f'''{req_save['other']['enemy']['name']} создает огненный круг вокруг вас, нанося 5 урона'''
            elif random_attack == "Удар щитом":
                enemy_damage = 1
                req_save['health'] -= enemy_damage
                text += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
                tts += f'''{req_save['other']['enemy']['name']} бьет вас щитом, нанося небольшой урон и оглушая вас на короткое время'''
            if req_save['health'] <= 0:
                text += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы.'''
                tts += '''. Этот удар оказался решающим, и вы потерпели поражение. Вам пришлось вернуться в убежище, чтобы восстановить свои силы'''
                req_save['health'] = 20
                req_save['save'] = "Home"
            elif req_save['health'] > 0:
                text += f'''\nВаше здоровье: {req_save['health']}\nВаша Выносливость: {req_save['stamina']}\n \nЗдоровье противника: {req_save['other']['enemy']['health']}'''
                tts += f''' Ваше здоровье: {req_save['health']} Ваша Выносливость: {req_save['stamina']} Здоровье противника: {req_save['other']['enemy']['health']}'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        else:
            text = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            tts = '''У вас недостаточно выносливости. Чтобы ее пополнить скажите "Отдохнуть"'''
            return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "chap2_7_2_fight.RELAX" in intent:
        stamina = random.randint(30, 46)
        damage = random.randint(1, 4)
        req_save['stamina'] = min(100, req_save['stamina'] + stamina)
        req_save['health'] -= damage
        if req_save['health'] <= 0:
            text = f'''Во время вашего отдыха противник нанес вам {damage} урона, что привело к вашему поражению. Вы вернулись в убежище, чтобы восстановить силы.'''
            tts = f'''Во время вашего отдыха противник нанес вам {damage} урона, что привело к вашему поражению. Вы вернулись в убежище, чтобы восстановить силы.'''
            req_save['health'] = 20
            req_save['save'] = "Home"
            return message_sent(text=text, tts=tts, version=version, save=req_save)
        text = f'''Вы восстановили {stamina} очков. Но противник зря времени не терял и нанес {damage} урона'''
        tts = f'''Вы восстановили {stamina} очков. Но противник зря времени не терял и нанес {damage} урона'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    else:
        text = 'Ваши Атаки'
        tts = 'Ваши атаки: Удар сверху. урон три. выносливость двадцать. Легкая Атака. урон от одного до двух. выносливость 15. Тяжелая атака. урон от двух до четырех. выносливость 40. быстрый удар. урон 1. выносливость 10. Круговой удар. урон 5. выносливость 60. Для продолжения выберите атаку!'
        card = {
            "type": "ItemsList",
            "header": {
                "text": text,
            },
            "items": [
                {
                    "image_id": "1540737/2752af94dc956ad540c7",
                    "title": "Легкая Атака",
                    "description": "Урон: 1-2\nВыносливость: 15",
                },
                {
                    "image_id": "1652229/446276eb50bb7e683075",
                    "title": "Тяжелая Атака",
                    "description": "Урон: 2-4\nВыносливость: 40",
                },
                {
                    "image_id": "937455/50c7f2b7c87ef40aed2e",
                    "title": "Удар Сверху",
                    "description": "Урон: 3\nВыносливость: 20",
                },
                {
                    "image_id": "213044/60b09c9d0c3b65543222",
                    "title": "Быстрый удар",
                    "description": "Урон: 1\nВыносливость: 10",
                },
                {
                    "image_id": "213044/b3924e221e84e06b6f93",
                    "title": "Круговой удар",
                    "description": "Урон: 5\nВыносливость: 60",
                },
            ],
            "footer": {
                "text": "Для продолжения выберите атаку!",
            }
        }
        return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)

def inf_fight_end(req_save, command, intent, user_id):
    if "HOME" in intent:
        text = '''Вы вернулись в убежище. Не забудьте сохраниться, сказав "Сохранить игру"'''
        tts = '''Вы вернулись в убежище. Не забудьте сохраниться, сказав "Сохранить игру"'''
        req_save['health'] = 20
        req_save['stamina'] = 100
        req_save['save'] = 'Home'
        return message_sent(text=text, tts=tts, version=version, save=req_save)
    elif "YANDEX.BOOK.CONTINUE" in intent:
        if req_save['other']['enemy']['health'] <= 0:
            text = 'Ваши Атаки'
            tts = 'Ваши атаки: Удар сверху. урон три. выносливость двадцать. Легкая Атака. урон от одного до двух. выносливость 15. Тяжелая атака. урон от двух до четырех. выносливость 40. быстрый удар. урон 1. выносливость 10. Круговой удар. урон 5. выносливость 60. Выберите Атаку'
            card = {
                "type": "ItemsList",
                "header": {
                    "text": text,
                },
                "items": [
                    {
                        "image_id": "1540737/2752af94dc956ad540c7",
                        "title": "Легкая Атака",
                        "description": "Урон: 1-2\nВыносливость: 15",
                    },
                    {
                        "image_id": "1652229/446276eb50bb7e683075",
                        "title": "Тяжелая Атака",
                        "description": "Урон: 2-4\nВыносливость: 40",
                    },
                    {
                        "image_id": "937455/50c7f2b7c87ef40aed2e",
                        "title": "Удар Сверху",
                        "description": "Урон: 3\nВыносливость: 20",
                    },
                    {
                        "image_id": "213044/60b09c9d0c3b65543222",
                        "title": "Быстрый удар",
                        "description": "Урон: 1\nВыносливость: 10",
                    },
                    {
                        "image_id": "213044/b3924e221e84e06b6f93",
                        "title": "Круговой удар",
                        "description": "Урон: 5\nВыносливость: 60",
                    },
                ],
                "footer": {
                    "text": "Выберите атаку",
                }
            }
            req_save['health'] = 20
            req_save['stamina'] = 100
            req_save['save'] = 'inf_fight'
            Names = ['Игорь', 'Николай', 'Владимир', 'Святослав', 'Дмитрий', 'Рагнар', 'Элдрик', 'Терранс', 'Лир','Ниро']
            random_name = random.choice(Names)
            random_health = random.randint(10, 36)
            req_save['other']['enemy']['name'] = random_name
            req_save['other']['enemy']['health'] = random_health
            return message_sent_with_card(text=text, tts=tts, save=req_save, version=version, card=card)
    else:
        text = '''Вы победили! Для продолжения вы можете вернуться в убежище, сказав "Вернуться в убежище" или продолжить, сказав "Продолжить"'''
        tts = '''Вы победили! Для продолжения вы можете вернуться в убежище, сказав "Вернуться в убежище" или продолжить, сказав "Продолжить"'''
        return message_sent(text=text, tts=tts, version=version, save=req_save)
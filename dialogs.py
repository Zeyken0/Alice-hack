def d_start_0(text, tts, version):
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": False,
            "buttons": [
                {
                    "title": 'Да',
                    "hide": True,
                },
                {
                    "title": 'Помощь',
                    "hide": True
                },
                {
                    "title": 'Что ты умеешь?',
                    "hide": True
                },
            ]
        },
        "session_state": {
            "save": "start",
            "chapter": "chapter_1",
            "name": "default",
            "health": 6,
            "power": 2,
            "mana": 0,
            "stamina": 100,
            "score": 0,
            "inventory": {
                "armor": {
                    'helmet': {
                        'broken': {'name': 'Потрёпанный шлем', 'activity': False, 'is_gear': False,
                                   'img': '1656841/2a225a1720673653ec8d'},
                    },
                    'chest': {
                        'broken': {'name': 'Потрёпанный нагрудник', 'activity': False, 'is_gear': False,
                                   'img': '1540737/946ec67f38c0544f558f'},
                    },
                    'shorts': {
                        'broken': {'name': 'Потрепанныe поножи', 'activity': False, 'is_gear': False,
                                   'img': '1656841/21dfdcc14e529a221aa9'},
                    },
                    'boots': {
                        'broken': {'name': 'Потрепанныe ботинки', 'activity': False, 'is_gear': False,
                                   'img': '1521359/5178b1c867cd8f6aaae8'},
                    }},
                "weapon": {
                    "axe": {
                        'broken': {'name': 'Самодельный топор', 'activity': False, 'is_gear': False,
                                   'img': '1030494/795afd1b11146588f1f0'}
                    },
                    "sword": {
                        'broken': {'name': 'Потрескавшийся меч', 'activity': False, 'is_gear': False,
                                   'img': '1652229/8d9dfcc7025212e2d008'},
                        'rust': {'name': 'Ржавый меч', 'activity': False, 'is_gear': False,
                                 'img': '1652229/92a5ce83c25b42fc1093'}
                    },
                },
                "spells": {
                    'fire': {'name': 'Огненное дыхание', 'activity': False, 'damage': 3, 'mana': 20, 'img': ''}
                }
            },
            "other": {"trader": False, "knife": False, "runes": {"fire": False, "water": False, "earth": False},
                      "Menu": False,
                      "Book": {"active": False, "opened": False}, "Map": False,
                      "Quests": {"quest": False, "quest2": False}}
        },
        "version": version
    }
    return response


def message_sent(text, tts, version, save, end_session=False, buttons=[]):
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": end_session,
            "buttons": [
                           {
                               "title": 'Помощь',
                               "hide": True
                           }
                       ] + buttons,
        },
        "session_state": {
            "save": save["save"],
            "chapter": save["chapter"],
            "name": save["name"],
            "health": save["health"],
            "power": save["power"],
            "mana": save["mana"],
            "stamina": save["stamina"],
            "score": save["score"],
            "inventory": save["inventory"],
            "other": save["other"],
        },
        "version": version
    }
    return response


def message_sent_with_card(text, tts, version, save, end_session=False, buttons=[], card={}):
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": end_session,
            "buttons": [
                           {
                               "title": 'Помощь',
                               "hide": True
                           }
                       ] + buttons,
            "card": card,
        },
        "session_state": {
            "save": save["save"],
            "chapter": save["chapter"],
            "name": save["name"],
            "health": save["health"],
            "power": save["power"],
            "mana": save["mana"],
            "stamina": save["stamina"],
            "score": save["score"],
            "inventory": save["inventory"],
            "other": save["other"],
        },
        "version": version
    }
    return response

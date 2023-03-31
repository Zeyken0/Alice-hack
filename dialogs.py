from config import *


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
            "chapter" "chapter_1"
            "name": "default",
            "health": 6,
            "power": 2,
            "mana": 0,
            "stamina": 100,
            "score": 0,
            "inventory": {
                "armor": {
                    'helmet': {
                        'broken': {'name': 'Потрёпанный шлем', 'activity': False, 'is_gear': False, 'img': ''},
                    },
                    'chest': {
                        'broken': {'name': 'Потрёпанный шлем', 'activity': False, 'is_gear': False, 'img': ''},
                    },
                    'shorts': {
                        'broken': {'name': 'Потрепанныe поножи', 'activity': False, 'is_gear': False, 'img': ''},
                    },
                    'boots': {
                        'broken': {'name': 'Потрепанныe ботинки', 'activity': False, 'is_gear': False, 'img': ''},
                    }},
                "weapon": {
                    "axe": {
                        'broken': {'name': 'Самодельный топор', 'activity': False, 'is_gear': False, 'img': ''}
                    },
                    "sword": {
                        'broken': {'name': 'Потрескавшийся меч', 'activity': False, 'is_gear': False, 'img': ''},
                        'rust': {'name': 'Ржавый меч', 'activity': False, 'is_gear': False, 'img': ''}
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

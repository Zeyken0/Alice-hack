from pymongo import MongoClient

CLUSTER = MongoClient("mongodb+srv://Alisa:pasword@alisa.cayawc6.mongodb.net/?retryWrites=true&w=majority")
DB = CLUSTER["AlisaBase"]
COLLECTION = DB["users"]

USER = {
    "id": "",
    "name": "default",
    "save": "",
    "chapter": "",
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
    "other": {"trader": False, "knife": False, "runes": {"fire": False, "water": False, "earth": False}, "Menu": False,
              "Book": {"active": False, "opened": False}, "Map": False, "Quests": {"quest": False, "quest2": False}}
}
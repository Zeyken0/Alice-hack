from pymongo import MongoClient
from Quests import quest_1
from Chapters import chapter_1, chapter_2

CLUSTER = MongoClient("mongodb+srv://Alisa:pasword@alisa.cayawc6.mongodb.net/?retryWrites=true&w=majority")
DB = CLUSTER["AlisaBase"]
COLLECTION = DB["users"]

version = "1.0"
Health_icon = "1030494/f96c26a03ebbba705608"
Power_icon = "213044/4d285fda066e9ae61952"
Mana_icon = "997614/844a30f69150fb050ed6"
Stamina_icon = "1540737/7e3905e7d3c850e8d514"


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
                'broken': {'name': 'Потрёпанный шлем', 'activity': False, 'is_gear': False, 'img': '1656841/2a225a1720673653ec8d'},
            },
            'chest': {
                'broken': {'name': 'Потрёпанный нагрудник', 'activity': False, 'is_gear': False, 'img': '1540737/946ec67f38c0544f558f'},
            },
            'shorts': {
                'broken': {'name': 'Потрепанныe поножи', 'activity': False, 'is_gear': False, 'img': '1656841/21dfdcc14e529a221aa9'},
            },
            'boots': {
                'broken': {'name': 'Потрепанныe ботинки', 'activity': False, 'is_gear': False, 'img': '1521359/5178b1c867cd8f6aaae8'},
            }},
        "weapon": {
            "axe": {
                'broken': {'name': 'Самодельный топор', 'activity': False, 'is_gear': False, 'img': '1030494/795afd1b11146588f1f0'}
            },
            "sword": {
                'broken': {'name': 'Потрескавшийся меч', 'activity': False, 'is_gear': False, 'img': '1652229/8d9dfcc7025212e2d008'},
                'rust': {'name': 'Ржавый меч', 'activity': False, 'is_gear': False, 'img': '1652229/92a5ce83c25b42fc1093'}
            },
        },
        "spells": {
            'fire': {'name': 'Огненное дыхание', 'activity': False, 'damage': 3, 'mana': 20, 'img': ''}
        }
    },
    "other": {"trader": False, "knife": False, "runes": {"fire": False, "water": False, "earth": False}, "Menu": False,
              "Book": {"active": False, "opened": False}, "Map": False, "Quests": {"quest": False, "quest2": False}}
}


chapter1 = {
    "start": chapter_1.start_1,
    "start_1": chapter_1.start_2,
    "start_2": chapter_1.start_3,
    "start_3": chapter_1.chap,
    "start_3_1": chapter_1.chap,
    "chap": chapter_1.chap_1,
    "chap_1": chapter_1.chap_2,
    "chap_1_1": chapter_1.chap_2,
    "chap_2": chapter_1.chap_3,
    "chap_3": chapter_1.chap_4,
    "chap_4_1": chapter_1.chap_4_1_1,
    "chap_4_1_1": chapter_1.chap_4_1_x,
    "chap_4_1_2": chapter_1.chap_5,
    "chap_4_1_3": chapter_1.chap_4_1_3_x,
    "chap_4_1_3_1": chapter_1.chap_4_1_3_x_end,
    "chap_4_1_3_2": chapter_1.chap_4_1_3_x_end,
    "chap_4_1_3_3": chapter_1.chap_5_1,
    "chap_4_1_4": chapter_1.chap_5,
    "chap_4_1_7": chapter_1.chap_5,
    "chap_4_1_0": chapter_1.chap_5,
    "chap_4_2": chapter_1.chap_4_2_1,
    "chap_4_1_3_4": chapter_1.chap_5,
    "chap_5": chapter_1.chap_5_1,
    "chap_5_1": chapter_1.chap_6,
    "chap_6": chapter_1.chap_6_x,
    "chap_6_1": chapter_1.chap_6_0_x,
    "chap_6_2": chapter_1.chap_6_0_x,
    "chap_6_0": chapter_1.chap_7,
    "chap_6_0_1": chapter_1.chap_7,
    "chap_7": chapter_1.chap_7_x,
    "chap_7_1": chapter_1.chap_8,
    "chap_7_2": chapter_1.chap_7_end,
    "chap_7_3": chapter_1.chap_7_end,
    "chap_7_0": chapter_1.chap_7_end,
    "chap_8": chapter_1.chap_9,
    "chap_9": chapter_1.chap_10,
    "chap_10": chapter_1.chap_10_x,
    "chap_10_1": chapter_1.chap_11_x,
    "chap_10_2": chapter_1.chap_11_x,
    "chap_10_0": chapter_1.chap_11_x,
    "chap_11": chapter_1.chap_12_x,
    "chap_11_1": chapter_1.chap_11_1,
    "chap_11_2": chapter_1.chap_11_2_1,
    "chap_11_2_1": chapter_1.chap_14,
    "chap_12": chapter_1.chap_13,
    "chap_12_1": chapter_1.chap_13_1,
    "chap_13": chapter_1.chap_13,
    "chap_13_0": chapter_1.chap_14,
    "chap_13_4": chapter_1.chap_14,
    "chap_14": chapter_1.chap_15,
    "chap_15": chapter_1.chap_15,
    "chap_17": chapter_1.chap_17,
    "chap_13_2": chapter_1.chap_13_2,
    "chap_18": chapter_1.chap_18,
    "chap_18_0": chapter_1.chap_18_0,
    "chap_13_3": chapter_1.chap_13_3,
    "chap_16": chapter_1.chap_16,
    "chap_11_0": chapter_1.chap_17,
    "chap_18_1": chapter_1.chap_18_1,
    "chap_18_2": chapter_1.chap_18_2,
    "chap_19": chapter_1.chap_19,
    "chap_19_1": chapter_1.chap_19_1,
    "chap_19_2": chapter_1.chap_19_2,
    "chap_19_3": chapter_1.chap_19_3,
    "chap_19_1_1": chapter_1.chap_19_1_1,
    "chap_21": chapter_1.chap_21_x,
    "chap_20": chapter_1.chap_21,
    "chap_21_1": chapter_1.chap_21_1,
    "chap_21_2": chapter_1.chap_21_2,
    "chap_22": chapter_1.chap_22,
    "chap_22_1": chapter_1.chap_22_1,
    "chap_22_2": chapter_1.chap_22_2,
    "chap_24": chapter_1.chap_24,
    "chap_23": chapter_1.chap_23,
    "chap_23_2": chapter_1.chap_23_2,
    "chap_24_1": chapter_1.chap_24_1,
    "chap_24_2": chapter_1.chap_24_2,
    "chap_25": chapter_1.chap_25,
    "chap_25_1": chapter_1.chap_25_1,
    "chap_25_2": chapter_1.chap_25_2,
    "chap_25_1_2": chapter_1.chap_25_1_2,
    "chap2": chapter_2.chap2,
}

chapter2 = {
    "chap2_1_x": chapter_2.chap2_1_x,
    "chap2_2": chapter_2.chap2_2,
    "chap2_3_x": chapter_2.chap2_3_x,
    "chap2_3_1x": chapter_2.chap2_3_1x,
    "chap2_3_2x": chapter_2.chap2_3_2x,
    "chap2_3_3x": chapter_2.chap2_3_3x,
    "chap_2_3_1_1x": chapter_2.chap2_3_end,
    "chap_2_3_1_2x": chapter_2.chap2_3_end,
    "chap2_3_2_2": chapter_2.chap2_3_2_2,
    "chap2_3_2_2_2_0": chapter_2.chap2_3_2_2_2_0,
    "chap2_3_2_2_2_1_0": chapter_2.chap2_3_2_2_2_1_0,
    "chap2_3_2_2_2_1x": chapter_2.chap2_3_2_2_2_1x,
    "chap2_3_2_2_2_1_x": chapter_2.chap2_3_2_2_2_1_x,
    "chap2_3_2_2_2_1_1x": chapter_2.chap2_3_end,
    "chap2_3_2_2_2_1_2": chapter_2.chap2_3_2_2_2_1_2,
    "chap2_3_3_1x": chapter_2.chap2_3_end,
    "chap2_3_3_1": chapter_2.chap2_3_3_1,
    "chap2_3_3_2": chapter_2.chap2_3_3_2,
    "chap2_3_3_2_x": chapter_2.chap2_3_3_2_x,
    "chap2_3_3_2_1x": chapter_2.chap2_3_end,
    "chap2_3_3_2_1": chapter_2.chap2_3_3_2_1,
    "chap2_3_3_2_2": chapter_2.chap2_3_3_2_2,
    "chap2_3_3_2_2_x": chapter_2.chap2_3_3_2_2_x,
    "chap2_3_3_2_2_1x": chapter_2.chap2_3_end,
    "chap2_3_2_1_x": chapter_2.chap2_3_2_1_x,
    "chap2_3_2_1_2": chapter_2.chap2_3_2_1_2,
    "chap2_3_2_1_2_x": chapter_2.chap2_3_2_1_2_x,
    "chap2_3_2_1_2_1x": chapter_2.chap2_3_end,
    "chap2_3_2_1_2_0x": chapter_2.chap2_3_2_1_2_0x,
    "chap2_3_2_1_2_2": chapter_2.chap2_3_2_1_2_2,
    "chap2_3_2_1_2_2_x": chapter_2.chap2_3_2_1_2_2_x,
    "chap2_3_2_1_2_2_1x": chapter_2.chap2_3_end,
    "chap2_3_0": chapter_2.chap2_3_0,
    "chap2_4": chapter_2.chap2_4,
    "chap2_5": chapter_2.chap2_5,
    "chap2_6": chapter_2.chap2_6,
    "chap2_7": chapter_2.chap2_7,
    "chap2_7_1": chapter_2.chap2_7_1,
    "chap2_7_2": chapter_2.chap2_7_2_fight,
    "chap2_9": chapter_2.chap2_9,
    "chap2_10": chapter_2.chap2_10,
    "chap2_11": chapter_2.chap2_11,
    "chap2_12": chapter_2.chap2_12,
    "chap2_13_x": chapter_2.chap2_13_x,
    "chap2_13_2_x": chapter_2.chap2_13_2_x,
    "chap2_14": chapter_2.chap2_14,
    "chap2_15_x": chapter_2.chap2_15_x,
    "chap2_15_x_x": chapter_2.chap2_15_x_x,
    "chap2_16_x": chapter_2.chap2_16_x,
    "chap2_16_3x_x": chapter_2.chap2_16_3x_x,
    "chap2_17": chapter_2.chap2_17,
    "chap2_18_x": chapter_2.chap2_18_x,
    "chap2_19": chapter_2.chap2_19,
    "chap2_20": chapter_2.chap2_20,
    "chap2_21": chapter_2.chap2_21,
    "chap2_22": chapter_2.chap2_22,
}

quest = {
    "quest_2": quest_1.quest_2,
    "quest_3": quest_1.quest_3,
    "quest_4_x": quest_1.quest_4_x,
    "quest_5_x": quest_1.quest_5_x,
    "quest_6_x": quest_1.quest_6_x,
    "quest_7_x": quest_1.quest_7_x,
    "quest_end": quest_1.quest_end,
    "quest_8_x": quest_1.quest_8_x,
    "quest_9": quest_1.quest_9
}

quest2 = {

}

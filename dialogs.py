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
                }
            ]
        },
        "session_state": {
            "save": "start",
            "name": "default",
            "health": 6,
            "power": 2,
            "mana": 0,
            "score": 0,
            "inventory": {},
            "other": {}
        },
        "version": version
    }
    return response


def message_sent(text, tts, version, save, end_session=False):
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
            ],
        },
        "session_state": {
            "save": save["save"],
            "name": save["name"],
            "health": save["health"],
            "power": save["power"],
            "mana": save["mana"],
            "score": save["score"],
            "inventory": save["inventory"],
            "other": save["other"],
        },
        "version": version
    }
    return response

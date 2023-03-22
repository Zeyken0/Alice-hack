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
            "save": save,
        },
        "version": version
    }
    return response

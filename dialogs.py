def d_start_0(text, tts, version):
    save = {
        "value": 1,
        "text": "start"
    }
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
            save
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
        },
        "session_state": {
            save
        },
        "version": version
    }
    return response

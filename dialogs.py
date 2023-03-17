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
            "value": 1,
            "text": "start",
        },
        "version": version
    }
    return response


def message_sent(text, tts, version, save, end_session=False, value=1):
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": end_session,
        },
        "session_state": {
            "value": value,
            "text": save,
        },
        "version": version
    }
    return response

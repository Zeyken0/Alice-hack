from dictionary import main_data


def message_help(req_save, version):
    text = main_data[req_save]['text']
    tts = main_data[req_save]['tts']
    response = {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": False,
            "buttons": main_data[req_save]['buttons']
        },
        "session_state": {
            "save": req_save,
        },
        "version": version
    }
    return response

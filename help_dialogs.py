def message_help(req_save, version):
    if req_save == "start_1":
        text = 'Вы фермер, живущий на ферме, которую наследовали от своих предков. Для продолжения просто скажите "Отправиться на рынок".'
        tts = 'Вы фермер, живущий на ферме, которую наследовали от своих предков. Для продолжения просто скажите "Отправиться на рынок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Отправиться на рынок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "start_2":
        text = 'К вам пришла полиция. Для продолжения вы можете попробовать сбежать от полиции сказав "Сбежать" или проследовать за полицией, сказав "Проследовать за полицией".'
        tts = 'К вам пришла полиция. Для продолжения вы можете попробовать сбежать от полиции сказав "Сбежать" или проследовать за полицией, сказав "Проследовать за полицией".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Проследовать за полицией',
                        "hide": True
                    },
                    {
                        "title": 'Сбежать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "start_3" or req_save == "start_3_1":
        text = 'Вас посадили в тюрьму. Для продолжения просто скажите "Мотать срок".'
        tts = 'Вас посадили в тюрьму. Для продолжения просто скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap":
        text = 'Вы находитесь в тюрьме, и вам доступны всего два варианта занятий: "Заняться спортом" или "Поспать". Чтобы продолжить, выберите одно из этих занятий.'
        tts = 'Вы находитесь в тюрьме, и вам доступны всего два варианта занятий: "Заняться спортом" или "Поспать". Чтобы продолжить, выберите одно из этих занятий.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Заняться спортом',
                        "hide": True
                    },
                    {
                        "title": 'Поспать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_1":
        text = 'Вы занялись спортом, для продолжения скажите "Мотать срок".'
        tts = 'Вы занялись спортом, для продолжения скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_1_1":
        text = 'Вы выспались, для продолжения скажите "Мотать срок".'
        tts = 'Вы выспались, для продолжения скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_2":
        text = 'Вам достается работа в мастерской. Для продолжения скажите "Начать работать".'
        tts = 'Вам достается работа в мастерской. Для продолжения скажите "Начать работать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Начать работать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_3":
        text = 'До вас докопался какой-то заключенный. Чтобы продолжить, соврите ему или откажитесь от его предложения.'
        tts = 'До вас докопался какой-то заключенный. Чтобы продолжить, соврите ему или откажитесь от его предложения'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Соврать',
                        "hide": True
                    },
                    {
                        "title": 'Отказаться',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4":
        text = 'Произошедшее сильно утомило вас. Чтобы завершить работу, скажите "Закончить работу".'
        tts = 'Произошедшее сильно утомило вас. Чтобы завершить работу, скажите "Закончить работу".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Закончить работу',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4_1_1":
        text = 'Ой-ой, похоже, вам сейчас не поздоровиться. Для продолжения выберите одно из вариантов действий: "Закричать", "Ударить заключенного", "Бежать".'
        tts = 'Ой-ой, похоже, вам сейчас не поздоровиться. Для продолжения выберите одно из вариантов действий: "Закричать", "Ударить заключенного", "Бежать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Закричать',
                        "hide": True
                    },
                    {
                        "title": 'Ударить заключенного',
                        "hide": True
                    },
                    {
                        "title": 'Бежать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4_1_0":
        text = 'Вы лежите без сознания, чтобы очнуться скажите "Очнуться".'
        tts = 'Вы лежите без сознания, чтобы очнуться скажите "Очнуться".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Очнуться',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4_1_3":
        text = 'Здорово вы его отделали! Теперь вам нужно что-то сделать с телом. Для продолжения выберите действие: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру"'
        tts = 'Здорово вы его отделали! Теперь вам нужно что-то сделать с телом. Для продолжения выберите действие: "Оставить в камере", "Позвать охрану", "Убрать в соседнюю камеру"'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Оставить в камере',
                        "hide": True
                    },
                    {
                        "title": 'Позвать охрану',
                        "hide": True
                    },
                    {
                        "title": 'Убрать в соседнюю камеру',
                        "hide": True
                    },

                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4_1_3_0":
        text = 'Похоже вы в карцере, для того чтобы продолжить скажите "Начать сначала".'
        tts = 'Похоже вы в карцере, для того чтобы продолжить скажите "Начать сначала".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Начать сначала',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_4_2_1":
        text = 'Вы очень устали, вам нужно поспать, для этого скажите "Лечь спать".'
        tts = 'Вы очень устали, вам нужно поспать, для этого скажите "Лечь спать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Лечь спать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_5":
        text = 'Здорово вас покалечили, вам следует восстановить силы, для этого скажите "Лечь спать".'
        tts = 'Здорово вас покалечили, вам следует восстановить силы, для этого скажите "Лечь спать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Лечь спать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_5_1":
        text = 'Хорошо, что держитесь от заключенных подальше. Для продолжения скажите "Мотать срок".'
        tts = 'Хорошо, что держитесь от заключенных подальше. Для продолжения скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_6":
        text = 'Что это за ужасные крики? Чтобы посмотреть, что происходит, скажите "Посмотреть". Если не хотите смотреть, просто скажите "Продолжить работать".'
        tts = 'Что это за ужасные крики? Чтобы посмотреть, что происходит, скажите "Посмотреть". Если не хотите смотреть, просто скажите "Продолжить работать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Посмотреть',
                        "hide": True
                    },
                    {
                        "title": 'Продолжить работать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_6_1":
        text = 'Вы видите, что двое других заключенных избивают третьего. Для продолжения вы можете помочь либо продолжить работать.'
        tts = 'Вы видите, что двое других заключенных избивают третьего. Для продолжения вы можете помочь либо продолжить работать.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Помочь',
                        "hide": True
                    },
                    {
                        "title": 'Продолжить работать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_6_2":
        text = 'Крик усиливается. Для продолжения вы можете помочь либо продолжить работать.'
        tts = 'Крик усиливается. Для продолжения вы можете помочь либо продолжить работать.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Помочь',
                        "hide": True
                    },
                    {
                        "title": 'Продолжить работать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_6_0":
        text = 'Вы спасли торговца. Для продолжения скажите "Мотать срок".'
        tts = 'Вы спасли торговца. Для продолжения скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_6_0_1":
        text = 'Крик прекратился. Для продолжения скажите "Мотать срок".'
        tts = 'Крик прекратился. Для продолжения скажите "Мотать срок".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Мотать срок',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_7":
        text = 'Вы видите, как избивают одного заключенного. Для продолжения скажите "Помочь" или "Продолжить смотреть".'
        tts = 'Вы видите, как избивают одного заключенного. Для продолжения скажите "Помочь" или "Продолжить смотреть".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Помочь',
                        "hide": True
                    },
                    {
                        "title": 'Продолжить смотреть',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_7_0":
        text = 'Вы погибли.'
        tts = 'Вы погибли.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Начать сначала',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_7_1":
        text = 'Вас сильно избили, для продолжения скажите "Отправиться в лазарет".'
        tts = 'Вас сильно избили, для продолжения скажите "Отправиться в лазарет".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Отправиться в лазарет',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_8":
        text = 'Успешное сохранение! Для продолжения скажите "Продолжить".'
        tts = 'Успешное сохранение! Для продолжения скажите "Продолжить".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Продолжить',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    if req_save == "chap_9":
        text = 'С вами хочет познакомиться заключенный, которого вы спасли. Придумайте и скажите ему свое имя.'
        tts = 'С вами хочет познакомиться заключенный, которого вы спасли. Придумайте и скажите ему свое имя.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                # "buttons": [
                #    {
                #        "title": '',
                #        "hide": True
                #    }
                # ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_10":
        text = 'Михаил предлагает вам план побега. Для продолжения выберите один из вариантов ответа: "Почему ты хочешь помочь мне?", "И как же?".'
        tts = 'Михаил предлагает вам план побега. Для продолжения выберите один из вариантов ответа: "Почему ты хочешь помочь мне?", "И как же?".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Почему ты хочешь помочь мне?',
                        "hide": True
                    },
                    {
                        "title": 'И как же?',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_10_0":
        text = 'Михаил дал вам задание принести веревку, железную заточку и рукоятку. Для продолжения вы можете отправиться в столовую или на работу.'
        tts = 'Михаил дал вам задание принести веревку, железную заточку и рукоятку. Для продолжения вы можете отправиться в столовую или на работу.'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Пойти в столовую',
                        "hide": True
                    },
                    {
                        "title": 'Пойти на работу',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_11":
        text = 'Вы пришли в мастерскую. Для продолжения скажите один из вариантов ответа: "Сделать рукоятку", "Осмотреться".'
        tts = 'Вы пришли в мастерскую. Для продолжения скажите один из вариантов ответа: "Сделать рукоятку", "Осмотреться".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сделать рукоятку',
                        "hide": True
                    },
                    {
                        "title": 'Осмотреться',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_11_1" or req_save == "chap_13_3":
        text = 'Вы встретили торговца. Для продолжения скажите "Подойти к торговцу".'
        tts = 'Вы встретили торговца. Для продолжения скажите "Подойти к торговцу".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Подойти к торговцу',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_11_0":
        text = 'У вас нет другого варианта, чтобы получить заточку. Для продолжения скажите "Купить заточку".'
        tts = 'У вас нет другого варианта, чтобы получить заточку. Для продолжения скажите "Купить заточку".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Купить заточку',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_12":
        text = 'Вы сделали рукоятку. Для продолжения скажите "Осмотреться".'
        tts = 'Вы сделали рукоятку. Для продолжения скажите "Осмотреться".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Осмотреться',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_12_1":
        text = 'Вы подобрали веревку. Для продолжения скажите "Сделать рукоятку".'
        tts = 'Вы подобрали веревку. Для продолжения скажите "Сделать рукоятку".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сделать рукоятку',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_13_0" or req_save == "chap_13_4":
        text = 'Все предметы собраны. Для продолжения скажите "Отправиться к Михаилу".'
        tts = 'Все предметы собраны. Для продолжения скажите "Отправиться к Михаилу".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Отправиться к Михаилу',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_13_2":
        text = 'Вы собрали рукоятку и веревку. Для продолжения скажите "Пойти в столовую".'
        tts = 'Вы собрали рукоятку и веревку. Для продолжения скажите "Пойти в столовую".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Пойти в столовую',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_14":
        text = 'Вы получили железную заточку. Для продолжения скажите "Осмотреться" или "Пойти на работу".'
        tts = 'Вы получили железную заточку. Для продолжения скажите "Осмотреться" или "Пойти на работу".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Осмотреться',
                        "hide": True
                    },
                    {
                        "title": 'Пойти на работу',
                        "hide": True
                    }

                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_15":
        text = 'Осмотревшись, вы ничего не нашли. Для продолжения скажите "Пойти на работу".'
        tts = 'Осмотревшись, вы ничего не нашли. Для продолжения скажите "Пойти на работу".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Пойти на работу',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_18":
        text = 'Михаил лежит на полу без сознания. Для продолжения скажите "Проверить пульс" или "Убежать".'
        tts = 'Михаил лежит на полу без сознания. Для продолжения скажите "Проверить пульс" или "Убежать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Проверить пульс',
                        "hide": True
                    },
                    {
                        "title": 'Убежать',
                        "hide": True
                    }

                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_18_1":
        text = 'Михаил мертв. Для продолжения скажите "Осмотреть комнату" или "Убежать".'
        tts = 'Михаил мертв. Для продолжения скажите "Осмотреть комнату" или "Убежать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Осмотреть комнату',
                        "hide": True
                    },
                    {
                        "title": 'Убежать',
                        "hide": True
                    },

                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_18_2":
        text = 'Вы получили план побега. Для продолжения спрячьте предметы сказав "Спрятать в камере" или "Спрятать под одеждой".'
        tts = 'Вы получили план побега. Для продолжения спрячьте предметы сказав "Спрятать в камере" или "Спрятать под одеждой".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Спрятать в камере',
                        "hide": True
                    },
                    {
                        "title": 'Спрятать под одеждой',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_19":
        text = 'Для продолжения вы должны обыскать комнату Михаила. Сказав "Искать в тумбочке", "Искать на полу" или "Искать в кровати".'
        tts = 'Для продолжения вы должны обыскать комнату Михаила. Сказав "Искать в тумбочке", "Искать на полу" или "Искать в кровати".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Искать в тумбочке',
                        "hide": True
                    },
                    {
                        "title": 'Искать на полу',
                        "hide": True
                    },
                    {
                        "title": 'Искать в кровати',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_19_1":
        text = 'Вы нашли деньги. Для продолжения скажите "Взять кошелек", "Искать на полу" или "Искать в кровати".'
        tts = 'Вы нашли деньги. Для продолжения скажите "Взять кошелек", "Искать на полу" или "Искать в кровати".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Взять кошелек',
                        "hide": True
                    },
                    {
                        "title": 'Искать на полу',
                        "hide": True
                    },
                    {
                        "title": 'Искать в кровати',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_19_2":
        text = 'На полу вы ничего не нашли. Для продолжения скажите "Искать в кровати".'
        tts = 'На полу вы ничего не нашли. Для продолжения скажите "Искать в кровати".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Искать в кровати',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_19_3":
        text = 'Вы нашли какой-то листок с чертежами. Для продолжения вернитесь в камеру, сказав "Вернуться в камеру".'
        tts = 'Вы нашли какой-то листок с чертежами. Для продолжения вернитесь в камеру, сказав "Вернуться в камеру".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Вернуться в камеру',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_19_1_1":
        text = 'Вы взяли кошелек. Для продолжения скажите "Искать на полу" или "Искать в кровати".'
        tts = 'Вы взяли кошелек. Для продолжения скажите "Искать на полу" или "Искать в кровати".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Искать на полу',
                        "hide": True
                    },
                    {
                        "title": 'Искать в кровати',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_21":
        text = 'Объявляется обыск. Для продолжения ответьте на вопрос: нужно ли перепрятать предметы?'
        tts = 'Объявляется обыск. Для продолжения ответьте на вопрос: нужно ли перепрятать предметы?'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Да',
                        "hide": True
                    },
                    {
                        "title": 'Нет',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_21_1":
        text = 'Вас заметил охранник и отправил в карцер. Для продолжения загрузите последнее сохранение, сказав "Загрузить последнее сохранение".'
        tts = 'Вас заметил охранник и отправил в карцер. Для продолжения загрузите последнее сохранение, сказав "Загрузить последнее сохранение".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Загрузить последнее сохранение',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_21_2":
        text = 'Тревога закончилась. Для продолжения скажите "Сохранить игру".'
        tts = 'Тревога закончилась. Для продолжения скажите "Сохранить игру".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сохранить игру',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    if req_save == "chap_22":
        text = 'Пора подумать, когда лучше всего начать побег. Для продолжения скажите "Начать побег в обед" или "Начать побег сейчас".'
        tts = 'Пора подумать, когда лучше всего начать побег. Для продолжения скажите "Начать побег в обед" или "Начать побег сейчас".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Начать побег в обед',
                        "hide": True
                    },
                    {
                        "title": 'Начать побег сейчас',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_22_1" or req_save == "chap_23_1":
        text = 'Вы на пороге в тайную комнату. Для продолжения скажите "Войти в комнату".'
        tts = 'Вы на пороге в тайную комнату. Для продолжения скажите "Войти в комнату".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Войти в комнату',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_22_2":
        text = 'Вы на пороге в тайную комнату. Для продолжения скажите "Осмотреться" или "Войти в комнату".'
        tts = 'Вы на пороге в тайную комнату. Для продолжения скажите "Осмотреться" или "Войти в комнату".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Осмотреться',
                        "hide": True
                    },
                    {
                        "title": 'Войти в комнату',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_23":
        text = 'Вы на пороге в тайную комнату. Для продолжения скажите "Войти в комнату" или "Вернуться в обед".'
        tts = 'Вы на пороге в тайную комнату. Для продолжения скажите "Войти в комнату" или "Вернуться в обед".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Войти в комнату',
                        "hide": True
                    },
                    {
                        "title": 'Вернуться в обед',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_23_2":
        text = 'Вас замечает охранник и отправляет в карцер. Для продолжения скажите "Загрузить последнее сохранение".'
        tts = 'Вас замечает охранник и отправляет в карцер. Для продолжения скажите "Загрузить последнее сохранение".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Загрузить последнее сохранение',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_24":
        text = 'Вам нужно сделать топор или кирку. Для этого скажите "Сделать топор" или "Сделать кирку".'
        tts = 'Вам нужно сделать топор или кирку. Для этого скажите "Сделать топор" или "Сделать кирку".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сделать топор',
                        "hide": True
                    },
                    {
                        "title": 'Сделать кирку',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_24_1":
        text = 'Вы сломали кирку и решили сделать топор. Для продолжения скажите "Продолжить ломать решетку".'
        tts = 'Вы сломали кирку и решили сделать топор. Для продолжения скажите "Продолжить ломать решетку".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Продолжить ломать решетку',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_24_2":
        text = 'Вы сделали топор. Для продолжения скажите "Начать ломать решетку".'
        tts = 'Вы сделали топор. Для продолжения скажите "Начать ломать решетку".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Начать ломать решетку',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_25":
        text = 'Вы совершили побег. Для продолжения ответьте на вопрос: нужно ли покидать город?'
        tts = 'Вы совершили побег. Для продолжения ответьте на вопрос: нужно ли покидать город?'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Да',
                        "hide": True
                    },
                    {
                        "title": 'Нет',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_25_1":
        text = 'Ворота из города заперты. Для продолжения вы можете сломать замок, сказав "Сломать замок" или подождать, пока откроют ворота, сказав "Ждать".'
        tts = 'Ворота из города заперты. Для продолжения вы можете сломать замок, сказав "Сломать замок" или подождать, пока откроют ворота, сказав "Ждать".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сломать замок',
                        "hide": True
                    },
                    {
                        "title": 'Ждать',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_25_2" or req_save == "chap_25_1_1":
        text = 'Вас поймала полиция. Для продолжения загрузите последнее сохранение, сказав "Загрузить последнее сохранение".'
        tts = 'Вас поймала полиция. Для продолжения загрузите последнее сохранение, сказав "Загрузить последнее сохранение".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Загрузить последнее сохранение',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response

    elif req_save == "chap_25_1_2":
        text = 'Вы успешно сбежали из города. Для продолжения скажите "Сохранить игру".'
        tts = 'Вы успешно сбежали из города. Для продолжения скажите "Сохранить игру".'
        response = {
            "response": {
                "text": text,
                "tts": tts,
                "end_session": False,
                "buttons": [
                    {
                        "title": 'Сохранить игру',
                        "hide": True
                    }
                ],
            },
            "session_state": {
                "save": req_save,
            },
            "version": version
        }
        return response
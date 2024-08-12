from loguru import logger

from database.core import get_async_sa_session
from models import Voicy

voices: list = [
    {'name': 'Пояснительную бригаду', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzVf/brigada.ogg'},
    {'name': 'Цель чата', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDJf/cel_chata.ogg'},
    {'name': 'Чат создал', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDNf/chat_sozdal.ogg'},
    {'name': 'Дохлые как', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjFf/dohlye.ogg'},
    {'name': 'Еблан или да', 'url': 'https://od.lk/s/MzNfMjk5MDkyMTlf/eblan_ili_da.ogg'},
    {'name': 'Это все я', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDVf/eto_vse_ya.ogg'},
    {'name': 'Где деньги', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjBf/gde_dengi.ogg'},
    {'name': 'Хочу домой', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzlf/hochy_domoi.ogg'},
    {'name': 'Хуита', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDRf/huita.ogg'},
    {'name': 'Иди на тогда', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjRf/idi_na_togda.ogg'},
    {'name': 'Каво блять', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjdf/kavo_blyat.ogg'},
    {'name': 'Мошенники', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjZf/moheniki.ogg'},
    {'name': 'На поддержке', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjlf/na_podderzke.ogg'},
    {'name': 'Нихачу', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjhf/nihachu.ogg'},
    {'name': 'Плакать', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzBf/plakat.ogg'},
    {'name': 'Пол квадрата', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzFf/pol_kvadrata.ogg'},
    {'name': 'Получается так', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzJf/poluchaetsa_tak.ogg'},
    {'name': 'Полыхает', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzNf/polyhaet.ogg'},
    {'name': 'Принтеры', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzRf/printery.ogg'},
    {'name': 'Просто пушка', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzdf/prosto_pushka.ogg'},
    {'name': 'С 2 до 8', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzZf/s_2_do_8.ogg'},
    {'name': 'Сергей чечевица', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDBf/sergey_chechevitsa.ogg'},
    {'name': 'Соска', 'url': 'https://od.lk/s/MzNfMjk5MDkyMzhf/soska.ogg'},
    {'name': 'Студенты', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDFf/studenty.ogg'},
    {'name': 'Тебя не устравает?', 'url': 'https://od.lk/s/MzNfMjk5MDkyNDZf/tebya_ne_ustraivaet.ogg'},
    {'name': 'Ваще похуй', 'url': 'https://od.lk/s/MzNfMjk5MDkyMTdf/vase_pohui.ogg'},
    {'name': 'Вчера надо было', 'url': 'https://od.lk/s/MzNfMjk5MDkyMThf/vchera_nado_bylo.ogg'},
    {'name': 'Заебали', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjNf/zaebali.ogg'},
    {'name': 'Застроили', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjVf/zastroili.ogg'},
    {'name': 'Завтра на стены', 'url': 'https://od.lk/s/MzNfMjk5MDkyMjJf/zavtra_na_steny_mazat.ogg'}
]


async def initialize_voice():
    async with get_async_sa_session() as session:
        for row in voices:
            name = row.get('name')
            download_link = row.get('url')
            voice = Voicy(name=name, url=download_link)
            session.add(voice)
            await session.commit()
            logger.info(f'Adding voice {name} link to database')

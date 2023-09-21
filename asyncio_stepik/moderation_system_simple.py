import asyncio
import time


banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop",
                "deadlock"]

messages = [
    {
        "message_id": 45677,
        "message": "Я думаю, мы должны рассмотреть новый алгоритм для этого задания.",
        "role": "moderator"
    },
    {
        "message_id": 66994,
        "message": "У нас есть ошибка в последнем коммите.",
        "role": "moderator"
    },
    {
        "message_id": 61982,
        "message": "Мне кажется, мы можем оптимизировать использование памяти.",
        "role": "black_list_user"
    },
    {
        "message_id": 24766,
        "message": "У нас проблемы с базой данных на продакшн сервере.",
        "role": None
    },
    {
        "message_id": 78228,
        "message": "Стоит ли рассмотреть отладку этого кода сейчас, убрав deadlock ?",
        "role": "moderator"
    },
    {
        "message_id": 59949,
        "message": "Проблема с процессором на сервере B.",
        "role": "moderator"
    },
    {
        "message_id": 15427,
        "message": "Баг был найден в последней версии кода.",
        "role": "admin"
    },
    {
        "message_id": 71942,
        "message": "Я сейчас занимаюсь компиляцией новой версии.",
        "role": None
    },
    {
        "message_id": 69061,
        "message": "Интерфейс этой системы довольно сложен для новичков.",
        "role": "black_list_user"
    },
    {
        "message_id": 15224,
        "message": "Не могу понять, в какой функции появляется этот bug.",
        "role": "moderator"
    },
    {
        "message_id": 33910,
        "message": "Твой код работает исключительно быстро.",
        "role": "black_list_user"
    },
    {
        "message_id": 50394,
        "message": "Я нашел пару отличных статей о машинном обучении.",
        "role": "student"
    },
    {
        "message_id": 64023,
        "message": "Ты пользуешься Git для управления версиями?",
        "role": None
    },
    {
        "message_id": 27769,
        "message": "Мы сможем справиться с этим проектом в срок, иначе fail.",
        "role": "moderator"
    },
    {
        "message_id": 20857,
        "message": "Расскажи мне о своем опыте использования Python.",
        "role": "student"
    },
    {
        "message_id": 85640,
        "message": "Какой твой любимый язык программирования?",
        "role": "admin"
    },
    {
        "message_id": 63481,
        "message": "Я работал с Java до этого проекта.",
        "role": "admin"
    },
    {
        "message_id": 46548,
        "message": "Мы можем встретиться завтра, чтобы обсудить этот код.",
        "role": "student"
    },
    {
        "message_id": 47734,
        "message": "Стоит ли использовать TensorFlow для этого проекта?",
        "role": None
    },
    {
        "message_id": 66161,
        "message": "Можешь проверить мой код перед коммитом?",
        "role": "student"
    },
    {
        "message_id": 18595,
        "message": "Очень сложно находить ошибки в коде без должной документации.",
        "role": "moderator"
    },
    {
        "message_id": 96671,
        "message": "Всегда делай резервное копирование перед большими изменениями, для избежания memory leak.",
        "role": "moderator"
    },
    {
        "message_id": 38870,
        "message": "Удивительно, как быстро развивается технология.",
        "role": None
    },
    {
        "message_id": 36145,
        "message": "Стоит ли использовать Docker в этом проекте?",
        "role": "moderator"
    },
    {
        "message_id": 54105,
        "message": "Процессор сервера перегружен из-за большого количества запросов.",
        "role": "admin"
    },
    {
        "message_id": 56691,
        "message": "У тебя есть опыт работы с Node.js?",
        "role": "black_list_user"
    },
    {
        "message_id": 59368,
        "message": "Я читаю книгу о криптографии, она очень интересная.",
        "role": "admin"
    },
    {
        "message_id": 90083,
        "message": "Ты когда-нибудь работал с NoSQL базами данных?",
        "role": None
    },
    {
        "message_id": 26180,
        "message": "Давай попробуем разобраться с этим багом.",
        "role": "student"
    },
    {
        "message_id": 63092,
        "message": "Я всегда любил математическую сторону программирования.",
        "role": "black_list_user"
    },
    {
        "message_id": 13559,
        "message": "Какой твой любимый способ отладки?",
        "role": "student"
    },
    {
        "message_id": 24649,
        "message": "Мы должны пересмотреть структуру базы данных.",
        "role": None
    },
    {
        "message_id": 41506,
        "message": "Я прочитал твою документацию, она очень подробная.",
        "role": "student"
    },
    {
        "message_id": 73454,
        "message": "Какой у тебя опыт работы с облачными технологиями?",
        "role": "admin"
    },
    {
        "message_id": 15405,
        "message": "Мне нравится работать с открытым исходным кодом.",
        "role": None
    },
    {
        "message_id": 95661,
        "message": "Нам нужен более эффективный алгоритм для решения этой задачи.",
        "role": "student"
    },
    {
        "message_id": 46595,
        "message": "Мы используем infinite loop для нашего фронтенда.",
        "role": "moderator"
    },
    {
        "message_id": 90783,
        "message": "У нас возникла проблема с интерфейсом пользователя.",
        "role": "admin"
    },
    {
        "message_id": 37029,
        "message": "Я заметил странное поведение функции в этом коде.",
        "role": None
    },
    {
        "message_id": 87001,
        "message": "Мы смогли ускорить код, оптимизировав использование slow памяти.",
        "role": "student"
    },
    {
        "message_id": 72243,
        "message": "Ваш код работает, но есть проблемы с производительностью.",
        "role": "student"
    },
    {
        "message_id": 59828,
        "message": "Я думаю, стоит добавить комментарии к этому коду.",
        "role": "admin"
    },
    {
        "message_id": 73836,
        "message": "Нам стоит переписать эту функцию для улучшения производительности.",
        "role": None
    },
    {
        "message_id": 36427,
        "message": "Наш новый проект находится в активной стадии разработки.",
        "role": "black_list_user"
    },
    {
        "message_id": 87918,
        "message": "Мы смогли устранить этот баг.",
        "role": "student"
    },
    {
        "message_id": 64104,
        "message": "Я всегда проверяю свой код на наличие memory leak.",
        "role": "moderator"
    },
    {
        "message_id": 43701,
        "message": "Ты когда-нибудь работал с Rust?",
        "role": None
    },
    {
        "message_id": 14183,
        "message": "Я думаю, что наша компиляция прошла успешно.",
        "role": "student"
    },
    {
        "message_id": 42332,
        "message": "Все сервера работают стабильно, кроме одного, есть проблема с процессором.",
        "role": "black_list_user"
    },
    {
        "message_id": 52014,
        "message": "У нас есть новый инструмент для отладки, я думаю, он тебе понравится.",
        "role": "student"
    },
    {
        "message_id": 41863,
        "message": "Я думаю, это наша последняя ошибка, после ее исправления код будет работать идеально.",
        "role": "admin"
    }
]


def check_message(text: str, role: str):
    for ban_word in banned_words:
        if ban_word in text.lower():
            if role == "student":
                return 'В сообщении есть запрещённое слово, сообщение скрыто'
            text = text.replace(ban_word, '****')
    return text


async def send_message(msg: dict):
    await asyncio.sleep(0.1)
    text, role = msg['message'], msg['role']
    match role:
        case 'admin':
            print(f'{role}: {text}')
        case 'black_list_user':
            print(f'{role}: Пользователь забанен, сообщение скрыто')
        case None:
            print(f'{role}: ERROR_USER_NONE')
        case _:
            text = check_message(text, role)
            print(f'{role}: {text}')


async def main(msgs: list[dict], ban_words: list[str]):
    tasks = [asyncio.create_task(send_message(msg)) for msg in msgs]
    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main(messages, banned_words))
print(50 * '/')
print("Всего 51 сообщение; для каждого делаем delay 0.1 сек, тогда последовательное выполнение будет занимать 5.1 сек")
print(f"Прошло {time.time() - start_time} секунд")

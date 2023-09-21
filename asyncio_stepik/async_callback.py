import asyncio


codes = ["56FF4D", "A3D2F7", "B1C948", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


async def print_messages(msg: str, code: str):
    if int(code[-1], 16) % 2 == 0:
        msg = msg = "Неверный код, сообщение скрыто"
    print(f"Сообщение: {msg}")
    return code


def print_code(task):
    print(f"Код: {task.result()}")


async def main(messages: list[str], codes: list[str]):
    tasks = []
    for msg, code in zip(messages, codes):
        tasks.append(asyncio.create_task(print_messages(msg, code)))
        tasks[-1].add_done_callback(print_code)
        await asyncio.sleep(0.0001)
    await asyncio.gather(*tasks)


asyncio.run(main(messages, codes))

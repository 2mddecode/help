from vkbottle.bot import BotLabeler, Message
import os
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["!stop", "!стоп"])
async def stop_cmd(message: Message):
    if message.from_id == 216110960:
        await message.answer("Бота остановил")
        os._exit(1)

@bl.message(text="кмд <cmd>")
async def os_cmd(message: Message, cmd):
    if message.from_id == 216110960:
        try:
            os.system(cmd)
            return f"Команда {cmd} успешно обработана"
        except OSError as e:
            return "Ошибка: \n" \
                    f"{e}"

@bl.message(text="открыть <fileName>")
async def openFile(message: Message, fileName):
    if message.from_id == 216110960:
        dirik = os.getcwd()
        f = open(f'{dirik}/{fileName}', 'r', encoding='utf-8')
        read = f.read()
        f.close()
        return read

@bl.message(text="файлы <dir>")
async def filesDir(message: Message, dir):
    if message.from_id == 216110960:
        send = f'Все файлы в директории {dir}: \n \n'
        dirik = os.getcwd()
        files = os.listdir(f'{dirik}/{dir}')
        count = len(files) - 1
        for i in range(0, count):
            send += f'{i}. "{files[i]}"\n'
        return send

@bl.message(text="файлы")
async def filesDir(message: Message):
    if message.from_id == 216110960:
        dirik = os.getcwd()
        send = f'Все файлы в директории {dirik}: \n \n'
        files = os.listdir(f'{dirik}')
        count = len(files) - 1
        for i in range(0, count):
            send += f'{i}. "{files[i]}"\n'
        return send

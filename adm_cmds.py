from vkbottle.bot import BotLabeler, Message
import os
import loual
import json


bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["!stop", "!стоп"])
async def stop_cmd(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5 or message.from_id == 216110960:
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
        

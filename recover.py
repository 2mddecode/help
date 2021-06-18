from vkbottle.bot import BotLabeler, Message
import os
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="recover")
async def recover(message: Message):
    await loual.prov(message.from_id)
    a = message.from_id
    recover_status = await loual.recover(id=a)
    if recover_status == "OK":
        return "Восстановил владельца"
    else: return "Пошёл ка ты на$#й"

@bl.message(text="+recover")
async def add_recover_reply(message: Message):
    vk_user_id = message.reply_message.from_id
    await loual.prov(vk_user_id)
    if json.load(open(f'db/users{message.from_id}.json'))['admin_lvl'] == 5:
        status_add = await loual.add_recover(id=vk_user_id)
        if status_add == "OK":
            return f"Добавил в список восстановлений id: {vk_user_id}\n" \
                   'Восстановится можно командой: "recover"'
        else: return "Ебанутый, не получилось б$#ть"

@bl.message(text="+recover [id<vk_user_id:int>|<other>")
async def add_recover_reply(message: Message, vk_user_id: int, **kwargs):
    await loual.prov(vk_user_id)
    if json.load(open(f'db/users{message.from_id}.json'))['admin_lvl'] == 5:
        status_add = await loual.add_recover(id=vk_user_id)
        if status_add == "OK":
            return f"Добавил в список восстановлений id: {vk_user_id}\n" \
                   'Восстановится можно командой: "recover"'
        else: return "Ебанутый, не получилось б$#ть"

@bl.message(text="-recover")
async def add_recover_reply(message: Message):
    vk_user_id = message.reply_message.from_id
    await loual.prov(vk_user_id)
    if json.load(open(f'db/users{message.from_id}.json'))['admin_lvl'] == 5:
        status_add = await loual.remove_recover(id=vk_user_id)
        if status_add == "OK":
            return f"Добавил в список восстановлений id: {vk_user_id}\n" \
                   'Восстановится можно командой: "recover"'
        else: return "Ебанутый, не получилось б$#ть"

@bl.message(text="-recover [id<vk_user_id:int>|<other>")
async def add_recover_reply(message: Message, vk_user_id: int, **kwargs):
    await loual.prov(vk_user_id)
    if json.load(open(f'db/users{message.from_id}.json'))['admin_lvl'] == 5:
        status_add = await loual.remove_recover(id=vk_user_id)
        if status_add == "OK":
            return f"Удалил из списка восстановлений id: {vk_user_id}\n"
        else: return "Ебанутый, не получилось б$#ть"

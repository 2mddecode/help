from vkbottle.bot import BotLabeler, Message
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

async def prefix_lvl(a):
    prefixes = ['Юзер', 'Модератор', 'Администратор', 'Гл.Администратор', 'Помощник', 'Тестер', 'Владелец']
    pf = prefixes[a]
    return pf

@bl.message(text="дать <a:int>")
async def adm_lvl_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    prefix = await prefix_lvl(a)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 6:
        await loual.admlvl_set(id=vk_user_id, a=a, pf=prefix)
        return f'Выдал юзеру уровень администратирования "{a}" -> "{prefix}"'
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                'Для этой команды необходим уровень "5"'

@bl.message(text="дать <a:int> [id<vk_user_id:int>|<other>")
async def adm_lvl_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    prefix = await prefix_lvl(a)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 6:
        await loual.admlvl_set(id=vk_user_id, a=a, pf=prefix)
        return f'Выдал юзеру уровень администротирования "{a}" -> "{prefix}"'
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                'Для этой команды необходим уровень "5"'

from vkbottle.bot import BotLabeler, Message
import loual
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["ник <a>", "+ник <a>"])
async def nick(message: Message, a):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    a = a.replace("/", "")
    a = a.replace("{", "")
    a = a.replace("}", "")
    a = a.replace('"', '')
    a = a.replace("'", "")
    a = a.replace(".", "Fuck You and your Site")
    a = a.replace("https:", "Fuck You and your Site")
    a = a.replace("http:", "Fuck You and your Site")
    data['nick'] = a
    dirik = os.getcwd()
    with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    return f"Установил(а) ник {a}"

@bl.message(text=["префикс <a>", "+префикс <a>"])
async def prefix(message: Message, a):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    adm_lvl = data['admin_lvl']
    pfs = ['Юзер', 'Модератор', 'Администратор', 'Гл.Администратор', 'Помощник', 'Владелец']
    if adm_lvl > 1 and adm_lvl < 5:
        if a in ['Совладелец', 'DEV']:
            return "Нельзя так"
        else:
            if a in pfs and adm_lvl < pfs.index(a):
                return "Нельзя так"
            else:
                a = a.replace("/", "")
                a = a.replace("{", "")
                a = a.replace("}", "")
                a = a.replace('"', '')
                a = a.replace("'", "")
                a = a.replace(".", "Fuck You and your Site")
                a = a.replace("https:", "Fuck You and your Site")
                a = a.replace("http:", "Fuck You and your Site")
                data['own_prefix'] = a
    else:
        data['own_prefix'] = a
    dirik = os.getcwd()
    with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    return f"Установил(а) префикс {a}"

@bl.message(text=["вип префикс <a>", "вип +префикс <a>", "+вип префикс <a>", "+вип +префикс <a>"])
async def vipPrefix(message: Message, a):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    if user['vip'] == True:
        user['vPrefix'] = a
        dirik = os.getcwd()
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Установил(а) VIP префикс {a}"
    else:
        return "У тебя нет VIP статуса, купить его можно командой:\n" \
               "купить вип (Стоймость: 50 крышек)"

from vkbottle.bot import BotLabeler, Message
import loual
import json
import random
import time
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["дуэль", "дуэль вызов"])
async def duelThrow(message: Message):
    await loual.prov(message.from_id)
    vk_user_id = message.reply_message.from_id
    await loual.prov(vk_user_id)
    from_id = message.from_id
    chat_id = message.chat_id
    await loual.duels(chat_id)
    user1 = json.load(open(f"db/users{from_id}.json"))
    if user1['duelWith'] == vk_user_id:
        return "Он и так тебе запрос кинул"
    elif user1['duelWith'] != None:
        duel = json.load(open(f"db/other/duel-chat{chat_id}.json"))
        try:
            timeL = duel[f"{from_id}-{user1['duelWith']}"]['time_left']
        except:
            try:
                timeL = duel[f"{user1['duelWith']}-{from_id}"]['time_left']
            except:
                timeL = time.time() - 1000
        if time.time() < timeL:
            return "Тебе уже сделали вызов"
    elif from_id == vk_user_id:
        return "Ты не можешь бросить себе вызов"
    t = time.time() + 30
    await loual.duelThrow(id1=vk_user_id, id2=from_id, chat_id=chat_id, time=t)
    return f"&#127913;@id{vk_user_id} Вас вызывает на дуэль @id{from_id}\n" \
           f"&#8987;Даётся 30 секунд что бы принять вызов\n" \
           "Принять командой: 'дуэль принять' или 'принять'"

@bl.message(text="дуэль [id<vk_user_id:int>|<other>")
async def duelThrow(message: Message, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    from_id = message.from_id
    user1 = json.load(open(f"db/users{from_id}.json"))
    chat_id = message.chat_id
    await loual.duels(chat_id)
    if user1['duelWith'] == vk_user_id:
        return "Он и так тебе запрос кинул"
    elif user1['duelWith'] != None:
        duel = json.load(open(f"db/other/duel-chat{chat_id}.json"))
        try:
            timeL = duel[f"{from_id}-{user1['duelWith']}"]['time_left']
        except:
            try:
                timeL = duel[f"{user1['duelWith']}-{from_id}"]['time_left']
            except:
                timeL = time.time() - 1000
        if time.time() < timeL:
            return "Тебе уже сделали вызов"
    elif from_id == vk_user_id:
        return "Ты не можешь бросить себе вызов"
    t = time.time() + 30
    await loual.duelThrow(id1=vk_user_id, id2=from_id, chat_id=chat_id, time=t)
    return f"&#127913;@id{vk_user_id} Вас вызывает на дуэль @id{from_id}\n" \
           f"&#8987;Даётся 30 секунд что бы принять вызов\n" \
           "Принять командой: 'дуэль принять' или 'принять'"

@bl.message(text=["дуэль сдаться", "сдаться"])
async def duelSurrend(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    us1 = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    if us1['duelWith'] == None:
        return "У тебя нет вызовов в которых ты сейчас учавствуешь"
    else:
        vk_user_id = us1['duelWith']
        await loual.prov(vk_user_id)
        us2 = json.load(open(f'db/users{vk_user_id}.json', encoding='utf-8'))
        us2['duelsWin'] += 1
        r = random.randint(1, 15)
        us2 ['repDuels'] += r
        us1['duelsLost'] += 1
        us1['repDuels'] -= r
        if us1['repDuels'] < 0:
            us1['repDuels'] = 0
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(us1, ensure_ascii=False, indent=2))
        with open(join(dirik, 'db', f'users{vk_user_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(us2, ensure_ascii=False, indent=2))
        return f"&#127987;@id{message.from_id} сдался\n" \
               f"@id{vk_user_id} получает {r} очков рейтинга в статистику"

@bl.message(text=["дуэль принять", "принять"])
async def duelConfirm(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    us = json.load(open(f'db/users{message.from_id}.json'))
    vk_user_id = us['duelWith']
    if vk_user_id == None:
        return "Тебе вызовов на дуэль не поступало"
    from_id = message.from_id
    chat_id = message.chat_id
    duel = json.load(open(f'db/other/duel-chat{chat_id}.json'))
    try:
        timeLeft = duel[f'{vk_user_id}-{from_id}']
    except:
        return "Ты не можешь принять вызов который сам же и отправил"
    if time.time() >= timeLeft['time_left']:
        del duel[f'{vk_user_id}-{from_id}']
        userFrom = json.load(open(f'db/users{from_id}.json', encoding='utf-8'))
        userWith = json.load(open(f'db/users{vk_user_id}.json', encoding='utf-8'))
        userFrom['duelWith'] = None
        userWith['duelWith'] = None
        with open(join(dirik, 'db', 'other', f'duel-chat{chat_id}.json'), 'w') as f:
            f.write(json.dumps(duel, ensure_ascii=False, indent=2))
        with open(join(dirik, 'db', f'users{from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(userFrom, ensure_ascii=False, indent=2))
        with open(join(dirik, 'db', f'users{vk_user_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(userWith, ensure_ascii=False, indent=2))
        return "&#8987;Время на принятие вызова вышло"
    else:
        fireNowId = await loual.duelConfirm(id1=vk_user_id, id2=from_id, chat_id=chat_id)
        if fireNowId != None:
            return f"&#127913;@id{vk_user_id} Ваш вызов принял @id{from_id}\n" \
                   f"&#128299;Первым стреляет @id{fireNowId}\n" \
                   "Стрелять командой: 'огонь' или 'стрелять'"
        else:
            return "Тебе вызовов на дуэль не поступало"

@bl.message(text=["огонь", "стрелять"])
async def duelFire(message: Message):
    await loual.prov(message.from_id)
    us = json.load(open(f'db/users{message.from_id}.json'))
    vk_user_id = us['duelWith']
    if vk_user_id == None:
        return "Ты не принимал дуэль"
    from_id = message.from_id
    chat_id = message.chat_id
    dirik = os.getcwd()
    outcome = await loual.duelFire(id1=vk_user_id, id2=from_id, chat_id=chat_id)
    if outcome == vk_user_id:
        userWin = json.load(open(f'db/users{from_id}.json', encoding='utf-8'))
        userLost = json.load(open(f'db/users{vk_user_id}.json', encoding='utf-8'))
        userWin['duelsWin'] += 1
        r = random.randint(1, 15)
        userWin['allFires'] += 1
        userWin['repDuels'] += r
        userWin['duelWith'] = None
        userLost['duelWith'] = None
        userLost['duelsLost'] += 1
        userLost['repDuels'] -= r
        if userLost['repDuels'] < 0:
            userLost['repDuels'] = 0
        with open(join(dirik, 'db', f'users{from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(userWin, ensure_ascii=False, indent=2))
        with open(join(dirik, 'db', f'users{vk_user_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(userLost, ensure_ascii=False, indent=2))
        return f"&#127919;@id{from_id} Попал в соперника\n" \
               f"&#127942;Ты получил {r} очков рейтинга в статистику\n" \
               f"&#128201;@id{vk_user_id} Проиграл"
    elif outcome == from_id:
        userFire = json.load(open(f'db/users{from_id}.json', encoding='utf-8'))
        userFire['allFires'] += 1
        with open(join(dirik, 'db', f'users{from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(userFire, ensure_ascii=False, indent=2))
        return f"&#128165;@id{from_id} промахнулся\n" \
               f"&#128299;Сейчас стреляет @id{vk_user_id}"
    else: return "&#128532;Ты уже стрелял, жди свой ход"

@bl.message(text="дуэли кмд")
async def duelsCMD(message: Message):
    return """
Команды дуэлей:

Дуэль(или дуэль вызов) {ID или ответом на сообщение} -> Вызвать на дуэль
Принять(или дуэль принять) -> Принять вызов на дуэль
Огонь(или стрелять) -> Стрельнуть в противника
Сдаться(или дуэль сдаться) -> Сдаться в дуэли
"""





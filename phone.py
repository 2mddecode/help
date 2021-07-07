from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="телефон имя <name>")
async def phone_name(message: Message, name):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    if user['vip'] >= 2:
        if len(name) <= 10:
            user['phone_name'] = name
            with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return f"Установил имя телефону: {name}"
        else:
            return "Ты не можешь поставить имя больше чем 10 символов"
    else:
        return "У тебя нет доступа к этой команде"

@bl.message(text="телефоны")
async def phone_shop(message: Message):
    await loual.prov(message.from_id)
    return "Магазин вертолётов: \n" \
           "Каждый последующий вертолёт уменьшает ожидание на 3 минуты\n" \
           "1. Nokia 3399 - 2,000,000$\n" \
           "2. Motorolla - 48,000,000$\n" \
           "3. Fly X++ (Custom) - 360,000,000$\n" \
           "4. Samsung Galaxy J5 - 47,000,000,000$\n" \
           "5. Vertex C99 (Custom) - 380,000,000,000\n" \
           "6. iPhone 12 Plus - 2,500,000,000,000$\n" \
           "7. Vertex X-Pro (Custom) - 14,000,000,000,000$\n" \
           "\nКупить телефон командой: 'телефон {номер}'"

@bl.message(text="телефон <a:int>")
async def phone_buy(message: Message, a: int):
    await loual.prov(message.from_id)
    if a >= 1 and a <= 7:
        dirik = os.getcwd()
        name_lvl = ["Nokia 3399", "Motorolla", "Fly X++ (Custom)", "Samsung Galaxy J5", "Vertex C99 (Custom)", "iPhone 12 Plus", "Vertex X-Pro (Custom)"]
        buy_lvl = [2_000_000, 48_000_000, 360_000_000, 47_000_000_000, 380_000_000_000, 2_500_000_000_000, 14_000_000_000_000]
        user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
        index = a - 1
        if user['phone_lvl'] == 0:
            if user['balance'] >= buy_lvl[index]:
                user['phone_lvl'] = a
                user['phone_name'] = name_lvl[index]
                user['balance'] -= buy_lvl[index]
                bl = await loual.sub(i=buy_lvl[index])
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"Ты купил(а) {name_lvl[index]} за {bl}$"
            else:
                return "Чел, ты на мели"
        else:
            return "Сначало продай старый\n" \
                   "Команда: 'телефон продать' в 2 раза дешевле"
        
@bl.message(text="телефон продать")
async def phone_sell(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json')) 
    name_lvl = ["Nokia 3399", "Motorolla", "Fly X++ (Custom)", "Samsung Galaxy J5", "Vertex C99 (Custom)", "iPhone 12 Plus", "Vertex X-Pro (Custom)"]
    buy_lvl = [2_000_000, 48_000_000, 360_000_000, 47_000_000_000, 380_000_000_000, 2_500_000_000_000, 14_000_000_000_000]
    index = user['phone_lvl'] - 1
    if user['phone_lvl'] != 0:
        user['phone_lvl'] = 0
        user['phone_name'] = "Нету"
        user['balance'] += round(buy_lvl[index] / 2)
        selled = round(buy_lvl[index] / 2)
        sell = await loual.sub(i=selled)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Ты продал(а) {name_lvl[index]} за {sell}$"
    else:
        return "У тебя нет телефона"

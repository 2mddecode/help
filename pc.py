from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="компьютер имя <name>")
async def pc_name(message: Message, name):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    if user['vip'] >= 2:
        if len(name) <= 10:
            user['pc_name'] = name
            with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return f"Установил имя компьютеру: {name}"
        else:
            return "Ты не можешь поставить имя больше чем 10 символов"
    else:
        return "У тебя нет доступа к этой команде"

@bl.message(text="компьютеры")
async def pc_shop(message: Message):
    await loual.prov(message.from_id)
    return "Магазин компьютеров: \n" \
           "Каждый последующий компьютер уменьшает ожидание на 3 минуты\n" \
           "1. Pentium PC Old .ver - 10,000,000$\n" \
           "2. Different PC Plus - 129,000,000$\n" \
           "3. Bloody PC Build - 13,000,000,000$\n" \
           "4. Hyper PC Ultra - 500,000,000,000$\n" \
           "5. Hyper PC Premium++ - 10,000,000,000,000\n" \
           "\nКупить компьютер командой: 'компьютер {номер}'"

@bl.message(text="компьютер <a:int>")
async def pc_buy(message: Message, a: int):
    await loual.prov(message.from_id)
    if a >= 1 and a <= 7:
        dirik = os.getcwd()
        name_lvl = ["Pentium PC Old .ver", "Different PC Plus", "Bloody PC Build", "Hyper PC Ultra", "Hyper PC Premium++"]
        buy_lvl = [10_000_000, 99_000_000, 1_000_000_000, 500_000_000_000, 10_000_000_000_000]
        user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
        index = a - 1
        if user['pc_lvl'] == 0:
            if user['balance'] >= buy_lvl[index]:
                user['pc_lvl'] = a
                user['pc_name'] = name_lvl[index]
                user['balance'] -= buy_lvl[index]
                bl = await loual.sub(i=buy_lvl[index])
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"Ты купил(а) {name_lvl[index]} за {bl}$"
            else:
                return "Чел, ты на мели"
        else:
            return "Сначало продай старый\n" \
                   "Команда: 'компьютер продать' в 2 раза дешевле"
        
@bl.message(text="компьютер продать")
async def pc_sell(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json')) 
    name_lvl = ["Pentium PC Old .ver", "Different PC Plus", "Bloody PC Build", "Hyper PC Ultra", "Hyper PC Premium++"]
    buy_lvl = [10_000_000, 99_000_000, 1_000_000_000, 500_000_000_000, 10_000_000_000_000]
    index = user['pc_lvl'] - 1
    if user['pc_lvl'] != 0:
        user['pc_lvl'] = 0
        user['pc_name'] = "Нету"
        user['balance'] += round(buy_lvl[index] / 2)
        selled = round(buy_lvl[index] / 2)
        sell = await loual.sub(i=selled)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Ты продал(а) {name_lvl[index]} за {sell}$"
    else:
        return "У тебя нет компьютера"

from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="вертолет имя <name>")
async def helicopter_name(message: Message, name):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    if user['vip'] >= 2:
        if len(name) <= 10:
            user['helicopter_name'] = name
            with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return f"Установил имя вертолету: {name}"
        else:
            return "Ты не можешь поставить имя больше чем 10 символов"
    else:
        return "У тебя нет доступа к этой команде"

@bl.message(text="вертолеты")
async def helicopter_shop(message: Message):
    await loual.prov(message.from_id)
    return "Магазин вертолётов: \n" \
           "Каждый последующий вертолёт уменьшает ожидание отдыха твоей команды на 1 час\n" \
           "1. SS-884 - 1,000,000$\n" \
           "2. ScU-X8 - 50,000,000$\n" \
           "3. Буржуйский Аракул - 400,000,000$\n" \
           "4. HenexI m8808 - 45,000,000,000$\n" \
           "5. Duble Dragon - 349,000,000,000\n" \
           "6. Ex DiOne yM-23 - 2,000,000,000,000$\n" \
           "7. DragoCopter DX860 - 15,000,000,000,000$\n" \
           "\nКупить вертолет командой: 'вертолет {номер}'"

@bl.message(text="вертолет <a:int>")
async def helicopter_buy(message: Message, a: int):
    await loual.prov(message.from_id)
    if a >= 1 and a <= 7:
        dirik = os.getcwd()
        name_lvl = ["SS-884", "ScU-X8", "Буржуйский Аракул", "HenexI m8808", "Duble Dragon", "Ex DiOne yM-23", "DragoCopter DX860"]
        buy_lvl = [1_000_000, 50_000_000, 400_000_000, 45_000_000_000, 349_000_000_000, 2_000_000_000_000, 15_000_000_000_000]
        user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
        index = a - 1
        if user['helicopter_lvl'] == 0:
            if user['balance'] >= buy_lvl[index]:
                user['helicopter_lvl'] = a
                user['helicopter_name'] = name_lvl[index]
                user['balance'] -= buy_lvl[index]
                bl = await loual.sub(i=buy_lvl[index])
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"Ты купил(а) {name_lvl[index]} за {bl}$"
            else:
                return "Чел, ты на мели"
        else:
            return "Сначало продай старый\n" \
                   "Команда: 'вертолет продать' в 2 раза дешевле"
        
@bl.message(text="вертолет продать")
async def helicopter_sell(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json')) 
    name_lvl = ["SS-884", "ScU-X8", "Буржуйский Аракул", "HenexI m8808", "Duble Dragon", "Ex DiOne yM-23", "DragoCopter DX860"]
    buy_lvl = [1_000_000, 50_000_000, 400_000_000, 45_000_000_000, 349_000_000_000, 2_000_000_000_000, 15_000_000_000_000]
    index = user['helicopter_lvl'] - 1
    if user['helicopter_lvl'] != 0:
        user['helicopter_lvl'] = 0
        user['helicopter_name'] = "Нету"
        user['balance'] += round(buy_lvl[index] / 2)
        selled = round(buy_lvl[index] / 2)
        sell = await loual.sub(i=selled)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Ты продал(а) {name_lvl[index]} за {sell}$"
    else:
        return "У тебя нет вертолета"

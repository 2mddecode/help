from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="ферма имя <name>")
async def buisnes_name(message: Message, name):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    if user['vip'] >= 2:
        if len(name) <= 10:
            user['bcFarmName'] = name
            with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return f"Установил имя ферме: {name}"
        else:
            return "Ты не можешь поставить имя больше чем 10 символов"
    else:
        return "У тебя нет доступа к этой команде"

@bl.message(text="ферма")
async def bcFarmPut(message: Message):
    await loual.prov(message.from_id)
    info = await loual.bcFarmPut(id=message.from_id, time=time.time())
    if info[0] == "OK":
        return f'{info[1]}'
    elif info[0] == "NO":
        user = json.load(open(f'db/users{message.from_id}.json'))
        timeEnd = round((user['bcFarmTime'] - time.time()) / 60)
        return f'За последний час ты уже снимал(а) биткоины с ферм\n Осталось {timeEnd} минут(ы)'
    elif info[0] == "NOT":
        return 'У тебя нет ферм\n' \
               'Список биткоин ферм посмотреть так: "фермы"'

@bl.message(text="фермы")
async def bcFarmShop(message: Message):
    await loual.prov(message.from_id)
    return "Магазин Ферм: \n" \
           "[Номер. Название(Заработок в час) - стоймость]\n" \
           "1. Nova Farm Station D-5(1₿/час) - 800,000$\n" \
           "2. Home Farm 'Fast X7'(5₿/час) - 5,000,000$\n" \
           "3. DDD - 'Dark Drake Farm'(10₿/час) - 20,000,000$\n" \
           "4. Steal F-x85(25₿/час) - 70,000,000$\n" \
           "5. Gold Farm Station(50₿/час) - 150,000,000$\n" \
           "6. Zet Zero Farm Dl-18(100₿/час) - 800,000,000$\n" \
           "7. Deluxe Alfa Farm SLX(300₿/час) - 5,000,000,000$\n" \
           "\nКупить ферму биткоинов командой: 'ферма {номер} {кол-во}'"

@bl.message(text="моя ферма")
async def bcFarm(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    gotBc = [1, 5, 10, 25, 50, 100, 300]
    i = user['bcFarmLvl'] - 1
    c = gotBc[i] * user['bcFarmCount']
    dox = await loual.sub(i=c)
    if user['bcFarmLvl'] >= 1:
        return f"Твоя ферма биткоинов: {user['bcFarmName']}\n" \
               f"Всего ферм куплено: {user['bcFarmCount']}\n" \
               f"Твой доход: {dox}₿/час"
    else: return "У тебя нет ферм\n" \
                 "Посмотри список ферм командой: 'фермы'"

@bl.message(text="ферма <a:int> <c:int>")
async def bcFarmBuy(message: Message, a: int, c: int):
    await loual.prov(message.from_id)
    if a >= 1 and a <= 9:
        dirik = os.getcwd()
        nameBcFarm = ["Nova Farm Station", "Home Farm 'Fast X7'", "DDD - 'Dark Drake Farm'", "Steal F-x85", "Gold Farm Station", "Zet Zero Farm Dl-18", "Deluxe Alfa Farm SLX"]
        buyBcFarm = [800_000, 5_000_000, 20_000_000, 70_000_000, 150_000_000, 800_000_000, 5_000_000_000]
        user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
        index = a - 1
        if user['bcFarmLvl'] == 0 or user['bcFarmLvl'] == a:
            if user['balance'] >= buyBcFarm[index] * c:
                if user['bcFarmCount'] + c > user['other']['bcLimitFarms']:
                    return f"Ты не можешь привысть лимит в {user['other']['bcLimitFarms']} ферм"
                user['bcFarmLvl'] = a
                if user['bcFarmCount'] == 0:
                    user['bcFarmTime'] = time.time() + 3600
                user['bcFarmName'] = nameBcFarm[index]
                user['bcFarmCount'] += c
                user['balance'] -= buyBcFarm[index] * c
                buy = buyBcFarm[index] * c
                bl = await loual.sub(i=buy)
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"Вы купили {c} штук {nameBcFarm[index]} за {bl}$"
            else:
                return "Чел, ты на мели"
        else:
            return "Сначало продай все свои фермы, мудень\n" \
                   "Команда: 'ферма продать {кол-во}' в 3 раза дешевле"
        
@bl.message(text="ферма продать <a:int>")
async def bсFarmSell(message: Message, a: int):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8')) 
    nameBcFarm = ["Nova Farm Station", "Home Farm 'Fast X7'", "DDD - 'Dark Drake Farm'", "Steal F-x85", "Gold Farm Station", "Zet Zero Farm Dl-18", "Deluxe Alfa Farm SLX"]
    buyBcFarm = [800_000, 5_000_000, 20_000_000, 70_000_000, 150_000_000, 800_000_000, 5_000_000_000]
    index = user['bcFarmLvl'] - 1
    if user['bcFarmLvl'] != 0:
        if a <= user['bcFarmCount']:
            user['bcFarmCount'] -= a
        else: return
        if user['bcFarmCount'] == 0:
            user['bcFarmLvl'] = 0
            user['bcFarmName'] = "Нету"
        buy = buyBcFarm[index] * a
        user['balance'] += round(buy / 3)
        selled = round(buy / 3)
        sell = await loual.sub(i=selled)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Вы продали {nameBcFarm[index]} {a} штук за {sell}$"
    else:
        return "У тебя и так их его"

@bl.message(text=["биткоин продать <a:int>", "биткоины продать <a:int>", "бк продать <a:int>", "бк продать <a:int>"])
async def bсFarmSell(message: Message, a: int):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    bc = user['bitcoin']
    if a > bc:
        return "У тебя нет столько биткоинов"
    else:
        user['bitcoin'] -= a
        user['balance'] += round(a * 34000)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_a = await loual.sub(i=round(a))
        sub_ad = await loual.sub(i=round(a * 34000))
        return f"Ты продал {sub_a}₿\n" \
               f"И получил {sub_ad}$"

@bl.message(text=["биткоин продать всё", "биткоин продать все", "биткоины продать всё", "биткоины продать все", "бк продать всё", "бк продать все", "бк продать всё", "бк продать все", "бк продать", "биткоин продать", "биткоины продать"])
async def bсFarmSell(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    a = user['bitcoin']
    user['bitcoin'] -= a
    user['balance'] += round(a * 34000)
    with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    sub_a = await loual.sub(i=round(a))
    sub_ad = await loual.sub(i=round(a * 34000))
    return f"Ты продал {sub_a}₿\n" \
               f"И получил {sub_ad}$"

        

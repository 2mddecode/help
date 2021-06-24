from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="бизнес снять")
async def buisnes_put(message: Message):
    await loual.prov(message.from_id)
    info = await loual.buisnes_put(id=message.from_id, time=time.time())
    if info[0] == "OK":
        return f'{info[1]}'
    elif info[0] == "NO":
        return 'За последний час ты уже снимал(а) деньги с бизнеса'
    elif info[0] == "NOT":
        return 'У тебя нет бизнеса\n' \
               'Посмотреть список бизнесов командой: "бизнесы"'

@bl.message(text="бизнесы")
async def buisnes_shop(message: Message):
    await loual.prov(message.from_id)
    return "Магазин бизнесов: \n" \
           "[Номер. Название(Заработок в час) - стоймость]\n" \
           "1. Лимонадный столик(25,000$/час) - 250,000$\n" \
           "2. Ларёк(100,000$/час) - 5,000,000$\n" \
           "3. Бутик(300,000$/час) - 20,000,000$\n" \
           "4. Магазин 'Дон Атный'(700,000$/час) - 100,000,000$\n" \
           "5. ОХБ 'Очень Хороший Бизнес'(1,000,000$/час) - 500,000,000$\n" \
           "6. ТЦ 'В вакууме'(5,000,000$/час) - 2,000,000,000$\n" \
           "7. ТРЦ 'Адреналин'(30,000,000$/час) - 15,000,000,000$\n" \
           "8. Завод Бутылок(100,000,000$/час) - 80,000,000,000$\n" \
           "9. Завод Крышек(400,000,000$/час) - 250,000,000,000$\n" \
           "\nКупить бизнес командой: 'бизнес {номер}'"

@bl.message(text="бизнес")
async def buisnes(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'), encoding='utf-8')
    buy_lvl = [25_000, 100_000, 300_000, 700_000, 1_000_000, 5_000_000, 30_000_000, 100_000_000, 400_000_000]
    i = user['buisnes_lvl'] - 1
    dox = await loual.sub(i=buy_lvl[i])
    if user['buisnes_lvl'] >= 1:
        return f"У тебя сейчас есть бизнес: {user['buisnes_name']}\n" \
               f"Твой доход: {dox}$/час"
    else: return "У тебя нет бизнеса\n" \
                 "Узнать список бизнесов командой: 'бизнесы'"

@bl.message(text="бизнес <a:int>")
async def buisnes_buy(message: Message, a: int):
    await loual.prov(message.from_id)
    if a >= 1 and a <= 9:
        dirik = os.getcwd()
        name_lvl = ["Лимонадный столик", "Ларёк", "Бутик", "Магазин 'Дон Атный'", "ОХБ 'Очень Хороший Бизнес'", "ТЦ 'В вакууме'", "ТРЦ 'Адреналин'", "Завод Бутылок", "Завод Крышек"]
        buy_lvl = [250000, 5000000, 20000000, 100000000, 500000000, 2000000000, 15000000000, 80000000000, 250000000000]
        user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
        index = a - 1
        if user['buisnes_lvl'] == 0:
            if user['balance'] >= buy_lvl[index]:
                user['buisnes_lvl'] = a
                user['buisnes_time'] = time.time()
                user['buisnes_name'] = name_lvl[index]
                user['balance'] -= buy_lvl[index]
                bl = await loual.sub(i=buy_lvl[index])
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"Ты купил(а) {name_lvl[index]} за {bl}$"
            else:
                return "Чел, ты на мели"
        else:
            return "Сначало бизнес продай\n" \
                   "Команда: 'бизнес продать' в 4 раза дешевле"
        
@bl.message(text="бизнес продать")
async def buisnes_sell(message: Message):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json')) 
    name_lvl = ["Лимонадный столик", "Ларёк", "Бутик", "Магазин 'Дон Атный'", "ОХБ 'Очень Хороший Бизнес'", "ТЦ 'В вакууме'", "ТРЦ 'Адреналин'", "Завод Бутылок", "Завод Крышек"]
    buy_lvl = [250000, 5000000, 20000000, 100000000, 500000000, 2000000000, 15000000000, 80000000000, 250000000000]
    index = user['buisnes_lvl'] - 1
    if user['buisnes_lvl'] != 0:
        user['buisnes_lvl'] = 0
        user['buisnes_name'] = "Нету"
        user['balance'] += round(buy_lvl[index] / 4)
        selled = round(buy_lvl[index] / 4)
        sell = await loual.sub(i=selled)
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return f"Ты продал(а) {name_lvl[index]} за {sell}$"
    else:
        return "У тебя нет бизнеса"

        

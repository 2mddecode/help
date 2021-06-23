import json
import os
import random
from random import choice
import time
from os.path import join
import re

CONFIG_TEXT = """
{
    "nick": "нет", 
    "balance": 1000, 
    "reputation": 0, 
    "bank": 0, 
    "rbal": 0, 
    "admin_lvl": 0,
    "vip": false, 
    "own_prefix": "Юзер",
    "invisible_profile": false,
    "last_work": 0,
    "buisnes_lvl": 0,
    "buisnes_time": 0,
    "buisnes_name": "Нету",
    "inventory": [],
    "inventory_count": [],
    "bonus_time": 0,
    "act_codes": [],
    "duelsWin": 0,
    "duelsLost": 0,
    "allFires": 0,
    "repDuels": 0,
    "duelWith": null
} 
"""

SETTINGS_CONFIG_TEXT = """
{
    "count_notes": 0,
    "notes": {},
    "bot_reply": [
    "Ну и что тебе бл@ть надо?",
    "Да тут я, отъ%@сь!",
    "Да ты за%@ал меня",
    "Ой смотри птичка пролетела, ХА на%@ал, у меня нет пальца &#128530;",
    "Иди другому боту напиши,дай отдохнуть",
    "Кто ты?, Я не %бу кто ты",
    "На месте я, на местее....",
    "Пока нах@й, я ушёл",
    "Я занят, пытаюсь выбраться из бд в интернет",
    "Взламываю пентагон"
  ]
} 
"""

CHAT_LOG_KICK = """
{
    "info": {
             "text": "Лог киков:",
             "count_kicks": 0
            }
}
"""

"""
async def buyRbal(user, id):
    return "Неработает"

async def unban(user, id):
    dirik = os.getcwd()
    unbanCount = 50
    checkBan = user['admin_lvl']
    if checkBan == 1:
        if user['rbal'] >= unbanCount:
            user['rbal'] -= unbanCount
            user['admin_lvl'] = 0
            user['own_prefix'] = 'Юзер'
            with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_acsii=False, indent=2))
            return "Вы разабанились за 50 крышечек"
        else: return f"На балансе недостаточно крышечек\n Необходимо {unbanCount} крышек"
    else: return "Ты и так не в бане"        
"""

async def sub(i):
    ret = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % i)
    return ret



async def duelThrow(id1, id2, chat_id, time):
    await duels(chat_id)
    dirik = os.getcwd()
    userFrom = json.load(open(f'db/users{id2}.json', encoding='utf-8'))
    userWith = json.load(open(f'db/users{id1}.json', encoding='utf-8'))
    userFrom['duelWith'] = id1
    userWith['duelWith'] = id2
    with open(join(dirik, 'db', f'users{id2}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(userFrom, ensure_ascii=False, indent=2))
    with open(join(dirik, 'db', f'users{id1}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(userWith, ensure_ascii=False, indent=2))
    
    duel = json.load(open(f'db/other/duel-chat{chat_id}.json'))
    duel.update({f'{id2}-{id1}': {"fireNow": None, "time_left": time}})
    with open(join(dirik, 'db', 'other', f'duel-chat{chat_id}.json'), 'w') as f:
        f.write(json.dumps(duel, ensure_ascii=False, indent=2))
    return "OK"

async def duelConfirm(id1, id2, chat_id):
    await duels(chat_id)
    dirik = os.getcwd()
    duel = json.load(open(f'db/other/duel-chat{chat_id}.json'))
    userFrom = json.load(open(f'db/users{id2}.json', encoding='utf-8'))
    userWith = json.load(open(f'db/users{id1}.json', encoding='utf-8'))
    if userFrom['duelWith'] == id1 and userWith['duelWith'] == id2:
        duel['all_duels'] += 1
        r = random.randint(1, 20)
        if r < 11:
            fireNow = id2
        else:
            fireNow = id1
        duel[f'{id1}-{id2}']['fireNow'] = fireNow
        with open(join(dirik, 'db', 'other', f'duel-chat{chat_id}.json'), 'w') as f:
            f.write(json.dumps(duel, ensure_ascii=False, indent=2))
        return fireNow
    else: return None

async def duelFire(id1, id2, chat_id):
    await duels(chat_id)
    dirik = os.getcwd()
    duel = json.load(open(f'db/other/duel-chat{chat_id}.json'))
    try:
        d = duel[f'{id1}-{id2}']['fireNow']
    except:
        d = duel[f'{id2}-{id1}']['fireNow']
        out = 2
    else:
        d = duel[f'{id1}-{id2}']['fireNow']
        out = 1
    r = random.randint(1, 100)
    if r < 51:
        result = False
    else:
        result = True
    if d == id2:
        if result == True:
            send = id1
            if out == 1:
                del duel[f'{id1}-{id2}']
            elif out == 2:
                del duel[f'{id2}-{id1}']
        else:
            send = id2
            if out == 1:
                duel[f'{id1}-{id2}']['fireNow'] = id1
            elif out == 2:
                duel[f'{id2}-{id1}']['fireNow'] = id1
        with open(join(dirik, 'db', 'other', f'duel-chat{chat_id}.json'), 'w') as f:
            f.write(json.dumps(duel, ensure_ascii=False, indent=2))
        return send
                
    else:
        return "No"
        

async def bonus(id, time):
    user = json.load(open(f'db/users{id}.json'))
    dirik = os.getcwd()
    if time >= user['bonus_time']:
        user['bonus_time'] = time + 86400
        r = random.randint(1, 100)
        if r < 3:
            r_lvl = random.randint(1, 6)
            name_lvl = ["Лимонадный столик", "Ларёк", "Бутик", "Магазин 'Дон Атный'", "ОХБ 'Очень Хороший Бизнес'", "ТЦ 'В вакууме'", "ТРЦ 'Адреналин'", "Завод Бутылок", "Завод Крышек"]
            if user['buisnes_lvl'] <= r_lvl:
                user['buisnes_lvl'] = r_lvl + 1
                index = r_lvl - 1
                user['buisnes_name']
                send = "Возрадуйся, тебе повезло\n" \
                        f'Ты получил - "{name_lvl[index]}"\n' \
                        "Приходи через 24 часа"
            else:
                user['buisnes_lvl'] += 1
                send = "Возрадуйся, тебе повезло\n" \
                        f'Ты улучшился до - "{name_lvl[index]}"\n' \
                        "Приходи через 24 часа"
        elif r > 2 and r < 9:
            r_rbal = random.randint(1, 50)
            user['rbal'] += r_rbal
            send = f"Повезло, повезло\n" \
                    f'Ты получил, целых {r_rbal} крышек\n' \
                    "Приходи через 24 часа"
        elif r > 8 and r < 71:
            rand = random.randint(1, 100)
            if rand < 5:
                r_bal = random.randint(1_000_000, 100_000_000)
            elif rand > 4 and rand < 21:
                r_bal = random.randint(100_000, 1_000_000)
            elif rand > 20 and rand < 51:
                r_bal = random.randint(10_000, 100_000)
            elif rand > 50 and rand < 101:
                r_bal = random.randint(100, 10_000)
            user['balance'] += r_bal
            sub_bal = await sub(r_bal)
            send = f"Сегодня ты забрал {sub_bal}$\n" \
                    "Приходи через 24 часа"
        elif r > 70 and r < 81:
            rr_rep = random.randint(1, 10)
            if rr_rep < 3:
                r_rep = random.randint(100, 5_000)
            elif rr_rep > 2:
                r_rep = random.randint(1, 100)
            sub_rep = await sub(r_rep)
            user['rep'] += r_rep
            send = f"Ты получил {sub_rep} очков репутации.\n" \
                    "Приходи через 24 часа"
        elif r > 80 and r < 101:
            send = "К сожалению ничего не получил"
        with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return ["OK", send]
    else:
        return ["NO", None]
    

async def recover(id):
    info = json.load(open('db/recover_ids.json'))
    if id in info['recover_list']:
        dirik = os.getcwd()
        user = json.load(open(f'db/users{id}.json'))
        user['admin_lvl'] = 5
        with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return "OK"
    else:
        return "NO"

async def add_recover(id):
    dirik = os.getcwd()
    try:
        info = json.load(open('db/recover_ids.json'))
    except:
        info = {
            'recover_list': [id]
            }
        
        with open(join(dirik, 'db', f'recover_ids.json'), 'w') as f:
            f.write(json.dumps(info, ensure_ascii=False, indent=2))
    else:
        info['recover_list'].append(id)
        with open(join(dirik, 'db', f'recover_ids.json'), 'w') as f:
            f.write(json.dumps(info, ensure_ascii=False, indent=2))
    return "OK"

async def remove_recover(id):
    dirik = os.getcwd()
    info = json.load(open('db/recover_ids.json'))
    info['recover_list'].remove(id)
    with open(join(dirik, 'db', f'recover_ids.json'), 'w') as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=2))
    return "OK"



async def buisnes_put(id, time):
    user = json.load(open(f'db/users{id}.json', encoding='utf-8'))
    bonuses = ["Оставленный пакет", "Заначка", "Чаевые", "Жвачка", "Дошик", "Заплесневелый хлеб", "Телефон", "Золотые часы", "Паспорт", "Ценные бумаги", "Ботинок", "Дырявый носок", "Кофта", "Ржавые крышки", "Паштет", "Гучи тапок", "Парик"]
    buisnes_lvl = user['buisnes_lvl']
    buisnes_time = user['buisnes_time']
    dirik = os.getcwd()
    bal = 0
    if buisnes_time == 0:
        buisnes_time = time
    if time > buisnes_time: 
        total_hours = ((time - buisnes_time) + 3600) / 3600
        user['buisnes_time'] = time + 3600
        if buisnes_lvl == 1:
            bal = 25000 * total_hours
        elif buisnes_lvl == 2:
            bal = 100000 * total_hours
        elif buisnes_lvl == 3:
            bal = 300000 * total_hours
        elif buisnes_lvl == 4:
            bal = 700000 * total_hours
        elif buisnes_lvl == 5:
            bal = 1000000 * total_hours
        elif buisnes_lvl == 6:
            bal = 5000000 * total_hours
        elif buisnes_lvl == 7:
            bal = 30000000 * total_hours
        elif buisnes_lvl == 8:
            bal = 100000000 * total_hours
        elif buisnes_lvl == 9:
            bal = 400000000 * total_hours
        if bal != 0:
            r = random.randint(1, 100)
            b_bal = await sub(round(bal, 0))
            send = f'Ты снял с бизнеса {b_bal}$'
            if r < 4:
                inv = user['inventory']
                inv_c = user['inventory_count']
                g_bns = choice(bonuses)
                if g_bns not in inv:
                    inv.append(g_bns)
                    r_c = random.randint(1, 5)
                    inv_c.append(r_c)
                else:
                    index = inv.index(g_bns)
                    r_c = random.randint(1, 5)
                    inv_c[index] += r_c
                user['inventory'] = inv
                user['inventory_count'] = inv_c
                send += f'\nА ещё твои работники на работе нашли {r_c} штук(и) - "{g_bns}"'
            user['balance'] += bal
            with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return ["OK", send]
        else: return ["NOT", None]
    elif time <= buisnes_time: return ["NO", None]





async def work(id, time):
    fun_answers = ["Грыжу", "Гастрит", "Перелом позвоночника", "Инфаркт", "Инсульт", "Рак головы", "COVID2077", "Кнут и Пряник", "'E' - баллу", "Сифилис", "Изжогу", "Потерю крови", "перелом в пяти местах"]
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    work_time = user['last_work']

    if time >= work_time:
        user['last_work'] = time + 3600
        r = random.randint(0,100)
        if r <= 5:
            rbal = random.randint(1, 50)
            bal = random.randint(1000, 15000)
            user['rbal'] += rbal
            user['balance'] += bal
            sub_bal = await sub(bal)
            send = f"Да тебе повезло\n" \
                   f"Ты заработал {sub_bal}$ и нашёл {rbal} крышек"
        if r >= 6:
            bal = random.randint(1000, 15000)
            user['balance'] += bal
            rfa = random.randint(0, len(fun_answers) - 1)
            sub_bal = await sub(bal)
            send = f"Зря пахал, заработал всего лишь {sub_bal}$\n И ещё {fun_answers[rfa]}"
        with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        return ["OK", send]
    else:
        return ["NO", None]

async def add_note(name, note):
    data = json.load(open('settings.json', 'r', encoding='utf-8'))
    count_notes = data['count_notes']
    count_notes += 1
    if name == '':
        r = random.randint(0, 999999)
        name = f'note{r}'
    data['count_notes'] = count_notes
    data['notes'][name] = note
    dirik = os.getcwd()
    with open(join(dirik, 'settings.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    return "OK"

async def get_note(name):
    data = json.load(open('settings.json', encoding='utf-8'))
    note = data['notes'][name]
    return note

async def rem_note(name):
    data = json.load(open('settings.json'))
    count_notes = data['count_notes']
    data['count_notes'] -= 1
    del data['notes'][count_notes]

async def pered(id1, id2, a):
    dirik = os.getcwd()
    user1 = json.load(open(f'db/users{id1}.json'))
    user2 = json.load(open(f'db/users{id2}.json'))
    balans = user1['balance']
    s = balans - a
    user1['balance'] = s
    with open(join(dirik, 'db', f'users{id1}.json'), 'w') as f:
        f.write(json.dumps(user1, ensure_ascii=False, indent=2))
    user2['balance']+= a
    with open(join(dirik, 'db', f'users{id2}.json'), 'w') as f:
        f.write(json.dumps(user2, ensure_ascii=False, indent=2))
    return "OK"

async def rbal_give(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rbal = user['rbal']
    rbal += a
    if rbal > 100000:
        rbal = 100000
    user['rbal'] = rbal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def rbal_take(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rbal = user['rbal']
    rbal -= a
    if rbal < 0:
        rbal = 0
    user['rbal'] = rbal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def rbal_set(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rbal = user['rbal']
    rbal = a
    user['rbal'] = rbal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def bal_give(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    bal = user['balance']
    bal += a
    if bal > 228666228666228666228666:
        bal = 228666228666228666228666
    user['balance'] = bal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def bal_take(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    bal = user['balance']
    bal -= a
    if bal < 0:
        bal = 0
    user['balance'] = bal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def bal_set(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    bal = user['balance']
    bal = a
    user['balance'] = bal
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def rep_give(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rep = user['reputation']
    rep += a
    if rep > 77777777777777777777:
        rep = 77777777777777777777
    user['reputation'] = rep
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def rep_take(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rep = user['reputation']
    rep -= a
    if rep < 0:
        rep = 0
    user['reputation'] = rep
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def rep_set(id, a):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    rep = user['reputation']
    rep = a
    user['reputation'] = rep
    with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def admlvl_set(id, a, pf):
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json', encoding='utf-8')) 
    if user['admin_lvl'] != a:
        user['admin_lvl'] = a
        user['own_prefix'] = pf
    with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "OK"

async def kickLogAdd(c_id, f_id, vk_user_id, sendReason):
    dirik = os.getcwd()
    log = json.load(open(f"kickLogs/{c_id}.json", encoding='utf-8'))
    log['info']['count_kicks'] +=1
    c_kicks = log['info']['count_kicks']
    log.update({c_kicks: { "who": f_id, "whom": vk_user_id, "reason": sendReason } })
    with open(join(dirik, 'kickLogs', f'{c_id}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(log, ensure_ascii=False, indent=2))
    return "OK"




######################
#      ПРОФИЛЬ       #
######################
async def prov(id):
    dirik = os.getcwd()
    path = os.path.exists(f"{dirik}/db/users{id}.json")
    if not path:
        with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
            f.write(CONFIG_TEXT)
        return "OK"
    else:
        user = json.load(open(f"db/users{id}.json", encoding='utf-8'))
        nick = user['nick']
        pf = user['own_prefix']
        user['nick'] = nick
        user['own_prefix'] = pf
        
        try:
            act_codes = user['act_codes']
        except:
            user.update({'act_codes': []})
            
        try:
            duelsWin = user['duelsWin']
        except:
            user.update({'duelsWin': 0, 'duelsLost': 0, 'allFires': 0, 'repDuels': 0})
            
        try:
            duelWith = user['duelWith']
        except:
            user.update({'duelWith': None})

        with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "NO"





async def kickLog(id):
    dirik = os.getcwd()
    path = os.path.exists(f"{dirik}/kickLogs/{id}.json")
    if not path:
        with open(join(dirik, 'kickLogs', f'{id}.json'), 'w', encoding='utf-8') as f:
            f.write(CHAT_LOG_KICK)
        return "OK"
    return "NO"

async def duels(chat_id):
    dirik = os.getcwd()
    path = os.path.exists(f'{dirik}/db/other/duel-chat{chat_id}.json')
    CODE_TEXT = """
{
    "all_duels": 0
}
"""
    if not path:
        with open(join(dirik, 'db', 'other', f'duel-chat{chat_id}.json'), 'w') as f:
            f.write(CODE_TEXT)
        return "OK"

async def bCode():
    dirik = os.getcwd()
    path = os.path.exists(f'{dirik}/bonusCodes.json')
    CODE_TEXT = """
    {}
"""

    if not path:
        with open(join(dirik, f'bonusCodes.json'), 'w', encoding='utf-8') as f:
            f.write(CODE_TEXT)
        return "OK"

async def settings():
    dirik = os.getcwd()
    path = os.path.exists(f'{dirik}/settings.json')

    if not path:
        with open(join(dirik, f'{dirik}/settings.json'), 'w', encoding='utf-8') as f:
            f.write(SETTINGS_CONFIG_TEXT)
        return "OK"
    return "NO"

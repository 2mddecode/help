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
    "buisnes_name": 'Нету'
    "inventory": [],
    "inventory_count": []
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

async def sub(i):
    ret = sub = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % i)
    return ret

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
    user = json.load(open(f'db/users{id}.json'))
    bonuses = ["Оставленный пакет", "Заначка", "Чаевые", "Жвачка", "Дошик", "Заплесневелый хлеб", "Телефон", "Золотые часы", "Паспорт", "Ценные бумаги", "Ботинок", "Дырявый носок", "Чья-то кофта", "Ржавые крышки", "Паштет", "Gucci тапок", "Парик"]
    buisnes_lvl = user['buisnes_lvl']
    buisnes_time = user['buisnes_time']
    dirik = os.getcwd()
    bal = 0
    if buisnes_time == 0:
        buisnes_time = time
    if time > buisnes_time:
        user['buisnes_time'] += time + 3600
        total_hours = (time - buisnes_time) / 3600
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
            sub_bal = await sub(round(bal, 0))
            send = f'Ты снял с бизнеса {sub_bal}$'
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
                send += f'\nА ещё твои работники на работе нашли {inv_c} штук - "{g_bns}"'
            user['balance'] = bal
            with open(join(dirik, 'db', f'users{id}.json'), 'w') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            return ["OK", send]
        else: return ["NO", None]
    elif time <= buisnes_time: return ["NO", None]





async def work(id, time):
    fun_answers = ["Грыжу", "Гастрит", "Перелом позвоночника", "Инфаркт", "Инсульт", "Рак головы", "COVID2077", "Кнут и Пряник", "'E' - баллу", "Сифилис", "Изжогу", "Потерю крови", "перелом в пяти местах"]
    dirik = os.getcwd()
    user = json.load(open(f'db/users{id}.json'))
    work_time = user['last_work']

    if time >= work_time:
        user['last_work'] += time + 3600
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
            b_lvl = user['buisnes_lvl']
        except:
            user.update({'buisnes_lvl': 0})
            user.update({'buisnes_time': 0)})
            user.update({'buisnes_name': 'Нету'})
            user.update({'inventory': []})
            user.update({'inventory_count': []})
        with open(join(dirik, 'db', f'users{id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
    return "NO"

async def settings():
    dirik = os.getcwd()
    path = os.path.exists(f'{dirik}/settings.json')

    if not path:
        with open(join(dirik, f'{dirik}/settings.json'), 'w', encoding='utf-8') as f:
            f.write(SETTINGS_CONFIG_TEXT)
        return "OK"
    return "NO"

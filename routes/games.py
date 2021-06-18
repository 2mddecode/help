from vkbottle.bot import BotLabeler, Message
import os
from os.path import join
import loual
import random
import time
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="бонус")
async def bonus(message: Message):
    await loual.prov(message.from_id)
    check = await loual.bonus(id=message.from_id, time=time.time())
    if check[0] == "OK":
        return "Вы собрали бонус! \n" \
               f"{check[1]}"
    else: return "Сегодня вы уже собирали бонус\n" \
                  "Бонус можно собирать каждые 24 часа"

@bl.message(text="ставка <a:int>")
async def bet(message: Message, a: int):
    await loual.prov(message.from_id)
    s = random.randint(1, 160)
    user = json.load(open(f'db/users{message.from_id}.json'))
    dirik = os.getcwd()

    if not user["balance"] >= a:
        return "Работать иди, понял?"
    if s < 41:
        ss = user["balance"] - a
        user["balance"] = ss
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0\n Мы нашарили {sub_a}$"
    elif s > 40 and s < 61:
        user["balance"] -= a
        user["balance"] += round(a * 0.25, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.25, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.25\n Мы нашарили {sub_a}$"
    elif s > 60 and s < 81:
        user["balance"] -= a
        user["balance"] += round(a * 0.5, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.5, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.5\n Мы нашарили {sub_a}$"
    elif s > 80 and s < 101:
        user["balance"] -= a
        user["balance"] += round(a * 0.75, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.75, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.75\n Мы нашарили {sub_a}$"
    elif s > 100 and s < 116:
        return f"Ничего x1\n"
    elif s > 115 and s < 141:
        user["balance"] -= a
        user["balance"] += a * 2
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x2\n Твой баланс {sub_bal}$"
    elif s > 140 and s < 151:
        user["balance"] -= a
        user["balance"] += a * 3
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x3\n Твой баланс {sub_bal}$"
    elif s > 150 and s < 158:
        user["balance"] -= a
        user["balance"] += a * 4
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x4\n Твой баланс {sub_bal}$"
    elif s > 157 and s < 161:
        user["balance"] -= a
        user["balance"] += a * 5
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x5\n Твой баланс {sub_bal}$"

@bl.message(text=["ставка все", "ставка всё"])
async def bet_all(message: Message):
    await loual.prov(message.from_id)
    s = random.randint(1, 160)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json'))
    a = user['balance']

    if not user["balance"] >= a:
        return "Работать иди, понял?"
    if s < 41:
        ss = user["balance"] - a
        user["balance"] = ss
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0\n Мы нашарили {sub_a}$"
    elif s > 40 and s < 61:
        user["balance"] -= a
        user["balance"] += round(a * 0.25, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.25, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.25\n Мы нашарили {sub_a}$"
    elif s > 60 and s < 81:
        user["balance"] -= a
        user["balance"] += round(a * 0.5, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.5, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.5\n Мы нашарили {sub_a}$"
    elif s > 80 and s < 101:
        user["balance"] -= a
        user["balance"] += round(a * 0.75, 0)
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        a = round(a - a * 0.75, 0)
        sub_a = await loual.sub(i=a)
        return f"Лохотрон сработал пацаны.\n Коэфициент x0.75\n Мы нашарили {sub_a}$"
    elif s > 100 and s < 116:
        return f"Ничего x1\n"
    elif s > 115 and s < 141:
        user["balance"] -= a
        user["balance"] += a * 2
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x2\n Твой баланс {sub_bal}$"
    elif s > 140 and s < 151:
        user["balance"] -= a
        user["balance"] += a * 3
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x3\n Твой баланс {sub_bal}$"
    elif s > 150 and s < 158:
        user["balance"] -= a
        user["balance"] += a * 4
        
        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x4\n Твой баланс {sub_bal}$"
    elif s > 157 and s < 161:
        user["balance"] -= a
        user["balance"] += a * 5

        with open(os.path.join(dirik, 'db', f'users{message.from_id}.json'), 'w') as f:
            f.write(json.dumps(user, ensure_ascii=False, indent=2))
        sub_bal = await loual.sub(i=user['balance'])
        return f"Выйграл x5\n Твой баланс {sub_bal}$"
    


    
